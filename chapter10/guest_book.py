from pathlib import Path
target=Path('guest.txt')
content=''
while True:
    name=input("enter your name")
    if name.lower() == 'exit':
        break
    content+=name
    content+='\n'

target.write_text(content)