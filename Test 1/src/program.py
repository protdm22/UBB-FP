from src.functions import test_add_new_flight
from ui import menu

if __name__ == "__main__":
    list_of_flights = [
        {"code": "0G6762", "duration": 400, "departure_city": "Cluj-Napoca",
         "destination_city": "Iasi"},
        {"code": "0G4280", "duration": 300, "departure_city": "Cluj-Napoca",
         "destination_city": "Paris"},
        {"code": "0G2357", "duration": 600, "departure_city": "Bucharest",
         "destination_city": "Paris"}
    ]
    test_add_new_flight()
    menu(list_of_flights)
