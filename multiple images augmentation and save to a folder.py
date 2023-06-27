import os
import cv2
import matplotlib.pyplot as plt
import re

# Memilih direktori asal dengan dialog
from tkinter import Tk, filedialog
Tk().withdraw()
directory_asal = filedialog.askdirectory()

# Mendapatkan daftar file gambar dalam direktori asal
list_file = [file for file in os.listdir(directory_asal) if file.endswith(('.png','.jpg', '.jpeg'))]

# Memilih direktori tujuan dengan dialog
Tk().withdraw()
directory_tujuan = filedialog.askdirectory()

# Menampilkan setiap gambar dan menyimpannya
for index, file in enumerate(list_file, start=1):
    path_file = os.path.join(directory_asal, file)
    
    # Membaca gambar menggunakan OpenCV
    img = cv2.imread(path_file)
    
    #red
    # img[:,:,1] = 0
    # img[:,:,2] = 0
    
    #blue
    # img[:,:,0] = 0
    # img[:,:,1] = 0
    
    # #green
    # img[:,:,0] = 0
    # img[:,:,2] = 0

    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    # img=cv2.rotate(img,cv2.ROTATE_180)
    img=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
    
    # Mengubah urutan kanal gambar dari BGR ke RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Mengecek apakah direktori tujuan kosong atau tidak
    file_list = os.listdir(directory_tujuan)
    if file_list:
        last_file_name = file_list[-1]
        match = re.match(r'(\d+)(\..+)', last_file_name)
        if match:
            numeric_part = int(match.group(1))
            file_extension = match.group(2)
            filename = str(numeric_part + 1) + file_extension
        else:
            print("Invalid file name format.")
    else:
        filename = "1.jpg"  # Nama file pertama
    
    # Menyimpan gambar ke direktori tujuan dengan nama baru
    save_path = os.path.join(directory_tujuan, filename)
    img_save = cv2.cvtColor(img, cv2.COLOR_RGB2BGR) 
    cv2.imwrite(save_path, img_save)
    
    # Menampilkan pesan bahwa gambar telah disimpan
    print("Image saved successfully.")
print(filename)