
def coffee():
    coffee_yield = get_valid_number("Coffee yield (g): ", 0)
    dose = get_valid_number("Coffee dose (g): ", 0)
    brew_ratio = calculate_brew_ratio(coffee_yield, dose)
    style = coffee_style(brew_ratio)
    print(f"The brew ratio is 1:{brew_ratio:.1f}, which is a coffee style of {style}")


def get_valid_number(prompt, low):
    number = float(input(prompt))
    while number < low:
        print("Invalid Input!")
        number = float(input(prompt))
    return number


def calculate_brew_ratio(coffee_yield, dose):
    return coffee_yield / dose


def coffee_style(brew_ratio):
    if brew_ratio < 2:
        return "“ristretto” espresso"
    elif brew_ratio < 3:
        return "“normale” espresso"
    else:
        return "“lungo” espresso"


coffee()
