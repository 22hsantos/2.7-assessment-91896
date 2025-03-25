
'''

My program will be a menu and ordering system 
for the parody fast food chain “Baco Tell”.
The program allows the user to look through
the food menu, add food to their cart,
customise any food item, and also 
customise delivery options.

'''


#Taco list
Taco_selection = [
    ['Double Taco Supreme',9.50],
    ['Double Crispy Chicken Taco',10.50]
    ]


'''
Prints the taco menu
'''
def taco_menu():
    for (i,taco) in enumerate(Taco_selection, start = 1):
        print(f'{i}. {taco[0]} - ${taco[1]}')
    user_selection(Taco_selection)

"""
Allows the user to enter a number
(ranging from the number of items in the menu list)
and select an item to be added into the basket and/or 
modified.
"""
def user_selection(x):
    print('Enter the number of the item you would like to select\n'
    'to go back, enter B')
    menu_input = int(input('>'))


    """
    if user_selection is more or equal to 1 AND less or equal to the max,
    print the list item corresponding to the menu input?
    """


    if 1 <= user_selection <= len(x):
        print(f'{x[menu_input]}')
    else:
        print('NOOOO')



    


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