"""
CP1401 - Checkpoint 2
strings.py
"""
# 6. Data Strings
# data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
#                 "Something else that's very important = 9.2%", "x = 42%"]
#
# data_strings = [string.replace(" ", "") for string in data_strings]
#
# print(data_strings)
#
# for string in data_strings:
#     start_index = string.find("=")
#     end_index = string.find("%")
#     value = float(string[start_index + 1:end_index])
#     if value.is_integer():
#         print(f"{value:.0f}")
#     else:
#         print(value)
#
#
# # 7. Date Strings
#
# import datetime
#
#
# def main():
#     print("Enter date of birth. Enter q to quit")
#     get_date = input("DOB (dd/mm/yy) or (dd/mm/yyyy): ")
#     while get_date != "q":
#         value_valid_date = dob_checker(get_date)
#         if value_valid_date == "invalid":
#             print("The date of birth is not valid..")
#         else:
#             print(get_date)
#             day, month, year = get_date.split('/')
#             if len(year) == 4 and int(year) > 1900:
#                 print(f"You were born in {year}")
#                 print(f"You age is/will be {2022 - int(year)} in 2022.")
#             elif len(year) == 2:
#                 if int(year) > 22:
#                     print(f"You were born in 19{year}")
#                     print(f"age is/will be {2022 - 1900 - int(year)} in 2022.")
#                 else:
#                     print(f"You were born in 19{year}")
#                     print(f"age is/will be {2022 - 2000 - int(year)} in 2022.")
#             else:
#                 print("The date of birth is not valid..")
#         get_date = input("DOB (dd/mm/yy)  or (dd/mm/yyyy): ")
#     print("Why u quit lmao")
#
#
# def dob_checker(get_date):
#     if get_date.count("/") == 2:
#         day, month, year = get_date.split('/')
#         if len(year) in [2, 4] and len(month) in [1, 2] and len(day) in [1, 2]:
#             is_valid_date = True
#             try:
#                 datetime.datetime(int(year), int(month), int(day))
#             except ValueError:
#                 is_valid_date = False
#             if is_valid_date and int(year) > 2021:
#                 return "invalid"
#             elif is_valid_date:
#                 return "valid"
#             else:
#                 return "invalid"
#         else:
#             return "invalid"
#     else:
#         return "invalid"
#
#
# main()


# 8. Subject Code Strings

def main():
    get_subject_code = input("Enter Subject Code: ")
    while len(get_subject_code) != 0:
        string_letters = get_subject_code[0:2]
        string_numbers = get_subject_code[2:6]
        string_letters_num = string_letters.isnumeric()
        string_numbers_num = string_numbers.isnumeric()
        if len(get_subject_code) == 6 and string_numbers_num and not string_letters_num:
            string_letters = string_letters.upper()
            year_value = subject_year(string_numbers)
            it_string = ""
            if string_letters == "CP":
                it_string = " IT"
                print(f"This is a {year_value}{it_string} subject.")
            else:
                print(f"This is a {year_value}{it_string} subject.")
        else:
            print("Invalid subject code.")
        get_subject_code = input("Enter Subject Code: ")
    print("bye bye")


def subject_year(string_numbers,):
    string_numbers_1 = int(string_numbers[0])
    if string_numbers_1 == 1:
        return "first-year"
    elif string_numbers_1 == 2:
        return "second-year"
    elif string_numbers_1 == 3:
        return "third-year"
    else:
        return "Masters or other"


main()
