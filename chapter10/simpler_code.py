from pathlib import Path
path=Path('learning_python.txt')
contents=path.read_text()
list=[]
for line in contents.splitlines():
    list.append(line)
for l in list:
    print(l)