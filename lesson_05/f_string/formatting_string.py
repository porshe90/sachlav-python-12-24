name = "Alexander"
surname = "Komanov"
age = 36

# formatted_string = "Hello " + name + " " + surname + "! My age is: " + str(age)

formatted_string = "Hello {{{2} {0}! My age is: {1}}}".format( surname, age, name)
print(formatted_string)