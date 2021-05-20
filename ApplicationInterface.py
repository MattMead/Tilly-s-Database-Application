import mysql.connector
import pandas as pd
import pyfiglet
from pandas import DataFrame
import re

# Pandas display options
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)


# Connecting to database
db = mysql.connector.connect(
        host='34.94.182.22',
        user='pascualmead@chapman.edu',
        passwd='FooBar!@#$',
        database='pascualmead_db',
    )

# Creating a cursor
mycursor = db.cursor()

# Database main menu
def mainMenu():
        out = pyfiglet.figlet_format("Tilly's Database", font="slant")
        print(out)
        print("                              DATABASE MENU")
        print("                       |-------------------------|")
        print("                       | (1)Display Data         |")
        print("                       | (2)Delete Data          |")
        print("                       | (3)Update Data          |")
        print("                       | (4)Create Data          |")
        print("                       | (5)Data Reports         |")
        print("                       | (6)Exit Application     |")
        print("                       |-------------------------|")

# Display Data Menu
def displayMenu():
        out = pyfiglet.figlet_format("Display Data", font="slant")
        print(out)
        print("                          DISPLAY MENU")
        print("                  |-------------------------|")
        print("                  | (1)Customers Data       |")
        print("                  | (2)Employees Data       |")
        print("                  | (3)Stores Data          |")
        print("                  | (4)Brands Data          |")
        print("                  | (5)Items Data           |")
        print("                  | (6)Sales Data           |")
        print("                  | (7)Sale Items Data      |")
        print("                  | (8)Back to Main Menu    |")
        print("                  |-------------------------|")

# Delete Menu
def deleteMenu():
        out = pyfiglet.figlet_format("Delete Data", font="slant")
        print(out)
        print("                         DELETE MENU")
        print("                 |-------------------------|")
        print("                 | (1)Delete Customer      |")
        print("                 | (2)Delete Employee      |")
        print("                 | (3)Delete Store         |")
        print("                 | (4)Delete Brand         |")
        print("                 | (5)Delete Item          |")
        print("                 | (6)Delete Sale          |")
        print("                 | (7)Back to Main Menu    |")
        print("                 |-------------------------|")

# Update Menu
def updateMenu():
        out = pyfiglet.figlet_format("Update Data", font="slant")
        print(out)
        print("                          UPDATE MENU")
        print("                 |-----------------------|")
        print("                 | (1)Update Customer    |")
        print("                 | (2)Update Employee    |")
        print("                 | (3)Update Store       |")
        print("                 | (4)Update Brand       |")
        print("                 | (5)Update Item        |")
        print("                 | (6)Update Sale        |")
        print("                 | (7)Update Sale Items  |")
        print("                 | (8)Back to Main Menu  |")
        print("                 |-----------------------|")

# Insert Menu
def insertMenu():
        out = pyfiglet.figlet_format("Create Data", font="slant")
        print(out)
        print("                         CREATE MENU")
        print("                 |-------------------------|")
        print("                 | (1)Create Customer      |")
        print("                 | (2)Create Employee      |")
        print("                 | (3)Create Store         |")
        print("                 | (4)Create Brand         |")
        print("                 | (5)Create Item          |")
        print("                 | (6)Create Sale          |")
        print("                 | (7)Back to Main Menu    |")
        print("                 |-------------------------|")

# Query Menu
def queryMenu():
        out = pyfiglet.figlet_format("Data Reports", font="slant")
        print(out)
        print("                        REPORTS MENU")
        print("                 |-------------------------|")
        print("                 | (1)Company Reports      |")
        print("                 | (2)Store Reports        |")
        print("                 | (3)Employee Reports     |")
        print("                 | (4)Customer Reports     |")
        print("                 | (5)Brand Reports        |")
        print("                 | (6)Item Reports         |")
        print("                 | (7)Back to Main Menu    |")
        print("                 |-------------------------|")

# Company Menu
def companyMenu():
        out = pyfiglet.figlet_format("Company Data", font="slant")
        print(out)
        print("                        COMPANY MENU")
        print("                 |-------------------------|")
        print("                 | (1)Total Revenue        |")
        print("                 | (2)Top 5 State Revenue  |")
        print("                 | (3)Total Employees      |")
        print("                 | (4)Total Stores         |")
        print("                 | (5)Back to Reports Menu |")
        print("                 |-------------------------|")

# Store Menu
def storeMenu():
        out = pyfiglet.figlet_format("Store Data", font="slant")
        print(out)
        print("                    STORE MENU")
        print("          |----------------------------|")
        print("          | (1)Top 5 Store Revenues    |")
        print("          | (2)Lowest 5 Store Revenues |")
        print("          | (3)Back to Reports Menu    |")
        print("          |----------------------------|")

# Employee Menu
def employeeMenu():
        out = pyfiglet.figlet_format("Employee Data", font="slant")
        print(out)
        print("                              EMPLOYEE MENU")
        print("                 |-------------------------------------|")
        print("                 | (1)Top 5 Performing Employees       |")
        print("                 | (2)Bottom 5 Performing Employees    |")
        print("                 | (3)Top Employees by State           |")
        print("                 | (4)Employees Above Sales Cutoff     |")
        print("                 | (5)Employees Below Sales Cutoff     |")
        print("                 | (6)Employee Sales by Store          |")
        print("                 | (7)Employee Search                  |")
        print("                 | (8)Back to Reports Menu             |")
        print("                 |-------------------------------------|")

# Customer Menu
def customerMenu():
        out = pyfiglet.figlet_format("Customer Data", font="slant")
        print(out)
        print("                              CUSTOMER MENU")
        print("                      |---------------------------|")
        print("                      | (1)5 Best Customers       |")
        print("                      | (2)Back to Reports Menu   |")
        print("                      |---------------------------|")

# Brand Menu
def brandMenu():
        out = pyfiglet.figlet_format("Brand Data", font="slant")
        print(out)
        print("                     BRAND MENU")
        print("           |-----------------------------|")
        print("           | (1)5 Most Popular Brands    |")
        print("           | (2)5 Least Popular Brands   |")
        print("           | (3)5 Highest Revenue Brands |")
        print("           | (4)5 Lowest Revenue Brands  |")
        print("           | (5)Back to Reports Menu     |")
        print("           |-----------------------------|")

