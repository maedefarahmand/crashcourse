prompt="please enter the name of a city you have visited"
prompt+="enter 'quit' when you are finished"
while True:
    city=input(prompt)
    if city=='quit':
        break
    else:
        print(f"i'd love to go to {city.title()}")