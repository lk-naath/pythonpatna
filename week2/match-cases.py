# ==========================================================
# this is session we will try to cover use cases in python
# =========================================================

# this is using if and else for achieveing the same result
direction = input("please enter a number in range 1 - 3:: ")


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


# same as above bt using match and cases
# match and cases doesn't support conditions it only compares the match variable which in this case is direction
# with the case value which in this case we have 4 and last one is fallback value which are (1, 2, 3, 4) and for other _ value

direction = ()

match direction:
    case []:
        pretty_direction(direction="top")
    case {}:
        pretty_direction(direction="left")
    case ():
        pretty_direction(direction="right")
    case 20:
        pretty_direction(direction="bottom")
    case _:
        pretty_direction(direction="invalid range !!")
