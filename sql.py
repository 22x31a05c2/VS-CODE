import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def fetch_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM your_table_name")  # Change 'your_table_name' to your actual table name
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def insert_data(connection, data):
    cursor = connection.cursor()
    query = "INSERT INTO your_table_name (column1, column2) VALUES (%s, %s)"  # Change columns as needed
    cursor.execute(query, data)
    connection.commit()
    print("Data inserted successfully")

def main():
    # Replace with your actual MySQL credentials and database name
    host_name = "localhost"
    user_name = "your_username"
    user_password = "your_password"
    db_name = "your_database_name"

    # Create a connection to the database
    connection = create_connection(host_name, user_name, user_password, db_name)

    # Fetch and display data from the table
    print("Fetching data from the table:")
    fetch_data(connection)

    # Insert new data into the table
    new_data = ("value1", "value2")  # Replace with actual values to insert
    insert_data(connection, new_data)

    # Fetch and display data again to see the changes
    print("Fetching data from the table after insertion:")
    fetch_data(connection)

    # Close the connection
    if connection:
        connection.close()

if __name__ == "__main__":
    main()