requested_toppings=['mushroom', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping=='green peppers':
        print("sorry, we are out of green peppers right now")
    else:
        print(f"adding {requested_topping}")
print("finished making your pizza")