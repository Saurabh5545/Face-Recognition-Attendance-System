import cv2
import os
import mysql.connector as msc

def add_new_stu():
    name = input("Enter the name :")
    rollno = input("Assign rollno :")
    path = r'C:\Users\ASUS\Desktop\Rohit\attendancepro\imagebase'

    vid = cv2.VideoCapture(0)
    img_counter =0
    os.chdir(path)
    print("Enter Q to capture imag")
    while(True):

        success, frame = vid.read()

        cv2.imshow("webcam",frame)



        img_name = f'{rollno}_{name}.jpg'.format(img_counter)

        cv2.imwrite(img_name, frame)
        img_counter+=1

        cv2.imshow('webcam', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    mydb = msc.connect( host='localhost' ,user= 'root',password = '' , port = '3306' , database = 'attendance_p')
    mycursor = mydb.cursor()
    add_re = "INSERT INTO STUDENT (rollno,name) VALUES (%s,%s)"
    mycursor.execute(add_re,(rollno,name))
    mydb.commit()
    mycursor.close()
    mydb.close()
    vid.release()
    cv2.destroyAllWindows()

