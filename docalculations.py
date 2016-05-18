class DoCalculations:

    def get_average(self, values_to_get_average):

        def increment_sum(sum_lng_or_lat, new_addition):
            return sum_lng_or_lat + new_addition

        def increment_numerator(divide_by):
            return divide_by + 1

        def get_average(sum_of_coords,divide_by):
            return sum_of_coords / divide_by

        sum_of_lat = 0.0
        divide_lat_by = 0
        sum_of_lng = 0.0
        divide_lng_by = 0

        for geocode_result_tuple in values_to_get_average:
            print geocode_result_tuple
            if geocode_result_tuple[0] != 'Index Error' and geocode_result_tuple[0] != 'Value Error':
                new_lat_to_add = float(geocode_result_tuple[0])
                new_lng_to_add = float(geocode_result_tuple[1])
                sum_of_lat = increment_sum(sum_of_lat, new_lat_to_add)
                sum_of_lng = increment_sum(sum_of_lng, new_lng_to_add)
                divide_lat_by = increment_numerator(divide_lat_by)
                divide_lng_by = increment_numerator(divide_lng_by)
        
        avg_lat = get_average(sum_of_lat,divide_lat_by)
        avg_lng = get_average(sum_of_lng,divide_lng_by)
        return [avg_lat, avg_lng]

    #Range of successful geocoded points
    def get_range(self, rowArray):

        def check_number(list_to_check):
            list_of_numerical_tuples = []
            for elem in list_to_check:
                if type(elem[0]) == float or type(elem[0]) == int:
                    list_of_numerical_tuples.append(elem)
            return list_of_numerical_tuples

        elements_to_consider_in_range = check_number(rowArray)
        min_lat = elements_to_consider_in_range[0][0]
        min_lng = elements_to_consider_in_range[0][1]
        max_lat = elements_to_consider_in_range[0][0]
        max_lng = elements_to_consider_in_range[0][1]

        for get_coords_range in elements_to_consider_in_range:
            if min_lat < get_coords_range[0]:
                min_lat = get_coords_range[0]
            if min_lng < get_coords_range[1]:
                min_lng = get_coords_range[1]
            if max_lat > get_coords_range[0]:
                max_lat = get_coords_range[0]
            if max_lng > get_coords_range[1]:
                max_lng = get_coords_range[1]
        range_lat = max_lat - min_lat
        range_lng = max_lng - min_lng
        return [range_lat, range_lng]