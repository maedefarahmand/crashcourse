def greet_users(names):
    """print a simple greeting to each user in the list"""
    for name in names:
        msg=f"hello {name.title()}"
        print(msg)
user_names=["hannah", "ty", "margot"]
greet_users(user_names)