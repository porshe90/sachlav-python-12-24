users = []
print(users)
users.append('kevin')
users.append('bob')
users.append('alice')
print(users)
index_of_removed = users.index("bob")
print(f"{index_of_removed = }")
users.remove('bob')
print(users)
rev_users = users[::-1]
print(f"{rev_users = }")
users.insert(index_of_removed, 'melody')
print(users)
users.extend(['andy', 'wanda', 'jim'])
print(users)
center_users = users[2:4]
print(center_users)