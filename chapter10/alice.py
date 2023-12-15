from pathlib import Path

path=Path('alice.txt')
try:
    contents=path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"sorry the file {path} doesn't exist")
else:
    #count the approximate number of words in a document
    words=contents.split()
    num_words=len(words)
    print(f"the file {path} has about {num_words} words")