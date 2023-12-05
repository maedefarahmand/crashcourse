class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"the restaurant's name is {self.restaurant_name} and it has a {self.cuisine_type} cuisine") 
    def open_restaurant(self):
        print("the restaurant is open")
restaurant=Restaurant('sindi', 'good')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

