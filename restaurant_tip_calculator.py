# A quick script to split the bill
print("Welcome to the tip calculator!")
bill = input("What is the total bill in dollars?")
tip_amount = input("How much tip would you like to give? 10, 12, or 15 percent?")
people_splitting_bill = input("How many people are splitting the bill?")

#Turning user input into floats and integers
total_bill = float(bill)
percent_tip = float(tip_amount) / 100 + 1
split_by = int(people_splitting_bill)

def tip_calculaton():
  result = (total_bill * percent_tip) / split_by
  total_rounded = round(result, 2)
  print(f"Each person should pay: ${total_rounded}")
tip_calculaton() ###Output
