class ResultsFormatter:
    
    def format_google(self, json_data):
        elem1 = json_data['results'][0]['geometry']['location']['lat']
        elem2 = json_data['results'][0]['geometry']['location']['lng']    
        return [elem1, elem2]

    def format_pick_point(self, json_data):
        elem1 = json_data[0]['lat']
        elem2 = json_data[0]['lon']
        return [elem1, elem2]

    def format_bing(self, json_data):
        elem1 = json_data['resourceSets'][0]['resources'][0]['point']['coordinates'][0]
        elem2 = json_data['resourceSets'][0]['resources'][0]['point']['coordinates'][1]
        return [elem1, elem2]

    def format_open_cage(self, json_data):
        elem1 = json_data['results'][0]['geometry']['lat']
        elem2 = json_data['results'][0]['geometry']['lng']
        return [elem1, elem2]

    def format_map_quest(self, json_data):
        elem1 = json_data['results'][0]['locations'][0]['latLng']['lat']
        elem2 = json_data['results'][0]['locations'][0]['latLng']['lng']
        return [elem1, elem2]