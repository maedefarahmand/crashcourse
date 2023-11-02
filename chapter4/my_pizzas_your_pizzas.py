pizzas=['mashroom', 'roastbeaf' , 'pepperoni']
friend_pizzas=pizzas[:]
pizzas.append('chicken')
friend_pizzas.append('salmon')
print("my favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("my friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
