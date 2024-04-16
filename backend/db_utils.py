import os
import mysql.connector
from config import USER, PASSWORD, HOST
# this import helps to convert binary image data to a an encoded string 
import base64


def _connect_to_db():
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
    )
    print("Connected to DB: %s" % mydb)

    return mydb

_connect_to_db()

def get_all_dbs():
    db_connection = _connect_to_db()
    mycursor = db_connection.cursor()
    mycursor.execute('SHOW DATABASES')

def _connect_to_specific_db(database_name):
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database = database_name
    )
    print("Connected to DB: %s" % mydb)

    return mydb

db_name = "Shop_Management"
_connect_to_specific_db(db_name)

def _show_all_table_in_specific_db(database_name):
    specific_db = _connect_to_specific_db(database_name)
    mycursor = specific_db.cursor()
    mycursor.execute("SHOW TABLES")
    
    for x in mycursor:
        print(x)
    mycursor.close()

_show_all_table_in_specific_db(db_name)

class DbConnectionError (Exception):
    pass

def insert_image(image_filename, product_id):

    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the absolute path to the image file
    image_path = os.path.join(script_dir, image_filename)
    db_name = "Shop_Management"
    db_connection = _connect_to_specific_db(db_name)

    try:
        my_cursor = db_connection.cursor()
        print("////connected to DB: %s" % db_name)
        
         # Open the file in binary mode
        with open(image_path, 'rb') as file:
            binary_data = file.read()  # Read the entire file as binary
            
            # Inserting the image
        query = "INSERT INTO Image_Table (Image_Data, Product_ID) VALUES (%s, %s)"
        my_cursor.execute(query, (binary_data, product_id))
        db_connection.commit()
        my_cursor.close()
            
        print(f"Image inserted with Product ID {product_id}")

    except Exception as e:
       raise DbConnectionError("Failed to read data from DB", e)
    
    finally:
        # Closing the file and cursor/database connection
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

# Example usage
# insert_image('creamSofa.png',101 )
# insert_image('lamp.png', 102)
# insert_image('greenVase.png', 103)
# insert_image('rattanBed.png', 104)
# insert_image('whiteBed.png', 105)
# insert_image('blackWardrobe.png', 106)
# insert_image('sidetable.png', 107)
# insert_image('whiteDesk.png', 108)
# insert_image('armchair.png', 109)

def get_images():
    try:    
        db_name = "Shop_Management"
        db_connection = _connect_to_specific_db(db_name)
        my_cursor = db_connection.cursor()
        print("////connected to DB: %s" % db_name)
        query = 'SELECT * FROM Image_Table'
        my_cursor.execute(query)
        result = my_cursor.fetchall()
        # for i in result:
        #     print(i)
        my_cursor.close
        
        products_with_base64_images = []
        for row in result:
            product_with_base64_image = list(row)
            # Assuming the image data is in the last column (adjust if necessary)
            image_data = product_with_base64_image[-1]
            if image_data:
                base64_image = base64.b64encode(image_data).decode('utf-8')
                product_with_base64_image[-1] = base64_image
            products_with_base64_images.append(product_with_base64_image)
        
        return products_with_base64_images

    except Exception as e:
        raise DbConnectionError("Failed to read data from DB", e)
    finally:
        if db_connection:
                db_connection.close()
                print("DB connection is closed")

def get_products():
    try:
        db_name = "Shop_Management"
        db_connection = _connect_to_specific_db(db_name)
        my_cursor = db_connection.cursor()
        print("////connected to DB: %s" % db_name)
        query = 'SELECT Products.Product_ID, Products.Product_Name, Products.Product_Type, Products.Material, Products.Price, Products.Colours, Products.Image_Link, Image_Table.Image_Data FROM Products INNER JOIN Image_Table ON Products.Product_ID = Image_Table.Product_ID'
        my_cursor.execute(query)
        result = my_cursor.fetchall()

        products_with_base64_images = []
        for row in result:
            product_with_base64_image = list(row)
            # Assuming the image data is in the last column (adjust if necessary)
            image_data = product_with_base64_image[-1]
            if image_data:
                base64_image = base64.b64encode(image_data).decode('utf-8')
                product_with_base64_image[-1] = base64_image
            products_with_base64_images.append(product_with_base64_image)
        
        return products_with_base64_images

    except Exception as e:
        raise DbConnectionError("Failed to read data from DB", e)
    finally:
        if db_connection:
                db_connection.close()
                print("DB connection is closed")
    

# get_products()
