'''
Personal Income Tax Brackets (2026/2027)


Taxable Income (R)	Rates of Tax (R)
1       - 245,100	18% of taxable income
245,101 - 383,100	R44,118 + 26% of taxable income above R245,100
383,101 - 530,200	R79,998 + 31% of taxable income above R383,100
530,201 - 695,800	R125,599 + 36% of taxable income above R530,200
695,801 - 887,000	R185,215 + 39% of taxable income above R695,800
887,001 - 1,878,600	R259,783 + 41% of taxable income above R887,000

'''
print("\nSouth African(zar) TAX Calculator\nthis calculator, calculates tax according to your tax bracket(%)")
print("Brackets(%)\n[18%, 26%, 31%, 36%, 39%, 41%]\n------------------------------\n")
try:
    income = float(input("Enter annual salary (R): "))
    if income < 0:
        print("Salary cannot be negative")
    else:
        if income <= 245100 :
            tax = income * 0.18
        elif income >= 245101 and income <= 383100:
            tax = ((income - 245100) * 0.26 + 44118)
        elif income >= 383101 and income <= 530200:
            tax = ((income - 383100) * 0.31 + 79998)
        elif income >=530201 and income <= 695800:
            tax = ((income - 530200) * 0.36 + 125599)
        elif income >= 695801 and income <= 887000:
            tax = ((income - 695800) * 0.39 + 185215)
        else:
            tax = ((income - 887000) * 0.41 + 259783)
       
    tax = round(tax,0)    
    print(f"annual tax is R{tax}")
except  ValueError as err:
    print("Invalid syntax"+ str(err)) 