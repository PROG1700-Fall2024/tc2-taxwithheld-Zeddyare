# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    #federal tax is 25% 
    #provincial tax is 6%
    #dependent reduction is 2% per (get back)

    federalTax=0.25
    provincialTax=0.06
    dependentTax=0.02

    print("Tax Withholding Calculator\n")

    salary=float(input("Please enter the full amount of your weekly salary: $"))
    dependents=int(input("How many dependents do you have?: ")) 

    fedTaxHeld=salary*federalTax
    provTaxHeld=salary*provincialTax
    depDeduction=(salary*dependentTax)*dependents 
    totalWithheld=fedTaxHeld+provTaxHeld-depDeduction 
    totalTakeHome=salary-totalWithheld 

    if dependents > 0:
        print("Provincial Tax Withheld: ${0:,.2f}".format(provTaxHeld))
        print("Federal Tax Withheld: ${0:,.2f}".format(fedTaxHeld))
        print("Dependent Deduction for {0} dependents: ${1:,.2f}".format(dependents, depDeduction))
        print("Total Withheld: ${0:,.2f}".format(totalWithheld))
        print("Total Take-Home Pay: ${0:,.2f}".format(totalTakeHome))
    







    # YOUR CODE ENDS HERE

main()
