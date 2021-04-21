
# BELİRTİLEN KONUMDAKİ, ADET KADAR FOTOĞRAFI, BRİGHTNESS DEĞERİ KADAR KOYULAŞTIRIR
# VERİ ÇOKLAMA İÇİN KULLANILABİLİR


def resimParlaklıkArtırma(konum,adet,brightness):           # belirtilen brightness değeri kadar alındı
    sayac = 0
    os.chdir(konum)
    for i in os.listdir():
        if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".jpeg"):

            if sayac < adet:
                contrast = 30
                img = cv2.imread(i)
                img = np.int16(img)
                img = img * (contrast / 127 + 1) - contrast - brightness        #PARLAKLIK DEĞİŞTİRME KODU
                img = np.clip(img, 0, 255)
                img = np.uint8(img)
                sayac += 1
                cv2.imwrite(i[:-3] + "b.jpg",img)
                cv2.waitKey(0)

