from pathlib import Path
target=Path('guest.txt')

name=input("enter your name")
target.write_text(name)