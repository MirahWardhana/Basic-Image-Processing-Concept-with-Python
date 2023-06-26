from tkinter import filedialog, messagebox
from tkinter import*
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import numpy as np
from subprocess import call
from tkinter import simpledialog

root= Tk()
root.title("Image Enchantment Program")
root.geometry("785x462")
root.configure(bg='white')

def reset_image():
    root.destroy()  
    call(["python", "C:/Users/user/OneDrive/Documents/Tugas Tugas Kuliah Semester 3/Pengolahan Citra Digital/Tugas3 (IMAGE ENHANCEMENT)/tugas3.py"])
    
def insert_file():
    global img_pixel, x, y, w, h, rvalue, gvalue, bvalue, img
    x = 0 
    y = 0
    img_pixel = []

    path= filedialog.askopenfilename(title="Select an Image", filetype=(('image files','*.jpg'),('all files','*.*')))
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
        img_resized=img.resize((230,230))
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
    
def grayscale_image():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        a= int((rvalue+ gvalue+bvalue)/3)
        load[x, y] = (a, a, a)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=1, columnspan=2)

def BlackandWhite_image(): 
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        a= int((rvalue+ gvalue+bvalue)/3)
        if (a>=0 and a<=112):
            a=0
        else:
            a=225
        load[x, y] = (a, a, a)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=1, columnspan=2)

def BrightnessAdjustment():
    ans=simpledialog.askinteger("input nilai brightness", "Masukkan kenaikkan konstanta penyesuaian (-225 sampai 225)", parent=root)
    result = messagebox.askquestion("grayscale atau citra berwarna", "Apakah mau dalam citra berwarna?")
    b=int(ans)
    if result == 'yes':
        size = w, h
        img2 = Image.new('RGB', size)
        load = img2.load()
        for cr in img_pixel:
            x, y, rvalue, gvalue, bvalue = cr
            load[x, y] = (b+rvalue, b+gvalue, b+bvalue)
    else:       
        size = w, h
        img2 = Image.new('RGB', size)
        load = img2.load()
        for cr in img_pixel:
            x, y, rvalue, gvalue, bvalue = cr
            a= int((rvalue+ gvalue+bvalue)/3)
            load[x, y] = (b+a, b+a, b+a)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=3, columnspan=2)

    
def Negation():
    result = messagebox.askquestion("grayscale atau citra berwarna", "Apakah mau dalam citra berwarna?")
    if result == 'yes':
        size = w, h
        img2 = Image.new('RGB', size)
        load = img2.load()
        n=225
        for cr in img_pixel:
            x, y, rvalue, gvalue, bvalue = cr
            load[x, y] = (n-rvalue, n-gvalue, n-bvalue)
    else:       
        size = w, h
        img2 = Image.new('RGB', size)
        load = img2.load()
        n=225
        for cr in img_pixel:
            x, y, rvalue, gvalue, bvalue = cr
            a= int((rvalue+ gvalue+bvalue)/3)
            load[x, y] = (n-a, n-a, n-a)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=3, columnspan=2)

def GammaCorrection():
    ans=simpledialog.askfloat("input nilai gamma correction", "Masukkan kenaikkan konstanta penyesuaian (0.5-1)", parent=root)
    result = messagebox.askquestion("grayscale atau citra berwarna", "Apakah mau dalam citra berwarna?")
    if result == 'yes':
        size = w, h
        img2 = Image.new('RGB', size)
        load = img2.load()

        for cr in img_pixel:
            x, y, rvalue, gvalue, bvalue = cr
            a= pow(rvalue,1/ans)
            b= pow(gvalue,1/ans)
            c= pow(bvalue,1/ans)
            load[x, y] = (int(a), int(b), int(c))

    else: 
        size = w, h
        img2 = Image.new('RGB', size)
        load = img2.load()

        for cr in img_pixel:
            x, y, rvalue, gvalue, bvalue = cr
            c= int((rvalue+ gvalue+bvalue)/3)
            b= pow(c,1/ans)
            # a= int(b)
            a = np.zeros((b), dtype=np.int64)
            load[x, y] = (a, a, a)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=3, columnspan=2)

