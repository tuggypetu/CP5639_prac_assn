
def main():
    human_years = int(input("Human years: "))
    while human_years >= 0:
        dog_years = calculate_dog_years(human_years)
        print(f"{human_years} human years is {dog_years} dog years.")
        human_years = int(input("Human years: "))
    print("The end.......")


def calculate_dog_years(human_years):
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 21 + 4 * (human_years - 2)
    return dog_years


main()
