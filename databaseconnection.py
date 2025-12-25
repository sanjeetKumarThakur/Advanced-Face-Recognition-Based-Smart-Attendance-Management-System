import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="login"
    )

    if connection.is_connected():
        print("Connected to MySQL database")

except mysql.connector.Error as e:
    print("Failed to connect")
    print(e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()