# Item Menu
def itemMenu():
        out = pyfiglet.figlet_format("Item Data", font="slant")
        print(out)
        print("                    ITEM MENU")
        print("          |----------------------------|")
        print("          | (1)5 Most Popular Items    |")
        print("          | (2)5 Least Popular Items   |")
        print("          | (3)Highest 5 Revenue Items |")
        print("          | (4)Lowest 5 Revenue Items  |")
        print("          | (5)Back to Reports Menu    |")
        print("          |----------------------------|")

# Method to export reports to csv
def exportCSV(df):
        while True:
                try:
                        choice = int(input("Would you like to export this report to a CSV?\n(1)Yes (2)No: "))
                except ValueError:
                        print("This is not a valid value. Try again.")
                        continue
                if isinstance(choice, int):
                        break
        if choice == 1:
                file_name = input("Name the file: ")
                csv_file = file_name + ".csv"
                df.to_csv(csv_file,index = False)
                print("Data exported to '" + csv_file +"'")
        else:
                print("")

# Method that Clears the terminal
def newPage():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")




# Starting the Interface
while True:
        mainMenu()
        while True:
            try:
                choice = int(input("\nSelect the number you would like: "))
            except ValueError:
                print("This is not a valid value. Try again.")
                continue
            if isinstance(choice, int):
                break
        #Displaying Data
        if choice == 1:
                newPage()
                while True:
                        displayMenu()
                        while True:
                                try:
                                        selection = int(input("\nSelect the data you would like to display: "))
                                except ValueError:
                                        print("This is not a valid value. Try again.")
                                        continue
                                if isinstance(selection, int):
                                        break
                        print("\n")
                        # Displays Customer Data
                        if selection == 1:
                                formatting = "-----------------------------------------------------------------------------"
                                mycursor.execute("SELECT * FROM Customers;")
                                myrecords = mycursor.fetchall()
                                df = DataFrame(myrecords)
                                df.columns = ['CustomerId', 'FirstName', 'LastName', 'Email', 'Phone']
                                newPage()
                                print("                                     CUSTOMERS")
                                print(formatting)
                                print(df)
                                print(formatting)
                                print("\n")
                        # Displays Employee Data
                        elif selection == 2:
                                formatting = "-------------------------------------------------------------------------------------------"
                                mycursor.execute("SELECT * FROM Employees;")
                                myrecords = mycursor.fetchall()
                                df = DataFrame(myrecords)
                                df.columns = ['CustomerId', 'FirstName', 'LastName', 'Email', 'Phone', 'StoreId']
                                newPage()
                                print("                                     EMPLOYEES")
                                print(formatting)
                                print(df)
                                print(formatting)
                                print("\n")
                        # Displays Store Data
                        elif selection == 3:
                                formatting = "-------------------------------------------------------------------------------------"
                                mycursor.execute("SELECT * FROM Stores;")
                                myrecords = mycursor.fetchall()
                                df = DataFrame(myrecords)
                                df.columns = ['StoreId', 'Street', 'City', 'State', 'Zipcode']
                                newPage()
                                print("                                        STORES")
                                print(formatting)
                                print(df)
                                print(formatting)
                                print("\n")
                        # Displays Brands Data
                        elif selection == 4:
                                formatting = "------------------------------"
                                mycursor.execute("SELECT * FROM Brands;")
                                myrecords = mycursor.fetchall()
                                df = DataFrame(myrecords)
                                df.columns = ['BrandId', 'Brand']
                                newPage()
                                print("            BRANDS")
                                print(formatting)
                                print(df)
                                print(formatting)
                                print("\n")
                        # Displays Items Data
                        elif selection == 5:
                                formatting = "----------------------------------------------------"
                                mycursor.execute("SELECT * FROM Items;")
                                myrecords = mycursor.fetchall()
                                df = DataFrame(myrecords)
                                df.columns = ['ItemId', 'Item', 'Price', 'BrandId']
                                newPage()
                                print("                      ITEMS")
                                print(formatting)
                                print(df)
                                print(formatting)
                                print("\n")
                        # Displays Sales Data
                        elif selection == 6:
                                formatting = "------------------------------------------------"
                                mycursor.execute("SELECT * FROM Sales;")
                                myrecords = mycursor.fetchall()
                                df = DataFrame(myrecords)
                                df.columns = ['SaleId', 'CustomerId', 'EmployeeId', 'Date']
                                newPage()
                                print("                    SALES")
                                print(formatting)
                                print(df)
                                print(formatting)
                                print("\n")
                        # Displays SaleItems Data
                        elif selection == 7:
                                formatting = "------------------------------"
                                mycursor.execute("SELECT * FROM SaleItems;")
                                myrecords = mycursor.fetchall()
                                df = DataFrame(myrecords)
                                df.columns = ['SaleId', 'itemId', 'Quantity']
                                newPage()
                                print("         SALE ITEMS")
                                print(formatting)
                                print(df)
                                print(formatting)
                                print("\n")
                        else:
                                newPage()
                                break
        # Deleting Data
        elif choice == 2:
                newPage()
                while True:
                        deleteMenu()
                        while True:
                                try:
                                        selection = int(input("\nSelect which you want to delete: "))
                                except ValueError:
                                        print("This is not a valid value. Try again.")
                                        continue
                                if isinstance(selection, int):
                                        break
                        # Deletes Customer
                        if selection == 1:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the customer you want to delete: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                mycursor.execute("DELETE FROM Customers WHERE CustomerId = (%s)", (id,))
                                newPage()
                                print("Customer deleted.")
                                db.commit()
                        # Deletes Employee
                        elif selection == 2:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the employee you want to delete: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                mycursor.execute("DELETE FROM Employees WHERE EmployeeId = (%s)", (id,))
                                newPage()
                                print("Employee deleted.")
                                db.commit()
                        # Deletes Store
                        elif selection == 3:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the store you want to delete: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                mycursor.execute("DELETE FROM Stores WHERE StoreId = (%s)", (id,))
                                newPage()
                                print("Store deleted.")
                                db.commit()
                        # Deletes Brand
                        elif selection == 4:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the brand you want to delete: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                mycursor.execute("DELETE FROM Brands WHERE BrandId = (%s)", (id,))
                                newPage()
                                print("Brand deleted.")
                                db.commit()
                        # Deletes Item
                        elif selection == 5:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the item you want to delete: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                mycursor.execute("DELETE FROM Items WHERE ItemId = (%s)", (id,))
                                newPage()
                                print("Item deleted.")
                                db.commit()
                        # Deletes Sale
                        elif selection == 6:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the sale you want to delete: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                mycursor.execute("DELETE FROM Sales WHERE SaleId = (%s)", (id,))
                                newPage()
                                print("Sale deleted.")
                                db.commit()
                        else:
                                newPage()
                                break
        # Updating Data
        elif choice == 3:
                newPage()
                while True:
                        updateMenu()
                        while True:
                                try:
                                        selection = int(input("\nSelect which you want to update: "))
                                except ValueError:
                                        print("This is not a valid value. Try again.")
                                        continue
                                if isinstance(selection, int):
                                        break
                        # Updates Customers
                        if selection == 1:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the customer you want to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                attributes = print("(1)First Name (2)Last Name (3)Email (4)Phone (5)Update All")
                                while True:
                                        try:
                                                select = int(input("Which attribute would you like to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(select, int):
                                                break
                                # Updating First name
                                if select == 1:
                                        f_name = input("Enter their first name: ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Customers SET FirstName = (%s) WHERE CustomerId = (%s)",
                                                        (f_name, id))
                                                newPage()
                                                print("Customer first name updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Customer first name Update Failed.")
                                                db.rollback()
                                #Updating last name
                                elif select == 2:
                                        l_name = input("Enter their last name: ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Customers SET LastName = (%s) WHERE CustomerId = (%s)",
                                                        (l_name, id))
                                                newPage()
                                                print("Customer last name updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Customer last name Update Failed.")
                                                db.rollback()
                                # Updating their email
                                elif select == 3:
                                        email = input("Enter their email: ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Customers SET Email = (%s) WHERE CustomerId = (%s)",
                                                        (email, id))
                                                newPage()
                                                print("Customer email updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Customer email Update Failed.")
                                                db.rollback()
                                # Updating their phone number
                                elif select == 4:
                                        while True:
                                                try:
                                                        phone = int(input("Enter their phone number (Only Digits): "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(phone, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Customers SET Phone = (%s) WHERE CustomerId = (%s)",
                                                        (phone, id))
                                                newPage()
                                                print("Customer phone updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Customer phone Update Failed.")
                                                db.rollback()
                                #Updating all their data
                                elif select == 5:
                                        f_name = input("Enter their first name: ")
                                        l_name = input("Enter their last name: ")
                                        email = input("Enter their email: ")
                                        while True:
                                                try:
                                                        phone = int(input("Enter their phone number (Only Digits): "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(phone, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Customers SET FirstName = (%s), LastName = (%s), Email = (%s), Phone = (%s) "
                                                        "WHERE CustomerId = (%s)", (f_name, l_name, email, phone, id))
                                                newPage()
                                                print("Customer updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Customer Update Failed.")
                                                db.rollback()
                                else:
                                        print("Not a valid choice. Returning to update menu. ")
                                        newPage()
                        # Updates Employees
                        elif selection == 2:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the employee you want to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                attributes = print("(1)First Name (2)Last Name (3)Email (4)Phone (5)StoreId (6)Update All")
                                while True:
                                        try:
                                                select = int(input("Which attribute would you like to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(select, int):
                                                break
                                # Update their first name
                                if select == 1:
                                        f_name = input("Enter their first name: ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Employees SET FirstName = (%s) WHERE EmployeeId = (%s)",
                                                        (f_name, id))
                                                newPage()
                                                print("Employee first name updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Employee first name Update Failed.")
                                                db.rollback()
                                # Update their last name
                                elif select == 2:
                                        l_name = input("Enter their last name: ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Employees SET LastName = (%s) WHERE EmployeeId = (%s)",
                                                        (l_name, id))
                                                newPage()
                                                print("Employee last name updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Employee last name Update Failed.")
                                                db.rollback()
                                #Update their email
                                elif select == 3:
                                        email = input("Enter their email: ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Employees SET Email = (%s) WHERE EmployeeId = (%s)",
                                                        (email, id))
                                                newPage()
                                                print("Employee email updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Employee email Update Failed.")
                                                db.rollback()
                                #Update their phone number
                                elif select == 4:
                                        while True:
                                                try:
                                                        phone = int(input("Enter their phone number (Only Digits): "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(phone, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Employees SET Phone = (%s) WHERE EmployeeId = (%s)",
                                                        (phone, id))
                                                newPage()
                                                print("Employee phone updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Employee phone Update Failed.")
                                                db.rollback()
                                #Update the store they work at
                                elif select == 5:
                                        while True:
                                                try:
                                                        store = int(input("Enter the ID of the store they work in: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(store, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Employees SET StoreId = (%s) WHERE EmployeeId = (%s)",
                                                        (store, id))
                                                newPage()
                                                print("Employee store updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Employee store Update Failed.")
                                                db.rollback()
                                # Update all their information
                                elif select == 6:
                                        f_name = input("Enter their first name: ")
                                        l_name = input("Enter their last name: ")
                                        email = input("Enter their email: ")
                                        while True:
                                                try:
                                                        phone = int(input("Enter their phone number (Only Digits): "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(phone, int):
                                                        break
                                        while True:
                                                try:
                                                        store = int(input("Enter the ID of the store they work in: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(store, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Employees SET FirstName = (%s), LastName = (%s), Email = (%s), Phone = (%s), StoreId = (%s) "
                                                        "WHERE EmployeeId = (%s)",
                                                        (f_name, l_name, email, phone, store, id))
                                                newPage()
                                                print("Employee updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Employee Update Failed.")
                                                db.rollback()
                                else:
                                        newPage()
                                        print("Not a valid choice. Returning to update menu.")
                        # Updates Stores
                        elif selection == 3:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the store you want to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                attributes = print("(1)Street (2)City (3)State (4)Zipcode (5)Update All")
                                while True:
                                        try:
                                                select = int(input("Which attribute would you like to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(select, int):
                                                break
                                #Update the store street
                                if select == 1:
                                        street = input("Enter the store street: ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Stores SET Street = (%s) WHERE StoreId = (%s)",
                                                        (street, id))
                                                newPage()
                                                print("Store street updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Store street Update Failed.")
                                                db.rollback()
                                #Update the store city
                                elif select == 2:
                                        city = input("Enter the store city: ")
                                        try:
                                                mycursor.execute("UPDATE Stores SET City = (%s) WHERE StoreId = (%s)",
                                                                 (city, id))
                                                newPage()
                                                print("Store city updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Store city Update Failed.")
                                                db.rollback()
                                #Update the store state
                                elif select == 3:
                                        state = input("Enter the store state: ")
                                        try:
                                                mycursor.execute("UPDATE Stores SET State = (%s) WHERE StoreId = (%s)",
                                                                 (state, id))
                                                newPage()
                                                print("Store state updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Store state Update Failed.")
                                                db.rollback()
                                # Update the store zipcode
                                elif select == 4:
                                        zipcode = input("Enter the store zipcode: ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Stores SET Zipcode = (%s) WHERE StoreId = (%s)",
                                                        (zipcode, id))
                                                newPage()
                                                print("Store zipcode updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Store zipcode Update Failed.")
                                                db.rollback()
                                # Update all store information
                                elif select == 5:
                                        street = input("Enter the store street: ")
                                        city = input("Enter the store city: ")
                                        state = input("Enter the store state: ")
                                        zipcode = input("Enter the store zipcode: ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Stores SET Street = (%s), City = (%s), State = (%s), Zipcode = (%s) WHERE StoreId = (%s)",
                                                        (street, city, state, zipcode, id))
                                                newPage()
                                                print("Store updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Store Update Failed.")
                                                db.rollback()

                                else:
                                        print("Not a valid choice. Returning to update menu.")
                        # Updates Brands
                        elif selection == 4:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the brand you want to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                brand = input("Enter the brand name: ")
                                try:
                                        mycursor.execute("UPDATE Brands SET Brand = (%s) WHERE BrandId = (%s)", (brand, id))
                                        newPage()
                                        print("Brand updated.")
                                        db.commit()
                                except mysql.connector.Error as error:
                                        newPage()
                                        print("Brand name Update Failed.")
                                        db.rollback()
                        # Updates Items
                        elif selection == 5:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the item you want to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                attributes = print("(1)Item (2)Price (3)BrandId (4)Update All")
                                while True:
                                        try:
                                                select = int(input("Which attribute would you like to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(select, int):
                                                break
                                # Update Item Name
                                if select == 1:
                                        item = input("Enter the name of the item: ")
                                        try:
                                                mycursor.execute("UPDATE Items SET Item = (%s) WHERE ItemId = (%s)", (item, id))
                                                newPage()
                                                print("Item name updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Item name Update Failed.")
                                                db.rollback()
                                #Update item price
                                elif select == 2:
                                        while True:
                                                try:
                                                        price = float(input("Enter the price of the item: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(price, float):
                                                        break
                                        try:
                                                mycursor.execute("UPDATE Items SET Price = (%s) WHERE ItemId = (%s)",
                                                                 (price, id))
                                                newPage()
                                                print("Price updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Price Update Failed.")
                                                db.rollback()
                                # Update the item brand
                                elif select == 3:
                                        while True:
                                                try:
                                                        brandid = int(input("Enter the ID of the brand of the item: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(brandid, int):
                                                        break
                                        try:
                                                mycursor.execute("UPDATE Items SET BrandId = (%s) WHERE ItemId = (%s)",
                                                                 (brandid, id))
                                                newPage()
                                                print("Brand updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Brand Update Failed.")
                                                db.rollback()
                                # Update all item information
                                elif select == 4:
                                        item = input("Enter the name of the item: ")
                                        while True:
                                                try:
                                                        price = float(input("Enter the price of the item: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(price, float):
                                                        break
                                        while True:
                                                try:
                                                        brandid = int(input("Enter the ID of the brand of the item: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(brandid, int):
                                                        break
                                        # Using rollback on update statement
                                        try:
                                                mycursor.execute("UPDATE Items SET Item = (%s), Price = (%s), BrandId = (%s) WHERE ItemId = (%s)",
                                                                 (item, price, brandid, id))
                                                newPage()
                                                print("Item updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Item Update Failed.")
                                                db.rollback()
                                else:
                                        print("Not a valid choice. Returning to update menu.")
                        # Updates Sales
                        elif selection == 6:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the sale you want to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                attributes = print("(1)CustomerId (2)EmployeeId (3)Date (4)Update All")
                                while True:
                                        try:
                                                select = int(input("Which attribute would you like to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(select, int):
                                                break
                                # Update the sale customer
                                if select == 1:
                                        while True:
                                                try:
                                                        customer = int(input("Enter the ID of the customer for this sale: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(customer, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Sales SET CustomerId = (%s) WHERE SaleId = (%s)",
                                                        (customer, id))
                                                newPage()
                                                print("Sale customer updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Sale Customer Update Failed.")
                                                db.rollback()
                                # Update the sale employee
                                elif select == 2:
                                        while True:
                                                try:
                                                        employee = int(input("Enter the ID of the employee for this sale: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(employee, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Sales SET EmployeeId = (%s) WHERE SaleId = (%s)",
                                                        (employee, id))
                                                newPage()
                                                print("Sale employee updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Sale Employee Update Failed.")
                                                db.rollback()
                                #Update the sale date
                                elif select == 3:
                                        while True:
                                                date = input(
                                                        "Enter the date of the sale (Year,Month,Day -> xxxx-xx-xx): ")
                                                pattern = "\d{4}\-\d{2}-\d{2}"
                                                isdate = re.match(pattern, date)
                                                if isdate:
                                                        break
                                                else:
                                                        print("This is not a valid date. Try again. ")
                                        try:
                                                mycursor.execute("UPDATE Sales SET Date = (%s) WHERE SaleId = (%s)",
                                                                 (date, id))
                                                newPage()
                                                print("Sale date updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Sale date update Failed.")
                                                db.rollback()
                                # Updating  all sale information
                                elif select == 4:
                                        while True:
                                                try:
                                                        customer = int(input("Enter the ID of the customer for this sale: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(customer, int):
                                                        break
                                        while True:
                                                try:
                                                        employee = int(input("Enter the ID of the employee for this sale: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(employee, int):
                                                        break
                                        while True:
                                                date = input(
                                                        "Enter the date of the sale (Year,Month,Day -> xxxx-xx-xx): ")
                                                pattern = "\d{4}\-\d{2}-\d{2}"
                                                isdate = re.match(pattern, date)
                                                if isdate:
                                                        break
                                                else:
                                                        print("This is not a valid date. Try again. ")
                                        try:
                                                mycursor.execute(
                                                        "UPDATE Sales SET CustomerId = (%s), EmployeeId = (%s), Date = (%s) WHERE SaleId = (%s)",
                                                        (customer, employee, date, id))
                                                newPage()
                                                print("Sale customer updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Sale Update Failed.")
                                                db.rollback()
                                else:
                                        newPage()
                                        print("Not a valid choice. Returning to update menu.")
                        # Update SaleItems
                        elif selection == 7:
                                while True:
                                        try:
                                                id = int(input("Enter the ID of the sale you want to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(id, int):
                                                break
                                attributes = print("(1)Item (2)Quantity (3)Update All")
                                while True:
                                        try:
                                                select = int(input("Which attribute would you like to update: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(select, int):
                                                break
                                #Update sale item
                                if select == 1:
                                        while True:
                                                try:
                                                        item = int(input("Enter the ID of the item for this sale: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(item, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE SaleItems SET ItemId = (%s) WHERE SaleId = (%s)",
                                                        (item, id))
                                                newPage()
                                                print("Sale item updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Sale item Update Failed.")
                                                db.rollback()
                                #Update sale item quantity
                                elif select == 2:
                                        while True:
                                                try:
                                                        quantity = int(input("Enter the quantity of the item for this sale: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(quantity, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE SaleItems SET Quantity = (%s) WHERE SaleId = (%s)",
                                                        (quantity, id))
                                                newPage()
                                                print("Sale quantity updated.")
                                                db.commit()
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Sale quantity Update Failed.")
                                                db.rollback()
                                #Update all sale item information
                                elif select == 3:
                                        while True:
                                                try:
                                                        item = int(input("Enter the ID of the item for this sale: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(item, int):
                                                        break
                                        while True:
                                                try:
                                                        quantity = int(
                                                                input("Enter the quantity of the item for this sale: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(quantity, int):
                                                        break
                                        try:
                                                mycursor.execute(
                                                        "UPDATE SaleItems SET ItemId = (%s), Quantity = (%s) WHERE SaleId = (%s)",
                                                        (item, quantity, id))
                                                db.commit()

                                                newPage()
                                                print("Sale updated.")
                                        except mysql.connector.Error as error:
                                                newPage()
                                                print("Sale Update Failed.")
                                                db.rollback()

                                else:
                                        newPage()
                                        print("Not a valid choice. Returning to update menu.")
                        else:
                                newPage()
                                break

        # Inserting/Creating Data
        elif choice == 4:
                newPage()
                while True:
                        insertMenu()
                        while True:
                                try:
                                        selection = int(input("\nSelect which you want to create: "))
                                except ValueError:
                                        print("This is not a valid value. Try again.")
                                        continue
                                if isinstance(selection, int):
                                        break
                        # Inserts new customer
                        if selection == 1:
                                f_name = input("Enter their first name: ")
                                l_name = input("Enter their last name: ")
                                email = input("Enter their email: ")
                                while True:
                                        try:
                                                phone = int(input("Enter their phone number (Only Digits): "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(phone, int):
                                                break
                                try:
                                        mycursor.execute(
                                                "INSERT INTO Customers(FirstName, LastName, Email, Phone)"
                                                "VALUES(%s,%s,%s,%s)", (f_name, l_name, email, phone))
                                        newPage()
                                        print("Customer created.")
                                        db.commit()
                                except mysql.connector.Error as error:
                                        newPage()
                                        print("Customer creation Failed.")
                                        db.rollback()
                        # Inserts new employee
                        elif selection == 2:
                                f_name = input("Enter their first name: ")
                                l_name = input("Enter their last name: ")
                                email = input("Enter their email: ")
                                while True:
                                        try:
                                                phone = int(input("Enter their phone number (Only Digits): "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(phone, int):
                                                break
                                while True:
                                        try:
                                                storeid = int(input("Enter the ID of the store they work in: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(storeid, int):
                                                break
                                try:
                                        mycursor.execute(
                                                "INSERT INTO Employees(FirstName, LastName, Email, Phone, StoreId)"
                                                "VALUES(%s,%s,%s,%s,%s)", (f_name, l_name, email, phone, storeid))
                                        newPage()
                                        print("Employee created.")
                                        db.commit()
                                except mysql.connector.Error as error:
                                        newPage()
                                        print("Employee creation Failed.")
                                        db.rollback()
                        # Inserts new store
                        elif selection == 3:
                                street = input("Enter the store street: ")
                                city = input("Enter the store city: ")
                                state = input("Enter the store state: ")
                                zipcode = input("Enter the store zipcode: ")
                                try:
                                        mycursor.execute(
                                                "INSERT INTO Stores(Street, City, State, Zipcode)"
                                                "VALUES(%s,%s,%s,%s)", (street, city, state, zipcode))
                                        newPage()
                                        print("Store created.")
                                        db.commit()
                                except mysql.connector.Error as error:
                                        newPage()
                                        print("Store creation Failed.")
                                        db.rollback()
                        # Inserts new brand
                        elif selection == 4:
                                brand = input("Enter the brand name: ")
                                try:
                                        mycursor.execute(
                                                "INSERT INTO Brands(Brand) VALUES(%s)", (brand,))
                                        newPage()
                                        print("Brand created.")
                                        db.commit()
                                except mysql.connector.Error as error:
                                        newPage()
                                        print("Brand creation Failed.")
                                        db.rollback()
                        # Inserts new Item
                        elif selection == 5:
                                item = input("Enter the name of the item: ")
                                while True:
                                        try:
                                                price = float(input("Enter the price of the item: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(price, float):
                                                break
                                while True:
                                        try:
                                                brandid = int(input("Enter the ID of the brand of the item: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(brandid, int):
                                                break
                                try:
                                        mycursor.execute(
                                                "INSERT INTO Items(Item, Price, BrandId)"
                                                "VALUES(%s,%s,%s)", (item, price, brandid))
                                        newPage()
                                        print("Item created.")
                                        db.commit()
                                except mysql.connector.Error as error:
                                        newPage()
                                        print("Item creation Failed.")
                                        db.rollback()
                        # Inserts new sale
                        elif selection == 6:
                                # stops the coninuation of making sale items data if a rollback occurs
                                stop = 0
                                while True:
                                        try:
                                                customer = int(input("Enter the ID of the customer for this sale: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(customer, int):
                                                break
                                while True:
                                        try:
                                                employee = int(input("Enter the ID of the employee for this sale: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(employee, int):
                                                break
                                while True:
                                        date = input("Enter the date of the sale (Year,Month,Day -> xxxx-xx-xx): ")
                                        pattern = "\d{4}\-\d{2}-\d{2}"
                                        isdate = re.match(pattern, date)
                                        if isdate:
                                                break
                                        else:
                                                print("This is not a valid date. Try again. ")
                                try:
                                        mycursor.execute(
                                                "INSERT INTO Sales(CustomerId, EmployeeId, Date)"
                                                "VALUES(%s,%s,%s)", (customer, employee, date))
                                        db.commit()
                                        sale_Id = mycursor.lastrowid
                                except mysql.connector.Error as error:
                                        newPage()
                                        print("Sale creation Failed.")
                                        db.rollback()
                                        stop += 1
                                # restarting the loop
                                if stop > 0:
                                        continue
                                # Have to add sales Item record
                                while True:
                                        try:
                                                item = int(input("Enter the ID of the sale item: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(item, int):
                                                break
                                while True:
                                        try:
                                                quantity = int(input("Enter the quantity of the sale item: "))
                                        except ValueError:
                                                print("This is not a valid value. Try again.")
                                                continue
                                        if isinstance(quantity, int):
                                                break
                                try:
                                        mycursor.execute(
                                                "INSERT INTO SaleItems(SaleId, ItemId, Quantity)"
                                                "VALUES(%s, %s,%s)", (sale_Id, item, quantity))
                                        newPage()
                                        print("Sale and Sale Items created.")
                                        db.commit()
                                except mysql.connector.Error as error:
                                        newPage()
                                        print("Sale and Sale Items creation Failed.")
                                        db.rollback()
                                        # deleting last sale committed to make sure all sales have sale item data
                                        mycursor.execute("DELETE FROM Sales WHERE SaleId = (%s)", (sale_Id,))
                                        db.commit()
                        else:
                                newPage()
                                break
        # Querying the data
        elif choice == 5:
                while True:
                        newPage()
                        queryMenu()
                        while True:
                                try:
                                        selection = int(input("\nSelect the report section: "))
                                except ValueError:
                                        print("This is not a valid value. Try again.")
                                        continue
                                if isinstance(selection, int):
                                        break
                        newPage()
                        # Company Reports
                        if selection == 1:
                                while True:
                                        companyMenu()
                                        while True:
                                                try:
                                                        choose = int(input("\nSelect the company report you want to see: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(choose, int):
                                                        break
                                        # Total Company Revenue
                                        if choose == 1:
                                                print("\n")
                                                formatting = "-----------------"
                                                mycursor.execute("Select ROUND(SUM(Price * Quantity),2) as TotalRevenue "
                                                                 "FROM Stores "
                                                                 "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                                 "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                                 "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                                 "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Total Revenue']
                                                newPage()
                                                print(" TOTAL REVENUE")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # Top State Revenues
                                        elif choose == 2:
                                                print("\n")
                                                formatting = "-------------------------"
                                                mycursor.execute("Select State, ROUND(SUM(Price * Quantity),2) as Revenue FROM Stores "
                                                                 "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId"
                                                                 " INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                                 "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                                 "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                                 "GROUP BY State "
                                                                 "ORDER BY SUM(Price * Quantity) DESC "
                                                                 " LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['State', 'Revenue']
                                                newPage()
                                                print("    TOP STATE REVENUE")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # Total company employees
                                        elif choose == 3:
                                                print("\n")
                                                formatting = "-----------------"
                                                mycursor.execute("SELECT COUNT(*) as TotalEmployees FROM Employees;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Total Employees']
                                                newPage()
                                                print(" TOTAL EMPLOYEES")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # Total company stores
                                        elif choose == 4:
                                                print("\n")
                                                formatting = "-----------------"
                                                mycursor.execute("SELECT COUNT(*) as TotalStores FROM Stores;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Total Stores']
                                                newPage()
                                                print(" TOTAL STORES")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        else:
                                                newPage()
                                                break
                        # Store Reports
                        elif selection == 2:
                                while True:
                                        storeMenu()
                                        while True:
                                                try:
                                                        choose = int(input("\nSelect the store report you want to see: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(choose, int):
                                                        break
                                        # Top 5 Performing Stores
                                        if choose == 1:
                                                print("\n")
                                                formatting = "---------------------"
                                                mycursor.execute("Select StoreId, ROUND(SUM(Price * Quantity),2) as Revenue "
                                                                 "FROM vAllStores "
                                                                 "GROUP BY StoreId "
                                                                 "ORDER BY SUM(Price * Quantity) DESC "
                                                                 "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Store ID', 'Revenue']
                                                newPage()
                                                print(" TOP 5 STORES")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # Worst Performing 5 Stores
                                        elif choose == 2:
                                                print("\n")
                                                formatting = "---------------------"
                                                mycursor.execute(
                                                        "Select StoreId, ROUND(SUM(Price * Quantity),2) as Revenue "
                                                        "FROM vAllStores "
                                                        "GROUP BY StoreId "
                                                        "ORDER BY SUM(Price * Quantity) ASC "
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Store ID', 'Revenue']
                                                newPage()
                                                print("WORST 5 STORES")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        else:
                                                newPage()
                                                break
                        # Employee Reports
                        elif selection == 3:
                                counter = 0
                                while True:
                                        employeeMenu()
                                        while True:
                                                try:
                                                        choose = int(input("\nSelect the employee report you want to see: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(choose, int):
                                                        break
                                        # Top 5 Employees
                                        if choose == 1:
                                                print("\n")
                                                formatting = "---------------------------------------------------------------------------------------------"
                                                mycursor.execute("Select Employees.EmployeeId, Employees.FirstName as FirstName, Employees.LastName as LastName, Employees.Email, Employees.Phone, SUM(Price * Quantity) as Sales_Revenue "
                                                                 "FROM Stores "
                                                                 "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                                 "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                                 "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                                 "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                                 "GROUP BY Employees.EmployeeId "
                                                                 "ORDER BY SUM(Price * Quantity) DESC "
                                                                 "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Employee ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Sales Revenue']
                                                newPage()
                                                print("                           5 HIGHEST PERFORMING EMPLOYEES")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # Worst 5 Employees
                                        elif choose == 2:
                                                print("\n")
                                                formatting = "------------------------------------------------------------------------------------------"
                                                mycursor.execute(
                                                        "Select Employees.EmployeeId, Employees.FirstName as FirstName, Employees.LastName as LastName, Employees.Email, Employees.Phone, SUM(Price * Quantity) as Sales_Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "GROUP BY Employees.EmployeeId "
                                                        "ORDER BY SUM(Price * Quantity)"
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Employee ID', 'First Name', 'Last Name', 'Email', 'Phone', 'Sales Revenue']
                                                newPage()
                                                print("                            5 LOWEST PERFORMING EMPLOYEES")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # Best Employees by State
                                        elif choose == 3:
                                                state = input("Please enter the state name of the employee: ")
                                                print("\n")
                                                formatting = "----------------------------------------------------------------------------------------------------"
                                                mycursor.execute(
                                                        "SELECT Employees.EmployeeId, Employees.FirstName as FirstName, Employees.LastName as LastName, Employees.Email, Employees.Phone, State, SUM(Price * Quantity) as Sales_Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "WHERE State = (%s) "
                                                        "GROUP BY Employees.EmployeeId "
                                                        "ORDER BY SUM(Price * Quantity) DESC "
                                                        "LIMIT 5;", (state,))
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Employee ID', 'First Name', 'Last Name', 'Email', 'Phone', 'State', 'Sales Revenue']
                                                newPage()
                                                print("                                   TOP EMPLOYEES IN " + state.upper())
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # Employees with sales above a cutoff
                                        elif choose == 4:
                                                cutoff = float(input("Enter Sales Cutoff: "))
                                                print("\n")
                                                formatting = "------------------------------------------------------------------------------------------------------------"
                                                mycursor.execute(
                                                        "Select Employees.EmployeeId, Employees.FirstName as FirstName, Employees.LastName as LastName, Employees.Email, Employees.Phone, State, SUM(Price * Quantity) as Sales_Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "WHERE Employees.EmployeeId IN ( "
                                                        "       SELECT Employees.EmployeeId "
                                                        "       FROM Stores "
                                                        "       INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "       INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "       INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "       INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "       GROUP BY Employees.EmployeeId "
                                                        "       HAVING SUM(Price * Quantity) > (%s) "
                                                        "       ORDER BY SUM(Price * Quantity) DESC"
                                                        ") "
                                                        "GROUP BY Employees.EmployeeId "
                                                        "ORDER BY SUM(Price * Quantity) DESC;", (cutoff,))
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Employee ID', 'First Name', 'Last Name', 'Email', 'Phone', 'State', 'Sales Revenue']
                                                newPage()
                                                print("                                   EMPLOYEES WITH SALES ABOVE $" + str(cutoff))
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # Employees with sales above a cutoff
                                        elif choose == 5:
                                                cutoff = float(input("Enter Sales Cutoff: "))
                                                print("\n")
                                                formatting = "------------------------------------------------------------------------------------------------------------"
                                                mycursor.execute(
                                                        "Select Employees.EmployeeId, Employees.FirstName as FirstName, Employees.LastName as LastName, Employees.Email, Employees.Phone, State, SUM(Price * Quantity) as Sales_Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "WHERE Employees.EmployeeId IN ( "
                                                        "       SELECT Employees.EmployeeId "
                                                        "       FROM Stores "
                                                        "       INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "       INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "       INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "       INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "       GROUP BY Employees.EmployeeId "
                                                        "       HAVING SUM(Price * Quantity) < (%s) "
                                                        "       ORDER BY SUM(Price * Quantity) DESC"
                                                        ") "
                                                        "GROUP BY Employees.EmployeeId "
                                                        "ORDER BY SUM(Price * Quantity);", (cutoff,))
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Employee ID', 'First Name', 'Last Name', 'Email', 'Phone', 'State', 'Sales Revenue']
                                                newPage()
                                                print("                                   EMPLOYEES WITH SALES BELOW $" + str(cutoff))
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # Employee Sales by Store choice
                                        elif choose == 6:
                                                store = int(input("Please enter the ID of the store: "))
                                                print("\n")
                                                formatting = "---------------------------------------------------------------------------------------------------------"
                                                mycursor.execute(
                                                        "SELECT Employees.EmployeeId, Employees.FirstName as FirstName, Employees.LastName as LastName, Employees.Email, Employees.Phone, State, SUM(Price * Quantity) as Sales_Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "WHERE Stores.StoreId = (%s) "
                                                        "GROUP BY Employees.EmployeeId "
                                                        "ORDER BY SUM(Price * Quantity) DESC;", (store,))
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Employee ID', 'First Name', 'Last Name', 'Email', 'Phone', 'State', 'Sales Revenue']
                                                newPage()
                                                print("                                             EMPLOYEES STORE " + str(store))
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        elif choose == 7:
                                                employee = int(input("Please enter the ID of the employee: "))
                                                print("\n")
                                                formatting = "----------------------------------------------------------------------------------------------------------"
                                                mycursor.execute(
                                                        "SELECT Employees.StoreId, Employees.EmployeeId, Employees.FirstName as FirstName, Employees.LastName as LastName, "
                                                        "Employees.Email, Employees.Phone, State, SUM(Price * Quantity) as Sales_Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "WHERE Employees.EmployeeId = (%s);", (employee,))
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Store ID', 'Employee ID', 'First Name', 'Last Name', 'Email', 'Phone', 'State', 'Sales Revenue']
                                                newPage()
                                                print("                                             EMPLOYEES STORE " + str(employee))
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        else:
                                                newPage()
                                                break
                        # Customer Reports
                        elif selection == 4:
                                while True:
                                        customerMenu()
                                        while True:
                                                try:
                                                        choose = int(input("\nSelect the customer report you want to see: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(choose, int):
                                                        break
                                        # 5 Best Customers
                                        if choose == 1:
                                                print("\n")
                                                formatting = "-------------------------------------------------------------------------------------"
                                                mycursor.execute(
                                                        "Select Customers.CustomerId, Customers.FirstName as FirstName, Customers.LastName as LastName, Customers.Email, Customers.Phone, SUM(Price * Quantity) as Amount_Spent "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN Customers ON Sales.CustomerId = Customers.CustomerId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "GROUP BY Customers.CustomerId "
                                                        "ORDER BY SUM(Price * Quantity) DESC "
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Customer ID', 'First Name', 'Last Name', 'Email',
                                                              'Phone', 'Total Spent']
                                                newPage()
                                                print("                                 TOP 5 CUSTOMERS")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        else:
                                                newPage()
                                                break
                        # Brand Reports
                        elif selection == 5:
                                while True:
                                        brandMenu()
                                        while True:
                                                try:
                                                        choose = int(input("\nSelect the brand report you want to see: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(choose, int):
                                                        break
                                        # 5 Most Popular Brands
                                        if choose == 1:
                                                print("\n")
                                                formatting = "---------------------------------------"
                                                mycursor.execute(
                                                        "Select Brand, COUNT(*) as Brand_Orders "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "INNER JOIN Brands ON Items.BrandId = Brands.BrandId "
                                                        "GROUP BY Brand "
                                                        "ORDER BY COUNT(*) DESC "
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Brand', 'Total Brand Sales']
                                                newPage()
                                                print("         5 MOST POPULAR BRANDS")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # 5 Least Popular Brands
                                        elif choose == 2:
                                                print("\n")
                                                formatting = "---------------------------------"
                                                mycursor.execute(
                                                        "Select Brand, COUNT(*) as Brand_Orders "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "INNER JOIN Brands ON Items.BrandId = Brands.BrandId "
                                                        "GROUP BY Brand "
                                                        "ORDER BY COUNT(*)"
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Brand', 'Total Brand Sales']
                                                newPage()
                                                print("      5 LEAST POPULAR BRANDS")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # 5 Best Revenue Brands
                                        elif choose == 3:
                                                print("\n")
                                                formatting = "-----------------------------------"
                                                mycursor.execute(
                                                        "Select Brand, ROUND(SUM(Price * Quantity),2) as Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "INNER JOIN Brands ON Items.BrandId = Brands.BrandId "
                                                        "GROUP BY Brand "
                                                        "ORDER BY SUM(Price * Quantity) DESC "
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Brand', 'Revenue Generated']
                                                newPage()
                                                print("    5 HIGHEST REVENUE BRANDS")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # 5 Worste Revenue Brands
                                        elif choose == 4:
                                                print("\n")
                                                formatting = "-----------------------------------"
                                                mycursor.execute(
                                                        "Select Brand, ROUND(SUM(Price * Quantity),2) as Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "INNER JOIN Brands ON Items.BrandId = Brands.BrandId "
                                                        "GROUP BY Brand "
                                                        "ORDER BY SUM(Price * Quantity) "
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Brand', 'Revenue Generated']
                                                newPage()
                                                print("       5 LOWEST REVENUE BRANDS")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        else:
                                                newPage()
                                                break
                        # Item Reports
                        elif selection == 6:
                                while True:
                                        itemMenu()
                                        while True:
                                                try:
                                                        choose = int(input("\nSelect the item report you want to see: "))
                                                except ValueError:
                                                        print("This is not a valid value. Try again.")
                                                        continue
                                                if isinstance(choose, int):
                                                        break
                                        # 5 Most Popular Items
                                        if choose == 1:
                                                print("\n")
                                                formatting = "-------------------------------------------------------------"
                                                mycursor.execute(
                                                        "Select Items.ItemId, Item, Brand, COUNT(*) as Item_Orders "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "INNER JOIN Brands ON Items.BrandId = Brands.BrandId "
                                                        "GROUP BY Items.ItemId "
                                                        "ORDER BY COUNT(*) DESC "
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Item ID', 'Item', 'Brand', 'Total Item Sales']
                                                newPage()
                                                print("                 5 MOST POPULAR ITEMS")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # 5 Least Popular Items
                                        elif choose == 2:
                                                print("\n")
                                                formatting = "-------------------------------------------------------------"
                                                mycursor.execute(
                                                        "Select Items.ItemId, Item, Brand, COUNT(*) as Item_Orders "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "INNER JOIN Brands ON Items.BrandId = Brands.BrandId "
                                                        "GROUP BY Items.ItemId "
                                                        "ORDER BY COUNT(*)"
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Item ID', 'Item', 'Brand', 'Total Item Sales']
                                                newPage()
                                                print("                 5 LEAST POPULAR ITEMS")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # 5 Best Revenue Items
                                        elif choose == 3:
                                                print("\n")
                                                formatting = "----------------------------------------------------------------"
                                                mycursor.execute(
                                                        "Select Items.ItemId, Item, Brand, ROUND(SUM(Price * Quantity),2) as Item_Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "INNER JOIN Brands ON Items.BrandId = Brands.BrandId "
                                                        "GROUP BY Items.ItemId "
                                                        "ORDER BY SUM(Price * Quantity) DESC "
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Item ID', 'Item', 'Brand', 'Revenue Generated']
                                                newPage()
                                                print("                     5 BEST REVENUE ITEMS")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        # 5 Worst revenue Items
                                        elif choose == 4:
                                                print("\n")
                                                formatting = "----------------------------------------------------------------"
                                                mycursor.execute(
                                                        "Select Items.ItemId, Item, Brand, ROUND(SUM(Price * Quantity),2) as Item_Revenue "
                                                        "FROM Stores "
                                                        "INNER JOIN Employees ON Stores.StoreId = Employees.StoreId "
                                                        "INNER JOIN Sales ON Employees. EmployeeId = Sales.EmployeeId "
                                                        "INNER JOIN SaleItems ON Sales.SaleId = SaleItems.SaleId "
                                                        "INNER JOIN Items ON SaleItems.ItemId = Items.ItemId "
                                                        "INNER JOIN Brands ON Items.BrandId = Brands.BrandId "
                                                        "GROUP BY Items.ItemId "
                                                        "ORDER BY SUM(Price * Quantity)"
                                                        "LIMIT 5;")
                                                myrecords = mycursor.fetchall()
                                                df = DataFrame(myrecords)
                                                df.columns = ['Item ID', 'Item', 'Brand', 'Revenue Generated']
                                                newPage()
                                                print("                     5 WORST REVENUE ITEMS")
                                                print(formatting)
                                                print(df)
                                                print(formatting)
                                                exportCSV(df)
                                                print("\n")
                                        else:
                                                newPage()
                                                break

                        else:
                                newPage()
                                break
        # Exit Message
        else:
                newPage()
                out = pyfiglet.figlet_format("T I L L Y ' S    D B\n    C L O S E D .", font="slant")
                print(out)
                break

