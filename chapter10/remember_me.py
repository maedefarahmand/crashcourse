from pathlib import Path
import json

username=input("please enter your username: ")
file=Path('username.json')
a=json.dumps(username)
file.write_text(a)

print(f"next time we'll remember your name {username}")