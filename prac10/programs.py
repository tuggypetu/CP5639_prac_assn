"""Coding Exercises"""

# 1. Read a String from a File
in_file = open("name.txt", "r")
text = in_file.read().strip()
print(text)

# 2. Write Numbers to a File
out_file = open("range.txt", 'w')
out_file.write("-> All the odd numbers from 0 to 99\n")
for number in range(1, 99+1, 2):
    out_file.write(f"{number:4}")
out_file.write("\n\n")
out_file.write("-> 0 to 100 in 10's\n")
for number in range(0, 100+1, 10):
    out_file.write(f"{number:4}")
out_file.write("\n\n")
out_file.write("-> 20, 19, 18... 0\n")
for number in range(20, -1, -1):
    out_file.write(f" {number},")
out_file.write("\n\n")
out_file.write("-> Divisible by 69 between 1 and 1000\n")
for number in range(69, 1000, 69):
    out_file.write(f" {number}\n")
out_file.write("\n")
out_file.close()


# 3. Greater-Than Counter
file_name = "recentrain.txt"
THRESHOLD_RAIN = 13.9
greater_count = 0
total_count = 0
in_file = open(file_name, 'r')
for i in in_file:
    total_count += 1
    rain_value = float(i)
    if rain_value > THRESHOLD_RAIN:
        greater_count += 1
    else:
        greater_count += 0
print(f"Filename: {file_name}")
print(f"Threshold: {THRESHOLD_RAIN}")
print("Processing....")
print(f"{greater_count} out of {total_count} ({greater_count*100/total_count:.1f}%) values in {file_name} are"
      f" greater than {THRESHOLD_RAIN}.")
