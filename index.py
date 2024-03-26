list1 = {"hats": 5, "doors": 3, "computers": 2}
print(list1)

print("Would you like to change something in the list?")



input_controller = input("Type 'add' to add a product or 'remove' to remove a product: ")

if input_controller.lower() == "add":
    user_product = input("Type the product name: ")
    amount = int(input("Type the product amount: "))
    list1[user_product] = amount
    print("Product added successfully!")

elif input_controller.lower() == "remove":
    print(list1)
    what_to_remove = input("What item do you want to remove? ")
    if what_to_remove in list1:
        del list1[what_to_remove]
        print(f"The item '{what_to_remove}' has been removed.")
    else:
        print("Item not found in the list.")

print(f"youre updated list{list1}")
    
