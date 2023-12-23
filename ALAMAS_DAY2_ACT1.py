name = input('Enter your name: ')
Mgrade = float(input('Enter your Math grade: '))
Sgrade = float(input('Enter your Science grade: '))
Egrade = float(input('Enter your English grade: '))

Avg = (Mgrade + Sgrade + Egrade) / 3

if Avg >= 75:
    print(f'Average: {Avg:,.2f}')
    print('Congratulations! You have passed the semester. ', end="")
    if Mgrade < 75:
        if Sgrade < 75:
            print('But you need to re-enroll Math, Science next semester')
        elif Egrade < 75:
            print('But you need to re-enroll Math, English next semester')
        else:
            print('But you need to re-enroll Math next semester.') 
    elif Sgrade < 75:
        if Egrade < 75:
            print('But you need to re-enroll Science, English next semester.')
        else:
            print('But you need to re-enroll Science next semester.')
    elif Egrade < 75:
        print('But you need to re-enroll English next semester.')
else:
    print(f'Average: {Avg:,.2f}')
    print('Sorry! You have failed the semester. ')
