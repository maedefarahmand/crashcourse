try: 
    a=input("enter first number: ")
    b=input("enter second number: ")
    c=int(a)+int(b)
except ValueError:
    print("the number was not an integer")
else:
    print(c)