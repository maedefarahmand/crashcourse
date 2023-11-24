prompt="tell me something and i will repeat it back to you"
prompt+="enter 'quit' to end the program"

message=''
while message!='quit':
    message=input(prompt)

    if message!='quit':
        print(message)
