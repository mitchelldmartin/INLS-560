# Part A: while_menu.py

# Prime the loop
menu_option = ''

# While loop to display menu until user enters 'q'
while menu_option != 'q':
    print(
        'MENU:',
        'a: cut and fold brochures',
        'b: deliver print jobs',
        'q: quit',
        sep="\n"
    )
    
    # Get user input
    menu_option = input("Enter a letter for more info around the shop: ").lower()
    
    # Handle menu options
    if menu_option == 'a':
        print("You chose to cut and fold brochures. Make sure to use safety gloves!")
    elif menu_option == 'b':
        print("You chose to deliver print jobs. Don't forget to check the delivery schedule!")
    elif menu_option != 'q':  # Handle invalid input
        print("Invalid option. Please choose 'a', 'b', or 'q'.")
