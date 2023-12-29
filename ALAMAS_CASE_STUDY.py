import datetime

def date_format(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def time_format(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

class Reservation():

    def __init__(self, adult, child, ACost = 500, CCost = 300):

        self.adult = adult
        self.child = child
        self.Acost = ACost
        self.Ccost = CCost

    def Overall_total(self):
        return (int(self.adult) * self.Acost) + (int(self.child) * self.Ccost)
    
def delete_reservation(file_name, reserve_num):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            
        if reserve_num > len(lines) or reserve_num == 0:
            print(f'Reservation number {reserve_num} not found.\n')
            return
        
        with open(file_name, 'w') as file:
            for i, line in enumerate(lines, 1):
                if i != reserve_num:
                    file.write(line)
        print(f'\nReservation number {reserve_num} has been deleted. \n')
    except FileNotFoundError:
        print(f'File {file_name} not found!\n')

def count_total(file_name):
    total_adults = 0
    total_children = 0

    try:
        with open(file_name, 'r') as file:
            file.seek(0)
            for line in file:
                parts = line.split()
                if len(parts) >= 5:
                    Aadult = int(parts[3])
                    Cchild = int(parts[4])
                    total_adults += Aadult
                    total_children += Cchild
        
        print(f'\n==========SALES REPORT==========')
        print(f'  Total Number of Adults: {Aadult}')
        print(f'  Total Number of Children: {Cchild}') 

        return total_adults, total_children
        
    except FileNotFoundError:
        print(f'file "{file_name}" not found!')

file_name = 'ALAMAS_CASE_STUDY.txt'

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
                content = file.readlines()
                if not content:
                    print('No reservations found!')
                else:
                    print("{:<10} {:<15} {:<15} {:<25} {:<15} {:<15}".format("#", "Name", "Date", "Time of Arrival", "No. of Adult", "No. of Child"))
                    for i, line in enumerate(content, 1):
                        columns = line.strip().split()
                        Res_num, Nname, Ddate, Ttime, Aadult, Cchild = str(i), columns[0], columns[1], columns[2], columns[3], ' '.join(columns[4:])
                        print('{:<10} {:<15} {:<15} {:<25} {:<15} {:<15}'.format(Res_num, Nname, Ddate, Ttime, Aadult, Cchild))
                    print()
                    continue
        elif choice_lower == 'b':
            Nname = input('\nEnter Name: ')
            while True:
                Ddate = input('Enter Date (YYYY-MM-DD): ')
                if date_format(Ddate):
                    break
                else:
                    print('Invalid Date format! Please enter with Date format (YYYY-MM-DD)')
                    continue

            while True:             
                Ttime = input('Enter Time of arrival (HH:MM): ')
                if time_format(Ttime):
                    break
                else:
                    print('Invalid Time format! Please enter with Time format (HH:MM)')
                    continue
                
            while True:
                try:   
                    Aadult = int(input('No. of Adults: '))
                    break
                except ValueError:
                    print('Please enter a valid number: ')

            while True:
                try:
                    Cchild = int(input('No. of Children: '))
                    with open('ALAMAS_CASE_STUDY.txt', 'a') as file:
                        file.write(f'{Nname}     {Ddate}     {Ttime}     {Aadult}     {Cchild}\n') 
                        print('\nRESERVATION COMPLETE!\n')
                        break
                except ValueError:
                    print('Please enter a valid number: ')
                
        elif choice_lower == 'c':
            with open('ALAMAS_CASE_STUDY.txt', 'r') as file:
                content = file.readlines()
            if not content:
                print('No reservations found!')
            else:
                while True:
                    try:
                        reserve_num = int(input('Enter the reservation number to delete (0 to exit): '))
                        if reserve_num == 0:
                            break
                        else:
                            delete_reservation(file_name, reserve_num)
                            break
                    except ValueError:
                        print('Please enter a valid reservation number. ')

        elif choice_lower == 'd':
            with open('ALAMAS_CASE_STUDY.txt', 'r') as file:
                content = file.readlines()
            if not content:
                print('\nNo reservations found!')
            else:            
                try:
                    total_adults, total_children = count_total(file_name)
                    reserve = Reservation(total_adults, total_children)
                    grand_total = reserve.Overall_total()
                    print(f'  Grand Total: PHP {grand_total:,.2f}\n')
                    continue
                except:
                    pass
            
        elif choice_lower == 'e':
            print('Exit Program. Thank you!')
            break
        else:
            print('\nInvalid Input! Please select between A-E only.')
        print()
    except:
        pass