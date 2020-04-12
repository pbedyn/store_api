# -*- coding: utf-8 -*-

from flask_restful import Resource
from models.weather import WeatherModel

class WeatherList(Resource):
    def get(self):
        return WeatherModel.get_all_data().json()
