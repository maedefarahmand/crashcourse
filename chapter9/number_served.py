class Restaurant:
    def __init__(self, restaurant_name, cuisine_type ):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
    def describe_restaurant(self):
        print(f"the restaurant's name is {self.restaurant_name} and it has a {self.cuisine_type} cuisine") 
    def open_restaurant(self):
        print("the restaurant is open")
    def set_number_served(self,num):
        self.number_served=num
    def increment_number_served(self, number):
        self.number_served+=number
restaurant=Restaurant('sindi', 'good')
print(restaurant.number_served)
restaurant.number_served=5
print(restaurant.number_served)
restaurant.set_number_served(7)
print(restaurant.number_served)
restaurant.increment_number_served(12)
print(restaurant.number_served)