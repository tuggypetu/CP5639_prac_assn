
def main():
    num_people = int(input("Number of people: "))
    out_file = open("bmis.txt", 'w')
    for i in range(1, num_people+1):
        height = get_valid_number(f"Person {i} Height (m): ", 0, 3)
        weight = get_valid_number(f"Person {i} Weight (kg): ", 0, 300)
        bmi = calculate_bmi(height, weight)
        if i == 1:
            out_file.write(f"{bmi}")
        else:
            out_file.write(f"\n{bmi}")
    out_file.close()
    in_file = open("bmis.txt", 'r')
    person_num = 0
    for line in in_file:
        bmi_score = float(line)
        category = determine_category(bmi_score)
        person_num += 1
        print(f"Person {person_num}: BMI {bmi_score}, considered {category}.")
    in_file.close()


def get_valid_number(prompt, low, high):
    number = float(input(prompt))
    while number > high or number < low:
        print("Invalid Input!")
        number = float(input(prompt))
    return number


def calculate_bmi(height, weight):
    return f"{weight / height ** 2:.1f}"


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
