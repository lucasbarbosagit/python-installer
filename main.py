from tkinter import *
import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("green")

splash_screen = customtkinter.CTk()
splash_screen.title("Splash")

w = 208
h = 135

screen_width = splash_screen.winfo_screenwidth()
screen_height = splash_screen.winfo_screenheight()

x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)

splash_screen.geometry("%dx%d+%d+%d" % (w, h, x, y))
splash_screen.title('Instalador de Programas EPF')

splash_screen.wm_iconbitmap(r'C:\Users\lucas.b\Desktop\instaladorepf\img\epf_logo.ico')
splash_screen.resizable(False, False)

app_image = customtkinter.CTkImage(Image.open(r"C:\Users\lucas.b\Desktop\instaladorepf\img\epf_logo_branco.png"), size=(208, 135))
app_image_bt = customtkinter.CTkLabel(master=splash_screen,image=app_image, text="")
app_image_bt.grid(row=0,column=0, sticky=W)

def splash():
 splash_screen.withdraw()
 os.system("python installerepfprogs.py")
 splash_screen.destroy()   

splash_screen.after(3000,splash)

splash_screen.resizable(False, False)
splash_screen.mainloop()