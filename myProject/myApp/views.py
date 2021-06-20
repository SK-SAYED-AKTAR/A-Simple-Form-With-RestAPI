from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import serializers
from .models import UserInformation
from .serializers import UserSerializer 
from rest_framework.decorators import api_view
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

@api_view(["POST", "GET"])
# Create your views here.
def insertData(request):
    if request.method == "POST":
        data = request.data

        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            name = data['name']
            email = data['email']
            phone = data['phone']
            dob = data['dob']

            # sendMail(name, email, phone, dob)
            serializer.save()
            return JsonResponse({"msg":"Done"})
        else:
            return JsonResponse({"msg":"Not Done"})
    else:
            return JsonResponse({"msg":"Not Done"})


@api_view(["GET", "POST"])
def allusers(request):
    users=[]
    if request.method == "GET":
        obj = UserInformation.objects.all()
        serializer = UserSerializer(obj, many=True)
        
        return JsonResponse(serializer.data, safe=False)
        
    else:
        return JsonResponse({"msg":"This method not allowed here !"})

def sendMail(name, email, phone, dob):
    fromMail = "sayeddevil2@gmail.com"
    password = "sayedisahacker100%TRUE"

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(fromMail, password)
    print("Login successfull ....")


    message = MIMEMultipart("alternative")
    message['Subject'] = "You have successfully registered !!!"
    html = f'''
        <html>
            <head> </head>
            <body>
                    <b>Your Name: </b>{name} <br><br>
                    <b>Email Address: </b>{email} <br><br>
                    <b>Phone Number: </b>{phone} <br><br>
                    <b>Date of birth : </b>{dob} <br><br>               
            </body>
        </html>

    '''

    text = MIMEText(html, "html")
    message.attach(text)


    try:
        server.sendmail(fromMail, email, message.as_string())
        print("Email successfully send !!!!")
    except Exception as e:
        print(e)

    server.quit()
