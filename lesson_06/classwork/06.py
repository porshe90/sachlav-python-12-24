numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

removed_last = numbers.pop()

removed_first = numbers.pop(0)
removed_12th = numbers.pop(12 - 1)
removed_7th = numbers.pop(7 - 1)
sum_removed = removed_last + removed_first + removed_12th + removed_7th

print(numbers)
print(sum_removed)
