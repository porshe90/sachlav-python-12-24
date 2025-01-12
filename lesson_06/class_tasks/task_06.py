numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


sum_of_removed = 0
sum_of_removed += numbers.pop(-1)
sum_of_removed += numbers.pop(0)
sum_of_removed += numbers.pop(12)
sum_of_removed += numbers.pop(7)
print(f"{numbers = }")
print(f"{sum_of_removed = }")