from django.shortcuts import render
import boto3
from botocore.exceptions import NoCredentialsError
import mysql.connector

def one(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        uploaded = handle_uploaded_file(image_file)
        if uploaded:
            return render(request, 'success.html')
        else:
            return render(request, 'one.html')  # Render failure template if upload fails
    return render(request, 'one.html')
def handle_uploaded_file(file):
    AWS_ACCESS_KEY_ID = 'AKIA5M457HDX7DXDAAJ2'
    AWS_SECRET_ACCESS_KEY = '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'
    AWS_STORAGE_BUCKET_NAME = 'generalfordemo'
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    try:
        s3.upload_fileobj(file, AWS_STORAGE_BUCKET_NAME, file.name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
def two(request):
    return render(request,"success.html")

def show_images(request):
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

    return render(request,"show_images.html",{"data":data})

