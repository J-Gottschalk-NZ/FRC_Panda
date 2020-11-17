def num_check(question, error, num_type):
    valid = False

    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


#  *** Main routine starts here ***

# Set up dictionaries and lists

component_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Component": component_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# Get user data
item_name = not_blank("Item name: ", "The item name can't be blank.")

# loop to get component, quantity and price
comp_name = ""
while comp_name.lower() != "xxx":

    # get name, quantity and item
    comp_name = not_blank("Component name: ", "The component name can't be blank.")
    if comp_name.lower() == "xxx":
        break

    quantity = num_check("Quantity:",
                         "The amount must be a whole number more than zero",
                         int)
    price = num_check("How much for a single item? $",
                      "The price must be a number <more than 0>",
                      float)

    # add item, quantity and price to lists
    component_list.append(comp_name)
    quantity_list.append(quantity)
    price_list.append(price)
