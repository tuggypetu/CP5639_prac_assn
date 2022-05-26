# 1. Error Checking

worker_level = int(input("enter worker level: "))
while worker_level < 1 or worker_level > 10:
    print("Invalid Worker_level")
    worker_level = int(input("enter worker level: "))
salary = 5000 * worker_level
print("With worker level {}, your salary is ${}".format(worker_level, salary))


# 2. Number Sequences
# 2a. Write a loop that displays all of the odd numbers between 1 and 100 with a line break between each one.

Minimum_level = 1
Maximum_Level = 100
for count in range (1,100,2):
    print (count)


# 2b. Write a loop that displays all of the Summer Olympic years (i.e. every 4 years) between 1896 and today, with a space between each one.

for SOY in range(1896,2021,4):
    print(SOY , end= " ")

# 2c. Write one more loop that represents a meaningful sequence. Explain your chosen sequence in a comment.

# chosen sequence: check all numbers divisible by 69 between 0 and 700 with a space between each one.

    # 0 is the first number divisible by 69.
for nos in range(0, 700, 69):
    print(nos)
print()

# 3. Menus

while True:
    x = input('enter s for :), enter f for :(, enter q to quit: ')
    if x == "s":
        print(":)")
    elif x == "q":
        print("you have quit the program.")
        break
    elif x == "f":
        print(":(")
    else:
        print("invalid input")


# 4. Accumulation
# Average age

Sentinel = -1
Total = 0
number_count = 0
Enter_age_values = int(input("enter age (enter -1 to calculate average age of all entered values):"))
while Enter_age_values != -1:
    number_count += 1
    Total = Total + Enter_age_values
    Enter_age_values = int(input("enter age:"))
print("Average age", Total/number_count)


# Smileys count
smiley_count = 0
frowny_count = 0
while True:
    x = input('enter s for :), enter f for :(, enter q to quit: ')
    if x == "s":
        smiley_count += 1
        print(":)")
    elif x == "q":
        print("you have quit the program.", "   smiley count=", smiley_count, "   frowny count=", frowny_count)
        break
    elif x == "f":
        frowny_count += 1
        print(":(")
    else:
        print("invalid input")


# Total numbers

Total = 0
no_of_values = int(input("How many numbers do you want to add up?: "))
for Values in range(0, no_of_values):
    Values = int(input("Enter number: "))
    Total = Total+Values
print("Total of those", no_of_values, "numbers are = ", Total)


# 5. Guessing Game

guess_count = 0
SECRET = 6
guess = int(input("Guess a number: "))
while guess != SECRET:
    guess_count += 1
    if guess > 6:
        print("Lower")
    elif guess < 6:
        print("Higher")
    guess = int(input("Guess a number: "))
print("You got it in", guess_count, "guesses!")


# 6. Nested Loops
Rows = int(input("Rows: "))
Columns = int(input("Columns: "))
for rows in range(Rows):
    for columns in range(Columns):
        print(" ", columns, end="")
    print()
