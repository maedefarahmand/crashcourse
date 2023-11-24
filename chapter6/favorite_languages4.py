favorite_languages={
    'jen':['python','rust'],
    'sarah' : ['c'],
    'edward':['rust','go'],
    'phil':['python']

}
for name , languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")