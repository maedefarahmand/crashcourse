current_users=['amir', 'ali', 'adi', 'sara', 'samar']
cur_new=[]
for usr in current_users:
    cur_new.append(usr.lower())
new_users=['sami', 'amir', 'soroush', 'sara', 'samar']
for user in new_users:
    if user.lower() in cur_new:
        print("you need to choose a new username")
    else:
        print("username is available")