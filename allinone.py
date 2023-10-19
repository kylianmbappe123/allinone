import os
os.system('cls')
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import qrcode

def add(a,b):
   sum=x+y
   print("your anwser is",sum)
def sub(a,b):
   sub=x-y
   print("your anwser is",sub)
def mul(a,b):
   mul=x*y
   print("your anwser is",mul)
def div(a,b):
   div=x/y
   print("your anwser is",div)


def calculate_bmi(w,h):
    z=h*h
    bmi=w/z
    return bmi
def bmi_text(bmi):
    if bmi<18.5:
        print("go and eat something")
    elif 18.5<=bmi and bmi<=24.9:
        print("you are normal weight")
    elif 29.9<=bmi and bmi<=29.9:
        print("you are fat. go to the gym")
    else:
        print("you are a obese to this world")


def emailsender(reciever,subject,content,image):
    hostmail='dotproduct456@gmail.com'
    hostpassword='wpaieaoevumeczav'
    recievermail=reciever
    
    asd=MIMEMultipart()
    asd['from']=hostmail
    asd['to']=recievermail
    asd['subject']=subject
    asd.attach(MIMEText(content,'plain'))

    with open(image,'rb') as image_file:
         image_data=image_file.read()
         image=MIMEImage(image_data,name='image.jpg')
         asd.attach(image)

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(hostmail,hostpassword)
    text=asd.as_string()
    server.sendmail(hostmail,recievermail,text)
    server.quit()
    print("email sent successfully,\nyou are welcome for my service")


def qr(data,color,bg):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=color, back_color=bg)
    img.save(f"{filename}.png")
    print("QR code successfully created")

a=input("ENTER YOUR NAME: \n")
print("WELCOME TO MY APP ",a)
print("\nChoose an option: \n1. Calculator\n2. BMI Calculator\n3. Email Sender\n4. QR Code Generator")
option=int(input("\nENTER YOUR CHOICE: "))
print("\nyou have choosen",option)
if option==1:
    print("WELCOME TO CALCULATOR")
    x =float(input("Enter 1st number:"))
    y =float(input("Enter 2st number:"))

    print("choose an option:\n1. Add\n2. subtract\n3. multiply\n4. divid")
    option =int(input("choose an option:"))
    if option==1:
        add(x,y)
    elif option==2:
        sub(x,y)
    elif option==3:
        mul(x,y)
    elif option==4:
        div(x,y)   
    else:
        print("you have choosen the wrong option")
elif option==2:
    print("WELCOME TO BMI CALCULATOR")
    x=float(input("\n\nenter your weight in kg:"))
    y=float(input("enter your height in meters:"))

    bmi=calculate_bmi(x,y)
    
    print("your bmi is",bmi)
    
    bmi_value = bmi_text(bmi)
elif option==3:
    print("WECOME TO EMAIL SENDER")
    subject=input("type something spicy: ")
    content=input("enter email content:  ")
    reciever=input("enter reciever's email: ")
    image=input("enter the image path: ")


    print("comfirm details: ")
    print("reciever's mail: ",reciever)
    print("subject: ",subject)
    print("content: ",content)

    confirm=input("send?? (type yes/no):")
    if confirm=='yes':
        emailsender(reciever,subject,content,image)
    else:
        print("you have entered the wrong choice")
elif option==4:
    data=input("enter the content for QRcode: ")
    color=input("enter the color for QR: ")
    bg=input("enter the bg color for QR: ")
    filename=input("enter the file name: ")
    qr(data,color,bg)
else:
    print("you have entered the wrong choice")