def ContrastStretching1():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()
    b=[]

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        a= int((rvalue+ gvalue+bvalue)/3)
        load[x, y] = (a, a, a)
        
    for i in range (w):
        for j in range (h):
            rvalue = img.getpixel((x,y))[0]
            gvalue = img.getpixel((x,y))[1]
            bvalue = img.getpixel((x,y))[2]
            a= int((rvalue+ gvalue+bvalue)/3)
            b.append(a)
            j += 1
            y += 1
        x += 1
        i += 1
        y = 0
        j = 0
            
    max=b.max()
    min=b.min()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        c = int((rvalue+ gvalue+bvalue)/3)
        d= (c-min)/(max-min) * 255
        e= int(d)
        x, y, rvalue, gvalue, bvalue = cr
        load[x, y] = (e, e, e)

    if (img.height>img.width):
        img_resized=img2.resize((200,305))
 
    elif (img.height<img.width):
        img_resized=img2.resize((235,150))
        
    elif (img.height==img.width):
        img_resized=img2.resize((230,230))
        
    img_copy=ImageTk.PhotoImage(img_resized)
    labelimage2= Label(root,image= img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1,column=3, columnspan=2)

def ContrastStretching2():
    print("function has not finished")


def IntensitySlicing1():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    img_pixel = image.load()  # Load pixels from the input image

    for y in range(image.height):
        for x in range(image.width):
            pixel = img_pixel[x, y]  # Get the pixel value at the current coordinates
            r, g, b, _ = pixel  # Unpack pixel values, ignoring the alpha channel if present
            intensity = int((r + g + b) / 3)

            # Apply intensity slicing
            if intensity >= 0 and intensity <= 85:
                load[x, y] = (255, 0, 0)  # Set pixel to red
            elif intensity > 85 and intensity <= 170:
                load[x, y] = (0, 255, 0)  # Set pixel to green
            else:
                load[x, y] = (0, 0, 255)  # Set pixel to blue

    if image.height > image.width:
        img_resized = img2.resize((200, 305))
    elif image.height < image.width:
        img_resized = img2.resize((235, 150))
    else:
        img_resized = img2.resize((230, 230))

    img_copy = ImageTk.PhotoImage(img_resized)
    labelimage2 = tk.Label(root, image=img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1, column=3, columnspan=2)

def IntensitySlicing2():
    print("function has not finished")

def BitExtraction():
    ans = simpledialog.askinteger("Input bit position", "Enter the bit position to extract (0-7)", parent=root)
    bit_position = int(ans)

    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        r_binary = format(rvalue, '08b')
        g_binary = format(gvalue, '08b')
        b_binary = format(bvalue, '08b')

        if bit_position >= 0 and bit_position <= 7:
            r_bit = int(r_binary[bit_position])
            g_bit = int(g_binary[bit_position])
            b_bit = int(b_binary[bit_position])
        else:
            messagebox.showerror("Invalid bit position", "Please enter a valid bit position (0-7)")
            return

        r_extracted = r_bit * 255
        g_extracted = g_bit * 255
        b_extracted = b_bit * 255

        load[x, y] = (r_extracted, g_extracted, b_extracted)

    if img.height > img.width:
        img_resized = img2.resize((200, 305))
    elif img.height < img.width:
        img_resized = img2.resize((235, 150))
    elif img.height == img.width:
        img_resized = img2.resize((230, 230))

    img_copy = ImageTk.PhotoImage(img_resized)
    labelimage2 = Label(root, image=img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1, column=3, columnspan=2)

def RangeCompression():
    ans_start = simpledialog.askinteger("Input start position", "Enter the starting bit position (0-7)", parent=root)
    ans_end = simpledialog.askinteger("Input end position", "Enter the ending bit position (0-7)", parent=root)

    start_position = int(ans_start)
    end_position = int(ans_end)

    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    if start_position < 0 or start_position > 7 or end_position < 0 or end_position > 7:
        messagebox.showerror("Invalid bit position", "Please enter valid start and end positions (0-7)")
        return

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        r_binary = format(rvalue, '08b')
        g_binary = format(gvalue, '08b')
        b_binary = format(bvalue, '08b')

        r_range = r_binary[start_position : end_position+1]
        g_range = g_binary[start_position : end_position+1]
        b_range = b_binary[start_position : end_position+1]

        r_compressed = int(r_range + (8 - len(r_range)) * '0', 2)
        g_compressed = int(g_range + (8 - len(g_range)) * '0', 2)
        b_compressed = int(b_range + (8 - len(b_range)) * '0', 2)

        load[x, y] = (r_compressed, g_compressed, b_compressed)

    if img.height > img.width:
        img_resized = img2.resize((200, 305))
    elif img.height < img.width:
        img_resized = img2.resize((235, 150))
    elif img.height == img.width:
        img_resized = img2.resize((230, 230))

    img_copy = ImageTk.PhotoImage(img_resized)
    labelimage2 = Label(root, image=img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1, column=3, columnspan=2)

