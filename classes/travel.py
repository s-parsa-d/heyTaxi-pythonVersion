import driver
import passenger
from datetime import datetime
class Travel:
    def __init__(self, passenger):
        self.passenger = passenger
        self.driver = None

    def choose_driver(self):
        if not list_of_drivers:
            return None
        min_distance = float('inf')
        chosen_driver = None
        for driver in list_of_drivers:
            dx = self.passenger.fromx - driver['FromX']
            dy = self.passenger.fromy - driver['FromY']
            distance = (dx ** 2 + dy ** 2) ** 0.5
            if distance < min_distance:
                min_distance = distance
                chosen_driver = driver
        self.driver = chosen_driver
        return chosen_driver

    def show_travel_info(self):
        chosen_driver = self.choose_driver()
        if not chosen_driver:
            return "No driver found."
        return (f"Passenger: {self.passenger.name} {self.passenger.family}, "
                f"Driver: {chosen_driver['Name']} {chosen_driver['Family']}, "
                f"Distance: {self.passenger.distance:.2f} units")

    def price_of_travel(self):
        if not self.driver:
            self.choose_driver()
        if not self.driver:
            return 0.0
        distance_to_pickup = ((self.passenger.fromx - self.driver['FromX']) ** 2 +
                              (self.passenger.fromy - self.driver['FromY']) ** 2) ** 0.5
        price = (self.passenger.distance * 10) + (distance_to_pickup * 5) + 50
        return price

    def start_travel(self):
        if not self.driver:
            print("Cannot start travel: no driver assigned.")
            return
        now = datetime.now()
        start_time = now.strftime("%H:%M:%S")
        print(f"Travel started at {start_time}.")
        print(f"Travel started with driver {self.driver['Name']} {self.driver['Family']}.")

    def end_travel(self):
        now = datetime.now()
        end_time = now.strftime("%H:%M:%S")
        print(f"Travel ended at {end_time}.")
        print(f"Travel from ({self.passenger.fromx},{self.passenger.fromy}) to "
              f"({self.passenger.tox},{self.passenger.toy}) completed.")
    
