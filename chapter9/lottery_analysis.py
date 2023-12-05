from random import choice
list=[34, 2,4, 'e', 't', 'c', 5, 6, 21, 90, 'u', 4, 'a', 3, 1, 'p']
my_tickets=['e', 'g', 43, 9]
i=0
while True:
    a=choice(list)
    i=i+1
    if a in my_tickets:
        print(f"after {i} tries you got the chance to win the lottery")
        break