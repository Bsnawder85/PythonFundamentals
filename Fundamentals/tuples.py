#  Tuples are ordered, immutable collections of data.
#  -- commonly used for unchanging data.
#  Tuples are faster than lists
#  -- immutability makes for a lightweight data structure; 
#  -- no pushing/popping/(uh)shifting/etc.
#  Tuples can make your code safer from bugs
#  -- helpful in a dynamically-typed language.
#  Tuples can be used as valid keys in a dictionary.
#  Some methods return them to you -- like .items() when working with dictionaries!
#  Tuples can be accessed by index.
#  Tuples allow slicing, just like lists.



months = (
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
)
print(f'The first month of the years is {months[0]}.')

# Using tuples as keys for dictionaries
locations = {
    # name of the office, with the office latitude and longitute
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Fancisco Office"
}
print(f"Let's go to the {locations[(35.6895, 39.6917)]}.")
#       You actually can't do this with a list. 



#   Iterating over a Tuple

for month in months:
    print(month)



#   Tuple Methods



#   .count(val)  -- returns the number of times val appears in the Tuple
print(f"January appears {months.count('January')} time(s).")




#   .index(val)  -- returns the index at which a value is found in a Tuple
print(f"May is the {months.index('May')+1}th month of the year.")
#       only provides the first matching index.
#       if not in the Tuple, throws a ValueError.


