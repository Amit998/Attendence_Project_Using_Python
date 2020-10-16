import cv2
import numpy as np
import face_recognition
import os

path ='img'
images=[]
classNames=[]
myList=os.listdir(path)
print(myList)
# print(myList)

# for cls in myList:
#     currImage=cv2.imread(f'{path}/{cls}')
#     images.append(currImage)
#     classNames.append(os.path.splitext(cls)[0])



# # print(images)


# def findEncoding(images):
#     encodList=[]
#     for img in images:
#         img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#         encode=face_recognition.face_encodings(img)[0]
#         encodList.append(encode)

#     return encodList


# encodeListKnown=findEncoding(images)
# print('Encoding Complete')

# cap=cv2.VideoCapture(0)

# while True:
#     success,img =cap.read()
#     imgS=cv2.resize(img,(0,0),None,0.25,0.25)
#     cv2.imshow('Webcame',img)
   
#     imgS=cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

#     faceCurFrame=face_recognition.face_locations(imgS)
#     encodeCurFace=face_recognition.face_encodings(imgS,faceCurFrame)

#     for encodeFace,faceLoc in zip(encodeCurFace,faceCurFrame):
#         matches=face_recognition.compare_faces(encodeListKnown,encodeFace)
#         faceDistance=face_recognition.face_distance(encodeListKnown,encodeFace)
#         print(faceDistance)
#         matchIndex=np.argmin(faceDistance)

#         if matches[matchIndex]:
#             name=classNames[matchIndex].upper()
#             print(name)

    # cv2.waitKey(1)
    
    




# faceLoc=face_recognition.face_locations(imgBill)[0]
# endcodeBill=face_recognition.face_encodings(imgBill)[0]
# cv2.rectangle(imgBill,(faceLoc[3], faceLoc[0]),(faceLoc[1], faceLoc[2]),(255,0,255),2)
# # print(faceLoc)


# faceLocTest=face_recognition.face_locations(imgBill2)[0]
# endcodeBillTest=face_recognition.face_encodings(imgBill2)[0]
# cv2.rectangle(imgBill2,(faceLocTest[3], faceLocTest[0]),(faceLocTest[1], faceLocTest[2]),(255,0,255),2)


# result=face_recognition.compare_faces([endcodeBill],endcodeBillTest)
# face_dis=face_recognition.face_distance([endcodeBill],endcodeBillTest)






# imgBill=face_recognition.load_image_file('img/Bill Gates.jpg')
# imgBill=cv2.cvtColor(imgBill,cv2.COLOR_BGR2RGB)


# imgBill2=face_recognition.load_image_file('img/Bill-Gates-2011.jpg')
# imgBill2=cv2.cvtColor(imgBill2,cv2.COLOR_BGR2RGB)