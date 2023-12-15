from pathlib import Path
import json

file=Path('username.json')
contents=file.read_text()
a=json.loads(contents)

print(f"welcome back {a}")