a = set('abracadabra')
b = set('alacazam')

print(a)

print(b)

# Letras en a pero no en b
print(a - b)   # a.difference(b)

# Letras en a o en b o en ambas
print(a | b)   # a.union(b)

# Letras tanto en a como en b
print(a & b)   # a.intersection(b)

# Letras en a o en b pero no en ambas
print(a ^ b)   # a.symmetric_difference(b)
