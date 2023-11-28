def build_profile(first, last , **user_info):
    """build a dictionary containing everything we know about a user"""
    user_info['firstname']=first
    user_info['lastname']=last
    return user_info
user_profile=build_profile('albert', 'einstein', location='princeton', field='physics', country='america')
print(user_profile)