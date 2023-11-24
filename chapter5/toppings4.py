requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping=='green peppers':
            print("sorry, we are out of green peppers right now")
        else:
            print(f"adding {requested_topping}")
    print("finished making your pizza")
else:
    print("are you sure you want a plain pizza?")