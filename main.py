import json;


# The function load file from json file
def file_load_inventory(file_path):
    
    try:
        with open(file_path , 'r') as file:
            inventory = json.load(file)
    
    except FileNotFoundError:
        inventory = []
    return inventory

# The function is used to save the json in a file
def save_inventories(inventories , file_path):
    
    try: 
        with open(file_path , 'w') as file:
            json.dump(inventories , file , indent = 4)
    
    except:
        print("The file not found")

# The function is used to add inventories
def add_inventory(inventories , name , category , quantity , price):
    
    inventory = {
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price
    }
    inventories.append(inventory)
    print("The inventory is successfully added!!")

# The function is used to view the inventory
def view_inventory(inventories , user_choose_inventory):
    
    for inventory_item in inventories:
        
        name = inventory_item['name']
        category = inventory_item['category']
        price = inventory_item['price']
        print(f"Name: {name} | category: {category} | price: {price}")
        
        
# The function is used to update the quantity on existing name
def update_inventory(inventories , user_choose_name , user_quantity_update):
    
    for inventory_item in inventories:
        name = inventory_item['name']
        
        
        if user_choose_name == name:
            
            inventory_item['quantity'] += user_quantity_update
            print(f" The new quantity: {inventory_item['quantity']}")
            
            break
        
    else:
        print("The name is not found..") 
            
# The function delete the inventory according to the name
def delete_inventory(inventories , user_choose_num):
    
    inventories.pop(user_choose_num - 1)


def main():
    
    file_path = "inventory.json"
    inventories = file_load_inventory(file_path)

    
    
    while True:
        print("Welcome to the python inventory management system..")
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        user_choice = input("Choose the above from (1 - 6): ")
        
        if user_choice == "1":
            name = input("Enter item name: ")
            category = input("Enter the category: ")
            quantity = int(input("Enter the quantity: "))
            price = int(input("Enter the price: "))
            add_inventory(inventories , name , category , quantity , price)
            save_inventories(inventories , file_path)
        
        elif user_choice == "2":
            # user_choose_inventory = input("Enter item name: ")
            view_inventory(inventories)
        
        elif user_choice == "3":
            user_choose_inventory = input("Enter item name: ")
            user_quantity_update = int(input("Enter item quantity: "))
            update_inventory(inventories , user_choose_inventory , user_quantity_update)
            save_inventories(inventories , file_path)
        
        elif user_choice == "4":
            user_choose_num = int(input("Enter number of item to delete: "))
            delete_inventory(inventories , user_choose_num)
            save_inventories(inventories , file_path)
        
        else:
            break
            
            
            
            
            
            
if __name__ == "__main__":
    main()
