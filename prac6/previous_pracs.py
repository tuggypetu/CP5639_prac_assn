
# Calculate salary for worker level

def main():
    worker_level = validate_worker_level("Worker level: ", 1, 10)
    salary = calculate_salary(worker_level)
    print(f"With worker level {worker_level}, salary is ${salary:.2f}")


def validate_worker_level(prompt, low, high):
    number = int(input(prompt))
    while number < low or number > high:
        print("Invalid worker level.")
        number = int(input(prompt))
    return number


def calculate_salary(worker_level):
    return worker_level * 5000


main()


# Print grid(rows, columns)

def main():
    rows = validate_num("Rows: ", 0)
    columns = validate_num("Columns: ", 0)
    for i in range(rows):
        for j in range(columns):
            print(j, end=" ")
        print()


def validate_num(prompt, low):
    number = int(input(prompt))
    while number < low:
        print("Invalid input.")
        number = int(input(prompt))
    else:
        return number


main()
