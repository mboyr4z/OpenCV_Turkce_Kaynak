import cv2

def resme_yazi_ekleme():
    resim = cv2.imread("sayilar.jpg")

    font = cv2.FONT_HERSHEY_SIMPLEX         #kullanmak istediğinizi yazı tipi

    resim = cv2.putText(resim, "Selam", (100,50),font,3,(100,0,0),4)    #yazı koy fonksiyonu
    # PARAMETRELER ( resim , str("yazınız") , (konum Koordinatları) , font , yazı boyutu , renk , yazı kalınlığı)


    cv2.imshow("resim",resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def videoya_yazi_ekleme():

    kamera = cv2.VideoCapture(0)

    while(kamera.isOpened()):
        deger, video = kamera.read()

        font = cv2.FONT_HERSHEY_SIMPLEX

        if deger == True:
            video = cv2.putText(video, "naber", (100,100), font , 3, (100,100,0), 2)
            cv2.imshow("frame",video)

            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break

    kamera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    resme_yazi_ekleme()
    #videoya_yazi_ekleme()
