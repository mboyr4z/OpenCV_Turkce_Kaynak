import cv2
import numpy as np


class MyClass():
    def __init__(self):
        self.img = np.zeros((512,512,3),np.uint8)
        self.koordinatlar = []

def tikla_func(events, x, y, flags, param):


    if events == cv2.EVENT_LBUTTONDOWN:
        ui.koordinatlar.append((x,y))

        if len(ui.koordinatlar) >=2:
            cv2.arrowedLine(ui.img,ui.koordinatlar[-2],ui.koordinatlar[-1], (0,0,255),3)
            cv2.imshow("oyunumuz",ui.img)
def olayimiz():
    cv2.imshow("oyunumuz",ui.img)
    cv2.setMouseCallback("oyunumuz",tikla_func)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == "__main__":
    ui = MyClass()
    olayimiz()

