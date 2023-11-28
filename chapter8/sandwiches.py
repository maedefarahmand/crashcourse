def describe_sandwich(*items):
    """creating a sandwich containing items"""
    for item in items:
        print(f" {item}")
describe_sandwich('mushrooms', 'chips')
describe_sandwich('pepper', 'tomato', 'cabagge')