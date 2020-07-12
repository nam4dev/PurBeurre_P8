#!/usr/bin/env bash

coverage erase
coverage run --source='.'  manage.py test
coverage html
