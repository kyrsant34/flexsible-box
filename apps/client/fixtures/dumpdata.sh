#!/bin/sh
./manage.py dumpdata --indent 4 --natural-primary client.insuredobjecttype client.insuredobjectparameter > apps/client/fixtures/initial_data.json
