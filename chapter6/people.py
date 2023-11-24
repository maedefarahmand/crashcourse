person={'first_name':'neda', 'last_name':'maroofi', 'age':32, 'city':'toronto'}

person1={'first_name':'mahsa', 'last_name':'asgari', 'age':31, 'city':'tehran'}

person2={'first_name':'sarah', 'last_name':'dayi', 'age':30, 'city':'isfahan'}

l=[person, person1, person2]

for item in l:
    print(f"{item['first_name']} {item['last_name']} is {item['age']} years old and lives in {item['city']}")