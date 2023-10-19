            
from tkinter import *
from tkinter import messagebox
import random
import tkinter as tk
from PIL import Image, ImageTk

def cerrar_ventana():
    root.destroy()

def no():
    messagebox.showinfo(" ", "Ya sabia")
    cerrar_ventana()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 500), y=random.randint(0, 500))

root = Tk()
imagen = Image.open("C:\\Users\\user\\Desktop\\imagene\\La roca.png.jpg")
#ancho = 
##largo = 
#imagen_redimezionada = imagen.resize(ancho, largo), Image.ANTIALIAS
imagen_tk = ImageTk.PhotoImage(imagen)
label_imagen = tk.Label(root, image=imagen_tk)
label_imagen.pack()
root.geometry('600x600')
root.title('survey')
root.resizable(width=False, height=False)
root['bg'] = 'white'
label = Label(root, text=' ¿Te Gusta La Picha?', font='Arial 20 bold', bg='white').pack()
btnYes = Button(root, text='No', font='Arial 20 bold')
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)
btnNo = Button(root, text='Si', font='Arial 20 bold', command=no).place(x=350, y=100)
root.mainloop()