from pathlib import Path
import json
def get_stored_username(path):
    if path.exists():
        content=path.read_text()
        username=json.loads(content)
        return username
    else:
        return None
def get_new_username(path):
    username=input("please enter your username: ")
    content=json.dumps(username)
    path.write_text(content)
    return username   
def greet_user():
    """Greet the user by name"""
    path=Path('username.json')
    username=get_stored_username(path)
    if username:
        answer=input(f"is {username} your correct username?(y/n)")
        if answer=='y':
            print(f"wellcome back {username}")
        else:
            username=get_new_username(path)
            print(f"next time we will remember you {username}")
    else:
        username=get_new_username(path)
        print(f"next time we will remember you {username}")
        


greet_user()