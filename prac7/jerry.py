# Jerry the driver

CONVERT_CONSTANT_MIL_TO_KM = 1.60934


def main():
    speed_in_mph = get_valid_number("speed in mph: ")
    speed_limit_in_kph = get_valid_number("speed limit in kph: ")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_kph, speed_limit_in_kph)
    bank_balance = get_valid_number("Bank balance: ")
    print(f"Your fine is ${fine}. And your new bank balance is ${bank_balance-fine:.2f}.")


def get_valid_number(prompt):
    number = float(input(prompt))
    while number < 0:
        print("Invalid Input")
        number = float(input(prompt))
    return number


def convert_miles_to_km(speed_in_mph):
    kph_of_given_mph = speed_in_mph * CONVERT_CONSTANT_MIL_TO_KM
    return kph_of_given_mph


def determine_fine(speed_in_kph, speed_limit_in_kph):
    fine = 0
    difference = speed_in_kph - speed_limit_in_kph
    if difference <= 0:
        fine += 0
    elif difference < 13:
        fine += 177
    elif difference < 20:
        fine += 266
    elif difference < 30:
        fine += 444
    elif difference < 40:
        fine += 622
    else:
        fine += 1245
    return fine


main()
