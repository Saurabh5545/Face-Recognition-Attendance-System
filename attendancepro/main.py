import attendancesystem as attsy
import datab as db
import taking_img as ti
import mysql.connector as msc
import pandas as pd

print("\n\t\t\t\tATTENDANCE SYSTEM\n")

while True:
    move = int(input("\n1-Add new Student\n2-Take Attendance\n3-Show the database\n4-Exit\nInput Choice - "))

    if move == 1 :
       ti.add_new_stu()
       print("\nNew Student Added sucessfully..!!\n")

    elif move == 2 :

        print("\nTaking Attendance\n")
        attsy.face_project()
        print("\nAttendance finished....!!\nMaking Changes in Database\n")
        db.databasechanges()
        print("\nChanges Finished...!!\n")

    elif move == 3 :
        mydb = msc.connect(host='localhost', user='root', password='', port='3306', database='attendance_p')
        mycursor = mydb.cursor()
        detail = pd.read_sql_query("select * from student", mydb)
        print("\n",detail)

    else:
        print("Exiting....the System!!")
        exit(0)