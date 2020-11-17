import math


# rounding function
def round_up(amount, round_to):
    # rounds amount UP to the specified amount (round_to)
    return int(round_to * round(math.ceil(amount) / round_to))

# Main Routine starts here
to_round = [2.75, 2.25, 2]

for item in to_round:
  rounded = round_up(item, 1)
  print("${:.2f} --> ${:.2f}".format(item,rounded))
  
