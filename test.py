import mariadb

# Define the user settings
user_setting = {
    "user": "411177001",
    "password": "411177001",
    "host": "0.tcp.jp.ngrok.io",
    "port": 11051,
    "database": "411177001",
}

try:
    # Connect to the database
    connection = mariadb.connect(**user_setting)
    cursor = connection.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM customers")

    # Fetch all the results
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

except mariadb.Error as e:
    print(f"Error connecting to the database: {e}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
