
def main():
    enter_number = int(input("Enter number: "))
    while enter_number < 0:
        print("Invalid Input!")
        enter_number = int(input("Enter number: "))
    parity = get_parity(enter_number)
    odd_or_even = get_odd_even(parity)
    print("The parity of {} is {}. {} is an {} number.".format(enter_number, parity, enter_number, odd_or_even))


def get_parity(enter_number):
    return enter_number % 2


def get_odd_even(parity):
    if parity == 1:
        return "odd"
    else:
        return "even"


main()
