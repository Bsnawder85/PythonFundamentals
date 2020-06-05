print('with a for-loop')
for i in range(1, 11):
    print('🧇' * i)

print('with a while-loop')
n = 1
while n < 11:
    print('🌯' * n)
    n += 1

print('with nested for- and while-loops')
x = 1
z = ''
for y in range(1, 11):
    while x <= y:
        z += '🥑'
        x += 1
    print(z)