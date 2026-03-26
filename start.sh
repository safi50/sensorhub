#!/bin/sh
set -e

echo "[sensorhub] Initializing database..."

flask --app=sensorhub init-db
echo "[sensorhub] Generating test data..."
flask --app=sensorhub testgen
echo "[sensorhub] Generating master key file..."
flask --app=sensorhub masterkey > /tmp/masterkey.txt
echo "[sensorhub] MASTER KEY: $(cat /tmp/masterkey.txt)"

echo "[sensorhub] Initialization complete. Service is running on 0.0.0.0:8000"
exec gunicorn -w 3 -b 0.0.0.0:8000 'sensorhub:create_app()'