def HistogramEqualization():
    size = w, h
    img2 = Image.new('RGB', size)
    load = img2.load()

    # Calculate histogram
    histogram = np.zeros(256, dtype=np.int)

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        intensity = int((rvalue + gvalue + bvalue) / 3)
        histogram[intensity] += 1

    # Calculate cumulative distribution function (CDF)
    cdf = np.cumsum(histogram)
    cdf_normalized = (cdf / cdf.max()) * 255

    for cr in img_pixel:
        x, y, rvalue, gvalue, bvalue = cr
        intensity = int((rvalue + gvalue + bvalue) / 3)
        equalized_intensity = int(cdf_normalized[intensity])
        load[x, y] = (equalized_intensity, equalized_intensity, equalized_intensity)

    if img.height > img.width:
        img_resized = img2.resize((200, 305))
    elif img.height < img.width:
        img_resized = img2.resize((235, 150))
    elif img.height == img.width:
        img_resized = img2.resize((230, 230))

    img_copy = ImageTk.PhotoImage(img_resized)
    labelimage2 = Label(root, image=img_copy)
    labelimage2.image = img_copy
    labelimage2.grid(row=1, column=3, columnspan=2)



label= Label(root, text="Source Image", font= ('Times 10 bold'), fg="gray")
label.grid(row=0,column=0)

label= Label(root, text="Greyscale/Black and White Image", font= ('Times 10 bold'), fg="gray")
label.grid(row=0,column=1, columnspan=2)

label= Label(root, text="Enhanced Image", font= ('Times 10 bold'), fg="gray")
label.grid(row=0,column=3, columnspan=2)

frame= LabelFrame(root, text= "image", padx=200, pady=300)
frame.grid(padx=100,pady=155)
frame.grid(row=1,column=0)

frame= LabelFrame(root, text= "image", padx=200, pady=300)
frame.grid(padx=100,pady=155)
frame.grid(row=1,column=1, columnspan=2)

frame= LabelFrame(root, text= "image", padx=200, pady=300)
frame.grid(padx=100,pady=155)
frame.grid(row=1,column=3, columnspan=2)

btnInsert=Button(root, text ="insert file", bg="black", fg="white", padx=97, pady=26, command= insert_file)
btnGrayscale=Button(root, text ="greyscale", bg="grey", padx=36, pady=26, command= grayscale_image)
btnBlackandWhite=Button(root, text ="black and white", bg="black", fg="white", padx=15, pady=26, command= BlackandWhite_image)
btnReset=Button(root, text ="reset", bg="white", padx=235, pady=14, command= reset_image)
btnBrightnessAdjustment=Button(root, text ="Brightness Adjustment", bg="white", padx=9, pady=1, command= BrightnessAdjustment)
btnNegation=Button(root, text ="Negation", bg="white", padx=45, pady=1, command= Negation)
btnGammaCorrection=Button(root, text ="Gamma Correction", bg="white", padx=19, pady=1, command= GammaCorrection)
btnContrastStretching1=Button(root, text ="Contrast Stretching1", bg="white", padx=15, pady=1, command=ContrastStretching1)
btnContrastStretching2=Button(root, text ="Contrast Stretching2", bg="white", padx=15, pady=1, command=ContrastStretching2)
btnIntensitySlicing1=Button(root, text ="Intensity Slicing1", bg="white", padx=18, pady=1, command=IntensitySlicing1)
btnIntensitySlicing2=Button(root, text ="Intensity Slicing2", bg="white", padx=18, pady=1, command=IntensitySlicing2)
btnBitExtraction=Button(root, text ="Bit Extraction", bg="white", padx=28, pady=1, command=BitExtraction)
btnRangeCompression=Button(root, text ="Range Compression", bg="white", padx=10, pady=1, command=RangeCompression)
btnHistogramEqualization=Button(root, text ="Equalize Histogram",  bg="white", padx=9, pady=1, command=HistogramEqualization)


btnInsert.grid(row=2,column=0, rowspan=3)
btnGrayscale.grid(row=2,column=1, rowspan=3)
btnBlackandWhite.grid(row=2,column=2, rowspan=3)
btnReset.grid(row=5,column=0,rowspan=2,columnspan=3)
btnBrightnessAdjustment.grid(row=2,column=3)
btnNegation.grid(row=3,column=3)
btnGammaCorrection.grid(row=4,column=3)
btnContrastStretching1.grid(row=5,column=3)
btnContrastStretching2.grid(row=6,column=3)
btnIntensitySlicing1.grid(row=2,column=4)
btnIntensitySlicing2.grid(row=3,column=4)
btnBitExtraction.grid(row=4,column=4)
btnRangeCompression.grid(row=5,column=4)
btnHistogramEqualization.grid(row=6,column=4)

root.mainloop()