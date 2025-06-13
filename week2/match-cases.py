direction = int(input("please enter a number in range 1 - 3:: "))


def pretty_direction(direction):
    print("*******************************")
    print(direction)
    print("*******************************")

if direction == 1:
    pretty_direction(direction="top")
if direction == 2:
    pretty_direction(direction="left")
if direction == 3:
    pretty_direction(direction="right")
if direction == 4:
    pretty_direction(direction="bottom")
