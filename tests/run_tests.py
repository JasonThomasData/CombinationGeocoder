#! usr/bin/env python

import os, sys

parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

import sendrequesttoapi

send_request_to_api = sendrequesttoapi.SendRequestToAPI

def q_string_format_google():
	query = 'https://maps.googleapis.com/maps/api/geocode/json?address=2000%20NSW%20Australia&key=AIzaSyBELuMoNvl-9pyEZ2v4sjcZ1f8yE7aCTis'
	assert send_request_to_api.send_request(query, 'google') == True #[-33.8657305,151.20733]