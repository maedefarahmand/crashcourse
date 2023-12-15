from pathlib import Path 
import json
def retrieve_user_fav_number(path):
    if path.exists:
        try:
            content = path.read_text()
            num = json.loads(content)
            return num
        except json.decoder.JSONDecodeError:
            return None
    else:
        return None

def get_user_fav_number(path):
    fav_num=input("please enter your favorite number: ")
    content=json.dumps(fav_num)
    path.write_text(content)
    return fav_num

def favorite_number():
    path=Path('favorite_number.json')
    fav_num=retrieve_user_fav_number(path)
    if fav_num:
        print(f"your favorite number is {fav_num}")
    else:
        fav_num=get_user_fav_number(path)
        print(f"your new favorite number is {fav_num}")
favorite_number()