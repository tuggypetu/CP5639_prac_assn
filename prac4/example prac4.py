Minimum_month = 1
Maximum_month = 12
birth_month = int(input("Enter your birth month ({}-{}): ".format(Minimum_month, Maximum_month)))
while birth_month < 1 or birth_month > 12:
    print("Invalid month")
    birth_month = int(input("Enter your birth month: "))
for count in range(1, birth_month + 1):
    print(count, end=" ")
    print()
if birth_month in [1, 2, 3, 4, 5, 6]:
    print("Birth month is in first half of the year.")
elif birth_month in [7, 8, 9, 10, 11, 12]:
    print("Birth month is in second half of the year.")
