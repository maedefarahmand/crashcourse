from pathlib import Path
def count_words(path):
    
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"sorry the file {path} doesn't exist")
    else:
        #count the approximate number of words in a document
        words=contents.split()
        num_words=len(words)
        print(f"the file {path} has about {num_words} words")
path=Path('alice.txt')
count_words(path)