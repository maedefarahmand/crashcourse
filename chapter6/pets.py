pet1={'kind':'dog', 'owner':'david'}
pet2={'kind':'cat', 'owner':'maddie'}
l=[pet1, pet2]
for pet in l:
    print(f"{pet['owner']} has a {pet['kind']}")