import json
from flask import Response, request, url_for
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest, Conflict, UnsupportedMediaType

from sensorhub import db, cache
from sensorhub.constants import JSON
from sensorhub.models import Measurement
from sensorhub.utils import page_key

class MeasurementCollection(Resource):

    PAGE_SIZE = 50

    @cache.cached(timeout=None, make_cache_key=page_key, response_filter=lambda r: False)
    def get(self, sensor):
        try:
            page = int(request.args.get("page", 0))
        except ValueError as e:
            raise BadRequest(description=str(e))

        remaining = Measurement.query.filter_by(
            sensor=sensor
        ).order_by("time").offset(page * self.PAGE_SIZE)
        body = {
            "sensor": sensor.name,
            "measurements": []
        }
        for meas in remaining.limit(self.PAGE_SIZE):
            body["measurements"].append(meas.serialize())

        response = Response(json.dumps(body), 200, mimetype=JSON)
        if len(body["measurements"]) == self.PAGE_SIZE:
            cache.set(page_key(), response, timeout=None)
        return body

    def post(self, sensor):
        # replace with your answer from exercise "POSTing it All Together"
        raise NotImplementedError


class MeasurementItem(Resource):

    def delete(self, sensor, measurement):
        pass
