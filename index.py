list1 = {"hats": 5, "doors":3,"computers":2}

print("would you want to change something in the list")

input_controller = input("type add to add a product")
if input_controller.lower() == "add" :
    user_product = input("type the product name")  
    amount = int(input("type the product amount"))
list1[user_product] = amount

print (list1)