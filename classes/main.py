from driver import Driver
from passenger import Passenger
from travel import Travel
from travelManager import TravelManager

Passenger_name = input("Enter passenger name: ")
Passenger_family = input("Enter passenger family: ")
Passenger_fromx = float(input("Enter passenger fromx: "))
Passenger_fromy = float(input("Enter passenger fromy: "))
Passenger_tox = float(input("Enter passenger tox: "))
Passenger_toy = float(input("Enter passenger toy: "))
print("--------------------------------------------------------------------------")
print("\n")

passenger = Passenger(Passenger_name, Passenger_family, Passenger_fromx, Passenger_fromy, Passenger_tox, Passenger_toy)

Driver1 = Driver("Jamal", "Davoodi", 10.0, 20.0)
Driver2 = Driver("Ali", "Rezaei", 15.0, 25.0)
Driver3 = Driver("Sara", "Mohammadi", 5.0, 30.0)

travel = Travel(passenger)

print(travel.show_travel_info())
print(f"Total price of travel: {travel.price_of_travel():.2f} currency units")

travel.start_travel()
travel.end_travel()

manager = TravelManager()
manager.add_travel(travel)
manager.show_all_travels()
print(manager.total_income())

print("\n---------------------------------------------------------------")
