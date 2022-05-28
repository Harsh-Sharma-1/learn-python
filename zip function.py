# zip(*iterables) = aggregate elements from two or more iterables
# creates a zip object with paired elements stored in tuples for each element

usernames = ['Harsh', 'Rajesh', 'Dinesh']
passwords = ('Harshh@1', 'Suresh ki maa', 'jai mata di')

users = zip(usernames, passwords)

print(type(users))

users = list(users)

for i in users:
    print(i)
print()
# since we have two iterables we can convert it to a dictionary
user_with_password = dict(zip(usernames, passwords))

for key, value in user_with_password.items():
    print(f"{key} : {value}")
print()
login_date = ['1/1/2021', '1/2/2021', '1/3/2021']

users_with_login = zip(usernames, passwords, login_date)

for i in users_with_login:
    print(i)
