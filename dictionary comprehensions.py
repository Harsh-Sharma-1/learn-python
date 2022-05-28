# dictionary comprehensions = create dictionary using an expression

# dictionary = {key:expression for (key,value) in iterable}
# dictionary = {key:expression for (key,value) in iterable if condition}
# dictionary = {key:(if/else) for (key,value) in iterable}
# dictionary = {key:function(value) for (key,value) in iterable}

cities_in_F = {'Ujjain': 42, 'Indore': 30, 'Dewas': 50,
               'Bhopal': 35, 'Ratlam': 85, 'Gwalior': 70}

cities_in_C = {key: round((value-32)*(5 / 9))
               for (key, value) in cities_in_F.items()}

print(cities_in_C)

weather = {'Ujjain': 'sunny', 'Indore': 'snowing',
           'Dewas': 'cloudy', 'Bhopal': 'sunny'}

sunny_weather = {key: value for (
    key, value) in weather.items() if value == 'sunny'}

print(sunny_weather)

desc_cities = {key: ("WARM" if value >= 40 else 'COLD')
               for (key, value) in cities_in_F.items()}

print(desc_cities)


def check_temp(val):
    if val >= 70:
        return 'HOT'
    elif 69 >= val >= 40:
        return 'WARM'
    else:
        return 'COLD'


desc_cities_2 = {key: check_temp(value)
                 for (key, value) in cities_in_F.items()}

print(desc_cities_2)
