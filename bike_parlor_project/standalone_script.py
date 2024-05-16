import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "bike_parlor_project.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW
from bike_parlor_app.models import *

# when the program starts, I want to have a menu that routes user input.
# Create new customer? 
# Start an Order?
# Delete an Order?
# Recieve inventory?
# Edit Inventory?

# start program, routes based on number input.
def main_menu():
    print('Main Menu:')
    print('1. Manage Customers.')
    print('2. Manage Orders.')
    print('3. Manage Inventory.')
    print('4. Quit.')
    
    choice = input('Enter a Number...')
    if choice == "1":
        manage_customers_menu()
    elif choice == "2":
        manage_orders_menu()
    elif choice == "3":
        manage_inventory_menu()
    elif choice == "4":
        print("")
        return
    else:
        print("Invalid choice, try again.")
        main_menu()
   
# menu to initiate customer crud. 
def manage_customers_menu():
    print('\nManage Customers:')
    print('1. Add Customer.')
    print('2. Update Customer.')
    print('3. Delete Customer.')
    print('4. Show All Customers.')
    print('5. Back to Main Menu.')

    choice = input("Enter a Number...")
    if choice == "1":
        add_customer()
    elif choice == "2":
        update_customer()
    elif choice == "3":
        delete_customer()
    elif choice == "4":
        show_customers()
    elif choice == "5":
        main_menu()
    else:
        print("Invalid choice try again...")
        manage_customers_menu()


def add_customer():
    create_customer_first_name = input('Enter Customer\'s first name: ')
    create_customer_last_name = input('Enter Customer\'s last name: ')
    new_customer = Customer.objects.create(first_name=create_customer_first_name, last_name=create_customer_last_name)
    new_customer.save()
    print('Customer Added.')
    manage_customers_menu()

def update_customer():
    update_customer_first_name = input('Enter first name to be updated: ')
    update_customer_last_name = input('Enter last name to be updated: ')
    if not Customer.objects.filter(first_name = update_customer_first_name, last_name = update_customer_last_name).exists():
        print('No matching customer.')
        manage_customers_menu()
    new_first_name = input('Enter new first name: ')
    new_last_name = input('Enter new last name: ')
    Customer.objects.filter(first_name=update_customer_first_name, last_name=update_customer_last_name).delete()
    new_customer = Customer.objects.create(first_name=new_first_name, last_name=new_last_name)
    new_customer.save()
    print('customer updated')
    manage_customers_menu()

def delete_customer():
    delete_customer_first_name = input('Enter first name to be deleted: ')
    delete_customer_last_name = input('Enter last name to be deleted: ')
    # need to take first and last name and compare them against the Customer table and if matching, delete
    Customer.objects.filter(first_name = delete_customer_first_name, last_name = delete_customer_last_name).delete()
    manage_customers_menu()

def show_customers():
    customers = Customer.objects.all()
    for customer in customers:
        print(customer.first_name, customer.last_name)
    while True:
        choice = input('Press 1 to go back. ')
        if choice == "1":
            manage_customers_menu()
            break;
        
def manage_inventory_menu():
    print('\nManage Inventory:')
    print('1. Add inventory.')
    print('2. Update inventory.')
    print('3. Delete inventory.')
    print('4. Show All inventory.')
    print('5. Back to Main Menu.')

    choice = input("Enter a Number...")
    if choice == "1":
        add_inventory()
    elif choice == "2":
        update_inventory()
    elif choice == "3":
        delete_inventory()
    elif choice == "4":
        show_inventory()
    elif choice == "5":
        main_menu()
    else:
        print("Invalid choice try again...")
        manage_inventory_menu()

