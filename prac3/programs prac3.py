
# 1. Tax rate

"""
I didn't follow the code exactly as solution because I thought it was important to state negative numbers as invalid.
Pseudocode here

get income
if income between 0 and 100
    total_tax = 0
if income between 100 and 1000
    total_tax = income * 0.05
if income more than 1000
    total_tax = income * 0.1
else
    display "Invalid input"         (# in case of negative numbers.)
take_home_pay = income - total_tax
display total_tax
display take_home_pay
"""

TAX_RATE_LOW = 0.05  # 5%
TAX_RATE_HIGH = 0.1  # 10%
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000
total_tax = 0
print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $ "))
if 0 <= income <= TAX_THRESHOLD_LOW:
    total_tax = 0
elif TAX_THRESHOLD_LOW < income <= TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_LOW
elif income > TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_HIGH
else:
    print("Ain't no income tax like that. Invalid input.")      # in case someone enters negative numbers.
take_home_pay = income - total_tax
print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")


# 2. Car Insurance

print("Car rental company PAINZ")

age = abs(int(input("Age: ")))
if age >= 25:
    print("Not required to purchase insurance.")
elif 18 <= age < 25:
    print("Purchase Special Insurance.")
else:
    print("Hire is itself refused.")


# 3. Simple Password Checker

PASSWORD = "Genius123"
password = input("Enter password: ")
if password == PASSWORD:
    print("Access Granted. Wow! You're a Genius!")
else:
    print("Access Denied. Good guess Genius! Hehe.")


# 4. Dog years

human_age = abs(int(input("Age in human years: ")))
if human_age <= 2:
    dog_age = human_age * 10.5
else:
    dog_age = (2 * 10.5) + ((human_age - 2) * 4)
print("Age in dog years is", dog_age)
print("Woof Woof!")


# 5. Rock of Ages

age = int(input("Age: "))
if 0 > age > 120:
    print("Invalid age. You ain't human.")
elif age < 15:
    print("You are a Baby.")
elif age < 30:
    print("You are a  Big Baby.")
elif age < 60:
    print("You are a Bigger Baby.")
else:
    print("You are Biggest Baby.")


# 6. Speeding Fines
penalty_amount = 0
demerit_points = 0
speed = float(input("Enter your speed in km/h : "))
speed_limit = float(input("Enter the speed limit in km/h : "))
difference = speed - speed_limit
if speed < 0 or speed_limit < 0:
    print("Invalid input. speed or speed limit cannot be negative here.")
    exit()
elif difference <= 0:
    print("You have no fine! You have no demerit points!")
    exit()
elif difference < 13:
    penalty_amount += 177
    demerit_points += 1
elif difference < 20:
    penalty_amount += 266
    demerit_points += 3
elif difference < 30:
    penalty_amount += 444
    demerit_points += 4
elif difference < 40:
    penalty_amount += 622
    demerit_points += 6
else:
    penalty_amount += 1245
    demerit_points += 8
print("You have exceeded the speed limit by", difference, 'km/h')
print("Your fine is $", penalty_amount)
print("Your demerit points is", demerit_points)
