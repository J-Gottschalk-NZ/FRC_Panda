def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for item in to_check:
            if response == item:
                return response
            elif response == item[0]:
                return item

        print("Please enter either yes or no...\n")

# Loops to make testing faster...
for item in range(0,6):
  want_help = yes_no("Do want to read the instructions? ")
  print("You said '{}'\n".format(want_help))
