#!/bin/sh
./manage.py dumpdata --indent 4 --natural-primary contract.calculationtype contract.calculationparameter contract.resulttype contract.resultparameter contract.actiontype contract.actionparameter > apps/contract/fixtures/initial_data.json
