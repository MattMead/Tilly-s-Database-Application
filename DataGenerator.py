import mysql.connector
from faker import Faker
import csv
import random
from random import randint
db = mysql.connector.connect(
        host='34.94.182.22',
        user='pascualmead@chapman.edu',
        passwd='FooBar!@#$',
        database='pascualmead_db',
    )

#Function to read data from text files and store them in a list
def ReadFile(file_name):
    file_reader = open(file_name + ".txt", "r")
    data = []
    for line in file_reader:
        fileLine = line.strip()
        data.append(fileLine)
    return data
# List of All brands
brand_list = ReadFile("Brands")
num_brands = len(brand_list)
# total of 265 brands


# List of Items shuffled
mens_items = ReadFile("MensItems")
womens_items = ReadFile("WomensItems")
items = mens_items + womens_items
random.shuffle(items)


# Generating Customer data
def genCustomer(fileName, rows):
    fake = Faker()
    csv_file = open(fileName, "w")
    writer = csv.writer(csv_file)
    writer.writerow(['FirstName', 'LastName', 'Email', 'Phone'])
    for x in range(0, rows):
        phone_number = randint(1000000000, 9999999999)
        first = fake.first_name()
        last = fake.last_name()
        writer.writerow([first, last, first.lower() + "." + last.lower() + "@gmail.com", str(phone_number)])


# Importing Customer data
def importCustomer(fileName):
    mycursor = db.cursor()
    print("Please Wait...")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Inserting data into 'Customers' table
            mycursor.execute("INSERT INTO Customers(FirstName, LastName, Email, Phone)"
                             "VALUES (%s,%s,%s,%s);",
                             (row['FirstName'], row['LastName'], row['Email'], row['Phone']))
            db.commit()



# Generating Store Data
def genStores(fileName, rows):
    fake = Faker()
    csv_file = open(fileName, "w")
    writer = csv.writer(csv_file)
    writer.writerow(['Street', 'City', 'State', 'Zipcode'])
    for x in range(0, rows):
        writer.writerow([fake.street_address(), fake.city(), fake.state(), fake.zipcode()])

# Importing Store Data
def importStores(fileName):
    mycursor = db.cursor()
    print("Please Wait...")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Inserting data into 'Stores' table
            mycursor.execute("INSERT INTO Stores(Street, City, State, Zipcode)"
                             "VALUES (%s,%s,%s,%s);",
                             (row['Street'], row['City'], row['State'], row['Zipcode']))
            db.commit()

# Generating Employee Data
def genEmployees(fileName, rows, num_stores):
    fake = Faker()
    csv_file = open(fileName, "w")
    writer = csv.writer(csv_file)
    writer.writerow(['FirstName', 'LastName', 'Email', 'Phone', 'StoreId'])

    # generating list of all store IDs
    store_list = []
    for store in range(1, num_stores + 1):
        store_list.append(store)
    random.shuffle(store_list)

    #Generating the data
    for x in range(0, rows):
        if x < num_stores:
            if len(store_list) > 2:
                rand_num = randint(1, len(store_list) - 1)
                phone_number = randint(1000000000, 9999999999)
                first = fake.first_name()
                last = fake.last_name()
                writer.writerow([first, last, first.lower() + "." + last.lower() + "@tillys.com", str(phone_number), store_list[rand_num]])
                store_list.pop(rand_num)
            else:
                phone_number = randint(1000000000, 9999999999)
                first = fake.first_name()
                last = fake.last_name()
                writer.writerow([first, last, first.lower() + "." + last.lower() + "@tillys.com", str(phone_number),
                                 store_list[0]])
                store_list.pop(0)
        else:
            phone_number = randint(1000000000, 9999999999)
            first = fake.first_name()
            last = fake.last_name()
            writer.writerow([first, last, first.lower() + "." + last.lower() + "@tillys.com", str(phone_number),
                             randint(1, num_stores)])


# Importing Employee Data
def importEmployees(fileName):
    mycursor = db.cursor()
    print("Please Wait...")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Inserting data into 'Employees' table
            mycursor.execute("INSERT INTO Employees(FirstName, LastName, Email, Phone, StoreId)"
                             "VALUES (%s,%s,%s,%s,%s);",
                             (row['FirstName'], row['LastName'], row['Email'], row['Phone'], row['StoreId']))
            db.commit()

#Generate Brand Data
def genBrands(fileName,data):
    csv_file = open(fileName, "w")
    writer = csv.writer(csv_file)
    writer.writerow(['Brand'])
    for item in data:
        writer.writerow([item])

# Importing Brands Data
def importBrands(fileName):
    mycursor = db.cursor()
    print("Please Wait...")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Inserting data into 'Brands' table
            mycursor.execute("INSERT INTO Brands(Brand) VALUES (%s);", (row['Brand'],))
            db.commit()

#Generates a randomized list
def randomList(list,num_items):
    new_list = []
    for i in range(num_items):
        x = randint(0, len(list)-1)
        new_list.append(list[x])
    return new_list

#Generate Items Data
def genItems(fileName,item_list,num_brands):
    csv_file = open(fileName, "w")
    writer = csv.writer(csv_file)
    writer.writerow(['Item', 'Price', 'BrandId'])
    # generating brand list
    brand_list = []
    for brand in range(1, num_brands + 1):
        brand_list.append(brand)
    random.shuffle(brand_list)

    # Generating the items
    for x in range(0, len(item_list)):
        if x < num_brands:
            if len(brand_list) > 2:
                rand_num = randint(1, len(brand_list)-1)
                writer.writerow([item_list[x], round(random.uniform(0.01, 125.00), 2), brand_list[rand_num]])
                brand_list.pop(rand_num)
            else:
                writer.writerow([item_list[x], round(random.uniform(0.01, 125.00), 2), brand_list[0]])
                brand_list.pop(0)
        else:
            writer.writerow([item_list[x], round(random.uniform(0.01, 125.00), 2), randint(1,num_brands)])

