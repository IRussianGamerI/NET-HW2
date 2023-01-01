import mysql.connector


def fetch_pending():
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="your_database"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM notifications WHERE status = 'pending'")
    rows = cursor.fetchall()

    # Format the data as a list of dictionaries
    data = []
    for row in rows:
        data.append({
            "user_id": row[0],
            "date": row[1],
            "msg": row[2]
        })

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return data
