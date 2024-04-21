"""
Start 

Display a menu with options related to shopping cart
Implement While loop to keep the menu running (after user has selcted options)
Provide the user with the option to end the program (Break out of while)

End
"""

print("Welcome to my shop!\n")
while True:
    menu = input(" Select the Item following:\n\
             1. Add Item \n\
             2. Remove Item \n\
             3. Update Item \n\
             4. Exit Cart\n\
                 : " ) 
    
    if menu == "1":
        print("Added Item")         
    elif menu == "2":
        print("Item removed")
    elif menu == "3":
        print("Item updated")
    elif menu == "4":
        print("Have a good day!")
        break
    else:
        print("Invalid option \
              ")
    while True:
        Added_item = 0
        if Added_item:list
        list = input("select the List of the item:\n\
                            a. Apple, bannan, oranges and fresh fruit\n\
                            b. onion, garlik, spinach, cucumber,green vegitables and important vegitable\n\
                            c. Milk, Yogert, cheess and all dery product\n\
                            d. All veggan products\n\
                            e. chocolate, cookies, cake, cup cake and sweets\n\
                            f. all the frozen item, icecream, peas, etc\n\
                               :   ")
        if list == "a":
            A = ["Apple", "bannan", "oranges" and "all fresh fruit"]
            A_list = A[0]
            print(A)
