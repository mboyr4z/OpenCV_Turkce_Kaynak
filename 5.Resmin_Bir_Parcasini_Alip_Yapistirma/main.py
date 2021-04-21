import cv2

def resmin_bi_kismini_baska_yerine_yapistir():

    resim = cv2.imread("sayilar.jpg")
    cv2.imshow("ilk hali",resim)

    parcamiz = resim[0:150,0:200]           # resmin 0 la 150. satır arasındaki 0 la 200 sütun aralığının kapladığı alanı parcamiz adlı değişkene kaydet

    resim[150:300,150:350] = parcamiz       #belirtilen alana da yapıştır


    cv2.imshow("son hali",resim)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def videonun_bi_kismina_yapistir():

    kamera = cv2.VideoCapture(0)

    while kamera.isOpened():
        deger, video = kamera.read()

        if deger == 1:
            cv2.imshow("orjinal video",video)

            parcaniz = video[0:100,0:100]
            video[300:400,300:400] = parcaniz

            cv2.imshow("son hali",video)

            if cv2.waitKey(1) == ord('q'):
                break

    kamera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    #resmin_bi_kismini_baska_yerine_yapistir()
    videonun_bi_kismina_yapistir()
