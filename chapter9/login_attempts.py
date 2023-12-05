class User:
    def __init__(self, first_name, last_name, age,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.login_attempts=login_attempts
    def describe_user(self):
        print(f"user's name is {self.first_name} and user's last name is {self.last_name} and user's age is {self.age}")
    def greet_user(self):
        print(f"wellcome {self.first_name}")
    def increment_login_attempts(self):
        self.login_attempts+=1
    def reset_login_attempts(self):
        self.login_attempts=0
a=User('adi', 'taha', 5, 1)
a.increment_login_attempts()
print(a.login_attempts)
a.increment_login_attempts()
print(a.login_attempts)
a.increment_login_attempts()
print(a.login_attempts)
a.reset_login_attempts()
print(a.login_attempts)
