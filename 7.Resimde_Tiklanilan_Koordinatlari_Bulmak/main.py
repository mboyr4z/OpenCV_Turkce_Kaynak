import cv2
import numpy as np

class myClass():
    def __init__(self):
        self.img = np.ones((512, 512, 3), np.uint8)



def func(events,x,y,flags,param):           #asagındaki MouseCallBack fonksiyonundan 5 değer gelir event olayi , x ve y diğerleri önemli değil
    if events == cv2.EVENT_RBUTTONDOWN:         #eğer mouse olayımız sağ click olayı ise
        cv2.putText(ui.img, str(x)+","+str(y) , (x,y) , cv2.FONT_HERSHEY_SIMPLEX , 2, (255,0,0) , 2 , cv2.LINE_AA)  # tıklanılan koordinata yazı koy
        
        cv2.imshow("img", ui.img)



def olayimiz():
    cv2.imshow("img", ui.img)

    cv2.setMouseCallback("img",func)    # mouse ile herhangi bir değişiklik yapıldığında (konum veya tıklanma) fonksiyonu çağır

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":

    ui = myClass()
    olayimiz()
