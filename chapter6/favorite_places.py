favorite_places={'Maddie':['tehran', 'isfahan', 'mashhad'],'David':['istanbul', 'toronto']}
for key, value in favorite_places.items():
    for place in value:
        print(f"{key}'s favorite place is {place}")

