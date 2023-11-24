favorite_languages={
    'jen':'python',
    'sarah' : 'c',
    'edward':'rust',
    'phil':'python'

}
list1=['jen', 'sarah', 'marwa', 'adi']
for name in list1:
    if name in favorite_languages:
        print("thank you for taking the poll")
    else:
        print("please take the poll")