input_list = list(map(int, input("").split()))

sorted_list = sorted(input_list)
reverse_sorted_list = sorted(input_list, reverse=True)

print("Sorted List: ", sorted_list)
print("Reverse Sorted List: ", reverse_sorted_list)
