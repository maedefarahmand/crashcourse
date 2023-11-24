# def formatted_name(first_name, last_name):
#     """return a full name neatly formatted"""
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()
# musician=formatted_name('jimi', 'hendrix')
# print(musician)

def formatted_name1(first_name,last_name,middle_name='' ):
    """return a full name neatly formatted"""
    if middle_name:
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()

musician=formatted_name1('jimi', 'hendrix')
print(musician)

musician=formatted_name1('john', 'hooker','lee')
print(musician)