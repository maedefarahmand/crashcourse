def make_pizza(size , *toppings):
    """summerize the pizza we are about to make"""
    print(f"making a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"{topping}")
make_pizza(16, 'pepproni')
make_pizza(12, 'mushroom', 'green prpper', 'extra cheese')