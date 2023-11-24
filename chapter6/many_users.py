users={'aeinstein':{
    'first':'albert',
    'last':'einstein',
    'location':'princeton'


},
'mcurie':
{
    'first':'maria',
    'last':'curie',
    'location':'paris'
}
}
for username , user_info in users.items():
    print(f"Username {username}")
    full_name=f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"fullname {full_name}")
    print(f"location {location}")