# -*- coding: utf-8 -*-

from flask_restful import Resource
from models.weather import WeatherModel

class WeatherList(Resource):
    def get(self):
         return {'weather': [item.json() for item in WeatherModel.query.all()]}
