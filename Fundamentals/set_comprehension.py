squares = { x**2 for x in range(10) }

no_dupes_hello = { v.upper() for v in 'hello' }

def are_all_vowels_in_string(string):
    return len( {char for char in string if char in 'aeiou'} ) == 5


print(squares)
print(no_dupes_hello)
print(are_all_vowels_in_string('hello'))
print(are_all_vowels_in_string('aeiou'))
print(are_all_vowels_in_string('sequoia'))
print(are_all_vowels_in_string('asegagewewei3osweweeefut4'))