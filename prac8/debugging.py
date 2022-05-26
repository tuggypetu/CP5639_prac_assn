
"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
names = ["Abby", "Jerome", "Olivia", "Monique"]
print("My friends' names: ")
for i in range(len(names)):
    print(f"{i + 1}. {names[i]}")
last_number = len(names)


# Problem(s) for program 1:
# print(f"The last name (number {last_number}) is {names[last_number]}")
# list index out of range.

# Fixed code for program 1:
print(f"The last name (number {len(names)}) is {names[last_number -1]}")

# Debug program 2 - title-casing country names

# Problem(s) for program 2:
# countries = ("australia", "new zeaLAND", "India")
# should be list and not tuple.

# Fixed code for program 2:
countries = ["australia", "new zeaLAND", "India"]
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now
