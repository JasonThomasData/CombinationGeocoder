import filehandler

class Application:

    def __init__(self):
        self.file_name = '/home/john/Desktop/python/myScripts/CombinationGeocoderNFG/postcodesData/australian-postcodes_test.csv'
        self.file_handler = filehandler.FileHandler()
        self.geo_column_numbers = [1,2,3]
        self.query_strings = []
        self.csv_rows = file_handler.read_file(self.file_name)

    def join_geo_columns(self, columns_to_geocode):
        return '%2C'.join(columns_to_geocode)

    def remove_white_spaces(self, remove_white_in_this_query):
        return remove_white_in_this_query.replace(' ', '%20')

    def add_rows_to_q_string_list(self):
        for row in self.csv_rows:
            columns_to_geocode = [row[1], row[2], row[3]]
            q_string = self.join_geo_columns(columns_to_geocode)
            q_string_no_spaces = self.remove_white_spaces(q_string)
            self.query_strings.append(q_string_no_spaces)
        return iterate_over_q_strings(self.query_strings, self.file_name)