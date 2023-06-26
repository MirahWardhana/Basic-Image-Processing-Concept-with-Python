import cv2 
import cv2 as cv
import numpy as np
from tkinter import filedialog
from tkinter import*
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from matplotlib.widgets import TextBox
from matplotlib.widgets import RadioButtons
import mahotas 
import mahotas.demos

fig = plt.figure(figsize= (10, 5))
fig.canvas.manager.set_window_title('Morphology Image Proccesing')


def insertImage(event): 
    global h, w, img
    path= filedialog.askopenfilename()
    img2 = cv2.imread(path)
    img=cv2.cvtColor(img2, cv2.COLOR_BGR2RGBA)
    axImage1.imshow(img)

def reset(event):
    axImage1.clear()
    axImage2.clear()

def submit(expression):
    global b, kernel
    b = eval(expression)
    s = (rbuttonShape.value_selected)
    if s=="Rectangle": 
        kernel =  cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(b,b))
    elif s=="Cross": 
        kernel =  cv2.getStructuringElement(cv2.MORPH_CROSS, ksize=(b,b))
    elif s=="Elipse": 
        kernel =  cv2.getStructuringElement(cv2.MORPH_ELLIPSE, ksize=(b,b))
    elif s=="Gradient": 
        kernel =  cv2.getStructuringElement(cv2.MORPH_GRADIENT, ksize=(b,b))

def dilated(event): 
    global a
    # kernel =  cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(b,b))
    img_dilation = cv2.dilate(img, kernel)
    axImage2.imshow(img_dilation)
    a=img_dilation


def eroted(event):
    global a
    # kernel =  cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(b,b))
    img_erosion = cv2.erode(img, kernel)
    axImage2.imshow(img_erosion)
    a=img_erosion


def thinned(event): 
    img_thinned=img.max(2)
    skeleton = mahotas.otsu(img_thinned) 
    img_thinned = img_thinned > skeleton
    thinned = mahotas.thin(img_thinned)
    axImage2.imshow(thinned)
    # a= thinned
    # gray=cv.cvtColor(a, cv.COLOR_BGR2GRAY)
    # threshold,thresh=cv.threshold(gray, 127, 255, cv.THRESH_BINARY) 
    # img2=cv2.cvtColor(thresh, cv2.COLOR_BGR2RGBA)
    # axImage2.imshow(img2)

def opened(event): 
    global a
    # kernel =  cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(b,b))
    img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    axImage2.imshow(img_opening)
    a= img_opening

def closed(event): 
    global a
    # kernel =  cv2.getStructuringElement(cv2.MORPH_RECT, ksize=(b,b))
    img_closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    axImage2.imshow(img_closing)
    a= img_closing

def threshold(event):
    gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    threshold,thresh=cv.threshold(gray, 127, 255, cv.THRESH_BINARY) 
    img2=cv2.cvtColor(thresh, cv2.COLOR_BGR2RGBA)
    axImage1.imshow(img2)

    gray=cv.cvtColor(a, cv.COLOR_BGR2GRAY)
    threshold,thresh=cv.threshold(gray, 127, 255, cv.THRESH_BINARY) 
    img2=cv2.cvtColor(thresh, cv2.COLOR_BGR2RGBA)
    axImage2.imshow(img2)


axImage1 = fig.add_axes([1/8, 1/2, 1/4,5/12])
axImage2 = fig.add_axes([1/2+1/8, 1/2, 1/4,5/12])

axImage1.set_title("Original Image")
axImage2.set_title("Morphed Image")

axInsert = fig.add_axes([0, 1/4, 1/2, 1/8])
axThreshold = fig.add_axes([0, 0, 1/4, 1/4])
axReset = fig.add_axes([1/4, 0, 1/4, 1/4])

# 1/4+1/8=3/8
axDilate = fig.add_axes([1/2, 3/8-3/40, 1/4, 3/40])
axErode = fig.add_axes([1/2,3/8-6/40, 1/4, 3/40])
axThin = fig.add_axes([1/2, 3/8-9/40, 1/4, 3/40])
axOpen = fig.add_axes([1/2, 3/8-12/40, 1/4, 3/40])
axClose = fig.add_axes([1/2, 0, 1/4, 3/40])

buttonInsert = Button(axInsert, 'insert image')
buttonThreshold = Button(axThreshold, 'threshold')
buttonReset = Button(axReset, 'reset')

buttonDilate = Button(axDilate, 'Dilate')
buttonErode = Button(axErode, 'Erote')
buttonThin = Button(axThin, 'Thin')
buttonOpen = Button(axOpen, 'Open')
buttonClose = Button(axClose, 'Close')

buttonInsert.on_clicked(insertImage)
buttonThreshold.on_clicked(threshold)
buttonReset.on_clicked(reset)

buttonDilate.on_clicked(dilated)
buttonErode.on_clicked(eroted)
buttonThin.on_clicked(thinned)
buttonOpen.on_clicked(opened)
buttonClose.on_clicked(closed)

axshape  = fig.add_axes([3/4+1/8, 1/8, 1/8, 2/8])
rbuttonShape = RadioButtons(ax=axshape, labels=("Rectangle", "Cross", "Elipse","Gradient" ))
text_box = TextBox(axshape, "Bentuk kernel", color='white', textalignment='center')

axbox = fig.add_axes([3/4+1/8, 0, 1/8, 1/8])
text_box = TextBox(axbox, "Nilai kernel", color='white', textalignment='left')
text_box.on_submit(submit)
text_box.set_val("5") 

plt.show()
