from pathlib import Path
file=Path('gutenberg.txt')
file=file.read_text()
a=file.lower().count("the ")
print(a)