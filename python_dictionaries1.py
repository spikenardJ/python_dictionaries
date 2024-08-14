# Question 1: Real-World Python Dictionary Applications

# Task 1: Restaurant Menu Update

def add_category(menu, category):
    if category not in menu:
        menu[category] = {}
        print(f"Category '{category}' added to the menu.")
    else:
        print(f"Category '{category}' already exists in the menu.")

def add_item(menu, category, item, price):
    if category in menu:
        if item not in menu[category]:
            menu[category][item] = price
            print(f"Item '{item}: {price}' added to the '{category}' in the menu.")
        else:
            print(f"Item '{item}: {price}' already exist in '{category}' in the menu.")
    else:
        add_category(menu, category)
        print(f"Category '{category}' does not exist in the menu.")

def display_menu(menu):
    print("\n   MENU")
    for category, items in menu.items():
        print("\n" , category)
        print("-------------")
        for key in items:
            print(key + ":", items[key])

def remove_item(menu, category, item):
    if category in menu:
        if item in menu[category]:
            del restaurant_menu[category][item]
            print(f"Item '{item}' has been removed from the menu.")
        else:
            print(f"Item '{item}' does not exist in the menu.")
    else:
        remove_item(menu, category)
        print(f"Category '{category}' does not exist in the menu.")
    

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Main Course"]["Steak"] = 17.99

add_category(restaurant_menu, "Beverages")
add_item(restaurant_menu,"Beverages", "Tea", 1.99)
add_item(restaurant_menu, "Beverages", "Coke", 1.99)
add_item(restaurant_menu, "Beverages", "Coffee", 1.29)
add_item(restaurant_menu, "Starters", "Salad", 4.99)
remove_item(restaurant_menu, "Starters", "Bruschetta")
display_menu(restaurant_menu)