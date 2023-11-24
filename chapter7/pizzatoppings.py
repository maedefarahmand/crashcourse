prompt="enter your favorite pizza topping"
prompt+="enter 'quit' to quit"
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(f"i will add {message} to your pizza")