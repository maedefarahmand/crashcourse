my_foods=['pizza', 'falafel', 'carrot_cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("my favorite foods are:")
for food in my_foods:
    print(food)
print("my friend's favorite foods are:")
for food in friend_foods:
    print(food)