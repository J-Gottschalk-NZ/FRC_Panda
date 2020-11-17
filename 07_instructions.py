def instructions():

  print("****** Welcome to the Fund Raising Calculator ******")

  first_time = input("\nHave you used this program before? ")

  if first_time == "yes":
    return ""
  
  print()
  print("***** Instructions ******")
  print()
  print("This program will ask you for...")
  print("- The name of the product you are selling")
  print("- How many items you plan on selling")
  print("- The costs for each component of the product")
  print("- How much money you want o make")
  print()
  print("It will then output an itemised list of of the costs with subtotals for the variable and fixed costs.")
  print("Finally it will tell you how much you should sell each item for to reach your profit goal.")
  print()

instructions()