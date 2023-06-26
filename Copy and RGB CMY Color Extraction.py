from tkinter import filedialog
from tkinter import*
from PIL import Image, ImageTk
from subprocess import call

root= Tk()
root.title("Extracting RGB & CMY Program")
root.geometry("753x522")
root.configure(bg='white')

def reset_image():
    root.destroy()  
    call(["python", 'C:/Users/user/OneDrive/Documents/Tugas Tugas Kuliah Semester 3/Pengolahan Citra Digital/Tugas2 (RGB convert image)/Tugas PCD1 - Kelompok B - Kelas D.py'])
    #blok di atas diisi sesuai dengan path penyimpanan

def insert_file():
    global img_pixel, x, y, w, h, rvalue, gvalue, bvalue, img
    x = 0 
    y = 0
    img_pixel = []

    path= filedialog.askopenfilename(title="Select an Image", filetype=(('image files','*.png'),('all files','*.*')))
    img = Image.open(path)
    
    if (img.height>img.width):
        img_resized=img.resize((200,305))
        img_resized=ImageTk.PhotoImage(img_resized)
        labelimage1= Label(root,image= img_resized)
        labelimage1.image= img_resized
        labelimage1.grid(row=1,column=0)
    elif (img.height<img.width):
        img_resized=img.resize((230,150))
        img_resized=ImageTk.PhotoImage(img_resized)
        labelimage1= Label(root,image= img_resized)
        labelimage1.image= img_resized
        labelimage1.grid(row=1,column=0)
    elif (img.height==img.width):
        img_resized=img.resize((230,250))
        img_resized=ImageTk.PhotoImage(img_resized)
        labelimage1= Label(root,image= img_resized)
        labelimage1.image= img_resized
        labelimage1.grid(row=1,column=0)

    w, h = img.size
    for i in range (w):
        for j in range (h):
            rvalue = img.getpixel((x,y))[0]
            gvalue = img.getpixel((x,y))[1]
            bvalue = img.getpixel((x,y))[2]
            img_pixel.append([x, y, rvalue, gvalue, bvalue])
            j += 1
            y += 1
        x += 1
        i += 1
        y = 0
        j = 0
    
def copy_image():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        load[x, y] = (rvalue, gvalue, bvalue)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=1)


def red_image():
    global img2
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()
    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        load[x, y] = (rvalue, 0, 0)
        
    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=2, columnspan=2)

    
def green_image():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        load[x, y] = (0, gvalue,0)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=2, columnspan=2)

def blue_image():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        load[x, y] = (0, 0, bvalue)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=2, columnspan=2)

def cyan_image():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        load[x, y] = (0, gvalue, bvalue)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=2, columnspan=2)

def magenta_image():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        load[x, y] = (rvalue, 0, bvalue)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=2, columnspan=2)

def yellow_image():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        load[x, y] = (rvalue, gvalue, 0)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=2, columnspan=2)


label= Label(root, text="Source Image", font= ('Times 10 bold'), fg="gray")
label.grid(row=0,column=0)

label= Label(root, text="Copied Image", font= ('Times 10 bold'), fg="gray")
label.grid(row=0,column=1)

label= Label(root, text="Extracted Color Image", font= ('Times 10 bold'), fg="gray")
label.grid(row=0,column=2, columnspan=2)

frame= LabelFrame(root, text= "image", padx=200, pady=300)
frame.grid(padx=100,pady=155)
frame.grid(row=1,column=0)

frame= LabelFrame(root, text= "image", padx=200, pady=300)
frame.grid(padx=100,pady=155)
frame.grid(row=1,column=1)

frame= LabelFrame(root, text= "image", padx=200, pady=300)
frame.grid(padx=100,pady=155)
frame.grid(row=1,column=2, columnspan=2)

btninsert=Button(root, text ="insert file", bg="black", fg="white", padx=96, pady=50, command=insert_file)
btncopy=Button(root, text ="copy", bg="white", padx=105, pady=50, command=copy_image)
btnreset=Button(root, text ="reset", bg="white", padx=230, pady=20, command=reset_image)
btnred=Button(root, text ="red", bg="red", padx=50, pady=19, command=red_image)
btngreen=Button(root, text ="green", bg="green", padx=44, pady=20, command=green_image)
btnblue=Button(root, text ="blue", bg="blue", padx=47, pady=20, command=blue_image)
btncyan=Button(root, text ="cyan", bg="cyan", padx=50, pady=19, command=cyan_image)
btnmagenta=Button(root, text ="magenta", bg="magenta", padx=39, pady=20, command=magenta_image)
btnyellow=Button(root, text ="yellow", bg="yellow", padx=45, pady=20, command=yellow_image)

btninsert.grid(row=2,column=0, rowspan=2)
btncopy.grid(row=2,column=1, rowspan=2)
btnreset.grid(row=4,column=0,columnspan=2)
btnred.grid(row=2,column=2)
btngreen.grid(row=3,column=2)
btnblue.grid(row=4,column=2)
btncyan.grid(row=2,column=3)
btnmagenta.grid(row=3,column=3)
btnyellow.grid(row=4,column=3)

root.mainloop()