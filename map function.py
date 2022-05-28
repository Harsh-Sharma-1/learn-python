# map() = applies a function to each item in an iterable (list,tuple,etc.)
# map(function,iterable)

store = [("shirt", 20.00), ("pants", 35.00),
         ("jacket", 50.00), ("socks", 5.00)]


def to_euros(data): return (data[0], data[1]*0.82)


def to_dollars(data): return (data[0], data[1]/0.82)


store_euros = list(map(to_euros, store))
for i in store_euros:
    print(i)
print()
store_dollars = map(to_dollars, store_euros)
for i in store_dollars:
    print(i)
