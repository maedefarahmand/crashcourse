favorite_languages={
    'jen':'python',
    'sarah' : 'c',
    'edward':'rust',
    'phil':'python'

}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()} thank you for taking the poll")

print("the following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())