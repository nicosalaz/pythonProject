ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids)) # Lista clasificada lexicográficamente

sorted_ids = sorted(ids, key=lambda x: int(x[2:]))
print(sorted_ids) # Lista clasificada por su componente entero
