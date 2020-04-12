# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:44:52 2020

@author: pawel
"""
from db import db

class WeatherModel(db.Model):
    __tablename__ = 'weather_data'
    
    id = db.Column(db.Integer, primary_key = True)
    country = db.Column(db.String(80))
    location_name = db.Column(db.String(80))
    date_hour = db.Column(db.String(80))
    temp = db.Column(db.Float())
    cloud = db.Column(db.String(80))
    wind_dir = db.Column(db.String(80))
    wind_speed = db.Column(db.Float())
    gust_speed = db.Column(db.Float())
    dry_h = db.Column(db.Float())
    soar_h = db.Column(db.Float())
    b_level_height = db.Column(db.Float())
    freezing_level = db.Column(db.Float())
    TI700 = db.Column(db.Float())
    TI800 = db.Column(db.Float())
    TI850 = db.Column(db.Float())
    TI900 = db.Column(db.Float())
    num_ti = db.Column(db.Integer())
    lifted_index = db.Column(db.Float())
    cape = db.Column(db.Float())
    conv_inh = db.Column(db.Float())
    helicity = db.Column(db.Float())
    cloudwater = db.Column(db.Float())
    cloudice = db.Column(db.Float())
    
    def __init__(self, id):
        self._id = id
    
    ### returns json version of the name and price tuple
    def json(self):
        return {'_id': self._id}
