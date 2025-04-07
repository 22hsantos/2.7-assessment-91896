
"""
bare minimum :(
"""

basket = []


def return_menu():
    input('Press any key to return to the main menu.')
    menu()


#Taco list
Taco_selection = [
    ['Double Taco Supreme', 9.50],
    ['Double Crispy Chicken Taco',10.50]
    ]


def taco_menu():
    for (i,taco) in enumerate(Taco_selection, start = 1): #allows index to be printed, starts at 1 instead of 0
        print(f'{i}. {taco[0]} - ${taco[1]}') # (Index). (Item) - $(Price)
    user_selection(Taco_selection)


def user_selection(menu): # taco tingz

    while True:
            print('Enter the number of the item you would like to select\n'
            'to go back, enter 0')
            menu_item = int(input(" select one\n>"))
            menu_item = menu_item - 1 # -1 to input

            if 0 <= menu_item <= len(menu): # checks if number is in range with the list
                basket_item = (menu[menu_item]) # customises specific menu item, returns item
                basket_item[0] = basket_item[0] + ' NEW NE EW'
                print(basket_item)#prints new item
                return_menu()

            if menu_item == -1:
                return_menu()

            else:
                print('Please enter a number in range with available items.')


def menu():
    while True:
        print('MENU ORDER NOW')
        print('1. Tacos')
        print('6. View basket')
        menu_input = input('>')
        
        if menu_input == '1':
            taco_menu()
        if menu_input == '6':
            view_basket()

        else:
            print('Please enter only numbers 1 or 6 .')


colours = ['red', 'blue', 'yellow']

list = []

for index, colour in enumerate(colours, 1):

    if index == 1:
        print(index)
        print('hihi')
        user_input = input('>')
        list.append(user_input)

    else:
        user_input = ('hi')
        list.append(user_input)