names=['admin', 'david','sara','soroush','adi']
if names:
    for name in names:
        if name=='admin':
            print(f"hello {name}, would you like to see a status report?")
        else:
            print(f"hello {name}, thank you for logging in again")
else:
    print("we need to find some users!") 