import math


# rounding function
def round_up(amount, round_to):
    # rounds amount UP to the specified amount (round_to)
    return int(round_to * round(math.ceil(amount) / round_to))

# Main routine starts here
how_many = 200
total = 350
profit_goal = 200

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print("Profit Goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed / how_many
print("Selling Price (unrounded): ${:.2f}".format(selling_price))

recommended_price = round_up(selling_price, 1)
print("Recommended Price: ${:.2f}".format(recommended_price))
  
  
