class Reservation:

    def __init__(self, name, date, time, adult, child, adultPay, childPay):
        self.name = name
        self.date = date
        self.time = time
        self.adult = adult
        self.child = child
        self.adultPay = adultPay
        self.childPay = childPay

    def average(self):
        return self.adult + self.child




while True:
    try:
        print('Select')
        print(' A. View all Reservations')
        print(' B. Make Reservation')
        print(' C. Delete reservation')
        print(' D. Generate Report')
        print(' E. Exit Program\n')

        Choice = input('Enter Selection: ')
        choice_lower = Choice.lower()
        if choice_lower == 'a':
            print()
            with open('ALAMAS_CASE_STUDY.txt', 'r') as file:
                content = file.read()
                if not content.strip():
                    print('No records found! Add records first.')
                else:
                    lines = content.split('\n')
                    for line in lines:
                        columns = line.split()
                        print('{:<15} {:<25} {:<15}'.format(columns[0], columns[1], columns[2]))
                    print()
                    continue
        elif choice_lower == 'b':
            Nname = input('Enter Name: ')
            Ddate = input('Enter Date: ')
            Ttime = input('Enter Time: ')
            Aadult = input('No. of Adults: ')
            Cchild = input('No. of Children: ')
            
            with open('ALAMAS_CASE_STUDY.txt', 'a+') as file:
                file.write(f'{Nname}          ')
        elif choice_lower == 'c':
            break
        elif choice_lower == 'd':
            break
        elif choice_lower == 'e':
            print('Exit Program. Thank you!')
        else:
            print('Invalid Input! Please select between A-E only.')
        print()
    except:
        pass