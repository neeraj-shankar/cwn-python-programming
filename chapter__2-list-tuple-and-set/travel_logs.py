from useful_formats import equal_lines_formatting


class TravelHistory:

    def list_into_dictionary(self):
        travel_log = {
            'France' : ['Paris', 'Lille', 'Dijon'],
            'Germany': ['Berlin', 'Hamburg', 'Stuttgart'],
        }

        travel_log_detailed = {
             'France': {
             'visited_city': ['Paris', 'Lille', 'Dijon'],
            },
            'Germany': {'places_visited': ['Berlin', 'Hamburg', 'Stuttgart'],}
        }

        # Print the travel log
        equal_lines_formatting()
        print(travel_log)
        equal_lines_formatting()
        print(travel_log_detailed)
        equal_lines_formatting()   

    """
    Nested dictionary inside a list
    """ 
    def dict_into_list(self):
        travel_log = [
            {
             'country': 'India',
             'city_visited': ['Indore', 'Pune', 'New Delhi'],
             'total_visits': 10,

            },
            {
            'country': 
            },
            
                    ]

if __name__ == '__main__':
    # object of the TravelHistory
    obj_travel = TravelHistory()

    obj_travel.list_into_dictionary()
