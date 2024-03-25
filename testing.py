import mysql.connector

def retrieve_data_from_rds():
    # Database connection parameters
    db_host = 'demo.ctsce4iqgdo8.ap-south-1.rds.amazonaws.com'
    db_port = '3306'  # Default MySQL port
    db_name = 'karthik'
    db_user = 'admin'
    db_password = '9676291170'

    # List to store dictionaries
    data = []

    # Connect to MySQL
    try:
        conn = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            password=db_password,
            database=db_name
        )

        if conn.is_connected():
            print('Connected to MySQL database')

            # Create a cursor object
            cursor = conn.cursor(dictionary=True)  # Set dictionary=True to fetch rows as dictionaries

            try:
                # Example query
                query = "SELECT * FROM uploaded_urls LIMIT 10;"

                # Execute the query
                cursor.execute(query)

                # Fetch all the rows
                rows = cursor.fetchall()

                # Process the fetched data
                for row in rows:
                    data.append(row)

            except mysql.connector.Error as e:
                print("Error executing query:", e)

            finally:
                # Close the cursor and connection
                cursor.close()
                conn.close()
                print('MySQL connection closed')

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)

    return data

# Call the function to retrieve data
data_list = retrieve_data_from_rds()
print(data_list)
