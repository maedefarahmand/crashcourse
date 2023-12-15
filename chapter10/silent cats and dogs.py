from pathlib import Path
try:
    a=Path('cats.txt')
    b=Path('dogs.txt')
    a=a.read_text()
    b=b.read_text()
    print(a)
    print(b)
except FileNotFoundError:
    
    pass