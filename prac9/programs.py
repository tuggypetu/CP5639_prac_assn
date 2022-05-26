"""
CP1401 - Checkpoint 2
programs.py
"""


def question_1():
    """Print a line of 40 hyphens"""
    for i in range(0, 40):
        i = "-"
        print(i, end=" ")


def question_2():
    """Determine if Integer is Even"""
    get_integer = int(input("Enter integer: "))
    if get_integer % 2 == 1 or get_integer % 2 == -1:
        print(f"Not Even integer. {get_integer} is an odd integer.")
    else:
        print(f"{get_integer} is an Even integer. Yay!")


def question_3():
    """Get and print- name and birthplace"""
    get_name = get_valid_string("Enter your name: ")
    get_birthplace = get_valid_string("Enter your birthplace: ")
    print(f"Hi {get_name} from {get_birthplace}.")


def get_valid_string(prompt):
    """Get a non-empty string from User"""
    get_string = input(prompt)
    while get_string == "":
        print("You didn't enter anything.")
        get_string = input(prompt)
    return get_string


def question_4():
    """Generate a list of integers between Min and Max from user"""
    get_min = int(input("Minimum number: "))
    get_max = int(input("Maximum number: "))
    while get_max < get_min:
        print(f"Your maximum must be greater than {get_min}")
        get_max = int(input("Maximum number: "))
    list_of_numbers = [1,7, 34, 33, 56]
    for numbers in list_of_numbers:
        print(numbers, sep=", ")


def question_5():
    """Get subject code until blank"""
    subject_list = []
    get_subject_code = input("Enter Subject Code: ")
    while len(get_subject_code) != 0:
        if len(get_subject_code) == 6:
            get_subject_code = get_subject_code.upper()
            subject_list.append(get_subject_code)
        else:
            print("Invalid subject code.")
        get_subject_code = input("Enter Subject Code: ")
    if len(subject_list) == 0:
        print("You do no subjects.")
    else:
        print(f"You do {len(subject_list)} subjects:")
        for get_subject_code in subject_list:
            print(get_subject_code)
        if "CP1401" in subject_list or "CP5639" in subject_list:
            print("You are cool.")
        else:
            print("You could be cooler.")


question_4()
