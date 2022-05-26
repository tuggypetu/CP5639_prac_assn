
def main():
    print()
    print("Fixed height, various weights BMIs:")
    height = get_valid_number("Enter height (m): ", 0, 3)
    for weight in range(50, 101, 2):
        bmi = calculate_bmi(height, weight)
        category = determine_category(bmi)
        print(f"Height {height:.2f}m, Weight {weight:4}kg = BMI {bmi:.1f}, considered {category}.")
    print()
    print("----------------------------------------------------")
    print("Various height and weight BMIs:")
    for height in range(150, 200, 10):
        height /= 100
        for weight in range(50, 101, 10):
            bmi = calculate_bmi(height, weight)
            category = determine_category(bmi)
            print(f"Height {height:.1f}m, Weight {weight:4}kg = BMI {bmi:.1f}, considered {category}.")


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number < low or number > high:
        print("Invalid Input.")
        number = float(input(prompt))
    return number


def calculate_bmi(height, weight):
    cal_bmi = weight / height ** 2
    return cal_bmi


def determine_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese! Too fat"


main()
