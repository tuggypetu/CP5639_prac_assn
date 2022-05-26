"""
CP1401 2021-1 Assignment 1
Program 1 – Pizza Pay Calculator
Student Name: <Siddhanth Biswas>
Date started: <15 December 2021>
Pseudocode:
----------------------------------------
    pay per trip = $ 1.45
    pay per minute = $ 0.95
    get number of trips
    get number of minutes
    calculate total pay per trip
    calculate total pay per minute
    calculate total pay
----------------------------------------
"""

print("Warm Pizza Pay Calculator")

pay_per_trip = 1.45
pay_per_min = 0.95
no_of_trips = int(input("Number of trips: "))
no_of_min = int(input("Number of minutes: "))
total_pay_trip = no_of_trips * pay_per_trip
total_pay_min = no_of_min * pay_per_min
total_pay = total_pay_trip + total_pay_min

print(f"For {no_of_trips} trips, your pay is: ${total_pay_trip:.2f}")
print(f"For {no_of_min} minutes, your pay is: ${total_pay_min:.2f}")
print(f"Your total pay is ${total_pay:.2f}")
