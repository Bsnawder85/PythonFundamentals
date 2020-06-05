############################################################
# These are the exercises for Section 18 of the course.
# They should be ordered from easiest to hardest.
############################################################

#   -- 1 -- Write a function called product that accepts two parameters and returns the product of the two parameters (multiply them together)

def product(n1, n2):
    """Returns the product of the two parameters, n1 and n2"""
    return n1 * n2

#   -- 2 -- Write a function called return_day, which takes one parameter (a number from 1-7) and returns the day of the week (1 is Sunday). If the number is less than 1 or greater than 7, return None.

def return_day(day):
    """Returns the name of the day (str) based on the number given (1-7). Otherwise, returns None."""
    days_of_the_week = {
        1:'Sunday', 2:'Monday', 3:'Tuesday', 4:'Wednesday', 
        5:'Thursday', 6:'Friday', 7:'Saturday'
    }
    if type(day) == "<class 'str'>":
        day = int(day)

    if day < 1 or day > len(days_of_the_week):
        return None

    return days_of_the_week[day]

#   -- 3 -- Write a function called last_element, which takes one parameter (a list) and returns the last value in the list. Return None if the list is empty.

def last_element(myList):
    return None if len(myList)==0 else myList[-1]

#   -- 4 -- Write a function called number_compare, which takes two parameters (both numbers). If the first is greater than the second, return "First is greater." If the second number is greater than the first, return "Second is greater." Otherwise, return "Numbers are equal".

def number_compare(first, second):
    if first == second:
        return "Numbers are equal"
    elif first > second:
        return "First is greater"
    else:
        return "Second is greater"

#   -- 5 -- Write a function called single_letter_count, which takes in two strings. The first string should be a word, the second string should be a letter. Return the number of times the letter appears in the word. If the letter is not found, return 0. The function should be case-insensitive.

def single_letter_count(word, s):
    return word.lower().count(s.lower())

#   -- 6 -- Write a function called multiple_letter_count, which takes in one string and returns a dictionary with the keys being the letters and the values being the count of the letter. 

def multiple_letter_count(word):
    return {letter:word.count(letter) for letter in word}

# -- 7 -- Write a function called list_manipulation, which takes in four parameters (a list, command, location and value).


############################################################
# Function Output (to command line)
############################################################
print()
print('Exercise 1:  product()')
print(f'2 x 2 = {product(2,2)}')
print(f'2 x -2 = {product(2,-2)}')
print('\n')
print('Exercise 2:  return_day()')
print(f'Day 1 is {return_day(1)}')
print(f'Day 2 is {return_day(2)}')
print(f'Day 3 is {return_day(3)}')
print(f'Day 4 is {return_day(4)}')
print(f'Day 5 is {return_day(5)}')
print(f'Day 6 is {return_day(6)}')
print(f'Day 7 is {return_day(7)}')
print(f'Day 41 is {return_day(41)}')
print(f'Day 0 is {return_day(0)}')
print('\n')
print('Exercise 3:  last_element()')
print(f'The last element of [1,2,3] is {last_element([1,2,3])}')
print(f'The last element of [] is {last_element([])}')
print('\n')
print('Exercise 4:  number_compare()')
print(f'Compare 1 and 1:  {number_compare(1,1)}')
print(f'Compare 1 and 0:  {number_compare(1,0)}')
print(f'Compare 2 and 4:  {number_compare(2,4)}')
print('\n')
print('Exercise 5:  single_letter_count()')
print(f'Number of times "h" appears in "Hello World":  {single_letter_count("Hello World", "h")}')
print(f'Number of times "z" appears in "Hello World":  {single_letter_count("Hello World", "z")}')
print(f'Number of times "l" appears in "Hello World":  {single_letter_count("Hello World", "l")}')
print('\n')
print('Exercise 6: multiple_letter_count()')
print(f"Count the letters in the word 'awesome':\n {multiple_letter_count('awesome')}")
print('\n')
print('Exercise 7:  list_manipulation()')

print('\n')

print('\n')

print('\n')