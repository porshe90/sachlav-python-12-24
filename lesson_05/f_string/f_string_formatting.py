name = "Alexander"
surname = "komanov"
age = 36

# formatted_string = "Hello " + name + " " + surname + "! My age is: " + str(age)

formatted_string = f"Hello {name.upper()} {surname.capitalize()}! My age next year will be: {age + 1}"
print(formatted_string)

BASE_URL = "https://www.reqres.in"
CASES_API = f"{BASE_URL}/cases"
USERS_API = f"{BASE_URL}/users"
USER_API = f"{BASE_URL}/users/{name}"