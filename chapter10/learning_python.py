from pathlib import Path
path=Path('learning_python.txt')
contents=path.read_text()
lines=contents.splitlines()
list=[]
for line in lines:
    list.append(line)
print(contents)
for l in list:
    print(l)