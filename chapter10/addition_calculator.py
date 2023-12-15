while True:
    try: 
        a=input("enter first number: ")
        if a=='q':
            break
        b=input("enter second number: ")
        if b=='q':
            break
        c=int(a)+int(b)
    except ValueError:
        print("the number was not an integer")
    else:
        print(c)