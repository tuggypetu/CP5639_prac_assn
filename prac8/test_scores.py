
NUMBER_OF_SCORES = 4


def main():
    scores = []
    for i in range(1, NUMBER_OF_SCORES + 1):
        score = float(input(f"Enter score {i}: "))
        while 100 < score or score < 0:
            print("Invalid input.")
            score = float(input(f"Enter score {i}: "))
        scores.append(score)
    for i in range(NUMBER_OF_SCORES):
        print(f"Score {i+1} was {scores [i]}, which is {get_grade(scores[i])}.")
    average_score = get_average(scores)
    print(f"The average score was {average_score}")
    trend = get_trend(average_score, scores)
    print(f"The trend is {trend}.")


def get_grade(score):
    if score < 50:
        return "N"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"


def get_average(scores):
    avg = sum(scores) / len(scores)
    return avg


def get_trend(average_score, scores):
    if average_score < scores[-1]:
        return "positive"
    else:
        return "not positive"


main()
