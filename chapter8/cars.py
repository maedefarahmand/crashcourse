def build_profile(manufacturer, model , **car_info):
    """build a dictionary containing everything we know about a car"""
    car_info['manufacturer']=manufacturer
    car_info['model']=model
    return car_info
car=build_profile('subaru', 'outback', color='blue', tow_package=True)
print(car)