import cv2
import numpy as np

def bos_fonksiyon():
    pass


def trackBar_yap():

    resim = np.ones((1000,1000,3),np.uint8)       # resim 1000 satir 1000 sütundan ve 3 kanala sahip olan bir matristir ve
                                                  # her elemanı 0 olduğundan siyah bir resim

    resim.fill(255)                               # tüm elemanlarını bu sayede 255 yaptık ve beyaz oldu resmimiz




    cv2.imshow("frame",resim)

    cv2.createTrackbar("mavi","frame",0,255,bos_fonksiyon)
    cv2.createTrackbar("yesil","frame", 0, 255, bos_fonksiyon)
    cv2.createTrackbar("kirmizi", "frame", 0, 255, bos_fonksiyon)
    #TRACKBAR OLUŞTUR
    # PARAMETRELER ("trackbar_Adi" , "olacagi_ekran_Adi" , baslangic_Araligi , Bitis_Araligi , her_degistiginde_cagrilacak_fonksiyon)



    while True:
        mavi = cv2.getTrackbarPos("mavi","frame")   # frame adlı ekrandaki mavi adlı trackbar değerini mavi adlı değişkene ata
        yesil = cv2.getTrackbarPos("yesil","frame")
        kirmizi = cv2.getTrackbarPos("kirmizi","frame")

        resim[:] = ((mavi , yesil , kirmizi))       # resmin tüm pikselleri mavi,yeşil,ve kirmizi değerini alsın

        cv2.putText(resim,"bgr degeri = "+ str(mavi) +", "+str(yesil)+", "+str(kirmizi),(3,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
        cv2.imshow("frame",resim)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    trackBar_yap()
