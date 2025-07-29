class TravelManager:
    def __init__(self):
        self.travels = []

    def add_travel(self, travel):
        self.travels.append(travel)

    def show_all_travels(self):
        if not self.travels:
            print("No travels recorded.")
            return
        for i, travel in enumerate(self.travels, 1):
            print(f"--- Travel {i} ---")
            print(travel.show_travel_info())
            print(f"Price: {travel.price_of_travel():.2f}")

    def total_income(self):
        total = sum(travel.price_of_travel() for travel in self.travels)
        return f"Total income from all travels: {total:.2f} currency units"
    