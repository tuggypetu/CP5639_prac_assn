
# Input, Processing, Output
# 1. Percentage program

original_value = float(input("Original value: "))
change_percentage = float(input("Change percentage (enter value in decimals, example 0.1 is 10%): "))
result = original_value * (1 + change_percentage)
change_difference = result - original_value
print("Original:", original_value, ", Result:", result)
print("Change percentage:", change_percentage, ", Change difference: ", change_difference)


# Decision Structures
# 2. Time of day

time_of_day = int(input("Enter hour time of day (example- '14' is between 2pm and 3pm): "))
if time_of_day < 12:
    noon_time = "before"
    going_or_coming = "coming. Hi!"
else:
    noon_time = "after"
    going_or_coming = "going. Bye!"
# testing various strings for printing.
print("It is {} noon and you are {}".format(noon_time, going_or_coming))
print(f"It is {noon_time} noon and you are {going_or_coming}")


# 3. Coffee orders

coffee_type = input("Which coffee do you want? (White or Black coffee): ").lower()
coffee_size = input("Which coffee size do you want? (small, medium or large): ").lower()
coffee_price = 0
if coffee_size == "small":
    coffee_price += 3
elif coffee_size == "medium":
    coffee_price += 4
else:
    coffee_price += 5

if coffee_type != "black":
    coffee_price += 1

print("Coffee:", coffee_type, coffee_size, ". The price = $", coffee_price)


# Repetition Structures
# 4. Coffee order error checking

coffee_price = 0
coffee_type = input("Which coffee do you want? (White or Black coffee): ").lower()
while coffee_type not in ["black", "white"]:
    print("Invalid coffee colour type.")
    coffee_type = input("Which coffee do you want? (White or Black coffee): ").lower()
coffee_size = input("Which coffee size do you want? (small, medium or large): ").lower()
while coffee_size not in ["small", "medium", "large"]:
    print("Invalid coffee size.")
    coffee_size = input("Which coffee size do you want? (small, medium or large): ").lower()

if coffee_size == "small":
    coffee_price += 3
elif coffee_size == "medium":
    coffee_price += 4
else:
    coffee_price += 5

if coffee_type != "black":
    coffee_price += 1

print("Coffee: {} {}. The price = ${}".format(coffee_type, coffee_size, coffee_price))


# 5. Low-high printing

total = 0
low_value = int(input("Enter low value: "))
high_value = int(input("Enter high value: "))
while low_value > high_value:
    print("Invalid input. High value must be greater than low value. Enter both again.")
    low_value = int(input("Enter low value: "))
    high_value = int(input("Enter high value: "))

for row in range(low_value, high_value + 1):
    total += row
    print(row, end=" ")
print("Totals: ", total)
