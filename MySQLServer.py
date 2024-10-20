import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None  # Initialize the connection variable
    try:
        # Establish the connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # Replace with your MySQL username
            password='Welcome@2028'  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Handle any errors during connection or execution
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the cursor and connection if the connection was established
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function to create the database
if __name__ == "__main__":
    create_database()
