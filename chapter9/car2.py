"""a class that can be used to represent a car"""
class Car:
    """a simple attempt to represent a car"""
    def __init__(self, make, model , year):
        """initialize attributes to describe a car"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name=f'{self.year} {self.make} {self.model}'
        return long_name.title()
    def update_odometer(self, mileage):
        """set the odometer reading to the given value"""
        if mileage>self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer")
    def read_odometer(self):
        """print a statement showing the car's mileage"""
        print(f"this car has {self.odometer_reading} miles on it")
    def increment_odometer(self, miles):
        self.odometer_reading+=miles