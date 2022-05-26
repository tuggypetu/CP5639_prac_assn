"""
CP1401 2021-1 Assignment 1
Program 2 – Tennis Results
Student Name: <Siddhanth Biswas>
Date started: <15 December 2021>
Pseudocode:
----------------------------------------
    get your score
    get opponent score
    if your score > opponent score
        print you won.
    elif opponent score > your score
        print you lost.
    else
        print it is a draw.
----------------------------------------
Justification of decision pattern:
The if-elif-else decision pattern was used because there are 3 mutually exclusive cases of winning, losing, and draw.
"""
print("Welcome Player 1. How was your match?")

your_score = int(input("Your score: "))
opp_score = int(input("Opponent score: "))

if your_score > opp_score:
    print("You won! :)")
elif opp_score > your_score:
    print("You lost :( Keep trying.\nCongratulations on playing a fast match!")
else:
    print("It's a draw.\nCongratulations on playing a fast match!")
