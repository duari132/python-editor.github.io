from csinsc import *
shipping = "shipping_free"
item = "item_balloon"

label .menu
clear()
print("Your item:")
if item == "item_balloon":
    print("🎈")
elif item == "item_popper":
    print("🎉")

print("Shipping mode:")    
if shipping == "shipping_free":
    print(Colour.yellow + "Free!" + Colour.reset)
elif shipping == "shipping_standard":
    print("$5")
    
print("==== Menu ====")
print("[1] Change item")
print("[2] Change shipping")
print("[3] Exit")

choice = input("Enter your choice:")
if choice == "1":
    print(Colour.cyan + "   ==== Select item ====" + Colour.reset)
    print("   [1] 🎈 Balloon")
    print("   [2] 🎉 Popper")    
    item_choice = input("   Enter your item:")
    if item_choice == "1":
        item = "item_balloon"
    elif item_choice == "2":
        item = "item_popper"
    else:
        print(Colour.red + "   Invalid item selection" + Colour.reset)
        input("   Press [Enter] to return to main menu")
elif choice == "2":    
    # enter code for the sub menu below
goto .menu