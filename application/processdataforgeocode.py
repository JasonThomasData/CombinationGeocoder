import filehandler

class ProcessDataForGeocode:

    def __init__(self):
        self.query_strings = []

    def join_geo_columns(self, columns_to_geocode):
        return '%2C'.join(columns_to_geocode)

    def remove_white_spaces(self, remove_white_in_this_query):
        return remove_white_in_this_query.replace(' ', '%20')

    def add_rows_to_q_string_list(self, csv_rows_to_process):
        for row in csv_rows_to_process:
            columns_to_geocode = [row[2], row[3], row[4]] #currently using magic numbers, find a way to define these in the top level.
            q_string = self.join_geo_columns(columns_to_geocode)
            q_string_no_spaces = self.remove_white_spaces(q_string)
            self.query_strings.append(q_string_no_spaces)
        return self.query_strings