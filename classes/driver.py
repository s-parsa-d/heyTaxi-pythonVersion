list_of_drivers = []

class Driver:
    def __init__(self, name, family, fromx, fromy):
        self.name = name
        self.family = family
        self.fromx = fromx
        self.fromy = fromy
        driver_info = {
            'Name': self.name,
            'Family': self.family,
            'FromX': self.fromx,
            'FromY': self.fromy
        }
        list_of_drivers.append(driver_info)
