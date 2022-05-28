# slicing = create substring by extracting elements from another string
# indexing[] or slice()
# [start:stop:step]

name = "Harsh Sharma"
first_name = name[0:5]
last_name = name[6:]
reversed_name = name[::-1] # reverse a string using slicing
print(first_name)
print(last_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
website_slice = slice(7,-4)
print(website1[website_slice])
print(website2[website_slice])
