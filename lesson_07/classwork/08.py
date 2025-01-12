numbers = (2, 4, 6, 8, 10)
word = "hello"
result = (''.join(c * 2 for c in word), sum(numbers[:3]),
          word[0].upper() +word[1:-1]+ word[-1].upper())
print(result)

