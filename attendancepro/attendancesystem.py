import cv2
import numpy as np
import face_recognition as fr
import os
from datetime import datetime


def findencoding(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

def markattendence(name,rollno) :

    with open('attendence.csv','r+') as fin:
        mydatalist = fin.readlines()
        #print(mydatalist)
        namelist = []

        for line in mydatalist:
            entry = line.split(',')
            #print(entry)
            namelist.append(entry[0])
        #print("*",namelist)
        if rollno not in namelist :
            now = datetime.now()
            dtsting = now.strftime('%H:%M:%S')
            fin.writelines(f'\n{rollno},{name},{dtsting}')


def face_project():
    path = 'imagebase'
    images = []
    classnames = []
    mylist = os.listdir(path)
    print(mylist)

    for cls in mylist:
        curimg = cv2.imread(f'{path}/{cls}')
        images.append((curimg))
        classnames.append(os.path.splitext(cls)[0])
    print(classnames)

    fileVariable = open('attendence.csv', 'r+')
    fileVariable.truncate(0)
    fileVariable.writelines(f'ROLLNO,NAME,TIME')
    fileVariable.close()

    encodelistknown = findencoding(images)
    print('encoding completes')

    capt = cv2.VideoCapture(0)

    while True:
        success,img = capt.read()
        imgs = cv2.resize(img,(0,0),None,0.25,0.25)
        imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

        facescurrframe = fr.face_locations(imgs)
        encodescurrframe = fr.face_encodings(imgs,facescurrframe)

        for encodeface,faceloc in zip(encodescurrframe,facescurrframe):
            matches = fr.compare_faces(encodelistknown,encodeface)
            facedis = fr.face_distance(encodelistknown,encodeface)
            #print(facedis)
            #print("*",matches,sep='')
            matchindex = np.argmin(facedis)
            #print(matchindex)

            if matches[matchindex]:
                rollno,name = classnames[matchindex].split('_')

                y1,x2,y2,x1 = faceloc
                y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img,(x1,y2-30),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,name,(x1+4,y2-4),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                markattendence(name,rollno)

        cv2.imshow('webcam',img)
        if cv2.waitKey(1) == ord('s'):
            break

    capt.release()
    cv2.destroyAllWindows()


