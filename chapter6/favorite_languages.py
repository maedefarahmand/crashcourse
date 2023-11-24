favorite_languages={
    'jen':'python',
    'sarah' : 'c',
    'edward':'rust',
    'phil':'python'

}

language=favorite_languages['sarah'].title()
print(f"sarah's favorite language is {language}")

for name , language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

for name in favorite_languages.keys():
    print(f"{name.title()}")
for name in favorite_languages:
    print(f"{name}")

