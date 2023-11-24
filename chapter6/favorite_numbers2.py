favorite_numbers={'maryam':[1,2,3], 'nasrin':[56,34] , 'babak':[3]}
for key , value in favorite_numbers.items():
    for num in value:
        print(f"{key}'s favorite number is {num}")