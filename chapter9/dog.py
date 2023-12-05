class Dog:
    """a simple attempt to model a dog"""
    def __init__(self, name, age):
        """initialize age and name attributes"""
        self.name=name
        self.age=age
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """simulate roll over in response to a command"""
        print(f"{self.name} rolled over!")
my_dog=Dog('Willie', 6)
your_dog=Dog('Lucy', 3)
print(f"my dog's name is {my_dog.name}")
print(f"my dog's age is {my_dog.age}")
my_dog.sit()
print(f"your dog's name is {your_dog.name}")
print(f"your dog's age is {your_dog.age}")
your_dog.sit()