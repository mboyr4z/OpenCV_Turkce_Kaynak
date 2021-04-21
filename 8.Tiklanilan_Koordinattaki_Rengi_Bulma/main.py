import cv2
import numpy as np

class MyClass():
    def __init__(self):
        self.img = cv2.imread("sayilar.jpg")
        self.renk = np.zeros((512,512,3),np.uint8)

def func(events,x,y,flags,param):
    if events == cv2.EVENT_LBUTTONDOWN:

        print(x,y)
        b,g,r = ui.img[y,x]
        ui.renk[:] = b,g,r
        cv2.imshow("renk",ui.renk)

if __name__ == "__main__":
    ui = MyClass()
    cv2.imshow("img",ui.img)

    cv2.setMouseCallback("img",func)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
