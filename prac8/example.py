
places = []

place = input("Enter place you visited: ").title()
while place != "":
    places.append(place)
    place = input("Enter place you visited: ").title()
if not places:
    print("I went nowhere :(")
else:
    print("On my holiday I went to: ", end='')
    print(*places, sep=', ', end='')
    print('.')
    longest_place = max(places)
    print(f"The place with the longest name was {longest_place}.")
