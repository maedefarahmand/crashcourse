prompt="if you could visit one place in the world where would you go? if you want to quit type 'quit'"
vacation ={}
while True:
    name=input("enter your name")
    place=input(prompt)
    
    if place=='quit':
        break
    vacation[name]=place
print(vacation)