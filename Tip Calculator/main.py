#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60



bill_amount = float(input('What is your bill amount? '))
tip_percent = int(input('What % of tip would you will give? '))
no_of_person = int(input('How many members are? '))

total_bill_amt = bill_amount
total_tip_amt = tip_percent / 100 * bill_amount
total_bill_with_tip = total_bill_amt + total_tip_amt
total_bill_with_tip = (total_bill_with_tip / 5)

total_amt = round(total_bill_with_tip,2)

print(f"Each member have to pay tip amount is {total_amt}")
