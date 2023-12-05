from random import choice
list=[34, 2,4, 'e', 't', 'c', 5, 6, 21, 90, 'u', 4, 'a', 3, 1, 'p']
for i in range(4):
    a=choice(list)
    print(f"any ticket matching {a} will wins the prize")