# import libraries


# *** Functions go here ****

# checks that input is either a float or an
# integer that is more than zero
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



# **** Main Routine goes here ****
