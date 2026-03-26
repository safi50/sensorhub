FROM python:3.13-alpine
WORKDIR /opt/sensorhub
COPY . .
RUN pip install .
COPY start.sh .
RUN chmod +x start.sh
CMD ["sh", "start.sh"]