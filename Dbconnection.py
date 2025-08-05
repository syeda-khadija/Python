import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pythondb"
)
db_info =con.cursor()

print("--------- Student input ---------")
name =input("Enter your name :")
Guardian_name =input("Enter your Gurdian_name")
father_phone_no =input("Enter your father_phone_no")
Address =input("Enter your Address")

query ="INSERT INTO `student`(`Name`, `Guardian_name`, `Father_phone_number`, `Address`) VALUES (%s,%s,%s,%s)"
value =(name,Guardian_name,father_phone_no,Address)

run=db_info.execute(query,value)
con.commit()

print(f"{name} Data has been successfully")

con.close()