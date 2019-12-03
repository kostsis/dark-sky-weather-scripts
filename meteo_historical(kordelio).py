# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 12:13:33 2019

@author: kosts
"""
import sys
import os
import json
import csv
import requests 
import datetime
from datetime import timedelta, date,datetime
#%% Get console arguments
input_folder_path = r"C:\Users\kosts\Documents\ΑΠΘ\Computational Physics\Διπλωματική\Darksky\Kordelio\json"
output_file_path = r"C:\Users\kosts\Documents\ΑΠΘ\Computational Physics\Διπλωματική\Darksky\Kordelio\data.csv"
api_key= r"8f4369599392b10009e816c54c86707e"
api_key= r"0c4e12dbf04459f645e3464f71dbaf5d"
#%% Create target CSV file
output_file = open(
    file = output_file_path,
    mode = "wt",
    newline = "")

#%% Create a csv writer
csv_writer = csv.writer(output_file)

#%% Write header to file
csv_writer.writerow(["Date", "Latitude", "Longitude", "Humidity","Temperature","Wind speed","Wind Bearing","Visibility","Cloud cover","Nearest station"])

#%% Get list of files in source folder
input_files = os.listdir(input_folder_path)

#%% Process each source file
for input_file_name in input_files:

    # Create source file path
    source_file_path = os.path.join(
        input_folder_path, 
        input_file_name)
    
    # Open the source file
    source_file = open(source_file_path)
    
    # Load the JSON data
    json_data = json.load(source_file)
    
    # Close the source file
    source_file.close()
    
    # Get fields from JSON data
    date=datetime.fromtimestamp(int(input_file_name.replace(".json", ""))).strftime('%Y-%m-%d %H:%M:%S')
    #date = input_file_name.replace(".json", "")
    latitude = json_data["latitude"]
    longitude = json_data["longitude"]
    
    # Get daily data from JSON data
    daily_data = json_data["daily"]["data"][0]
    
    nearest_station=json_data["flags"]["nearest-station"]
    try:
        temperature=json_data["currently"]["temperature"]
    except KeyError:
        temperature=0
    try:
        humidity = json_data["currently"]["humidity"]
    except KeyError:
        humidity=0
        
    try:
        wind_speed=json_data["currently"]["windSpeed"]
    except KeyError:
        wind_speed=0
    
    try:
        wind_bearing=json_data["currently"]["windBearing"]
    except KeyError:
        wind_bearing=0
    
    try:
        visibility=json_data["currently"]["visibility"]
    except KeyError:
        visibility=0
    
    try:
        cloud_cover=json_data["currently"]["cloudCover"]
    except KeyError:
        wind_speed=0
        continue
    
    # Write CSV data to target file
    csv_writer.writerow([date, latitude, longitude, humidity,temperature, wind_speed,wind_bearing,visibility,cloud_cover,nearest_station])

#%% Close the target file
output_file.close()