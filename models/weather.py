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
    ti700 = db.Column(db.Float())
    ti800 = db.Column(db.Float())
    ti850 = db.Column(db.Float())
    ti900 = db.Column(db.Float())
    num_ti = db.Column(db.Integer())
    lifted_index = db.Column(db.Float())
    cape = db.Column(db.Float())
    conv_inh = db.Column(db.Float())
    helicity = db.Column(db.Float())
    cloudwater = db.Column(db.Float())
    cloudice = db.Column(db.Float())
    
    def __init__(self, country,
                       location_name,
                       date_hour,
                       temp,
                       cloud,
                       wind_dir,
                       wind_speed,
                       gust_speed,
                       dry_h,
                       soar_h,
                       b_level_height,
                       freezing_height,
                       ti700,
                       ti800,
                       ti850,
                       ti900,
                       num_ti,
                       lifted_index,
                       cape,
                       conv_inh,
                       helicity,
                       cloudwater,
                       cloudice):
        self.country = country
        self.location_name = location_name
        self.date_hour = date_hour
        self.temp = temp
        self.cloud = cloud
        self.wind_dir = wind_dir
        self.wind_speed = wind_speed
        self.gust_speed = gust_speed
        self.dry_h = dry_h
        self.soar_h = soar_h
        self.b_level_height = b_level_height
        self.freezing_height = freezing_height
        self.ti700 = ti700
        self.ti800 = ti800
        self.ti850 = ti850
        self.ti900 = ti900
        self.num_ti = num_ti
        self.lifted_index = lifted_index
        self.cape = cape
        self.conv_inh = conv_inh
        self.helicity = helicity
        self.cloudwater = cloudwater
        self.cloudice = cloudice
        
    ### returns json version of the name and price tuple
    def json(self):
        return {'country': self.country, 
                'location_name': self.location_name,
                'date_hour': self.date_hour,
                'temp': self.temp,
                'cloud': self.cloud,
                'wind_dir': self.wind_dir,
                'wind_speed': self.wind_speed,
                'gust_speed': self.gust_speed,
                'dry_h': self.dry_h,
                'soar_h': self.soar_h,
                'b_level_height': self.b_level_height,
                'freezing_height': self.freezing_height,
                'ti700': self.ti700,
                'ti800': self.ti800,
                'ti850': self.ti850,
                'ti900': self.ti900,
                'num_ti': self.num_ti,
                'lifted_index': self.lifted_index,
                'cape': self.cape,
                'conv_inh': self.conv_inh,
                'helicity': self.helicity,
                'cloudwater': self.cloudwater,
                'cloudice': self.cloudice}
