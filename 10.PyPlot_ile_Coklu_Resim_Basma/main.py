import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("sayilar.jpg")
img2 = cv2.imread("sayilar.jpg")


images = [img , cv2.putText(img2, "selam",(100,100),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0),3) ]

titles = ["sayilar","duzenlenmiş sayilar"]



for i in range(2):
    plt.subplot(1,2,i+1)                    # kaça kaçlık bir düzende gösterilsin
    plt.imshow(images[i], "gray")           # resimleri ekle
    plt.title(titles[i])                    # başlıkları ekle
    plt.xticks([])                          # x ve y scrollBarı yok et
    plt.yticks([])

plt.show()
