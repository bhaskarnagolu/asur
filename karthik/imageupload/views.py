from django.shortcuts import render
import boto3
from botocore.exceptions import NoCredentialsError

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
