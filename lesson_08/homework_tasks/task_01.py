# 1. Create a variable named 'value' prompt the user for a value,
# convert it to an int, and store it off in a variable
value = int(input("Enter an integer value: "))

# 2. Print "FizzBuzz" if the Value Is a Multiple of Three and Five
# Let's create our if statement and print "FizzBuzz" if the condition is met,
# then add an else to just print the value otherwise:

# if value % 5 == 0 and value % 3 == 0:
#     print("FizzBuzz")
# else:
#     print(f"{value = }")

# 3. Print "Fizz" if the Value Is a Multiple of Three, and "Buzz" if it's a Multiple of Five
if value % 5 == 0 and value % 3 == 0:
    print("FizzBuzz")
elif value % 3 == 0:
    print("Fizz")
elif value % 5 == 0:
    print("Buzz")
else:
    print(f"{value = }")