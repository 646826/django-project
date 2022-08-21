#!/bin/bash

# #.IGNORE:
# .DEFAULT_GOAL := init

source_folder="src"
app_name = "app"

clear:
	rm ${source_folder} -f -d -r

prepare:
	mkdir -p ${source_folder}
	docker-compose run app sh -c "django-admin startproject ${app_name} ."
	cp ./etalon_files/settings.py ./${source_folder}/${app_name}/
	# cp ./etalon_files/.flake8 ./${source_folder}/

build:
	docker-compose build

up:
	docker-compose -f ./docker-compose.yml up

# cl:
# 	docker stop $(docker ps -a -q)
# 	# docker rm $(docker ps -a -q)
# 	# docker system prune -a -f