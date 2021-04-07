fee = int(input(" What is the fee ?" ))
Discount_percent = int(input(" What is the discount percent ?"))


discount_amount= float(("Discount_percent" / 100) * fee)

print(" you have to pay", fee - discount_amount)
