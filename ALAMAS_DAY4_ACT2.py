class Student:
    def __init__(self, name, mathG, scieG, englG):
        self.name = name
        self.mathG = mathG
        self.scieG = scieG
        self.englG = englG

    def average(self):
        return (self.mathG + self.scieG + self.englG) / 3

while True:
    try:
        Nstud = input('Enter Name: ')
        if Nstud.isalpha():
            break
        else:
            print('Please input your name!')
            continue
    except:
        pass

while True:
    try:
        Mstud = float(input('Math grade: '))
        break
    except ValueError:
        print('Invalid Input! Please enter your Math grade!')
        continue

while True:
    try:
        Sstud = float(input('Science grade: '))
        break
    except ValueError:
        print('Invalid Input! Please enter your Science grade!')
        continue

while True:
    try:
        Estud = float(input('English grade: '))
        break
    except ValueError:
        print('Invalid Input! Please enter your English grade!')
        continue       


Sstud = Student(Nstud, Mstud, Sstud, Estud)
Oavg = Sstud.average()

print(f'\nName: {Sstud.name}')
print(f'Math: {Sstud.mathG}')
print(f'Science: {Sstud.scieG}')
print(f'English: {Sstud.englG}')
print(f'Average: {Oavg:.2f} {'(Passed)' if Oavg >= 75 else '(Failed)'}')
