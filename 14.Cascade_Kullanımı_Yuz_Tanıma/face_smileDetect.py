# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:27:40 2019

@author: mr.shark ' a teşekkürler
"""

import cv2  # opencv kütüphanemüzü import ettik .

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #xml dosyalarımızı kulanılabilir hale getiriyoruz 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') #xml dosyalarımızı kulanılabilir hale getiriyoruz 
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml') #xml dosyalarımızı kulanılabilir hale getiriyoruz 
def detect(gray ,frame): # detect adında fonsksiyon tanımladık bu fonksiyon  gray ve frame parametresini alıyor 
    faces =face_cascade.detectMultiScale(gray, 1.3, 5) #resimde yüz  bulmak için detectMultiScale fonsksiyonun'u kullanıyoruz 
    for (x,y ,w ,h) in faces : # her yüz için tanıma yapıyor döngü 
        cv2.rectangle(frame , (x,y), (x+w ,y+h) , (255,0,0) ,2 ) # yüzün çevresine dikdörtgen çiziyoruz 
        roi_gray = gray[ y:y+h ,x:x+w ] #bulunan yüzün oldugu kareyi siyah beyaz yapıyoruz 
        roi_color = frame[y:y+h ,x:x+w ]# bulunun yüzün olduğu kareyi renkli yapıyoruz
        
        eyes =eye_cascade.detectMultiScale(roi_gray, 1.1, 3)# bulunan yüz içerisinde göz tespit ediyoruz
        for (ex,ey,ew,eh) in eyes : #her yüz için bunu yapıyor 
            cv2.rectangle(roi_color , (ex, ey) , (ex+ew , ey+eh),(0,255,0),2) # gözün etrafına dikdörtgen çiziyoruz
            
        smile = smile_cascade.detectMultiScale(roi_gray, 1.7, 22) #bulunan yüz içerisinde gülücük arıyoruz 
        for (ix,iy,iw,ih) in smile :# her yüz için tekrarlıyor 
            cv2.rectangle(roi_color , (ix,iy) , (ix+iw , iy+ih), (0,0,255),2) # gülücük tespit edilirse dikdörtgen çiziyoruz
    return frame # baştan detect fonksiyonuna dönüyor 

capture = cv2.VideoCapture(0) # kamerayı açıyoruz 
while True : #sonsuz döngü oluşturuyoruz 
     _, frame =capture.read() # son resmi okutuyoruz 
     gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) # resmi gri yapıyor 
     canvas =detect(gray,frame)# fonksiyonumuza 2 parametre yolluyoruz 
     cv2.imshow('video',canvas)# kamera çıktısını alıyoruz 
     if cv2.waitKey(1) & 0xFF == ord('q'): #klavyeden tuşa basarsak 
            break # döngü duruyor
capture.release() # kamerayı kapatıyoruz
cv2.destroyAllWindows() # tüm kodu sonlandırıyoruz 
 
 
        
        

