import config, sendrequesttoapi

send_request_to_api = sendrequesttoapi.SendRequestToAPI()

class QStringFormatter:

    def google_maps_geocode(self, query_string):
        google_maps_options = "json"
        google_maps_API_key = config.google_maps_API_key
        google_maps_url = "https://maps.googleapis.com/maps/api/geocode/" + google_maps_options + "?address=" + query_string + "&key=" + google_maps_API_key
        return send_request_to_api.send_request(google_maps_url, 'google')

    def open_cage_geocode(self, query_string):
        openCageOptions = "json"
        open_cage_API_key = config.open_cage_API_key
        open_cage_url = "http://api.opencagedata.com/geocode/v1/" + openCageOptions + "?q=" + query_string + "&key=" + open_cage_API_key
        return send_request_to_api.send_request(open_cage_url, 'openC')

    def pick_point_geocode(self, query_string):
        pick_point_API_key = config.pick_point_API_key
        pick_point_url = "https://pickpoint.io/api/v1/forward?key=" + pick_point_API_key + "&q=" + query_string
        return send_request_to_api.send_request(pick_point_url, 'pickP')

    def map_quest_geocode(self, query_string):
        map_quest_options = "outFormat=json"
        map_quest_API_key = config.map_quest_API_key
        map_quest_url = "http://www.mapquestapi.com/geocoding/v1/address?&" + map_quest_options + "&key=" + map_quest_API_key + "&location=" + query_string
        return send_request_to_api.send_request(map_quest_url, 'mapQ')

    def bing_maps_geocode(self, query_string): 
        bing_options = "o=json"
        bing_API_key = config.bing_API_key
        bing_url = "http://dev.virtualearth.net/REST/v1/Locations/" + query_string + "?" + bing_options + "&key=" + bing_API_key
        return send_request_to_api.send_request(bing_url, 'bing')