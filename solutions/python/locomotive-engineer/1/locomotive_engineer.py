"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    wagon_list=args
    
    return list(wagon_list)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    each_wagons_id=[2, 5, 1, 7, 4, 12, 6, 3, 13]
    missing_wagons=[3, 17, 6, 15]
    """
    first_id,second_id,*rest=each_wagons_id
    first_comb=*rest,first_id,second_id
    first_id2,*rest2=first_comb
    fin_comb=first_id2,*missing_wagons,*rest2
    return list(fin_comb)
    


def add_missing_stops(route,**kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    route={"from": "New York", "to": "Miami"}
    stop_1="Washington DC",
    stop_2="Charlotte"
    -----------
    stop_dict={"stop_1":"Washington DC","stop_2":"Charlotte"}
    """
    stop_dict=kwargs
    route["stops"]=list(stop_dict.values())
    return route
    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extend_route={**route,**more_route_information}
    return extend_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    first,sec,third=wagons_rows
    red1,red2,red3=first
    blue1,blue2,blue3=sec
    orange1,orange2,orange3=third
    first_new=red1,blue1,orange1
    sec_new=red2,blue2,orange2
    third_new=red3,blue3,orange3
    fin_list=list(first_new),list(sec_new),list(third_new)
    return list(fin_list)
    
