from pathlib import Path
import json
def get_stored_info(path):
    if path.exists():
        content=path.read_text()
        info=json.loads(content)
        return info
    else:
        return None
def get_new_info(path):
    username=input("please enter your username: ")
    age=input("please enter your age: ")
    fav_num=input("please enter your favorite number: ")
    info={'username':username, 'age':age, 'fav_num':fav_num}
    content=json.dumps(info)
    path.write_text(content)
    return info   
def greet_user():
    """Greet the user by name"""
    path=Path('info.json')
    info=get_stored_info(path)
    if info:
        print(f"your username is {info['username']} and your age is {info['age']} and your favorite number is {info['fav_num']}")
        
    else:
        info=get_new_info(path)
        print(f"next time we will remember that your username is {info['username']} and your age is {info['age']} and your favorite number is {info['fav_num']}")
        #print(f"next time we will remember you {info}")
        


greet_user()