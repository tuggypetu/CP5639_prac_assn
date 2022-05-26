
import random


def main():
    total_score = float(input("Subject total score: "))
    while 100 >= total_score >= 0:
        grade = get_grade(total_score)
        print(f"The score {total_score} is {grade}.")
        total_score = float(input("Subject total score: "))
    num_of_random_scores = int(input("How many random scores: "))
    while num_of_random_scores < 0:
        print("Invalid input for number of random scores. Try again.")
        num_of_random_scores = int(input("How many random scores: "))
    for i in range(num_of_random_scores):
        total_score = random.randint(0, 100)
        grade = get_grade(total_score)
        print(f"{total_score} = {grade}")


def get_grade(total_score):
    if total_score < 50:
        return "N"
    elif total_score < 65:
        return "P"
    elif total_score < 75:
        return "C"
    elif total_score < 85:
        return "D"
    else:
        return "HD"


main()
