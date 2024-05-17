import os
import django
import sys
import time
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
from tabulate import tabulate


# when the program starts, I want to have a menu that routes user input.
# Create new customer? 
# Start an Order?
# Delete an Order?
# Recieve inventory?
# Edit Inventory?

# start program, routes based on number input.
def rainbow_text(text):
    colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']  # Red, Yellow, Green, Cyan, Blue, Magenta
    rainbow_text = ''
    for i, char in enumerate(text):
        rainbow_text += colors[i % len(colors)] + char
    rainbow_text += '\033[0m'  # Reset color
    return rainbow_text

def print_rainbow(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def main_menu():
    print('')
    print('Main Menu:')
    print('\n1. Manage Customers.')
    print('2. Manage Orders.')
    print('3. Manage Inventory.')
    print('4. Quit.')
    
    choice = input('\nEnter a Number...')
    if choice == "1":
        manage_customers_menu()
    elif choice == "2":
        manage_orders_menu()
    elif choice == "3":
        manage_inventory_menu()
    elif choice == "4":
        print("")
        quit()
    else:
        print("Invalid choice, try again.")
        main_menu()
   
# menu to initiate customer crud. 
def manage_customers_menu():
    print('\nManage Customers:')
    print('\n1. Add Customer.')
    print('2. Update Customer.')
    print('3. Delete Customer.')
    print('4. Show All Customers.')
    print('5. Back to Main Menu.')

    choice = input("\nEnter a Number...")
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
    create_customer_first_name = input('\nEnter Customer\'s first name: ')
    create_customer_last_name = input('\nEnter Customer\'s last name: ')
    new_customer = Customer.objects.create(first_name=create_customer_first_name, last_name=create_customer_last_name)
    new_customer.save()
    text = "Customer Added Succesfully!"
    print_rainbow(rainbow_text(text))
    print('-------------------------------------------')
    manage_customers_menu()

def update_customer():
    customers = Customer.objects.all()
    customer_data = [(customer.first_name, customer.last_name) for customer in customers]
    headers = ['FIRST NAME', 'LAST NAME']
    print('-------------------------------------------')
    print(tabulate(customer_data, headers=headers, tablefmt='pretty'))
    print('-------------------------------------------')
    update_customer_first_name = input('\nEnter first name to be updated: ')
    update_customer_last_name = input('\nEnter last name to be updated: ')
    if not Customer.objects.filter(first_name = update_customer_first_name, last_name = update_customer_last_name).exists():
        print('\nNo matching customer.')
        manage_customers_menu()
    new_first_name = input('\nEnter new first name: ')
    new_last_name = input('\nEnter new last name: ')
    Customer.objects.filter(first_name=update_customer_first_name, last_name=update_customer_last_name).delete()
    new_customer = Customer.objects.create(first_name=new_first_name, last_name=new_last_name)
    new_customer.save()
    text = "Customer Updated Succesfully!"
    print_rainbow(rainbow_text(text))
    print('-------------------------------------------')
    manage_customers_menu()

def delete_customer():
    customers = Customer.objects.all()
    customer_data = [(customer.first_name, customer.last_name) for customer in customers]
    headers = ['FIRST NAME', 'LAST NAME']
    print('-------------------------------------------')
    print(tabulate(customer_data, headers=headers, tablefmt='pretty'))
    print('-------------------------------------------')
    delete_customer_first_name = input('\nEnter first name to be deleted: ')
    delete_customer_last_name = input('\nEnter last name to be deleted: ')
    # need to take first and last name and compare them against the Customer table and if matching, delete
    Customer.objects.filter(first_name = delete_customer_first_name, last_name = delete_customer_last_name).delete()
    text = "Customer Deleted Succesfully!"
    print_rainbow(rainbow_text(text))
    manage_customers_menu()

def show_customers():
    customers = Customer.objects.all()
    customer_data = [(customer.first_name, customer.last_name) for customer in customers]
    headers = ['FIRST NAME', 'LAST NAME']
    print('-------------------------------------------')
    print(tabulate(customer_data, headers=headers, tablefmt='pretty'))
    print('-------------------------------------------')
    while True:
        choice = input('\nPress 1 to go back. ')
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
    text = "Inventory Added Succesfully!"
    print_rainbow(rainbow_text(text))
    manage_inventory_menu()

def show_inventory():
    inventory = Vehicle.objects.all()
    inventory_data = [(item.id, item.make, item.model, item.type, item.color, item.price, item.number_in_stock) for item in inventory]
    headers = ['ID', 'MAKE', 'MODEL', 'TYPE', 'COLOR', 'PRICE', 'STOCK'] 
    print('------------------------------------------------------')
    print(tabulate(inventory_data, headers=headers, tablefmt='pretty'))
    print('------------------------------------------------------')
    while True:
        choice = input('Press 1 to go back. ')
        if choice == "1":
            manage_inventory_menu()
            break;

def delete_inventory():
    # display inventory
    inventory = Vehicle.objects.all()
    inventory_data = [(item.id, item.make, item.model, item.type, item.color, item.price, item.number_in_stock) for item in inventory]
    headers = ['ID', 'MAKE', 'MODEL', 'TYPE', 'COLOR', 'PRICE', 'STOCK'] 
    print('------------------------------------------------------')
    print(tabulate(inventory_data, headers=headers, tablefmt='pretty'))
    print('------------------------------------------------------')
    while True:
        choice = input('\nPress 1 to go back.\nPress 2 to delete inventory ')
        if choice == "1":
            manage_inventory_menu()
            break;
        elif choice == "2":
            id_ask = input('which listing would you like to delete? enter ID: ')
            Vehicle.objects.filter(id=id_ask).delete()
            text = "Item Deleted Succesfully!"
            print_rainbow(rainbow_text(text))
            manage_inventory_menu()
            break;
    # prompt to delete all 

def update_inventory():
    inventory = Vehicle.objects.all()
    inventory_data = [(item.id, item.make, item.model, item.type, item.color, item.price, item.number_in_stock) for item in inventory]
    headers = ['ID', 'MAKE', 'MODEL', 'TYPE', 'COLOR', 'PRICE', 'STOCK'] 
    print('------------------------------------------------------')
    print(tabulate(inventory_data, headers=headers, tablefmt='pretty'))
    print('------------------------------------------------------')
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
            text = "Inventory Updated Succesfully!"
            print_rainbow(rainbow_text(text))
            manage_inventory_menu()

def manage_orders_menu():
    print('\nManage Orders:')
    print('1. Add Order.')
    print('2. Update Order.')
    print('3. Delete Order.')
    print('4. Show All Orders.')
    print('5. Back to Main Menu.')

    choice = input("Enter a Number...")
    if choice == "1":
        add_order()
    elif choice == "2":
        update_order()
    elif choice == "3":
        delete_order()
    elif choice == "4":
        show_orders()
    elif choice == "5":
        main_menu()
    else:
        print("Invalid choice try again...")
        manage_orders_menu()

def add_order():
    customers = Customer.objects.all()
    customer_data = [(customer.id, customer.first_name, customer.last_name) for customer in customers]
    headers = ['ID', 'FIRST NAME', 'LAST NAME']
    print('-------------------------------------------')
    print(tabulate(customer_data, headers=headers, tablefmt='pretty'))
    print('-------------------------------------------')
        # below, im already referencing customer.objects, in the parameter i can just put id
    while True:
        id_input = input('enter ID number of customer: ')
        if Customer.objects.filter(id=id_input).exists():
            text = "Customer Input Succesfully!"
            print_rainbow(rainbow_text(text))
            break;
        else:
            print("enter a valid id")

    inventory = Vehicle.objects.all()
    inventory_data = [(item.id, item.make, item.model, item.type, item.color, item.price, item.number_in_stock) for item in inventory]
    headers = ['ID', 'MAKE', 'MODEL', 'TYPE', 'COLOR', 'PRICE', 'STOCK'] 
    print('------------------------------------------------------')
    print(tabulate(inventory_data, headers=headers, tablefmt='pretty'))
    print('------------------------------------------------------')
    while True:
        inventory_input = input('enter bike id:')
        if Vehicle.objects.filter(id=inventory_input).exists():
            text = "Bike Input Succesfully!"
            print_rainbow(rainbow_text(text))
            break;
        else:
            print("invalid id")
    bike = Vehicle.objects.get(id=inventory_input)
    customer = Customer.objects.get(id=id_input)
    new_order = CustomerOrder.objects.create(customer=customer, paid_status=False)
    new_order.vehicles.add(bike)
    new_order.save()
    text = f'Order Created Succesfully!'
    print_rainbow(rainbow_text(text))
    print(f'{new_order}')
    manage_orders_menu()
    # new_order.save()


            
            #function to select customer.

def update_order():
    customers = Customer.objects.all()
    customer_data = [(customer.id, customer.first_name, customer.last_name) for customer in customers]
    headers = ['ID', 'FIRST NAME', 'LAST NAME']
    print('-------------------------------------------')
    print(tabulate(customer_data, headers=headers, tablefmt='pretty'))
    print('-------------------------------------------')
    
    while True:
        choice = input('\nPress 1 to go back.\nPress 2 to update an order.')
        if choice == "1":
            manage_orders_menu()
            break;
        elif choice == "2":
            orders = CustomerOrder.objects.all()

            table_data = []

            for order in orders:
                order_row = []
                order_row.append(f"ORDER ID: {order.id}")
                order_row.append(f"NAME: {order.customer.first_name} {order.customer.last_name}")
                order_row.append("BIKE:")
                for vehicle in order.vehicles.all():
                    order_row.append(f"MAKE: {vehicle.make}")
                    order_row.append(f"MODEL: {vehicle.model}")
                    order_row.append(f"TYPE: {vehicle.type}")
                    order_row.append(f"COLOR: {vehicle.color}")
                    order_row.append(f"PRICE: {vehicle.price}")
                order_row.append(f"PAID STATUS: {'Paid' if order.paid_status else 'Not Paid'}")
                table_data.append(order_row)
            print(tabulate(table_data, headers=["Order ID", "Customer Name", "Bike", "Make", "Model", "Type", "Color", "Price", "Paid Status"], tablefmt="grid"))
            id_ask = input('which order do you want to update? enter ID: ')
            CustomerOrder.objects.filter(id=id_ask).delete()
            text = "Customer Deleted Succesfully!"
            print_rainbow(rainbow_text(text))
            customers = Customer.objects.all()
            customer_data = [(customer.id, customer.first_name, customer.last_name) for customer in customers]
            headers = ['ID', 'FIRST NAME', 'LAST NAME']
            print('-------------------------------------------')
            print(tabulate(customer_data, headers=headers, tablefmt='pretty'))
            print('-------------------------------------------')
    
        # below, im already referencing customer.objects, in the parameter i can just put id
            while True:
                id_input = input('enter ID number of customer: ')
                if Customer.objects.filter(id=id_input).exists():
                    text = f'Customer Input Succesfully!'
                    print_rainbow(rainbow_text(text))
                    break;
                else:
                    print("enter a valid id")

            inventory = Vehicle.objects.all()
            inventory_data = [(item.id, item.make, item.model, item.type, item.color, item.price, item.number_in_stock) for item in inventory]
            headers = ['ID', 'MAKE', 'MODEL', 'TYPE', 'COLOR', 'PRICE', 'STOCK'] 
            print('------------------------------------------------------')
            print(tabulate(inventory_data, headers=headers, tablefmt='pretty'))
            print('------------------------------------------------------')
            while True:
                inventory_input = input('enter bike id:')
                if Vehicle.objects.filter(id=inventory_input).exists():
                    text = f'Bike Input Succesfully!'
                    print_rainbow(rainbow_text(text))
                    break;
                else:
                    print("invalid id")
            bike = Vehicle.objects.get(id=inventory_input)
            customer = Customer.objects.get(id=id_input)
            new_order = CustomerOrder.objects.create(customer=customer, paid_status=False)
            new_order.vehicles.add(bike)
            new_order.save()
            text = f'Order Updated Succesfully!'
            print_rainbow(rainbow_text(text))
            print(f'{new_order}')
            manage_orders_menu()

def delete_order():
    orders = CustomerOrder.objects.all()

    table_data = []

    for order in orders:
        order_row = []
        order_row.append(f"ORDER ID: {order.id}")
        order_row.append(f"NAME: {order.customer.first_name} {order.customer.last_name}")
        order_row.append("BIKE:")
        for vehicle in order.vehicles.all():
            order_row.append(f"MAKE: {vehicle.make}")
            order_row.append(f"MODEL: {vehicle.model}")
            order_row.append(f"TYPE: {vehicle.type}")
            order_row.append(f"COLOR: {vehicle.color}")
            order_row.append(f"PRICE: {vehicle.price}")
        order_row.append(f"PAID STATUS: {'Paid' if order.paid_status else 'Not Paid'}")
        table_data.append(order_row)

    print(tabulate(table_data, headers=["Order ID", "Customer Name", "Bike", "Make", "Model", "Type", "Color", "Price", "Paid Status"], tablefmt="grid"))

    while True:
        choice = input('\nPress 1 to go back.\nPress 2 to delete an order ')
        if choice == "1":
            manage_orders_menu()
            break;
        elif choice == "2":
            id_ask = input('which listing would you like to delete? enter ID: ')
            CustomerOrder.objects.filter(id=id_ask).delete()
            text = "Customer Deleted Succesfully!"
            print_rainbow(rainbow_text(text))
            manage_orders_menu()
            break;

def show_orders():
    orders = CustomerOrder.objects.all()

    table_data = []

    for order in orders:
        order_row = []
        order_row.append(f"ORDER ID: {order.id}")
        order_row.append(f"NAME: {order.customer.first_name} {order.customer.last_name}")
        order_row.append("BIKE:")
        for vehicle in order.vehicles.all():
            order_row.append(f"MAKE: {vehicle.make}")
            order_row.append(f"MODEL: {vehicle.model}")
            order_row.append(f"TYPE: {vehicle.type}")
            order_row.append(f"COLOR: {vehicle.color}")
            order_row.append(f"PRICE: {vehicle.price}")
        order_row.append(f"PAID STATUS: {'Paid' if order.paid_status else 'Not Paid'}")
        table_data.append(order_row)

    print(tabulate(table_data, headers=["Order ID", "Customer Name", "Bike", "Make", "Model", "Type", "Color", "Price", "Paid Status"], tablefmt="grid"))
    while True:
        choice = input("Press 1 to go back. ")
        if choice == "1":
            manage_orders_menu()
            break;


main_menu()


    # if create_customer_prompt.lower() == "add":
    #     add_user();
    # elif show_customer_list_prompt.lower() == "show":
    #     show_customers();
    # else: main_menu()