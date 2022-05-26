
def main():
    get_time = get_valid_seconds("Duration in seconds: ", 0)
    time_shown = convert_s_to_m_s(get_time)
    print(f"{get_time} seconds is {time_shown}.")
    print()
    for i in range(0, 3600, 635):
        converted_i = convert_s_to_m_s(i)
        print(f"{i} seconds is {converted_i}")
    print()
    get_fav_time = get_valid_seconds("Favourite duration in seconds: ", 0)
    fav_time_shown = convert_s_to_m_s(get_fav_time)
    print(f"You love {fav_time_shown}.")


def get_valid_seconds(prompt, low):
    number = int(input(prompt))
    while number < low:
        print("Invalid Input")
        number = int(input(prompt))
    return number


def convert_s_to_m_s(get_time):
    m = get_time // 60
    s = get_time % 60
    return f"{m}m {s}s"


main()
