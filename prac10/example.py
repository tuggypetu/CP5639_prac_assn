"""Calculate average score from file"""

total_score = 0
num_instances = 0
in_file = open("scores.txt", 'r')
# in_file = open("recentrain.txt", 'r')
for i in in_file:
    score = float(i)
    total_score += score
    num_instances += 1
    print(f"Score = {score:4.1f}       Total score so far = {total_score:5.1f}")
in_file.close()
print(f"The average is {total_score/num_instances:.1f}")
