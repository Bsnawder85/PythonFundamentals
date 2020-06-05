coords = [
    [10.423, 9.132] , [37.212, -14.092] , [21.376, 32.572]
]
print("[ [ print(crd) for crd in lst ]  for lst in coords ]\n")
# print out each coordinate
[ 
    [ print(crd) for crd in lst ]  
    for lst in coords 
]

print()


# using nested list comprehension with conditional logic

board = [
    [
        'X' if num%2 != 0 else 'O' for num in range(1,4)
    ]   
    for val in range(1,4)
]
print("[ [ 'X' if num%2 != 0 else 'O' for num in range(1,4) ]   for val in range(1,4) ]\n")
print(board)


print()


print("[ [ 'X' if num%2 != 0 else 'O' for num in range(1,4) ]   for val in range(1,4) ]\n")
[
    print( [ 'X' if num%2 != 0 else 'O' for num in range(1,4) ] )   
    for val in range(1,4)
]


print()


print("[ y for y in ['X' if num%2 != 0 else 'O' for num in range(1,4) ]   for val in range(1,4) ]\n")
[
    print(y) for y in [ 
        'X' if num%2 != 0 else 'O' for num in range(1,4) 
    ]   
    for val in range(1,4)
]


print()

# 10x10 numbers grid
grid = [
    [column for column in range(10)]
    for row in range(10)
]
print("[ [column for column in range(10)]   for row in range(10) ]\n")

for col in grid: print(col)

print()

