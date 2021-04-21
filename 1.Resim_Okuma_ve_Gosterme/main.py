import cv2  # opencv-python paketiyle gelen ve kullanacağımız kütüphane

resim = cv2.imread("sayilar.jpg",1)     #resmi okuduk ve resim adlı değişkene kaydettik
    # ilk parametre resim yolu, 2. parametre resmin hangi şekilde okunacağı
    # 2.parametre = 0 ise gri görünüm
    # = 1 ise orjinal görünümdür
    #bir şey girmezseniz varsayılan olarak 1 olur

cv2.imshow("ekranadi",resim)        # ilk parametre ekranda gçsterilecek çerçevenin başlığı sonraki hangi resmi göstereceğimiz

cv2.waitKey(0)                      # herhangi bir tuşa basana kadar ekran kalsın
cv2.destroyAllWindows()             #ve tüm pencereleri kapat


