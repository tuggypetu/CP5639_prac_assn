
# record = ["Jimmy", "Smith", (8, 12, 1928), "piano"]
record = ["Wes", "Montgomery", (6, 3, 1923), "guitar"]

print(f"Last name: {record[1]}")
print(f"DOB: {record[2]}")

person_dob = record[2]
print(f"{record[0]} was born in {person_dob[2]} and was a great {record[-1]} player.")
