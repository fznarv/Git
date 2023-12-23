# try:
#     with open('ALAMAS_DAY5_ACT1.txt', 'r') as file:
#         content = file.read()
#         if not content.strip():
#             print('No records found! Add records first.')
#         else:
#             lines = content.split('\n')  # Split content into lines
#             print("{:<15} {:<25} {:<15}".format("Name", "Email", "Location"))  # Header line
#             for line in lines:
#                 columns = line.split()  # Split each line into columns
#                 print("{:<15} {:<25} {:<15}".format(columns[0], columns[1], columns[2]))  # Print formatted columns
# except FileNotFoundError:
#     print("The file doesn't exist or cannot be found.")



# try:
#     with open('ALAMAS_DAY5_ACT1.txt', 'r') as file:
#         content = file.read()
#         if not content.strip():
#             print('No records found! Add records first.')
#         else:
#             lines = content.split('\n')  # Split content into lines
#             print("{:<15} {:<25} {:<15}".format("Name", "Email", "Location"))  # Header line
#             for line in lines:
#                 columns = line.split()  # Split each line into columns
#                 if len(columns) >= 3:  # Check if there are at least three columns
#                     name, email, location = columns[0], columns[1], ' '.join(columns[2:])  # Get name, email, and location
#                     print("{:<15} {:<25} {:<15}".format(name, email, location))  # Print formatted columns
#                 else:
#                     print("Insufficient data in line:", line)  # Print a message for lines with insufficient columns
# except FileNotFoundError:
#     print("The file doesn't exist or cannot be found.")





# try:
#     with open('ALAMAS_DAY5_ACT1.txt', 'r') as file:
#         content = file.read()
#         if not content.strip():
#             print('No records found! Add records first.')
#         else:
#             lines = content.split('\n')  # Split content into lines
#             print("{:<15} {:<25} {:<15}".format("Name", "Email", "Location"))  # Header line
#             for line in lines:
#                 columns = line.split()  # Split each line into columns
#                 if len(columns) >= 3:  # Check if there are at least three columns
#                     name, email, location = columns[0], columns[1], ' '.join(columns[2:])  # Get name, email, and location
#                     print("{:<15} {:<25} {:<15}".format(name, email, location))  # Print formatted columns
#                 else:
#                     print(f"Incomplete data: {line}")  # Print a message for lines with insufficient columns
# except FileNotFoundError:
#     print("The file doesn't exist or cannot be found.")


try:
    with open('ALAMAS_DAY5_ACT1.txt', 'r') as file:
        content = file.readlines()  # Read all lines in the file
        if not content:
            print('No records found! Add records first.')
        else:
            print("{:<15} {:<25} {:<15}".format("Name", "Email", "Location"))  # Header line
            for line in content:
                columns = line.strip().split()  # Split each line into columns
                if len(columns) >= 3:  # Check if there are at least three columns
                    name, email, location = columns[0], columns[1], ' '.join(columns[2:])  # Get name, email, and location
                    print("{:<15} {:<25} {:<15}".format(name, email, location))  # Print formatted columns
                else:
                    print(f"Incomplete data: {line}")  # Print a message for lines with insufficient columns
except FileNotFoundError:
    print("The file doesn't exist or cannot be found.")
