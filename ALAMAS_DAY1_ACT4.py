#Inquiring user to input values for each varible
name = input('Enter your name: ')
HrsW = float(input('Input how many hours you work: '))
HrsOT = float(input('Input how many hour you overtime: '))
SSS = float(input('Input SSS Contribution: '))
PhilH = float(input('Input PhilHealth Contribution: '))
HLoan = float(input('Input your Housing Loan: '))

#Calculating Gross with taxes

GrossS = (HrsW * 700) + (HrsOT * 850)
Tax = GrossS * 0.2
TDeduc = SSS + PhilH + Tax + HLoan
NSalary = GrossS - TDeduc

#Output
print('=================== PAY SLIP ====================')
print(f'\nNAME: {name}')
print(f'GROSS SALARY : {GrossS:,.2f}')
print(f'SSS : {SSS:,.2f}')
print(f'PHILHEALTH : {PhilH:,.2f}')
print(f'HOUSING LOAN : {HLoan:,.2f}')
print(f'TAX : {Tax:,.2f}')
print(f'TOTAL DEDUCTIONS : {TDeduc:,.2f}')
print(f'NET SALARY : {NSalary:,.2f}')






