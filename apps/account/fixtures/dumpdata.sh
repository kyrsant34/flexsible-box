#!/bin/sh
./manage.py dumpdata --indent 4 --natural-primary account.department account.user > apps/account/fixtures/initial_data.json
