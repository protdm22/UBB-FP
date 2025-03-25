from src.functions import add_new_flight, flight_to_string, modify_flight_duration, \
    reroute_flights, return_list_of_flights_with_a_given_departure_city, get_flight_duration

OPTION_ADD = 1
OPTION_MODIFY_DURATION = 2
OPTION_REROUTE = 3
OPTION_SHOW_FLIGHTS = 4


def request_input_for_new_flight():
    flight_code = input("Enter the code of the new flight: ")
    flight_duration = int(input("Enter the duration of the new flight: "))
    flight_departure = input("Enter the departure city of the new flight: ")
    flight_destination = input("Enter the destination city of the new flight: ")
    return flight_code, flight_duration, flight_departure, flight_destination


def print_menu():
    print("#######################################")
    print("[1] Add a new flight")
    print("[2] Modify the duration of a flight")
    print("[3] Reroute flights")
    print("[4] Show all flights from a given departure city")
    print("Enter your choice:")


def menu(list_of_flights):
    while True:
        print_menu()
        user_choice = 0
        try:
            user_choice = int(input(">>> "))
        except ValueError:
            pass

        if user_choice == OPTION_ADD:
            flight_code, flight_duration, flight_departure, flight_destination = request_input_for_new_flight()
            try:
                add_new_flight(list_of_flights, flight_code, flight_duration, flight_departure, flight_destination)
            except ValueError as add_error_message:
                print(f"ERROR! {add_error_message}")

        elif user_choice == OPTION_MODIFY_DURATION:
            flight_code = input("Enter the code of the flight: ")
            new_duration = int(input(f"Enter the new duration for flight {flight_code}: "))
            try:
                modify_flight_duration(list_of_flights, flight_code, new_duration)
            except ValueError as modify_error_message:
                print(f"ERROR! {modify_error_message}")

        elif user_choice == OPTION_REROUTE:
            initial_destination_city = input("Enter the name of the initial destination city: ")
            new_destination_city = input("Enter the name of the city to which you want to reroute the flights to: ")
            try:
                reroute_flights(list_of_flights, initial_destination_city, new_destination_city)
            except ValueError as reroute_error_message:
                print(f"ERROR! {reroute_error_message}")

        elif user_choice == OPTION_SHOW_FLIGHTS:
            given_departure_city = input("Enter the name of the departure city: ")
            list_to_print = return_list_of_flights_with_a_given_departure_city(list_of_flights, given_departure_city)
            list_to_print.sort(key=get_flight_duration)
            for i in range(len(list_to_print)):
                print(flight_to_string(list_to_print[i]))
