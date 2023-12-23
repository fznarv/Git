while True:
    print('A : ADD NUMBERS | B : SUBTRACT NUMBERS | C : MULTIPLY NUMBERS | D : DIVIDE NUMBERS')
    choice = input('Choice: ')
    choice_lower = choice.lower()
    if choice_lower == 'a':
        while True:
            try:
                num1 = float(input('Enter First Number: '))
                break
            except ValueError:
                print('Invalid input! Inputs must be numbers only!')
        while True:
            try:
                num2 = float(input('Enter Second Number: '))
                break
            except ValueError:
                print('Invalid input! Inputs must be numbers only!')
        result = num1 + num2
        print(f'ADDITION\n{num1} + {num2} = {result} ')
        while True:
            Question = input('ENTER ANOTHER? [Y/N]: ')
            Quest = Question.lower()
            if Quest == 'y' or Quest == 'yes':
                break
            elif Quest == 'n' or Quest == 'no':
                break
            else:
                print('Invalid input! Please choose between Yes and No only!')
                continue
        if Quest == 'n' or Quest == 'no':
            break         
    elif choice_lower == 'b':
        while True:
            try:
                num1 = float(input('Enter First Number: '))
                break
            except ValueError:
                print('Invalid input! Inputs must be numbers only!')
        while True:
            try:
                num2 = float(input('Enter Second Number: '))
                break
            except ValueError:
                print('Invalid input! Inputs must be numbers only!')
        result = num1 - num2
        print(f'SUBTRACTION\n{num1} - {num2} = {result} ')
        while True:
            Question = input('ENTER ANOTHER? [Y/N]: ')
            Quest = Question.lower()
            if Quest == 'y' or Quest == 'yes':
                break
            elif Quest == 'n' or Quest == 'no':
                break
            else:
                print('Invalid input! Please choose between Yes and No only!')
                continue
        if Quest == 'n' or Quest == 'no':
            break     
    elif choice_lower == 'c':
        while True:
            try:
                num1 = float(input('Enter First Number: '))
                break
            except ValueError:
                print('Invalid input! Inputs must be numbers only!')
        while True:
            try:
                num2 = float(input('Enter Second Number: '))
                break
            except ValueError:
                print('Invalid input! Inputs must be numbers only!')
        result = num1 * num2
        print(f'MULTIPLICATION\n{num1} X {num2} = {result} ')
        while True:
            Question = input('ENTER ANOTHER? [Y/N]: ')
            Quest = Question.lower()
            if Quest == 'y' or Quest == 'yes':
                break
            elif Quest == 'n' or Quest == 'no':
                break
            else:
                print('Invalid input! Please choose between Yes and No only!')
                continue
        if Quest == 'n' or Quest == 'no':
            break              
    elif choice_lower == 'd':
        while True:
            try:
                num1 = int(input('Enter First Number: '))
                break
            except ValueError:
                print('Invalid input! Inputs must be numbers only!')
        while True:
            try:
                num2 = int(input('Enter Second Number: '))
                break
            except ValueError:
                print('Invalid input! Inputs must be numbers only!')
        try:
            result = num1 / num2
            result1 = round(result, 2)
            print(f'DIVISION\n{num1} / {num2} = {result1} ')
        except ZeroDivisionError:
            print('Zero Division Error! Try again!')
            continue
        while True:
            Question = input('ENTER ANOTHER? [Y/N]: ')
            Quest = Question.lower()
            if Quest == 'y' or Quest == 'yes':
                break
            elif Quest == 'n' or Quest == 'no':
                break
            else:
                print('Invalid input! Please choose between Yes and No only!')
                continue
        if Quest == 'n' or Quest == 'no':
            break     
    else:
        print('Invalid input! Please choose between A-D only!')
        continue


