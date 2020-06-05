nums = [1, 2, 3]
print(nums)
print('[ x*10 for x in nums ]')
print([ x*10 for x in nums ])

print()

name = 'bobby'
print(name)
print('[ char.upper() for char in name ]')
print([char.upper() for char in name])

print()

friends = ['alan', 'david', 'matt', 'ryan', 'jason']
print(friends)
print('[friend[0].upper() + friend[1:] for friend in friends]')
print([friend[0].upper() + friend[1:] for friend in friends])

print()

# comprehensions with ranges (is a list anyway)

print('[num*10 for num in range(1, 6)]')
print([num*10 for num in range(1, 6)])

print()

# turning values into their boolean representation

print("[bool(val) for val in [0, [], '']]")
print([bool(val) for val in [0, [], '']])

print()

# converting a list of numbers into a list of strings

numbers = [1, 2, 3, 4, 5]
print(numbers)
string_list = [str(num) for num in numbers]
print(string_list)

print()


# LIST COMPREHENSION WITH CONDITIONAL LOGIC


another_numbers = [1, 2, 3, 4, 5, 6]
print(another_numbers)
evens = [n for n in another_numbers if n % 2 == 0]
print('[n for n in another_numbers if n % 2 == 0]')
print(evens)

odds = [n for n in another_numbers if n % 2 != 0]
print('[n for n in another_numbers if n % 2 != 0]')
print(odds)

print()

print('[ n*2   if n % 2 == 0   else n/2   for n in another_numbers ]')
print([ n*2   if n % 2 == 0   else n/2   for n in another_numbers ])

print()

# don't need the square brackets for this one...
with_vowels = "This is so much fun!"
print(with_vowels)
print("''.join( char  for char in with_vowels  if char not in \"aeiou\" )")
print(''.join( char  for char in with_vowels  if char not in "aeiou" ))

print(char  for char in with_vowels  if char not in "aeiou")

print()
