sandwich_orders=['chicken', 'vegetable', 'meat']
finished_sandwiches=[]
while sandwich_orders:
    sandwich=sandwich_orders.pop()
    print(f"i made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)
print(finished_sandwiches)