# Prime the loop
menu_option = ''

# While loop to display menu until user enters 'q'
while menu_option != 'q':
    print(f'''
    Shop information FAQS:
    a: cut and fold brochures
    b: deliver print jobs
    q: exit 
    ''')
    
    # Get user input
    menu_option = input("Enter a letter for more info around the shop: ").lower()
    
    # Handle menu options
    if menu_option == 'a':
        print("The cutter and folder can be dangerous. Get training before using!")
    elif menu_option == 'b':
        van_driver = input("Are you comfortable driving a class B van? Enter (y or n): ").lower()
        if van_driver == 'y':
            print("Awesome! It would be great to have you help deliver on occasion!")
        else:
            print("We won't ask you to drive!")
    elif menu_option != 'q': 
        print("Invalid option. Please choose 'a', 'b', or 'q'.")