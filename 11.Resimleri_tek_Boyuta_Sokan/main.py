import os
import cv2
from setuptools.command.py36compat import sdist_add_defaults


def boyutlandir(boyut):
    for i in os.listdir():
        if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".jpeg"):
            img = cv2.imread(i)
            img2 = cv2.resize(img,(boyut,boyut))

            cv2.imwrite("./kucultulmusler/"+i[:-3]+"y.jpg",img2)


def rastgeleAdlandir():
    id = 0
    for i in os.listdir():
        if i.endswith(".jpg") or i.endswith(".png") or i.endswith(".jpeg"):
            id += 1
            img  = cv2.imread(i)
            cv2.imwrite("silah" + str(id) + ".jpg" ,img)
        os.remove(i)

def sadeceJPGbirak():
    for i in os.listdir():
        if i.endswith(".txt"):
            os.remove(i)
konum = r"C:\Users\Muhammet\Desktop\TabancaDataset"
os.chdir(konum)
sadeceJPGbirak()
