# ------------------------------------------
# AI Engineer Bootcamp
# Day 2
# Program: Simple GST Calculator
# Author: Om Roy
# Date: 03-07-2026
# --------------------------------------


price=float(input("Enter Price : "))
gst=float(input("Enter GST Rate : "))
gst_amount=(price*gst)/100
total_price=price+gst_amount
print(f"Total Price : {total_price:.2f}")   

#End of the program