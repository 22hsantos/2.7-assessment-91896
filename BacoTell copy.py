
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

def return_menu():
    input('Press any key to return to the main menu.')
    menu()


'''
This fn will ask the user if they would like to put the selected
item into their basket, if yes, the item will be appended. If no,
They will be taken back into the main menu.
'''
def add_to_basket(basket_item):
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


'''
Allows the user to view their current basket and either continue shopping, or checkout.
'''
def view_basket():
    for item in basket:
        print(f'{item[0]}: {item[1]:.2f}')
    
    return_menu()

#Taco list
Taco_selection = [
    ['Double Taco Supreme', 9.50],
    ['Double Crispy Chicken Taco',10.50]
    ]

'''
Takes user input and checks if it is an integer
'''
def int_input_check(n):

    while True:
        try:
            num = int(input(n))#checks if input is integer
            return num # puts it back into variable
        
        except ValueError:
            print('Please enter only valid numbers')


'''
Prints the taco menu
'''
def taco_menu():
    for (i,taco) in enumerate(Taco_selection, start = 1): #allows index to be printed, starts at 1 instead of 0
        print(f'{i}. {taco[0]} - ${taco[1]}') # (Index). (Item) - $(Price)
    user_selection(Taco_selection)


"""
Allows the user to enter a number
(ranging from the number of items in the menu list)
and select an item to be added into the basket.
"""
def user_selection(menu): # inputs the current menu and then runs fn
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




"""
Allows for the chosen food item to be customised e.g vegan, gluten free.
"""
def customise_item(menu, menu_item):
    while True:
            print(menu[menu_item])
            print(''
        '1. Gluten free option\n'
        '2. Vegan option\n'
        '3. Go Back')
            custom_item = int_input_check(">") #sends through input check fn then returns

            if custom_item == 1:
                basket_item = (menu[menu_item])
                basket_item[0] = basket_item[0] + ' (gluten free)'
                return basket_item
            
            if custom_item == 2:
                basket_item[0] = basket_item[0] + ' (Vegan)'
                return basket_item
            
            if custom_item == 3:
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




menu()