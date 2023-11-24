sandwich_orders=['chicken', 'pastrami', 'vegetable', 'meat', 'pastrami']
finished_sandwiches=[]
print("we are out of pastrami today")
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    if sandwich !='pastrami':
        print(f"i made your {sandwich} sandwich")
        finished_sandwiches.append(sandwich)
print(finished_sandwiches)