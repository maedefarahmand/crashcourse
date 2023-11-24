favorite_languages={
    'jen':'python',
    'sarah' : 'c',
    'edward':'rust',
    'phil':'python'

}

friends=['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"hi {name}")

    if name in friends:
        language=favorite_languages[name].title()
        print(f"{name.title()} i see you love {language}")
if 'erin' not in favorite_languages.keys():
    print("erin, please take our poll")