#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:43:06 2019

@author: teorf
"""
import requests 
import datetime 
import time
from datetime import timedelta, date,datetime
def daterange(start_date, end_date,delta=timedelta(hours=1)):
    single_date=start_date
    while single_date<end_date:
        yield single_date
        single_date+=delta
#api_key= r"8f4369599392b10009e816c54c86707e"
api_key= r"0c4e12dbf04459f645e3464f71dbaf5d"        
start_date = datetime(2018, 1, 1, 0, 0)
end_date = datetime(2018, 2, 1, 0, 0)
for single_date in daterange(start_date, end_date):
    #print(single_date.strftime("%Y-%m-%d,%H:%M"))
    unixtime = time.mktime(single_date.timetuple())
    #print(unixtime)
    URL = " https://api.darksky.net/forecast/0c4e12dbf04459f645e3464f71dbaf5d/40.66964,22.89416,%s?units=si"%int(unixtime)
    
    r = requests.get(url = URL)

    data = r.json() 
    import json

    with open('json/%s.json'%int(unixtime), 'w') as json_file:
        json.dump(data, json_file)