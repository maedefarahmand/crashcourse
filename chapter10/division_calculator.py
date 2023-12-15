print("give me two numbers and i will divide them")
print("enter q to quit")
while True:
    first_number=input("first number: ")
    if first_number=='q':
        break
    second_number = input("second number: ")
    if second_number=='q':
        break
    try:
        answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you can't divide by zero")
    else:
        print(answer)