def get_formatted_name(firstname, lastname):
    """return a full name neatly formatted"""
    full_name=f"{firstname} {lastname}"
    return full_name.title()

#this is an infinite loop
while True:
    print("please tell me your name")
    print("enter 'q' at any time to quit")
    f_name=input("first name: ")
    if f_name=='q':
        break
    l_name=input("last name: ")
    if l_name=='q':
        break
    formatted_name=get_formatted_name(f_name, l_name)
    print(f"hello {formatted_name}")