#! usr/bin/env python

import csv, json, requests, os

import qstringformatter, filehandler, docalculations, processdataforgeocode

q_string_formatter = qstringformatter.QStringFormatter()
file_handler = filehandler.FileHandler()
do_calculations = docalculations.DoCalculations()
process_data_for_geocode = processdataforgeocode.ProcessDataForGeocode()

#Read the file first and then add to it
def save_to_csv(new_data, file_name, i):
    csv_rows = file_handler.read_file(file_name)
    file_handler.save_file(file_name, csv_rows, new_data, i)

#Takes a list of tuples and returns a list of single elems
def split_array_elements(array_to_process):
    results_after_split = []
    for tuple_to_split in array_to_process:
        results_after_split.append(tuple_to_split[0])
        results_after_split.append(tuple_to_split[1])
    return results_after_split

#Receives queryStrings from _init_()
def iterate_over_q_strings(query_strings, file_name, range_iter_limits):
    lower_limit = range_iter_limits[0]
    upper_limit = range_iter_limits[1]
    new_data = ['google_pos_lat','google_pos_lng', 'open_cage_result_lat', 'open_cage_result_lng', 'pick_point_result_lat','pick_point_result_lng', 'map_quest_result_lat', 'map_quest_result_lng', 'average_lat', 'average_lng', 'range_lat', 'range_lng']
    save_to_csv(new_data, file_name, 0) #Because this is the heading data
    for i in range(lower_limit, upper_limit):
        google_result = q_string_formatter.google_maps_geocode(query_strings[i])
        open_cage_result = q_string_formatter.open_cage_geocode(query_strings[i])
        pick_point_result = q_string_formatter.pick_point_geocode(query_strings[i])
        map_quest_result = q_string_formatter.map_quest_geocode(query_strings[i])
        #bing_result = q_string_formatter.bing_maps_geocode(single_q_string, k, rowArray) Up to 50 per day, then it costs.

        new_data = [google_result,open_cage_result,pick_point_result,map_quest_result]   
        average_lat_lng = do_calculations.get_average(new_data) 
        range_lat_lng = do_calculations.get_range(new_data)
        new_data.append(average_lat_lng)
        new_data.append(range_lat_lng)
        split_row_to_add = split_array_elements(new_data)
        save_to_csv(split_row_to_add, file_name, i)

class Application:

    def __init__(self, lower_limit, upper_limit):
        self.file_name = '../files_for_geo/locations_after_geo.csv'
        self.file_handler = filehandler.FileHandler()
        self.geo_column_numbers = [2,3,4]
        self.query_strings = []
        self.csv_rows = file_handler.read_file(self.file_name)
        self.range_iter_limits = [lower_limit, upper_limit]

app = Application(1,50)
list_of_query_strings = process_data_for_geocode.add_rows_to_q_string_list(app.csv_rows)
iterate_over_q_strings(list_of_query_strings, app.file_name, app.range_iter_limits)

#This project is undergoing a major refactor
#However, it's working well enough for me to geocode addresses now.

#Geocode this file in blocks of 1200 and tick them off as you go.

'''
1 - 600
601 - 1200
1201 - 1800
1801 - 2400
2401 - 3000
3601 - 4200
4201 - 4800
4801 - 5400
5401 - 6000
6001 - 6600
6601 - 7200
7201 - 7800
7801 - 8400
8401 - 9000
9001 - 9600
9601 - 10200
10201 - 10800
10801 - 11400
11401 - 12000
12001 - 12600
12601 - 13200
13201 - 13800
13801 - 14400
14401 - 15000
15001 - 15600
15601 - 16200
16201 - 16800
'''