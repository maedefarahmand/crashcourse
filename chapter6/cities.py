cities={'tehran':{'country':'iran', 'population':10000000, 'fact':'capital city'}, 'isfahan':{'country':'iran', 'population':8000000, 'fact':'historical city'}}
for key , value in cities.items():
    for key1 , value1 in value.items():
        print(f"about {key} : \t {key1} : {value1}")