prompt="enter your age"
prompt+="\n enter 'quit' to quit"
while True:
    age=input(prompt)
    if age=='quit':
        break
    age=int(age)
    if age<3:
        print("free ticket")
    elif age<12:
        print("your ticket is 10$")
    else:
        print("your ticket is 15$")
    