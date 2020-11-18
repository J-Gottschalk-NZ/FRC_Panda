# Version 7, attempt to fix output spacing.

# import libraries
import pandas
import math

# *** Functions go here ****


# checks that input is either a float or an
# integer that is more than zero.  Takes in custom error message
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


# Checks that user has entered yes / no to a question
def yes_no(question):

    to_check = ["yes", "no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")


# Checks that string response is not blank
def not_blank(question, error):

    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# Welcomes users and shows instructions on request
def instructions():

    print("****** Welcome to the Fund Raising Calculator ******")

    first_time = yes_no("\nHave you used this program before? ")

    if first_time == "yes":
        return ""

    print()
    print("***** Instructions ******")
    print()
    print("This program will ask you for...")
    print("- The name of the product you are selling")
    print("- How many items you plan on selling")
    print("- The costs for each component of the product")
    print("- How much money you want to make")
    print()
    print("It will then output an itemised list of of the costs with subtotals for the variable and fixed costs.")
    print("Finally it will tell you how much you should sell each item for to reach your profit goal.")
    print()
    print("The data will also be written to a text file which has the same "
          " name as your product.")
    print()


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Gets expenses, returns list which has
# the data frame and sub total
def get_expenses(var_fixed):
    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    expense_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Initial Instruction:
    print("Enter 'xxx' for the item name when done.")

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("Item name: ", "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity:",
                                 "The amount must be a whole number more than zero",
                                 int)
        else:
            quantity = 1

        price = num_check("How much? $",
                          "The price must be a number <more than 0>",
                          float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(expense_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    return [expense_frame, sub_total]


# Prints expense frames
def expense_print(heading, frame, subtotal):
    cost_heading = "**** {} Costs ****".format(heading)
    frame_txt = pandas.DataFrame.to_string(frame)
    subtotal_txt = "{} Costs: ${:.2f}".format(heading, subtotal)

    expense_txt_list = [cost_heading, frame_txt, subtotal_txt]

    return expense_txt_list


# work out profit goal and total sales required
def profit_goal(total_costs):

    # Initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        # ask for profit goal...
        response = input("What is your profit goal (eg $500 or 50%) ")

        # check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no("Do you mean ${:.2f}.  ie {:.2f} dollars? , y / n ".format(amount, amount))

            # Set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no("Do you mean {}%? , y / n".format(amount))
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# rounding function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to


# **** Main Routine goes here ****

instructions()

# Get product name
product_name = not_blank("Product name: ", "The product name can't be blank.")
how_many = num_check("How many items will you be producing? ",
                     "The number of items must be a whole number more than zero", int)

print()
print("Please enter your variable costs below...")
# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")

if have_fixed == "yes":
    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]
else:
    fixed_sub = 0

# work out total costs and profit target
all_costs = variable_sub + fixed_sub

print()
profit_target = profit_goal(all_costs)

# Calculates total sales needed to reach goal
sales_needed = all_costs + profit_target

# Ask user for rounding
print()
round_to = num_check("Round to nearest...? $",
                     "Please enter a whole dollar amount "
                     "(more than zero)", int)

# Calculate recommended price
selling_price = sales_needed / how_many
print("Selling Price (unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)

# *** Set up output list... ****

main_heading = "**** Fund Raising - {} *****".format(product_name)

variable_costs = expense_print("Variable", variable_frame, variable_sub)
variable_lbl = "{}\n{}\n{}".format(variable_costs[0], variable_costs[1], variable_costs[2])

if have_fixed == "yes":
    fixed_costs = expense_print("Fixed", fixed_frame[['Cost']], fixed_sub)
    fixed_costs_lbl = "{}\n{}\n{}".format(
        fixed_costs[0], fixed_costs[1], fixed_costs[2]
    )
else:
    fixed_costs_lbl = "*** No Fixed Costs ***"

total_costs_heading = "**** Total Costs: ${:.2f} ****".format(all_costs)

# Profit Sales Section
target_heading = "**** Profit & Sales Targets ****"
profit_target_lbl = "Profit Target: ${:.2f}".format(profit_target)
sales_lbl = "Total Sales: ${:.2f}".format(all_costs + profit_target)

profit_sales = "{} \n {}\n {}".format(target_heading, profit_target_lbl, sales_lbl)

# Pricing Section
pricing_heading = "**** Pricing *****"
min_price_lbl = "Minimum Price: ${:.2f}".format(selling_price)
recommended_lbl = "Recommended Price: ${:.2f}".format(recommended_price)

pricing = "{}\n {}\n {}".format(pricing_heading, min_price_lbl, recommended_lbl)

output_list = [
    main_heading,
    variable_lbl,
    fixed_costs_lbl,
    total_costs_heading,
    profit_sales, pricing
]

# Output to file
# Replace any spaces in product name with
# underscores so this can be used as a filename
file_name = product_name.replace(" ", "_")

# add .txt extension to filename
file_name = "{}.txt".format(file_name)
text_file = open(file_name, "w+")

# output file content
for item in output_list:
    text_file.write(item)
    text_file.write("\n\n")

# close file
text_file.close()

# **** Printing Area ****
print()
for item in output_list:
    print(item)
    print()
