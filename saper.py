import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
import random

#Tworzenie okna startowego"
start_window=Tk()
start_window.title("Saper")
start_window.geometry("350x400")

lgame=Label(start_window,text="Saper",font=("Arial Bold", 30))
lgame.grid(column=0, row=0)
#Tworzenie podstawowego formularza zawierajacego dane o wielkośc pola i ilosci min
l_input_m=Label(start_window,text="Podaj szerokość planszy",font=("Arial Bold", 20))
l_input_n=Label(start_window,text="Podaj wyskość planszy",font=("Arial Bold", 20))
l_input_miny=Label(start_window,text="Podaj liczbe min",font=("Arial Bold", 20))
l_input_m.grid(column=0, row=2)
l_input_n.grid(column=0, row=4)
l_input_miny.grid(column=0, row=6)
input_m=Entry(start_window,width='10')
input_n=Entry(start_window,width='10')
input_min=Entry(start_window,width='10')
input_m.grid(column=0, row=3)
input_n.grid(column=0, row=5)
input_min.grid(column=0, row=7)




#przycisk rozpoczynający gre po wprowadzeniu danych 
b_start=Button(start_window,text="Graj",width='20',height='5',command=getvalue_start)
b_start.grid(column=0, row=8)

m=input_m.get()
n=input_n.get()
l_min=input_min.get()
start_window.mainloop()
