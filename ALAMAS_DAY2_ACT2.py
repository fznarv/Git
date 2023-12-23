DEPT = input('Enter Designated Office [IT/ACCT/HR]: ').lower()

if DEPT == 'it':
    Years_in_Service = int(input('Enter the Number of years in Service: '))
    if Years_in_Service >= 10:    
        Bonus = 10000
    else: 
        Bonus = 5000
    print(f'Your bonus is {Bonus:,.2f}')

elif DEPT == 'acct':
    Years_in_Service = int(input('Enter the Number of years in Service: '))
    if Years_in_Service >= 10:
        Bonus = 12000
    else:
        Bonus = 6000
    print(f'Your bonus is {Bonus:,.2f}')

elif DEPT == 'hr':
    Years_in_Service = int(input('Enter the Number of years in Service: '))
    if Years_in_Service >= 10:
        Bonus = 15000
        print(f'Your bonus is {Bonus:,.2f}')
    else:
        Bonus = 7500
        print(f'Your bonus is {Bonus:,.2f}')
else:
    print('Invalid office.')