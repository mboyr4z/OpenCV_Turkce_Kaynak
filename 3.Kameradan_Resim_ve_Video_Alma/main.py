import cv2


def video_al_ve_kaydet():

    kamera = cv2.VideoCapture(0)                     #bilgisar kamerasindan videoyu kamera adlı değişkene kaydet (0 değeri pc kamerasi demektir)

    kaydetmetipi = cv2.VideoWriter_fourcc(*'XVID')                              #XVID türünde video kaydedilecek

    kaydet = cv2.VideoWriter('selam.avi',kaydetmetipi,60.0, (640,480))         #videowriter video kayıt oluşturma fonksiyonudur
    #parametreler ("videoadi.uzantisi" , kaydetmetipi , FPS , boyutlar )




    while(kamera.isOpened()):           #kamera açık olduğu sürece
        deger , video = kamera.read()   # video yu al

        if deger==True:

            kaydet.set(3,600)           # kaydedilecek videonun 3. özelliği (genişlik) 600pixel olsun
            kaydet.set(4,400)           # kaydedilecek videonun 4. özelliği (yukseklik) 400pixel olsun

            kaydet.write(video)         # videoyu sürekli yazdır

            cv2.imshow('frame',video)   # ekrana da ver

            if cv2.waitKey(1) == ord('q'):  # 'q' tui-şuna basınca bırak
                break
        else:
            break


    kamera.release()        # kamerayı kapat
    kaydet.release()        # kaydetmeyi de bitir
    cv2.destroyAllWindows()




def kameradan_fotograf_al():
    # KAMERADAN RESİM ALMA ASLINDA VİDEONUN HERHANGi BİR ANINDAKİ GÖRÜNTÜSÜNÜ ALMAKTIR

    kamera = cv2.VideoCapture(0)  # bilgisar kamerasindan videoyu kamera adlı değişkene kaydet 0 değeri pc kamerasi demektir

    while (kamera.isOpened()):  # kamera açık olduğu sürece
        deger, video = kamera.read()  # video yu al

        if deger == True:

            cv2.imshow('ekranadi', video)  # ekrana da ver

            if cv2.waitKey(1) == ord('q'):  # 'q' tuşuna basınca
                cv2.imwrite("fotografimiz.jpg",video)           # videonun o anlık görüntüsünü jpg olarak kaydet
                break   # bırak
        else:
            break

    kamera.release()  # kamerayı kapat
    cv2.destroyAllWindows()

if __name__ == "__main__":
    kameradan_fotograf_al()
