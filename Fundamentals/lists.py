items = ['socks', 'mug', 'tea pot', 'cat food']
print(items)

lastitem = items.pop()
print(items)
print(lastitem)

seconditem = items.pop(1)
print(items)
print(seconditem)

items.extend(['dog food', 'chew toys', 'leash'])
print(items)

names = ['Arya', 'Blue', 'Colt', 'Lena', 'Pablo', 'Selena']
names.insert(0, 'Mia')
print(' is my friend. '.join(names))


# SLICING UP THEM LISTS
# returns a copy!  does not alter the original list/string
newlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(newlist)
print(newlist[1:])
print(newlist[3:])
print(newlist[-1:]) #reverse order
print(newlist[-3:])
print(newlist[-2:0:-1])
print(newlist[-2::-1]) #how to get the first element when slicing in reverse order
print(newlist[-1::-1])
#can also do all these slicing things with Strings as well!


# VALUE SWAPPING!
swap_these_names = ['James', 'Michelle']
print(swap_these_names)
swap_these_names[0], swap_these_names[1] = swap_these_names[1], swap_these_names[0]
print(swap_these_names)
#when might you need to swap??????????????????????
# - shuffling
# - sorting 
# - algorithms?



