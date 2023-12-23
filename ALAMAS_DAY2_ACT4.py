list = []

while True:
    word = input('ENTER A WORD: ')

    list.append(word)
    Question = input('ENTER ANOTHER? [Y/N]: ')

    if Question.lower() == 'y' or Question.lower() == 'yes':
        continue
    elif Question.lower() == 'n' or Question.lower() == 'no':
        print('== WORD LIST ==')
        for i in list:
            print(i)
        count = len(list)
        print(f'NUMBER OF WORDS: {count}')
        print('Thank you.')
        break
    else:
        print('Invalid input. Program close!')
        break