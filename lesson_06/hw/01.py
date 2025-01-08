
users = []
print(users)
users.append('kevin')
users.append('bob')
users.append('alice')
print(users)
users.remove('bob')
print(users)
rev_users = users[::-1]
print("rev_users=", rev_users)
users.insert(1, 'melody')
print(users)
users.extend(['andy', 'wanda', 'jim'])
print(users)
center_users = users[2:4]
print(center_users)