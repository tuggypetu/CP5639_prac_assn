
import random
MINIMUM_LIMIT = 0
instances = int(input("How many numbers do you want? : "))
maximum_number = int(input("What is the maximum number? : "))

random_list = random.sample(range(MINIMUM_LIMIT, maximum_number), instances)
print(f"The numbers are: {random_list}.")

min_num_list = min(random_list)                             # minimum
print(f"The minimum is {min_num_list}.")
max_num_list = max(random_list)                             # maximum
print(f"The maximum is {max_num_list}.")

random_choice = random.choice(random_list)                  # random choice from existing list
print(f"A randomly chosen number is {random_choice}.")

random_list.reverse()                                       # the list reversed
print(f"The numbers reversed are{random_list}.")
random_list.sort()                                          # the list sorted
print(f"The numbers sorted are{random_list}.")
