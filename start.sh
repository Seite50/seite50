#!/bin/bash

python ./manage test && python ./manage.py migrate && python ./manage.py runserver