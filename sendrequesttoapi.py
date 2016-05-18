#! usr/bin/env python

import requests
import resultsformatter

results_formatter = resultsformatter.ResultsFormatter()

class SendRequestToAPI:
    
    def process_result(self, service_name, json_data):
        lat_lng_result = []
        try:
            if(service_name == 'google'):
                results = results_formatter.format_google(json_data)
                elem1, elem2 = results[0], results[1]
            elif(service_name == 'pickP'):
                results = results_formatter.format_pick_point(json_data)
                elem1, elem2 = results[0], results[1]
            elif(service_name == 'bing'):
                results = results_formatter.format_bing(json_data)
                elem1, elem2 = results[0], results[1]
            elif(service_name == 'openC'):
                results = results_formatter.format_open_cage(json_data)
                elem1, elem2 = results[0], results[1]
            elif(service_name == 'mapQ'):
                results = results_formatter.format_map_quest(json_data)
                elem1, elem2 = results[0], results[1]
        except IndexError:
            elem1 = 'Index Error'
            elem2 = 'Index Error'
        except ValueError:
            elem1 = 'Value Error'
            elem2 = 'Value Error'
        if type(elem1) == unicode:
            elem1 == float(elem1)
        if type(elem2) == unicode:
            elem2 == float(elem2)
        lat_lng_result.append(elem1)
        lat_lng_result.append(elem2)
        return lat_lng_result

    def send_request(self, url, service_name):
        r = requests.get(url)
        json_data = r.json()
        return self.process_result(service_name, json_data)