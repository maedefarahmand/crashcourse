class User:
    def __init__(self, first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def describe_user(self):
        print(f"user's name is {self.first_name} and user's last name is {self.last_name} and user's age is {self.age}")
    def greet_user(self):
        print(f"wellcome {self.first_name}")
a=User('adi', 'taha', 5)
b=User('maddie', 'alayo', 7)
c=User('sara', 'saba', 8)
a.describe_user()
a.greet_user()
b.describe_user()
b.greet_user()
c.describe_user()
c.greet_user()