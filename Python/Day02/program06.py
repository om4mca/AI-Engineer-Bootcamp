# ------------------------------------------
# AI Engineer Bootcamp
# Day 2
# Program: Profit and Loss
# Author: Om Roy
# Date: 03-07-2026
# ------------------------------------------

cp=float(input("Enter Cost Price : "))
sp=float(input("Enter Selling Price : "))

if sp > cp:
    profit = sp - cp
    print(f"Profit : {profit}")
elif sp < cp:
    loss = cp - sp
    print(f"Loss : {loss}")
else:
    print("No Profit No Loss")


#End of the program