# Importing Items Data
def importItems(fileName):
    mycursor = db.cursor()
    print("Please Wait...")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Inserting data into 'Items' table
            mycursor.execute("INSERT INTO Items(Item,Price,BrandId) VALUES (%s,%s,%s);",
                             (row['Item'], row['Price'], row['BrandId']))
            db.commit()


# Generating sale Data
def genSales(fileName, num_sales, num_customers, num_employees):
    fake = Faker()
    csv_file = open(fileName, "w")
    writer = csv.writer(csv_file)
    writer.writerow(['CustomerId', 'EmployeeId', 'Date'])

    # generating list of all customer IDs to ensure every customer has a sale
    customer_list = []
    for customer in range(1, num_customers + 1):
        customer_list.append(customer)
    random.shuffle(customer_list)

    # generating list of all employee IDs to ensure every employee has a sale
    employee_list = []
    for employee in range(1, num_employees + 1):
        employee_list.append(employee)
    random.shuffle(employee_list)

    for x in range(0, num_sales):
        # making sure all customers have a sale first
        if x < num_customers:
            if len(customer_list) > 2:
                if len(employee_list) == 0:
                    rand_num = randint(1, len(customer_list) - 1)
                    writer.writerow([customer_list[rand_num], randint(1, num_employees), fake.date()])
                    customer_list.pop(rand_num)
                elif len(employee_list) >= 1:
                    rand_num = randint(1, len(customer_list) - 1)
                    rand_emp = randint(0, len(employee_list) - 1)
                    writer.writerow([customer_list[rand_num], employee_list[rand_emp], fake.date()])
                    customer_list.pop(rand_num)
                    employee_list.pop(rand_emp)
            else:
                writer.writerow([customer_list[0], randint(1, num_employees), fake.date()])
                customer_list.pop(0)


        # after all customers have a sale we can now repeat customers as if they had multiple sales
        else:
            writer.writerow([randint(1, num_customers), randint(1, num_employees), fake.date()])


# Importing Sale Data
def importSales(fileName):
    mycursor = db.cursor()
    print("Please Wait...")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Inserting data into 'Sales' table
            mycursor.execute("INSERT INTO Sales(CustomerId, EmployeeId, Date)"
                             "VALUES (%s,%s,%s);",
                             (row['CustomerId'], row['EmployeeId'], row['Date']))
            db.commit()


# Generating SaleItems data
def genSaleItems(fileName, num_sales, num_items):
    fake = Faker()
    csv_file = open(fileName, "w")
    writer = csv.writer(csv_file)
    writer.writerow(['SaleId', 'ItemId', 'Quantity'])

    # Item list
    item_list = []
    for item in range(1, num_items + 1):
        item_list.append(item)
    random.shuffle(item_list)

    #total number of sales that we need to go through
    for x in range(1, num_sales + 1):
        if len(item_list) >= 1:
            rand_num = randint(0, len(item_list) - 1)
            writer.writerow([x, item_list[rand_num], randint(1, 5)])
            item_list.pop(rand_num)
        else:
            writer.writerow([x, randint(1, num_items), randint(1, 5)])

# Importing SaleItem Data
def importSaleItems(fileName):
    mycursor = db.cursor()
    print("Please Wait...")
    with open(fileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Inserting data into 'SaleItems' table
            mycursor.execute("INSERT INTO SaleItems(SaleId, ItemId, Quantity)"
                             "VALUES (%s,%s,%s);",
                             (row['SaleId'], row['ItemId'], row['Quantity']))
            db.commit()


# User Interface
choice = int(input("Would you like to generate data or import an existing data file? "
                   "(1)Generate Data (2)Exit: "))

# Generate and import data
if choice == 1:
    # Generating Customer table Data
    file = "./Customer.csv"
    print("Generating and importing Customer data.")
    num_customers = 500
    genCustomer(file, num_customers)
    importCustomer(file)

    # Generating Stores table Data
    file = "./Stores.csv"
    store_rows = 10
    print("Generating and importing stores data.")
    genStores(file, store_rows)
    importStores(file)

    # Generating Employee table Data
    file = "./Employees.csv"
    print("Generating and importing employee data.")
    num_employees = 30
    genEmployees(file, num_employees, store_rows)
    importEmployees(file)

    # Generating Brands table Data
    file = "Brands.csv"
    print("Generating and importing brand data.")
    genBrands(file, brand_list)
    importBrands(file)

    # Generating Items table Data
    file = "Items.csv"
    # must be more than 265
    num_items = 266
    print("Generating and importing item data.")
    random_item_list = randomList(items, num_items)
    random.shuffle(random_item_list)
    genItems(file, random_item_list, 265)
    importItems(file)

    # Generating sales table data
    file = "Sales.csv"
    print("Generating and importing sales data.")
    num_sales = 700
    genSales(file, num_sales, num_customers, num_employees)
    importSales(file)

    # Generating SaleItems table data
    file = "SaleItems.csv"
    print("Generating and importing sale items data.")
    genSaleItems(file, num_sales, num_items)
    importSaleItems(file)

    print("Data import complete.")


else:
    print("Exiting Program.")





