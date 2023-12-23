while True:
    try:
        print('[A] ADD RECORD | [B] VIEW RECORDS | [C] CLEAR ALL RECORDS | [D] EXIT ')
        Choice = input('Enter Choice: ')
        choice_lower = Choice.lower()
        
        if choice_lower == 'a':
            Record_holder_Name = input('Enter Name: ')
            Record_holder_Email = input('Enter Email: ')
            Record_holder_Address = input('Enter Address: ')
            with open('ALAMAS_DAY5_ACT1.txt', 'a+') as file:
                file.write(f'{Record_holder_Name}     {Record_holder_Email}     {Record_holder_Address}     \n')
            print(f'Record of {Record_holder_Name} is added! \n')
            continue

        elif choice_lower == 'b':
            print()
            try:
                with open('ALAMAS_DAY5_ACT1.txt', 'r') as file:
                    content = file.readlines()
                    if not content:
                        print('No records found! Add records first.')
                    else:
                        print("{:<15} {:<25} {:<15}".format("Name", "Email", "Location"))
                        for line in content:
                            columns = line.strip().split()
                            if len(columns) >= 3:
                                name, email, location = columns[0], columns[1], ' '.join(columns[2:])
                                print("{:<15} {:<25} {:<15}".format(name, email, location))
                                continue
                            else:
                                (f"Incomplete data: {line}")              
            except FileNotFoundError:
                print("The file doesn't exist or cannot be found")
      
        elif choice_lower == 'c':
            with open('ALAMAS_DAY5_ACT1.txt', 'r+') as file:
                file.truncate(0)
                print('All records are cleared. No records found. \n')
                continue

        elif choice_lower == 'd':
            print('Thank you!')
            break
        else:
            print('Invalid Input! Please choose between A-D only! \n')
    except ValueError:
        print('Invalid Input!')
