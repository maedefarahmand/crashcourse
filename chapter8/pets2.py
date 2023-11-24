def describe_pet( pet_name,animal_type='dog'):
    """display information about a pet"""
    print(f"i have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name}")
describe_pet( pet_name='willie')
describe_pet('willie')
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet( animal_type='hamster',pet_name='harry')
describe_pet()