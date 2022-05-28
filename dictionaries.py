# dictionary = a changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Las Vegas',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'
            }

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Washington DC'})
capitals.pop('China')


print(capitals['Russia'])
print(capitals.get('India'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key,':',value)
    
capitals.clear()