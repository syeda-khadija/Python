import firebase_admin
from firebase_admin import credentials,firestore

creden =credentials.Certificate("C:\\Users\\asp\\Desktop\\Python\\pythoncon.json")
firebase_admin.initialize_app(creden)
db=firestore.client()

print("Connection with firebase - firestore")

name=input("Enter Name :")
fathername=input("Enter fathername :")
phone_no =input("Enter phone_no :")
address =input("Enter address :")
eng=float(input("Enter English mark :"))
urdu =float(input("Enter urdu mark :"))
math =float(input("Enter math mark :"))
total= eng + urdu + math
print(f"Total mark :{total}")
per=(total/300)*100
print(f"Percentage:{per}")

fetch_Student =db.collection("Student").document()
fetch_Student.set({
    "Name":name,
    "Father_name":fathername,
    "Phone_no":phone_no,
    "Address":address,
    "Englist_mark":eng,
    "Urdu_mark":urdu,
    "Math_mark":math,
    "Total":total,
    "Percentage":per
})
print("Student data added sucessfully")
