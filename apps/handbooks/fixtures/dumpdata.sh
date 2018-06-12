#!/bin/sh
./manage.py dumpdata --indent 4 --natural-primary handbooks.insurancetype handbooks.paymenttype handbooks.carmark handbooks.carmodel handbooks.addresstype handbooks.contacttype handbooks.credentialtype handbooks.insurancecontractstatus > apps/handbooks/fixtures/initial_data.json
