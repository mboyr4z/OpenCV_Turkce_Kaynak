import cv2

kamera = cv2.VideoCapture("video.mp4")          # videoyu oku ve kamera adlı değişkene kaydet

while(kamera.isOpened()):                       # eğer kamera açık olduğu sürece while dönsün

    deger,video = kamera.read()                 # kameradan gelen veriyi oku ve video adlı değişkene kaydet
    # burda read() fonksiyonundan iki değer dönüyor 1. si video okunabiliyor mu? bunu değer adlı değişkene kaydet
    # videoyu ise video adlı değişkene kaydet

    if deger == True:
        print(deger)        #deger adlı değişkeni yazdırdğımızda video boyunca true dönecek video bitince false dönecek

        cv2.imshow("resim", video)  # bastır sürekli

        if cv2.waitKey(1) & 0xFF == ord('q'):       #klavyeden değer beklenir ve bu değer 'q' tuşu ise videoyu bitir ve ekranı kapat
            break
    else:                   #değer false ise video bitmiş demektir
        print(deger)
        break

kamera.release()            # kamera adlı değişkeni kapat
cv2.destroyAllWindows()     #tğm pencereleri kapat
