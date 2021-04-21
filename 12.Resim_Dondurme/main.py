# BELİRTİLEN KONUMDAKİ, BELİRTİLEN ADET KADAR FOTOĞRAFI 90,180 ve 270 derece dondurur ve o konuma kaydeder
#Veri çoklama için kullanılabilir

def resimDondurme(konum,adet):          #belirtilen konumdaki ilk adet kadar fotoğrafı döndürür ve kaydeder
    sayac = 0
    os.chdir(konum)                     # konuma git
    for i in os.listdir():
        if i.endswith(".jpg") or i.endswith(".png"):
            if sayac < adet:                #adet kadar yapması için

                img = cv2.imread(i)
                img1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)         #90 derece çevir ve kaydet
                cv2.imwrite(i[:-3]+"d90.jpg",img1)

                img1 = cv2.rotate(img1 ,cv2.ROTATE_90_CLOCKWISE)
                cv2.imwrite(i[:-3]+"d180.jpg", img1)

                img1 = cv2.rotate(img1, cv2.ROTATE_90_CLOCKWISE)
                cv2.imwrite(i[:-3]+"d270.jpg", img1)
                # 3 ker eçevrilip kaydedildi
                sayac += 1
                
      