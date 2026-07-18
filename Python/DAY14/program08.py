#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---class method---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Employee:

    company = "OpenAI"

    @classmethod
    def show_company(cls):
        print(cls.company)


Employee.show_company()