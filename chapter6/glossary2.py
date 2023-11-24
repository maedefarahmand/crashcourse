glossary={'list':'you can save a list of items in it', 'dictionary':'you can save key value pairs in it'}
glossary['set']='you can store unique values in it'
glossary['tuple']='you can store unchanging values in it'
for key , value in glossary.items():
    print(f"{key} is a data structure that {value}")
