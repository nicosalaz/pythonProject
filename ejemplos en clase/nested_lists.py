a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x) # [['a', 'b', 'c'], [1, 2, 3]]
print(len(x)) # 2

print(x[0]) # ['a', 'b', 'c']
print(len(x[0])) # 3

print(x[0][1]) # 'b'
print(len(x[0][1])) # 1
