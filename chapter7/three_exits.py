prompt="enter your favorite pizza topping"
prompt+="enter 'quit' to quit"
# message=""
# while message!='quit':
#     message=input(prompt)
#     if message!='quit':
#         print(f"i will add {message} to your pizza")


# message=""
# active=True
# while active:
#     message=input(prompt)
#     if message=='quit':
#         active=False
#     if message!='quit':
#         print(f"i will add {message} to your pizza")



while True:
    message=input(prompt)
    if message!='quit':
        print(f"i will add {message} to your pizza")
    else:
        break