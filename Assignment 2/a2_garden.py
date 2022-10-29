"""
CP5639 Assignment 2
Market Garden Simulator
Student Name: Siddhanth Biswas
Date completed: 26/01/2022

Pseudocode:

import random
RAINFALL_THRESHOLD = 30
MIN_RAINFALL = 0
MAX_RAINFALL = 100

display statements only at the start of the program to introduce Market Garden Simulator.

function main()
plant_list = [add plant 1-4]
display(plant_list) to show plant_list
num_days = 0
food = 0
status(num_days, plant_list, food) to show current days, number of plants, and food.

get instruction
while instruction != "Q":
    if instruction = "W":
        rainfall_value = random integer between MIN_RAINFALL and MAX_RAINFALL
        display rainfall
        num_days += 1
        food += get_food(rainfall_value, plant_list) to calculate and add new food
        plant_list = remove_or_not(plant_list, rainfall_value) to checking and removing a plant if required
    elif instruction = "D":
        display(plant_list) to show plant list
    elif instruction = "A":
        get new_plant = get_valid_plant_name(prompt)
        if new_plant in plant_list:
            display "already plant exists. can't have another."
        elif number of letters in new_plant > food:
            display "cannot afford it"
        else:
            add new plant to list using append
            subtract the number of letters in new_plant from food
    else:
        display invalid instruction
    status(num_days, plant_list, food) to show current days, number of plants, and food.
    get instruction
if number of plants in plant list == 0:
    display "finished with no plants"
else:
    display "finished with these {number of plants} plants"
    display(plant_list) to show plant list
status(num_days, plant_list, food) to show current days, number of plants, and food.
print "Thanks. The end."


function display(plant_list)
    joined_plant_list = join() items is plant list using ','
    display joined_plant_list

function status(num_days, plant_list, food)
    display "After {num_days} days, you have {number of plants} plants and your total food is {food}."


function get_food(rainfall_value, plant_list)
    total_food = 0
    for i in range(number of plants):
        count_of_each_plant = len(plant_list[i])
        display plant_list[i], end=" produced "
        random_for_calc_food = random value between rainfall_value/2 and  rainfall_value
        calculate_food = random_for_calc_food * count_of_each_plant / 100
        calculate_food = int(calculate_food)        # converts value to integer
        print(calculate_food, end=', ')
        total_food += calculate_food
    if number of plants > 0:
        print("that is all.")
        return total_food
    else:
        return total_food

function remove_or_not(plant_list, rainfall_value)
    if rainfall_value < RAINFALL_THRESHOLD and number of plants is not 0:
        plant_tobe_deleted = random choice of plant from plant_list
        display "Sadly, your {plant_tobe_deleted} plant has died.")
        remove plant_tobe_deleted from plant_list
        return plant_list
    else:
        return plant_list

function get_valid_plant_name(prompt)
    get new_plant_name
    while new_plant_name is blank:
        display "Invalid plant name"
        get new_plant_name
    return new_plant_name

"""

import random

RAINFALL_THRESHOLD = 30
MIN_RAINFALL = 0
MAX_RAINFALL = 100

print("Welcome to the Market Garden Simulator")
print("Plants cost and generate food according to their name length (e.g., Sage plants cost 4).")
print("You can buy new plants with the food your garden generates.")
print("You get up to 100 mm of rain per day. Not all plants can survive with less than 30.")
print("Let's hope it rains... a lot!")
print("You start with these plants: ")


def main():
    plant_list = ["Parsley", "Sage", "Rosemary", "Thyme"]
    # Calling display() function
    display(plant_list)
    num_days = 0
    food = 0
    # calling status function to show days, number of plants, and food.
    status(num_days, plant_list, food)
    instruction = input("(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit\nChoose: ").title()
    while instruction != "Q":
        if instruction == "W":
            rainfall_value = random.randint(MIN_RAINFALL, MAX_RAINFALL)
            print(f"Rainfall: {rainfall_value}mm")
            # adding a day after waiting
            num_days += 1
            # calculating food to be added by calling get_food function
            food += get_food(rainfall_value, plant_list)
            # checking and removing a plant if required by calling remove_or_not function
            plant_list = remove_or_not(plant_list, rainfall_value)
        elif instruction == "D":
            # calling display function to show plants
            display(plant_list)
        elif instruction == "A":
            # Using function to get a valid plant name
            new_plant = get_valid_plant_name("Enter plant name: ")
            if new_plant in plant_list:
                # checking if plant already exists in list
                print(f"You already have a {new_plant} plant.")
            elif len(new_plant) > food:
                # checking if food available to get the input plant
                print(f"{new_plant} would cost {len(new_plant)} food. With only {food} food, you can't afford it.")
            else:
                # adding new plant to list
                plant_list.append(new_plant)
                # subtracting food
                food -= len(plant_list[-1])
        else:
            print("Invalid choice")
        status(num_days, plant_list, food)
        instruction = input("(W)ait\n(D)isplay plants\n(A)dd new plant\n(Q)uit\nChoose: ").title()
    if len(plant_list) == 0:
        print("You finished with no plants.")
    else:
        print(f"You finished with these {len(plant_list)} plants:\n")
        display(plant_list)
    status(num_days, plant_list, food)
    print("Thank you for simulating. Now go and enjoy a real garden.")


def display(plant_list):
    """Sort and display List of plants"""
    joined_plant_list = ", ".join(plant_list)
    print(joined_plant_list, end=".\n")


def status(num_days, plant_list, food):
    """Shows the status of days, number of plants, and food"""
    print(f"After {num_days} days, you have {len(plant_list)} plants and your total food is {food}.")


def get_food(rainfall_value, plant_list):
    """Calculating new food to be added"""
    total_food = 0
    for i in range(len(plant_list)):
        count_of_each_plant = len(plant_list[i])
        print(plant_list[i], end=" produced ")
        random_for_calc_food = round(random.uniform(rainfall_value/2, rainfall_value))
        calculate_food = random_for_calc_food * count_of_each_plant / 100
        calculate_food = int(calculate_food)
        total_food += calculate_food
        print(calculate_food, end=', ')
    # To compensate for the comma at the end of the for loop
    if len(plant_list) > 0:             # if no plants "that is all" is obsolete
        print("that is all.")
        return total_food
    else:
        return total_food


def remove_or_not(plant_list, rainfall_value):
    """Checking if rainfall under threshold to remove a plant in list or not"""
    if rainfall_value < RAINFALL_THRESHOLD and len(plant_list) != 0:
        plant_tobe_deleted = random.choice(plant_list)
        print(f"Sadly, your {plant_tobe_deleted} plant has died.")
        plant_list.remove(plant_tobe_deleted)
        return plant_list
    else:
        return plant_list


def get_valid_plant_name(prompt):
    """Getting valid plant name"""
    new_plant_name = input(prompt).title()
    while new_plant_name == "":
        print("Invalid plant name")
        new_plant_name = input(prompt).title()
    return new_plant_name


main()
