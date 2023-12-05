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
class Battery:
    """a simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=40):
        """initialize battery's attributes"""
        self.battery_size=battery_size
    def describe_battery(self):
        """print a statement describe the battery size"""
        print(f"this car has a {self.battery_size} battery")
    def get_range(self):
        """print a statement about the range this battery provides"""
        if self.battery_size==40:
            range=150
        elif self.battery_size==65:
            range=225
        print(f"this car can go about {range} miles on a full charge")
class ElectricCar(Car):
    """represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model , year):
        """initialize attributes of the parent class"""
        super().__init__(make, model , year)
        self.battery=Battery()
    
    def fill_gas_tank(self):
        """electric cars don't have gas tank"""
        print("this car doesn't have a gas tank")

my_leaf=ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()