import mysql.connector as msc
from datetime import date


def databasechanges():
   mydb = msc.connect( host='localhost' ,user= 'root',password = '' , port = '3306' , database = 'attendance_p')
   mycursor = mydb.cursor()
   show = "Select * from student"
   #add_re = "INSERT INTO STUDENT (rollno,name) VALUES (%s,%s)"
   c_date = date.today()

   try:
      mycursor.execute("ALTER TABLE student ADD  `\'%s\'` varchar(1) NOT NULL DEFAULT 'A'"%c_date)
   except:
      mycursor.execute("ALTER TABLE student DROP  `\'%s\'`" % c_date)
      mycursor.execute("ALTER TABLE student ADD  `\'%s\'` varchar(1) NOT NULL DEFAULT 'A'" % c_date)

   with open('attendence.csv', 'r+') as fin:
      mydatalist = fin.readlines()
      #print(mydatalist)
      namelist = []

      for line in mydatalist:
         entry = line.split(',')
         namelist.append((entry[0], entry[1]))


      for i in namelist:
         mycursor.execute("UPDATE student SET `%(in)s` = 'P' where rollno = %(rn)s",{'in':c_date,'rn':i[0]})


   mydb.commit()

   mycursor.close()
   mydb.close()


