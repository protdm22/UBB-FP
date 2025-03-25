def create_flight(flight_code, flight_duration, flight_departure, flight_destination):
    return {"code": flight_code, "duration": flight_duration, "departure_city": flight_departure,
            "destination_city": flight_destination}


def get_flight_code(flight):
    return flight["code"]


def get_flight_duration(flight):
    return flight["duration"]


def get_flight_departure(flight):
    return flight["departure_city"]


def get_flight_destination(flight):
    return flight["destination_city"]


def set_flight_code(flight, new_code):
    flight["code"] = new_code


def set_flight_duration(flight, new_duration):
    flight["duration"] = new_duration


def set_flight_departure(flight, new_departure):
    flight["departure_city"] = new_departure


def set_flight_destination(flight, new_destination):
    flight["destination_city"] = new_destination


def flight_to_string(flight):
    return f"Flights with code '{flight["code"]}' has the duration of {flight["duration"]} minutes, the departure city of '{flight["departure_city"]}' and the destination city of '{flight["destination_city"]}'"


def test_add_new_flight():
    test_list_of_flights = []

    # test for valid flights
    add_new_flight(test_list_of_flights, "0X123", 120, "Cluj-Napoca", "Sibiu")
    add_new_flight(test_list_of_flights, "0X456", 80, "Iasi", "Cluj-Napoca")
    add_new_flight(test_list_of_flights, "0X789", 40, "Cluj-Napoca", "Brasov")

    assert test_list_of_flights == [
        {"code": "0X123", "duration": 120, "departure_city": "Cluj-Napoca", "destination_city": "Sibiu"},
        {"code": "0X456", "duration": 80, "departure_city": "Iasi", "destination_city": "Cluj-Napoca"},
        {"code": "0X789", "duration": 40, "departure_city": "Cluj-Napoca", "destination_city": "Brasov"}
    ]


def add_new_flight(list_of_flights: list, flight_code, flight_duration, flight_departure, flight_destination):
    """
    Function that adds a new flight to the list of flights
    :param list_of_flights: the list of flights
    :param flight_code: the code of the new flight
    :param flight_duration: the duration of the new flight
    :param flight_departure: the name of the departure city of the new flight
    :param flight_destination: the name of the destination city of the new flight
    :return: None
    """
    if len(flight_code) < 3:
        raise ValueError("The length of the flight code must be at least 3 characters")
    if flight_duration < 20:
        raise ValueError("The duration of the flight must be at least 20 minutes long")
    if len(flight_departure) < 3:
        raise ValueError("The length of the flight departure city must be at least 3 characters")
    if len(flight_destination) < 3:
        raise ValueError("The length of the flight destination city must be at least 3 characters")
    new_flight = create_flight(flight_code, flight_duration, flight_departure, flight_destination)
    list_of_flights.append(new_flight)


def modify_flight_duration(list_of_flights, flight_code, new_flight_duration):
    flight_exists = 0
    if new_flight_duration < 20:
        raise ValueError("The duration of a flight must be at least 20 minutes long")
    for i in range(len(list_of_flights)):
        if get_flight_code(list_of_flights[i]) == flight_code:
            flight_exists = 1
            set_flight_duration(list_of_flights[i], new_flight_duration)

    if flight_exists == 0:
        raise ValueError(f"The flight '{flight_code}' does not exist")


def reroute_flights(list_of_flights, initial_destination_city, new_destination_city):
    if len(initial_destination_city) < 3:
        raise ValueError("The length of the initial destination city must be at least 3 characters")
    if len(new_destination_city) < 3:
        raise ValueError("The length of the new initial destination city must be at least 3 characters")

    city_exists = 0
    for i in range(len(list_of_flights)):
        if get_flight_destination(list_of_flights[i]).lower() == initial_destination_city.lower():
            city_exists = 1
            set_flight_destination(list_of_flights[i], new_destination_city)

    if city_exists == 0:
        raise ValueError(f"No flights found with the initial destination city {initial_destination_city}")


def return_list_of_flights_with_a_given_departure_city(list_of_flights, departure_city):
    list_to_return = []
    for i in range(len(list_of_flights)):
        if get_flight_departure(list_of_flights[i]).lower() == departure_city.lower():
            list_to_return.append(list_of_flights[i])

    return list_to_return
