
'''

My program will be a menu and ordering system 
for the parody fast food chain “Baco Tell”.
The program allows the user to look through
the food menu, add food to their cart,
customise any food item, and also 
customise delivery options.

'''

#user's basket
basket = []

personal_information = []

card_information = [
    ['card number',16],
    ['expiry date (MMYY)', 4],
    ['CVV', 3],
    ['Cardholder name',20]
    ]

#Taco list
Taco_selection = [
    ['Double Taco Supreme', 9.50],
    ['Double Crispy Chicken Taco',10.50]
    ]

def return_menu():
    input('Press any key to return to the main menu.')
    menu()



def add_to_basket(basket_item):
    '''
    This fn will ask the user if they would like to put the selected
    item into their basket, if yes, the item will be appended. If no,
    They will be taken back into the main menu.
    '''
    
    print(f'Select this item? (y/n)')
    confirm_selection = input('>').strip().lower()

    while True:
        if confirm_selection == 'y':
            basket.append(basket_item)
            print(f'Basket Updated: {basket}')#delete later
            return_menu()
            break
            
        if confirm_selection == 'n':
            print('Item not added.')
            return_menu()
            break

        else:
            print("Please enter 'y' to add the item to the basket. To cancel, enter 'n'")
            confirm_selection = input('>').strip().lower()


def view_basket():
    '''
    Allows the user to view their current basket and either continue shopping, or checkout.
    '''
    total = 0

    for item in basket:
        total += item[1]
        print(f'{item[0]}: ${item[1]:.2f}')
    
    print(f'Total: {total}')
    
    print(""
    "Type '1' to continue shopping\n"
    "Type '2' to checkout")
    
    user_input = int_input_check('>')

    if user_input == 1:
        return_menu()
    if user_input == 2:
        checkout()
    
    while user_input != 1 or user_input != 2:
        print('Please 1 or 2')
        user_input = ('>')


#checkout fn
def checkout():

    total = 0

    for item in basket:
        total += item[1]
    print(f'Total: ${total:.2f}')

    while True:
        print(""
        "'1' to Delivery options\n"
        "'2' to continue shopping.")
        user_input = int_input_check('>')
        
        if user_input == 1:
            delivery_page()

        if user_input == 2:
            return_menu()

        else:
            print("Please enter only '1' or '2'.")


#delivery_page
def delivery_page():
    " Asks the user if they want to pickup or get the food delivered."

    print(""
    "'1' for pickup\n"
    "'2' for delivery\n"
    "Please type number of the option you choose.\n")
    user_input = int_input_check('>')

    if user_input == 1:
        pickup_time()

    if user_input == 2:
        address_page()


def pickup_time():
    print('Due to increase of demand, we have had to allocate four timeslots to pickup food.')
    print(""
    "1. 10:00 am\n"
    "2. 12:00 pm\n"
    "3. 3:00 pm\n"
    "4. 6:00 pm\n"
    "0. Go back"
    "")

    user_input = int_input_check('>')

    while True:
        if 0 < user_input <= 4:
            payment_page()
        
        if user_input == 0:
            return_menu()
        
        else:
            print(''
            'Please input the number of the timeslot you would like to select.\n'
            'To go back, type 0')

def payment_page():
   
   for index, item in enumerate(card_information):
       
       if index == 3:# for cardholder name input
           print('Please enter the cardholder name')
           user_input = input('>')

           if len(user_input) <= 20:
               personal_information.append(user_input)
               print(personal_information)

           while len(user_input) > 20:
               print('Cardholder name must be less that 20 characters!')
               user_input = input('>')

       print(f'Please enter your {item[0]}!!!')
       user_input = (input('>'))
       
       if len(user_input) == item[1]:
           personal_information.append(user_input)
           
       while len(user_input) != item[1]: #checks if user input exceeds the char limit
            print(f"Input doesn't meet character requirement!\n Must be {item[1]} characters long")
            print(f'Please enter your {item[0]}!!!')
            user_input = (input('>'))

def int_input_check(n):
    '''
    Takes user input and checks if it is an integer
    '''
    while True:
        try:
            num = int(input(n))#checks if input is integer
            return num # puts it back into variable
        
        except ValueError:
            print('Please enter only valid numbers')


def taco_menu():
    '''
    Prints the taco menu
    '''
    for (i,taco) in enumerate(Taco_selection, start = 1): #allows index to be printed, starts at 1 instead of 0
        print(f'{i}. {taco[0]} - ${taco[1]}') # (Index). (Item) - $(Price)
    user_selection(Taco_selection)


def user_selection(menu): # inputs the current menu and then runs fn

    """
    Allows the user to enter a number
    (ranging from the number of items in the menu list)
    and select an item to be added into the basket.
    """

    print('Enter the number of the item you would like to select\n'
    'to go back, enter 0')
    menu_item = int_input_check(" select one\n>") #sends through input check fn then returns
    menu_item = menu_item - 1 # -1 to input


    """
    if user_selection is more or equal to 1 AND less or equal to the max, go to customise item
    """
    while True:
        if 0 <= menu_item <= len(menu): # checks if number is in range with the list
            basket_item = customise_item(menu,menu_item) # customises specific menu item, returns item
            print(basket_item)#prints new item
            add_to_basket(basket_item)

        if menu_item == -1:
            return_menu()

        else:
            print('Please enter a number in range with available items.')
            print(menu)
            print('Enter the number of the item you would like to select\n'
            'to go back, enter 0')
            menu_item = int_input_check(" select one\n>") #sends through input check fn then returns
            menu_item = menu_item - 1 # -1 to input

def customise_item(menu, menu_item):
    """
    Allows for the chosen food item to be customised e.g vegan, gluten free.
    """
    while True:
            print(menu[menu_item])
            print(''
        '1. Gluten free option\n'
        '2. Vegan option\n'
        '3. No changes\n'
        '4. Go Back')
            custom_item = int_input_check(">") #sends through input check fn then returns

            basket_item = (menu[menu_item])

            if custom_item == 1:
                basket_item[0] = basket_item[0] + ' (gluten free)'
                return basket_item
            
            if custom_item == 2:
                basket_item[0] = basket_item[0] + ' (Vegan)'
                return basket_item
            
            if custom_item == 3:
                return basket_item

            if custom_item == 4:
                return_menu()

            else:
                print("Please type '1' for Gluten free, '2' for vegan, or '3' to go back.")
            


def menu():
    while True:
        print('Welcome to Baco Tell')
        print('How can we help you today?')
        print('1. Tacos')
        print('2. Burritos')
        print('3. Snacks & Sides')
        print('4. Desserts')
        print('5. Drinks')
        print('6. View basket')
        menu_input = input('>')

        if menu_input == '1':
            taco_menu()
            break

        if menu_input == '2':
            burrito_menu()
            break

        if menu_input == '3':
            snack_side_menu()
            break

        if menu_input == '4':
            dessert_menu()
            break

        if menu_input == '5':
            drink_menu()
            break
        
        if menu_input == '6':
            view_basket()

        else:
            print('Please enter only numbers 1-5.')

def baco_tell_location():

    while True:
        print('Please select your Baco Tell location')
        print(""
        "1. Queenstown\n"
        "2. Dunedin\n"
        "3. Invercargill\n"
        "")

        user_input = int_input_check('>')

        if 0 < user_input <= 3:
            menu()

        else:
            print('please select a number in range')


baco_tell_location()
