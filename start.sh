#!/bin/sh

flask --app=sensorhub init-db
flask --app=sensorhub testgen
flask --app=sensorhub masterkey > /tmp/masterkey.txt

gunicorn -w 3 -b 0.0.0.0 sensorhub:create_app()