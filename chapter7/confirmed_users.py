unconfirmed_users=['alice', 'brian','candace']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"verifying user {current_user}")
    confirmed_users.append(current_user)
print("the following users have been confirmed")
for user in confirmed_users:
    print(user.title())