class User:
    def __init__(self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print(f"user's name is {self.first_name} and user's last name is {self.last_name} and user's age is {self.age}")
    def greet_user(self):
        print(f"wellcome {self.first_name}")
class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges=['can add post', 'can delete post', 'can ban user']
    def show_privileges(self):
        for pri in self.privileges:
            print(f"you can {pri}")
a=Admin('adi', 'pro', 34)
a.show_privileges()