def add_inventory():
    add_make = input('Enter make: ')
    add_model = input('Enter model: ')
    while True:
        print('1 for Unicycle, 2 for Bicycle, 3 for Tricycle ')
        choice = input('Enter your choice. ')

        if choice == "1":
            add_type = "unicycle"
            break;
        if choice == '2':
            add_type = "bicycle"
            break;
        if choice == '3':
            add_type = "tricycle"
            break;
        else: 
            print('invalid choice ')
    
    add_color = input('Enter Color: ')

    add_price = input('Enter Price: ')
    while True:
        if add_price.isdigit():
            break;
        else:
            print('must be an integer ')
            add_price = input('Enter price: ')
    # check for int
    add_stock = input('How many to stock: ')
    while True:
        if add_stock.isdigit():
            break;
        else:
            print('must be an integer')
            add_stock = input('Enter stock: ')
    # check for int
    new_inventory = Vehicle.objects.create(make=add_make, model=add_model, type=add_type, color=add_color, price=add_price, number_in_stock=add_stock)
    new_inventory.save()
    print('Inventory Added.')
    manage_inventory_menu()

def show_inventory():
    inventory = Vehicle.objects.all()
    for item in inventory:
        print(f"ID: {item.id}, MAKE: {item.make}, MODEL: {item.model}, TYPE: {item.type}, COLOR: {item.color}, PRICE: {item.price}, STOCK: {item.number_in_stock}")
    while True:
        choice = input('Press 1 to go back. ')
        if choice == "1":
            manage_inventory_menu()
            break;

def delete_inventory():
    # display inventory
    inventory = Vehicle.objects.all()
    for item in inventory:
        print(f"ID: {item.id}, MAKE: {item.make}, MODEL: {item.model}, TYPE: {item.type}, COLOR: {item.color}, PRICE: {item.price}, STOCK: {item.number_in_stock}")
    while True:
        choice = input('\nPress 1 to go back.\nPress 2 to delete inventory ')
        if choice == "1":
            manage_inventory_menu()
            break;
        elif choice == "2":
            id_ask = input('which listing would you like to delete? enter ID: ')
            Vehicle.objects.filter(id=id_ask).delete()
            print(f"succesfully deleted")
            manage_inventory_menu()
            break;
    # prompt to delete all 

def update_inventory():
    inventory = Vehicle.objects.all()
    for item in inventory:
        print(f"ID: {item.id}, MAKE: {item.make}, MODEL: {item.model}, TYPE: {item.type}, COLOR: {item.color}, PRICE: {item.price}, STOCK: {item.number_in_stock}")
    while True:
        choice = input('\nPress 1 to go back.\nPress 2 to update a listing ')
        if choice == "1":
            manage_inventory_menu()
            break;
        elif choice == "2":
            id_ask = input('which listing do you want to update? enter ID: ')
            Vehicle.objects.filter(id=id_ask).delete()
            add_make = input('Enter make: ')
            add_model = input('Enter model: ')
            while True:
                print('1 for Unicycle, 2 for Bicycle, 3 for Tricycle ')
                choice = input('Enter your choice. ')

                if choice == "1":
                    add_type = "unicycle"
                    break;
                if choice == '2':
                    add_type = "bicycle"
                    break;
                if choice == '3':
                    add_type = "tricycle"
                    break;
                else: 
                    print('invalid choice ')
            
            add_color = input('Enter Color: ')

            add_price = input('Enter Price: ')
            while True:
                if add_price.isdigit():
                    break;
                else:
                    print('must be an integer ')
                    add_price = input('Enter price: ')
            # check for int
            add_stock = input('How many to stock: ')
            while True:
                if add_stock.isdigit():
                    break;
                else:
                    print('must be an integer')
                    add_stock = input('Enter stock: ')
            # check for int
            new_inventory = Vehicle.objects.create(make=add_make, model=add_model, type=add_type, color=add_color, price=add_price, number_in_stock=add_stock)
            new_inventory.save()
            print('Inventory Updated.')
            manage_inventory_menu()


main_menu()


    # if create_customer_prompt.lower() == "add":
    #     add_user();
    # elif show_customer_list_prompt.lower() == "show":
    #     show_customers();
    # else: main_menu()