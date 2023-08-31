import face_recognition
import numpy as np
import cv2
import csv
import os
from datetime import datetime
import glob
from pathlib import Path
from playsound import playsound
import mysql.connector

# directory=[]
# images=[]
# known_encoding=[]
# all_enrollment_numbers=[]

# def image_data():
#     n=0
#     all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
#     images.append(face_recognition.load_image_file(directory[n]))# to load all images
#     known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
 
sql = mysql.connector.connect(host="localhost",user="root",password="root")
cursor=sql.cursor()
query="use attendance_db"
cursor.execute(query)

section=""
category=""
subject=input("Enter the lecture name, use \"_\" to separate words :\n")
section=input("Enter the section: A, C, BOTH :\n").upper()
session_type=input("Enter the lecture type: LAB or THEORY :\n").upper()
if session_type=="LAB":
    if section=="A":
        category=input("Enter the group: T1, T2\n").upper()
    elif section=="C":
        category=input("Enter the group: T3, T4\n").upper()
elif session_type=="THEORY":
    if section=="A":
        category=""
        category="T1,T2"
    elif section=="C":
        category=""
        category="T3,T4"  
else:
    print("Wrong input.")
    exit(0)


directory=[]
images=[]
known_encoding=[]
all_enrollment_numbers=[]
n=0
filePathAT1='D:/Users/DELL/Desktop/python ai class/face rec/photo/Section A/T1'
filePathAT2='D:/Users/DELL/Desktop/python ai class/face rec/photo/Section A/T2'
filePathCT3='D:/Users/DELL/Desktop/python ai class/face rec/photo/Section C/T3'
filePathCT4='D:/Users/DELL/Desktop/python ai class/face rec/photo/Section C/T4'

if session_type=="LAB":
    if section=="A":
        if category=="T1":
            for filename in glob.iglob(f'{filePathAT1}/*'):
                directory.append(filename.replace("T1\\","T1/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))# to load all images
                known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
                n+=1
        elif category=="T2":
            for filename in glob.iglob(f'{filePathAT2}/*'):
                directory.append(filename.replace("T2\\","T2/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))# to load all images
                known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
                n+=1
    if section=="C":
        if category=="T3":
            for filename in glob.iglob(f'{filePathCT3}/*'):
                directory.append(filename.replace("T3\\","T3/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))# to load all images
                known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
                n+=1
        elif category=="T4":
            for filename in glob.iglob(f'{filePathCT4}/*'):
                directory.append(filename.replace("T4\\","T4/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))# to load all images
                known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
                n+=1
elif session_type=="THEORY":
    if section=="A":
        for filename in glob.iglob(f'{filePathAT1}/*'):
            directory.append(filename.replace("T1\\","T1/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))                
            images.append(face_recognition.load_image_file(directory[n]))# to load all images
            known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
            n+=1
        for filename in glob.iglob(f'{filePathAT2}/*'):
            directory.append(filename.replace("T2\\","T2/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))# to load all images
            known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
            n+=1
    elif section=="C":
        for filename in glob.iglob(f'{filePathCT3}/*'):
                directory.append(filename.replace("T3\\","T3/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))# to load all images                    known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
                n+=1
        for filename in glob.iglob(f'{filePathCT4}/*'):
                directory.append(filename.replace("T4\\","T4/"))
                all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
                images.append(face_recognition.load_image_file(directory[n]))# to load all images                    known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
                n+=1
    elif section=="BOTH":
        for filename in glob.iglob(f'{filePathAT1}/*'):
            directory.append(filename.replace("T1\\","T1/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))                
            images.append(face_recognition.load_image_file(directory[n]))# to load all images
            known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
            n+=1
        for filename in glob.iglob(f'{filePathAT2}/*'):
            directory.append(filename.replace("T2\\","T2/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))# to load all images
            known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
            n+=1
        for filename in glob.iglob(f'{filePathCT3}/*'):
            directory.append(filename.replace("T3\\","T3/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))# to load all images                    known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
            n+=1
        for filename in glob.iglob(f'{filePathCT4}/*'):
            directory.append(filename.replace("T4\\","T4/"))
            all_enrollment_numbers.append((os.path.basename(directory[n])).replace(".jpg",""))
            images.append(face_recognition.load_image_file(directory[n]))# to load all images                    known_encoding.append(face_recognition.face_encodings(images[n])[0])# to encode all the images
            n+=1

now=datetime.now()
current_date=now.strftime("%d-%m-%Y")
file_name=subject+'_'+section+'_'+category+'_'+current_date+'.csv'
f=open(file_name,'a', newline='')
lnwriter=csv.writer(f)
lnwriter.writerow(["Enrollment_Number","Name","Entry Time"])

face_locations=[]
face_encodings=[]
marked=[]
s=True
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame=small_frame[:,:,::-1]
    if s:
        face_locations=face_recognition.face_locations(rgb_small_frame)
        face_encodings=face_recognition.face_encodings(rgb_small_frame,face_locations)
        for face_encoding in face_encodings:
            matches=face_recognition.compare_faces(known_encoding,face_encoding)
            enrollment_number=""
            face_distance=face_recognition.face_distance(known_encoding,face_encoding)
            best_match_index=np.argmin(face_distance)
            if matches[best_match_index]:
                enrollment_number=all_enrollment_numbers[best_match_index]
            if enrollment_number in all_enrollment_numbers:
                if enrollment_number in marked:
                    continue
                else:
                    now=datetime.now()
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    org=(50,50)
                    fontScale= 1# setting attributes for the text
                    fontColor= (0,255,0)
                    thickness= 3
                    lineType = 2
                    cv2.putText(frame,'Marked',
                        org, 
                        font, 
                        fontScale,
                        fontColor,
                        thickness,
                        lineType)# writing text on opencv window
                    #playsound('"D:/Users/DELL/Desktop/python ai class/face rec/message-incoming-132126.mp3"')
                    current_time=now.strftime("%H:%M:%S")
                    print(enrollment_number,"is makred present.")
                    print("Entry time :",current_time)
                    query="update students set entry_time='"+current_time+"' where enrollment='"+enrollment_number+"'"
                    cursor.execute(query)
                    sql.commit()
                marked.append(enrollment_number)
    cv2.imshow("Attendacne system",frame)
    if cv2.waitKey(1)==ord('c'):
        break
if session_type=="LAB":
    query="Select enrollment, name, entry_time from students where category='"+category+"'"
elif session_type=="THEORY":
    if section=="BOTH":
        query="select enrollment, name, entry_time from students"
    elif section=="A" or section=="C":
        query="Select enrollment, name, entry_time from students where section='"+section+"'"
cursor.execute(query)
result=cursor.fetchall()
for i in result:
    lnwriter.writerow([i[0],i[1],i[2]])
query="update students set entry_time='none'"
cursor.execute(query)
sql.commit()
cap.release()
cv2.destroyAllWindows()
f.close()