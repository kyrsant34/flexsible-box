import json
import requests

from rest_framework import status
from rest_framework.response import Response

from apps.client.serializers import NaturalPersonSerializer
from apps.client.models import InsuredObject, NaturalPerson

from rest_framework import mixins, viewsets
from ..serializers import ResultParameterSerializer, ResultTypeSerializer, ResultSerializer
from ..models import ResultParameter, ResultType, Result, Calculation


class ResultParametersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ResultParameter.objects.all()
    serializer_class = ResultParameterSerializer
    filter_fields = ('code',)


class ResultViewSet(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer


    def create(self, request, *args, **kwargs):
        try:
            request.data['parameters'] = self.get_result_data(request.data)
        except Exception as exc:
            return Response({"logic_errors": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"serializer_errors": serializer.errors, "bad_data": request.data},
                        status=status.HTTP_400_BAD_REQUEST)

    def get_result_data(self, data):
        self.headers = {'content-type': 'application/json'}
        self.host = 'megarussd.dev.b2bpolis.ru'

        logic_data = {}
        calculation = Calculation.objects.get(id=data['calculation'])

        insured_object = InsuredObject.objects.get(id=calculation.parameters['insured_object'])
        driver = NaturalPerson.objects.get(id=insured_object.parameters['drivers'][0])

        logic_data['driver'] = self.create_natural_person(driver)

        owner = insured_object.insurant.natural_person
        logic_data['owner'] = self.create_natural_person(owner)

        logic_data['car'] = self.create_car(insured_object)

        logic_data['insured_object'] = self.create_insured_object(logic_data)

        logic_data['calculation'] = self.create_calculation(calculation, logic_data)

        logic_data['results'] = self.create_result(calculation, logic_data)
        if logic_data['results']:
            return self.clean_data(logic_data['results'][0])
        return {}

    def create_result(self, calculation, logic_data):
        calculation_id = logic_data['calculation']['id']
        insurance_program = calculation.parameters.get(
                'insurance_program', logic_data['calculation']['available_insurance_departments'][0]['id'])
        data = self.mk_request(
                f'rest/v3/default/calculation/{calculation_id}/result/{insurance_program}/?insurance_company=1&messages=1&vars=1')
        return data

    def create_calculation(self, calculation, logic_data):
        params = dict(calculation.parameters)
        params['insured_object'] = logic_data['insured_object']['id']
        params.pop('insurance_program', None)
        data = self.mk_request('rest/full/calculation/', params)
        return data

    def create_insured_object(self, logic_data):
        owner_person_id = logic_data['owner']['person']
        params = {
            "drivers": [logic_data['driver']['id']],
            "beneficiary": owner_person_id,
            "insurant": owner_person_id,
            "owner": owner_person_id,
            "object_id": logic_data['car']['id'],
            "object_type": "car"
        }
        data = self.mk_request('rest/default/client/insured-object', params)
        return data

    def create_car(self, insured_object):
        params = {}
        for param in ('car_mark', 'car_model', 'car_modification', 'cost', 'engine_power',
                      'engine_power_kilowatt', 'manufacturing_date', 'vin_number', 'car_type'):
            params[param] = insured_object.parameters.get(param)
        params['credential'] = [{
                'number': insured_object.parameters.get('car_registration_number'),
                'series': insured_object.parameters.get('car_registration_series'),
                'issue_date': insured_object.parameters.get('issue_date'),
                'credential_type': insured_object.parameters.get('credential_type'),
        }]
        data = self.mk_request('rest/default/client/car-create', params)
        return data

    def create_natural_person(self, natural_person):
        params = dict(NaturalPersonSerializer(instance=natural_person).data)
        params['address'] = []
        params.pop('contact', None)
        for idx, credential in enumerate(params.get('credential', [])):
            credential = self.clean_data(credential)
            credential['credential_type'] = 3
            params['credential'][idx] = credential
        params.pop('person', None)
        data = self.mk_request('rest/default/client/natural-person-create', self.clean_data(params))
        return data

    def mk_request(self, rest_url, params=None):
        url = f'http://{self.host}/{rest_url}'
        if params is None:
            params = {}
        request_msg = f'request: url: {url} with params: {params}'
        print(request_msg)
        try:
            response = requests.post(url, data=json.dumps(params), headers=self.headers)
            response_msg = f'response text: {response.text}'
            print(response_msg)
            return response.json()
        except Exception as exc:
            raise Exception({'request_data': request_msg, 'response_data': response_msg})

    def clean_data(self, data):
        data.pop('id', None)
        data.pop('creator', None)
        return dict(data)


class ResultTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ResultType.objects.all()
    serializer_class = ResultTypeSerializer
    filter_fields = ('department', 'insurance_type',)
