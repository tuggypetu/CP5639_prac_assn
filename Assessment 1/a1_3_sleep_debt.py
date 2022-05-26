"""
CP1401 2021-1 Assignment 1
Program 3 – Sleep Debt Calculator
Student Name: <Siddhanth Biswas>
Date started: <15 December 2021>
Pseudocode:
-----------------------------
    recommended sleep hours = 40
    total sleep = 0
    for night in range(1,6)
        get night hours sleep
        while night hours sleep > 24 or night hours sleep < 0
            print Invalid hours.
            get night hours sleep
        total sleep = 0 + night hours sleep
    print recommended sleep hours is 40.
    print total sleep
    if total sleep > recommended sleep
        sleep debt = recommended sleep hours - total sleep
        print sleep debt
    else
        print You are getting enough sleep
----------------------------------------
Justification/Explanation of pattern:
A nested loop is used.
The for loop is used to repeat the input over the definite known number of nights.
A while loop is used within the for loop to error check the input to be between 0 and 24 hours.

The if-else statement is also used to check if (total sleep is less than recommended sleep) or
(total sleep is equal to or greater than recommended sleep).
These are two mutually exclusive cases. Similar to true-false, suitable for if-else statement.
"""

print("Sleep Debt Calculator")

# constants
recommend_sleep = 40
total_sleep = 0
start_day = 1
end_day = 5
# for loop for repeating input over the number of nights
for night in range(start_day, end_day + 1):
    night_sleep_hours = float(input("Night {} hours sleep: ".format(night)))
    # while loop for error checking
    while night_sleep_hours > 24 or night_sleep_hours < 0:
        print("Invalid number of hours.")
        night_sleep_hours = float(input("Night {} hours sleep: ".format(night)))
    total_sleep += night_sleep_hours            # calculating total sleep while conditions met

print("Recommended total sleep (hours) is:", recommend_sleep)
print("Your total hours of sleep :", total_sleep)

if total_sleep < recommend_sleep:
    sleep_debt = recommend_sleep - total_sleep
    print("Your sleep debt (hours) over this time is:", sleep_debt)
else:
    print("You are getting enough sleep. Keep it up!")      # sleep got is more or equal to recommended sleep
