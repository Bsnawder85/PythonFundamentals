#  Sets are like formal mathematical sets.
#  Sets cannot/do not have duplicate values
#  -- Elements are unique. Duplicates are automatically removed upon creation.
#  Elements are not ordered.
#  -- Cannot be accessed by index.
#  Sets can be useful if you need to keep track of
#    a collection of elements, but don't care about 
#    ordering, keys or values, and duplicates.



#   Creating a Set using the built-in method.
myset = {1,2,3,4,5,6,6,6,7,5}

#   The prefered, Pythonic way to create a Set.
myotherset = {1,2,4,5,7,8,4,9}

print()
print("Using a built-in method to create a Set:\nmyset = set({1,2,3,4,5,6,6,6,7,5})\n")
print("Using the preferred/Pythonic way to create a Set:\nmyotherset = {1,2,4,5,7,8,4,9}\n") 
print(f"myset:\n\t{myset}\n")
print(f"myotherset:\n\t{myotherset}")
print("\n\n")
#   We can't get an item by indexing, but we can Test if a value is in the Set.
print(f"The number 4 is in myset? -- {4 in myset}")
print(f"The number 4 is in myotherset? -- {4 in myotherset}")

print('\n\n')

#       Set Methods


#       .add(val)  -- does not work if val is already in the Set (No dupes Allowed!)
#       .remove(val)  -- throws a KeyError if val is not in the Set
#       .discard(val)  -- like .remove(), but without throwing an error
#       .copy()  -- creates a copy.
#       .clear()  -- removes all contents.



#       Set Math

math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology_students = {'Jane', 'Matthew', 'Charlotte', 'Mesut', 'Oliver', 'James'}

print(f"Students in the Math class: {math_students}")
print(f"Students in the Biology class: {biology_students}\n")

#       |   -- take the Union of two Sets, no dupes (returns a Set)
print(f"All students: {math_students | biology_students}")

#       &   -- take the Intersection of two Sets (returns a Set)
print(f"Only the students taking both classes: {math_students & biology_students}")

print('\n\n')


# you can iterate over Unions and Intersections
union= ''
intersection= ''

for name in math_students | biology_students:
    union += f"{name}, "
union = union.strip()
union = union[:-1]

for name in math_students & biology_students:
    intersection += f"{name}, "
intersection = intersection.strip()
intersection = intersection[:-1]

print(f"All students: {union}")
print(f"Only the students taking both classes: {intersection}")





print()


