#!/bin/bash

# #.IGNORE:
# .DEFAULT_GOAL := init

build:
	docker-compose build

init:
	docker-compose run app sh -c "django-admin startproject app ."
	