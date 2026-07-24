#--------------------------------------------
# AI Engineer Bootcamp
# Day 19
# Program: Nested Function
# Author: Om Roy
# Date: 24-07-2026
#--------------------------------------------

def outer():

    def inner():
        print("Inside Inner Function")

    inner()


outer()