guest_list=['bill gates', 'mark zukerberg', 'andrew huberman']
print(f"hi {guest_list[0]} i'd like to invite you to dinner")
print(f"hi {guest_list[1]} i'd like to invite you to dinner")
print(f"hi {guest_list[2]} i'd like to invite you to dinner")
print("hey i just found bigger table for dinner")
guest_list.insert(0, 'yeri')
guest_list.insert(1, 'jasmine')
guest_list.append('maddie')
print(f"hi {guest_list[0]} i'd like to invite you to dinner")
print(f"hi {guest_list[1]} i'd like to invite you to dinner")
print(f"hi {guest_list[2]} i'd like to invite you to dinner")
print(f"hi {guest_list[3]} i'd like to invite you to dinner")
print(f"hi {guest_list[4]} i'd like to invite you to dinner")
print(f"hi {guest_list[5]} i'd like to invite you to dinner")
print("i can invite only two people for dinner")
removed_guest=guest_list.pop()
print(f"sorry {removed_guest} i can not have you for dinner")
removed_guest=guest_list.pop()
print(f"sorry {removed_guest} i can not have you for dinner")
removed_guest=guest_list.pop()
print(f"sorry {removed_guest} i can not have you for dinner")
removed_guest=guest_list.pop()
print(f"sorry {removed_guest} i can not have you for dinner")
print(f"hi {guest_list[0]} you are still invited to dinner")
print(f"hi {guest_list[1]} you are still invited to dinner")
del guest_list[0]
del guest_list[0]
