def make_pizza(*toppings):
    """summerize the pizza we are about to make"""
    print("making a pizza with the following toppings:")
    for topping in toppings:
        print(f" {topping}")
make_pizza('pepperoni')
make_pizza("mushroom", "green peppers", "extra cheese")