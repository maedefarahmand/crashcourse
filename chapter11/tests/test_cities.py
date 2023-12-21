from city_functions import city_country


def test_city_country():
    print("running the test")
    a=city_country('tehran', 'iran')
    assert a=='tehran iran'

def test_city_country_population():
    a=city_country('tehran', 'iran', 12000000)
    assert a=='tehran iran population 12000000'