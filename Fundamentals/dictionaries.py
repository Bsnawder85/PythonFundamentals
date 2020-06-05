
###############################################################
def whatsInside(arg):
    print()
    for key,value in developer.items():
        if key=='fav_stacks':
            print(f'\t{key}:')
            for k,v in value.items():
                print(f'\t    {k}: {v}')
        else:
            print(f'\t{key}: {value}')
    print()
###############################################################





# basic dictionary

developer = {
    'name': 'Bobby',
    'fav_pet_type': 'dogs',
    'fav_stacks': {
        '01': 'MERN',
        '02': 'MEAN',
        '03': 'React + Go + MongoDB'
    },
    'has_certs': True,
    'number_of_certs': 1
}

#   using a list of strings to control access
keys = [
    'name', 'fav_pet_type', 'fav_stacks', 'has_certs', 'number_of_certs'
]
print()
for key in keys: 
    print( developer[key] )
print()


# the more Pythonic way --> Keys and Values
print()

# just Values
for val in developer.values(): 
    print(val)

print()

# just Keys
for key in developer.keys(): 
    print(key)

print()

# both Keys and Values

for key,value in developer.items(): 
    print(f'{key}: {value}')

print()

whatsInside(developer)

print()
print()

# use truthiness 
if developer['name']:
    print('has name!')



###############################################################
###############################################################
###############################################################
# dictionary methods!
###############################################################
###############################################################
###############################################################
print('\n\n\nDictionary Methods!\n\n\n')

#  .clear()  - empties the entire dictionary

d = dict( a=1, b=2, c=3 )
print('\nd = dict( a=1, b=2, c=3 )\n')

print(f'd = {d}')
d.clear()
print('d.clear()')
print(f'd = {d}')

print()


#  copy()  - makes a copy 


d = dict( a=1, b=2, c=3 )
c = d.copy()

print(f'd = {d}')
print('c = d.copy()')
print(f'c = {c}')

print(f'\nd == c\t{d == c}')
print(f'\nd is c\t{d is c}')

print()
print()


###############################################################
#  .fromkeys()  - creates key-value pairs from comma-separated values
###############################################################
# typically called on an empty dictionary



newDict1 = {}.fromkeys('a', 'b') 
newDict2 = {}.fromkeys(['email'], 'unknown') 
newDict3 = {}.fromkeys('a', [1,2,3,4,5])

print("newDict1 = {}.fromkeys('a', 'b')")
print("newDict2 = {}.fromkeys(['email'], 'unknown') ")
print("newDict3 = {}.fromkeys('a', [1,2,3,4,5])")

print()

print(f'newDict1 = {newDict1}')
print(f'newDict2 = {newDict2}')
print(f'newDict3 = {newDict3}')

print()

#  notice that for newDict2, the string 'email' was placed in a list.
#  what happens if we just pass the string by itself as a key?

newDict4 = {}.fromkeys('email', 'unknown')
print("newDict4 = {}.fromkeys('email', 'unknown')")
print(f'newDict4 = {newDict4}')
#  this result occurs because a string is also an iterable, just like a list!

print()

#  can also use range() to generate keys

newDict5 = {}.fromkeys(range(5), 'same value')
print("newDict4 = {}.fromkeys(range(5), 'same value')")
print(f'newDict5 = {newDict5}')


###############################################################
#  .get(key)  - retrieves a key in an obect 
#           returns None instead of throwing a KeyError 
#           if the key doesn't exist
###############################################################
print('\n\n\n\t.get(key)\n\n\n')

# let's get our developer dict back
developer = {
    'name': 'Bobby',
    'fav_pet_type': 'dogs',
    'fav_stacks': {
        '01': 'MERN',
        '02': 'MEAN',
        '03': 'React + Go + MongoDB'
    },
    'has_certs': True,
    'number_of_certs': 1
}

print()

print(f"developer.get('name') = {developer.get('name')}")

print()

print(f"developer.get('has_waifu') = {developer.get('has_waifu')}")



###############################################################
#  .pop(key)  - takes a single argument (a key) and 
#            removes that key-value pair.
#            returns the value
###############################################################
print('\n\n\n\t.pop(key)\n\n\n')


developer['is_married'] = False
print("developer['is_married'] = False")

print()

print('developer = ')
whatsInside(developer)

print()

is_married = developer.pop('is_married')
print("is_married = developer.pop('is_married')")

print()

print(f'is_married = {is_married}')

print()

print('developer = ')
whatsInside(developer)



###############################################################
#   .popitem()  - removes and returns the last item in the dictionary
#               takes no args
###############################################################
print('\n\n\n\t.popitem()\n\n\n')

developer['is_married'] = False
print("developer['is_married'] = False")

print()

print('developer = ')
whatsInside(developer)

print()

is_married = developer.popitem()
print("is_married = developer.popitem()")

print()

print(f'is_married = {is_married}')

print()

print('developer = ')
whatsInside(developer)

print()


###############################################################
#   .update(dict)  - update keys and values in a dictionary 
#               with another set of key-value pairs
###############################################################
print('\n\n\n\t.update(dict)\n\n\n')

developer['is_married'] = False
print("developer['is_married'] = False")

print()

other_dev = {}
other_dev.update(developer)

print("other_dev = {}")
print("other_dev.update(developer)")

print()
print('developer = ')
whatsInside(developer)

print()
print('other_dev = ')
whatsInside(other_dev)

print()

#  overwrite an existing key 
other_dev['is_married'] = True
print("other_dev['is_married'] = True")

print()
print('developer = ')
whatsInside(developer)

print()
print('other_dev = ')
whatsInside(other_dev)

print()

#  if we update again, the update overrides the new value

other_dev.update(developer)
print("other_dev.update(developer)")

print()
print('developer = ')
whatsInside(developer)

print()
print('other_dev = ')
whatsInside(other_dev)

print()

#       however, if a new key-value pair is added to the new dictionary
#       and the update is called again, the new key-value pair remains
#       intact.

#       update(dict) only updates the properties in the calling dict 
#       which are also in the passed dict.

print()


developer.pop('is_married')
print("developer.pop('is_married')")

print()

other_dev.update(developer)
print("other_dev.update(developer)")

print()
print('developer = ')
whatsInside(developer)

print()
print('other_dev = ')
whatsInside(other_dev)

print()
print()


