# function goes here


def num_check(question, num_type):
    valid = False

    # error depends on type
    if num_type == float:
        error = "Please enter a number that is more than zero\n"
    else:
        error = "Please enter an integer (whole number) " \
                "that is more than zero\n"

    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# Main routine goes here
get_int = num_check("How many do you need? ", int)
get_cost = num_check("How much does it cost? ", float)

print("You need: {}".format(get_int))
print("It costs: ${}".format(get_cost))
