numbers = {
    'first':1,
    'second':2,
    'third':3
}

squared_numbers = {
    key: value**2   for key,value   in numbers.items()
}
print()
print(squared_numbers)
print('\n\n\n')


print( { num: num**2  for num in [1,2,3,4,5] } )
print('\n\n\n')

#   place each consecutive character in the two strings as key-value pairs
str1 = 'ABC'
str2 = '123'
combo = {
    str1[i]: str2[i]   for i in range(len(str1))
}
print(combo)

print('\n\n\n')


developer = {
    'name': 'Bobby',
    'fav_pet_type': 'dogs',
    'fav_stacks': 'React + Go + MongoDB',
    'has_certs': 'True',
    'number_of_certs': '1'
}

yelling_developer = {
    k.upper(): v.upper()  
    for k,v  in developer.items()
}

print(yelling_developer)




#       conditional logic
print('\n\n\n')

num_list = [1,2,3,4]
print({ num:('even' if num%2==0 else 'odd') for num in num_list })

print('\n\n\n')

yelling_developer = {
    (
        k.upper() if k is 'fav_pet_type' else k
    ): (
        v.upper() if v is 'dogs' else v
    )  
    for k,v  in developer.items()
}

print(yelling_developer)



print('\n\n\n')


