import cv2
import numpy as np
import face_recognition as fr

imgron = fr.load_image_file('imagebase/ronaldo.jpg')
imgron = cv2.cvtColor(imgron,cv2.COLOR_BGR2RGB)
imgtest = fr.load_image_file('imagebase/messi.jpg')
imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

faceloc = fr.face_locations(imgron)[0]
encoderon = fr.face_encodings(imgron)[0]
cv2.rectangle(imgron,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(0,255,0),2)

faceloct = fr.face_locations(imgtest)[0]
encoderontest = fr.face_encodings(imgtest)[0]
cv2.rectangle(imgtest,(faceloct[3],faceloct[0]),(faceloct[1],faceloct[2]),(0,255,0),2)

results = fr.compare_faces([encoderon],encoderontest)
facedist = fr.face_distance([encoderon],encoderontest)
print(results,facedist)
cv2.putText(imgtest,f'{results} {round(facedist[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
cv2.imshow('Ronaldo',imgron)
cv2.imshow('Ronalfo test',imgtest)
cv2.waitKey(0)