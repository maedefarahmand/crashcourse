class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"the restaurant's name is {self.restaurant_name} and it has a {self.cuisine_type} cuisine") 
    def open_restaurant(self):
        print("the restaurant is open")
a=Restaurant('sindi', 'good')
b=Restaurant('adi', 'well')
c=Restaurant('amy', 'good')
a.describe_restaurant()
b.describe_restaurant()
c.describe_restaurant()