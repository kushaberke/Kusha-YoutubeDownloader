from cgitb import text
from pytube import YouTube
import os
from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD
from tkinter import ttk

# Video Bilgilerini Getiren Fonksiyon
def video_info():
    link = link_field.get()
    yt = YouTube(link)
    title_label_2.config(text=yt.title)
    author_label_2.config(text=yt.author)
    view_label_2.config(text=yt.views)
    len_label_2.config(text=yt.length)
    download_label.config(text="")

# İndirilecek Konumu Seçtiren Fonksiyon
def select_directory():
    path_select = filedialog.askdirectory()
    path_label.config(text=path_select)

# İndirme İşlemini Yapan Fonksiyon
def download_mp3():
    link = link_field.get()
    
    try:
        yt = YouTube(link)
    except:
        download_label.config(text="Geçersiz Link")

    folder =path_label.cget("text")

    uzanti = cmb.get()
    if uzanti == ".mp3":
        mp3 = yt.streams.filter(only_audio=True).first() 
        output = mp3.download(folder)
        base ,ext  = os.path.splitext(output)
        to_mp3 = base + uzanti
        os.rename(output, to_mp3)
        download_label.config(text="Başarıyla İndirildi!")
    elif uzanti ==".mp4":

        mp4 = YouTube(link).streams.get_highest_resolution().download(folder)
        download_label.config(text="Başarıyla İndirildi!")



    

# GUI Panel Oluşturmak

screen = Tk()
screen.iconbitmap(default="youtube.ico")
title = screen.title("Kusha Youtube Mp3 İndirici")
canvas = Canvas(screen,width=1000,height=500)
canvas.pack()

# Uzantı Seçimi

ayarlar = [
    ".mp3",
    ".mp4"
]

cmb = ttk.Combobox(screen,value = ayarlar,width=10)

canvas.create_window(850,300,window=cmb)

yt_logo = PhotoImage(file= "youtube.png")

canvas.create_image(250,80,image=yt_logo)

ext_label = Label(screen,text="Uzantı Seçiniz",font=("Helvetica",12,BOLD),fg="black")

canvas.create_window(700,300,window=ext_label)


# Link Girilen Alan

link_field = Entry(screen,width=50)
link_label = Label(screen,text="Linki Giriniz",font=("Helvetica",12,BOLD),fg="#780b0b")


canvas.create_window(250,175,window=link_label)
canvas.create_window(250,220,window=link_field)

# İndirilecek Konumun Çekildiği Alan

path_label_text = Label(screen,text="İndirilecek Konumu Seçiniz",font=("Helvetica",12,BOLD),fg="#780b0b")
canvas.create_window(250,250,window=path_label_text)

path_label = Label(screen,text="",font=("Helvetica",10,BOLD),fg="#3e7804")
path_button = Button(screen,text="Konum Seçiniz",command=select_directory,fg="white",bg="#780b0b",font=("Helvetica",10))

canvas.create_window(250,290,window=path_label)
canvas.create_window(250,340,window=path_button)

# İndirme Butonu

download_button = Button(screen,text="İndir",command=download_mp3,fg="white",bg="#780b0b",font=("Helvetica",15))
canvas.create_window(700,360,window=download_button)

# İndiriliyor Bilgisi 

download_label = Label(screen,text="",font=("Helvetica",13,BOLD),fg="black")
canvas.create_window(850,360,window=download_label)

# Video Bilgileri

title_label_1 = Label(screen,text="Video Başlığı",font=("Helvetica",12,BOLD),fg="#780b0b")
title_label_2 = Label(screen,text="",font=("Helvetica",10,BOLD),fg="#3e7804")

canvas.create_window(700,50,window=title_label_1)
canvas.create_window(700,80,window=title_label_2)

author_label_1 = Label(screen,text="Video Sahibi",font=("Helvetica",12,BOLD),fg="#780b0b")
author_label_2 = Label(screen,text="",font=("Helvetica",10,BOLD),fg="#3e7804")

canvas.create_window(700,110,window=author_label_1)
canvas.create_window(700,140,window=author_label_2)

view_label_1 = Label(screen,text="Görüntülenme Sayısı",font=("Helvetica",12,BOLD),fg="#780b0b")
view_label_2 = Label(screen,text="",font=("Helvetica",10,BOLD),fg="#3e7804")

canvas.create_window(700,170,window=view_label_1)
canvas.create_window(700,200,window=view_label_2)

len_label_1 = Label(screen,text="Video Uzunluğu",font=("Helvetica",12,BOLD),fg="#780b0b")
len_label_2 = Label(screen,text="",font=("Helvetica",10,BOLD),fg="#3e7804")

canvas.create_window(700,230,window=len_label_1)
canvas.create_window(700,260,window=len_label_2)

# Video Bilgilerini Getiren Buton

info_button = Button(screen,text="Kontrol Et",command=video_info,fg="white",bg="#780b0b",font=("Helvetica",10))
canvas.create_window(450,220,window=info_button)



# Künye Alanı

kusha_logo = PhotoImage(file="kusha.png")

kusha_label = Label(image=kusha_logo)
kusha_label.place(x=30, y= 420)

label14 = Label(text="Kusha",font=("Helvetica",13,BOLD),fg="black")
label14.place(x=120, y=420)

label15 = Label(text="Engineering",font=("Helvetica",13,BOLD),fg="black")
label15.place(x=120, y=450)

label16 = Label(text="kusha-berke@hotmail.com",font=("Helvetica",10,BOLD),fg="#780b0b")
label16.place(x=800, y=445)

label17 = Label(text="İletişim:",font=("Helvetica",10,BOLD),fg="black")
label17.place(x=855, y=420)

label19 = Label(text="www.kushaengineering.com",font=("Helvetica",11,BOLD),fg="black")
label19.place(x=780, y=470)

screen.mainloop()




