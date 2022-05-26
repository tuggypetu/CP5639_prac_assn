# 1. Discount Price

DISCOUNT_RATE = 0.2
original_price = float(input("Enter original price here: $"))
new_price = original_price - (original_price * DISCOUNT_RATE)
print("The new discounted price is: $", new_price)

# 2. Kilometres to Miles

CONVERT_CONSTANT = 0.621371
print("Calculate miles to km. (Enter -1 to calculate km to miles.)")
miles_distance = float(input("Distance in miles = "))
while miles_distance != -1:
    km_distance = miles_distance * CONVERT_CONSTANT
    print(miles_distance, "miles =", km_distance, "km")
    break
while miles_distance == -1:
    km_distance = float(input("Distance in km = "))
    miles_distance = km_distance / CONVERT_CONSTANT
    print(km_distance, "km =", miles_distance, "miles")
    break


# 3. Holiday Cost
hotel_cost_per_day = 75
daily_food_cost = float(input("Daily food cost: $ "))
daily_activities_cost = float(input("Daily activities cost: $ "))
no_of_days = float(input("Number of days: "))
total_cost = (daily_food_cost * no_of_days) + (daily_activities_cost * no_of_days) + (no_of_days * hotel_cost_per_day)
print("The trip will cost: $ ", total_cost)


# 4. i-stop Calculation (Percentage)

i_stop_on = int(input("i-stop on in seconds: "))
time_stopped = int(input("Time stopped in seconds: "))

print("i-stop ON: ", i_stop_on // 60, "m", i_stop_on % 60, "s")
print("Time Stopped: ", time_stopped // 60, "m", time_stopped % 60, "s")
print("Percentage: ", i_stop_on * 100 / time_stopped,  "%")
