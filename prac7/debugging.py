"""CP1401 - Practical 7 - Debugging."""


# Problem(s) for program 1:
# ? no argument for parity = (function) .

# Fixed code for program 1:
def main_1():
    """Determine the parity of a user's number."""
    number = int(input("Enter number: "))
    parity = calculate_parity(number)
    print(parity)

def calculate_parity(number):
    return (number%2)


# Problem(s) for program 2:
#

# Fixed code for program 2:
def main_2():
    """Print numbers from 0 up to the user's input multiplied by 2."""
    # E.g., if input is 12, should print 0 2 4 6 8 10 12 14 16 18 20 22 24
    numnums = get_valid_number("How many: ", 0)
    for i in range(numnums+1):
        print(i * 2, end=" ")

def get_valid_number(prompt, low):
    number = int(input(prompt))
    while number < low:
        print("Invalid Input!")
        number = int(input(prompt))
    return number


# Problem(s) for program 3:
# return instead of print

# Fixed code for program 3:
def main_3():
    """Determine the area of a rectangle."""
    length, width = 12, 10
    area = calculate_area(length, width)
    print(f"The area is {area}")

def calculate_area(l, w):
    result = l * w
    return result


# Problem(s) for program 4:
# no calculation or addition of increment with age.

# Fixed code for program 4:
def main_4():
    """Show how old a person will be in the future."""
    increment = 10
    age = int(input("Age: "))
    while age < 0 and age > 120:
        print("Invalid age")
        age = int(input("Age: "))
    print(f"In {increment} years, you will be {age + increment} years old!")

# main_1()
# main_2()  # Note: these are not good names; just something to reduce the amount of copying we need to do
# main_3()
main_4()
