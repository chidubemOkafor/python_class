# This code is a bit redundant; there is a lot of repetitiveness that could have been avoided. Feel free to optimize it.
# No SQL injection protection. I just hardcoded the values into the query. could be done by separating the values from the query.
# Could have used return but i used print instead. you can use return if you want.

import mysql.connector as sql
import os


class DB:
    def __init__(self):
        self._db = sql.connect(
            host="localhost",
            user="root",
            password="",
            database="syudentmanagementsystem"
        )
        self.commit = self.db.commit()
        self.cursor = self._db.cursor()


class Products:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def add_product(self):
        DB().cursor.execute(f"INSERT INTO products(productname,category,price,stockQuantity) VALUES(%s,%s,%s,%s)",
                            (self.name, self.category, self.price, self.quantity))
        DB().commit

    def remove_product(self, name):
        DB().cursor.execute(f"DELETE FROM products WHERE productname = %s", (name))
        DB().commit

    def update_product(self, productID):
        self.cursor = DB().cursor
        self.commit = DB().commit

        # check if id is in database
        # sql injection prone
        self.cursor.execute(
            f"SELECT id FROM products WHERE id = '{productID}'")

        # fetch the result
        result = self.cursor.fetchone()

        if result:
            print("what do you want to update?")
            print("1. name")
            print("2. price")
            print("3. quantity")
            print("4. category")

            value = input("select a number: ")

            if (int(value) == 1):
                name = input("enter a new name: ")
                # this changes the name
                # # sql injection prone
                self.cursor.execute(
                    f"UPDATE products SET productname = '{name}' WHERE id = '{productID}'")
                self.commit
                print("name has been updated")

            elif (int(value) == 2):
                price = int(input("enter a new price: "))
                # this changes the price
                # # sql injection prone
                self.cursor.execute(
                    f"UPDATE products SET price = '{price}' WHERE id = '{productID}'")
                self.commit
                print("price has been updated")

            elif (int(value) == 3):
                quantity = int(input("enter a new quantity: "))
                # this changes the stock quantity
                # # sql injection prone
                self.cursor.execute(
                    f"UPDATE products SET stockQuantity = '{quantity}' WHERE id = '{productID}'")
                self.commit
                print("quantity has been updated")

            elif (int(value) == 4):
                category = input("enter a new category: ")
                # this changes the category
                # # sql injection prone
                self.cursor.execute(
                    f"UPDATE products SET category = '{category}' WHERE id = '{productID}'")
                self.commit
                print("category has been updated")

            else:
                print("number does not exist")
        else:
            print("productID does not exist")

    def get_products(self):
        self.cursor.execute("SELECT * FROM products")
        values = self.cursor.fetchall()  # returns the products
        for row in values:  # this loops the values to return the rows
            print(row)


class Customer:
    def __init__(self, customer_id, name, email, shipping_address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.shipping_address = shipping_address

    def register_customer(self):
        self.cursor = DB().cursor
        self.commit = DB().commit
        # first i need to check if the customer has already been registerd
        # I can identify the uniqueness with the customerID
        self.cursor.execute("SELECT customerID FROM ")

        self.order_ID = order_ID
        self.order_date = order_date
        self.customer_ID = customer_ID
        self.total_mount = total_mount


class OrderItem:
    def __init__(self, product_ID, quantity, sub_total):
        self.product_ID = product_ID
        self.quantity = quantity
        self.sub_total = sub_total

# class ShoppingSystem:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(sel:
#     def __init__(self)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f):
#     def __init__(self)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f)f):
#     def __init__(self):
