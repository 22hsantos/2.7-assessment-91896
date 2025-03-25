
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
def add_to_basket(item):
    print(f'Select {item}? (y/n)')
    confirm_selection = input('>').strip().lower()

    if confirm_selection == 'y':
        basket.append(item)
        
    if confirm_selection == 'n':
        print('Item not added.')

#Taco list
Taco_selection = [
    ['Double Taco Supreme',9.50],
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
and select an item to be added into the basket and/or 
modified.
"""
def user_selection(menu):
    print('Enter the number of the item you would like to select\n'
    'to go back, enter B')
    menu_item = int_input_check(" select one\n>")


    """
    if user_selection is more or equal to 1 AND less or equal to the max,
    print the list item corresponding to the menu input?
    """

    while True:
        if 1 <= menu_item <= len(menu): # checks if number is in range with the list
            break
        else:
            print('Please enter a number in range with available items.')

    add_to_basket(menu[menu_item])



    


def menu():
    while True:
        print('Welcome to Baco Tell')
        print('How can we help you today?')
        print('1. Tacos')
        print('2. Burritos')
        print('3. Snacks & Sides')
        print('4. Desserts')
        print('5. Drinks')
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

        else:
            print('Please enter only numbers 1-5.')




menu()