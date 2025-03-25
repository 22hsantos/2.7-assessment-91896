
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
Prints the taco menu and allows users to add tacos to the cart (MAKE)
'''
def taco_menu():
    for (i,taco) in enumerate(Taco_selection, start = 1):
        print(f'{i}. {taco[0]} - ${taco[1]}')


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