dict = {}

while True: #this will loop the function as long as the user doesnt enter or choose number '3'
    print('1. FOR ADD DATA | 2. FOR DELETE DATA | 3. FOR END')
    choice = input('')
    if choice == '1': 
        add_key = input('Enter Key: ')
        add_value = input('Enter Value: ')
        dict[add_key] = add_value #will add key and value to the dictionary
        print(dict)
        continue #it will loop the function to choose what option it should press
    elif choice == '2':
        del_key = input('Enter Key: ')
        del dict[del_key] #will delete the key that the user input
        print(dict)
        continue
    elif choice == '3':
        print('Thank you!') #exit program
        break
    else:
        print('Invalid Choice!')
        continue




        
