i = True

while i == True:
    num1 = float(input('ENTER FIRST NUMBER: '))
    num2 = float(input('ENTER SECOND NUMBER: '))

    sum = num1 + num2
    print(f'THE SUM OF TWO NUMBERS IS: {sum}')

    Question = input('ENTER ANOTHER? [Y/N]: ')

    if Question.lower() == 'y':
        continue
    elif Question.lower() == 'yes':
        continue
    elif Question.lower() == 'n':
        print('Thank you!')
        break
    elif Question.lower() == 'no':
        print('Thank you!')
        break
    else:
        print('Invalid input. Program close!')
        break


