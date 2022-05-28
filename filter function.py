# filter() = creates a collection of elements from an iterable for which a function returns true
# function(function,iterable)

friends = [
    ('bheem', 21),
    ('chutki', 18),
    ('indumati', 20),
    ('Raju', 16),
    ('Kaliya', 22),
    ('dholu', 15),
    ('bholu', 15)
]


def age(data): return data[1] >= 18


# this filter function returns a filter object so i have the list method to cast it to the list
drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)
