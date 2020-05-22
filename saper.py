import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from PIL import ImageTk, Image
import random

#Klasy obsługujące walidacje wprowadzanych danych
class Error(Exception):
    pass

class ZlyRozmiar(Error):
    def __str__(self):
        messagebox.showinfo("Blad",'Wielkośc planszy musi być wieksza od 2 i mniejsza lub równa 15',)
class ZlyIloscMin(Error):
    def __str__(self):
        messagebox.showinfo("Blad",'Ilość min musi być mniejsza od długości i szerokośc planszy -1 oraz wieksza od zera',)        
class BrakDanych(Error):   
    def __str__(self):
        messagebox.showinfo("Blad",'Podano złe dane ',)   



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


# Popieranie danych z okna startowego,walidacja wprowadzonych danych startowych oraz wywołanie okna gry
def getvalue_start():
    try:     
        m=input_m.get()
        n=input_n.get()
        l_min=input_min.get()
    
        m_m=int(m)
        n_n=int(n)
        l_mine=int(l_min)
    except ValueError:
        raise BrakDanych()
    if(m_m<=2 or n_n<=2 or m_m>15 or n_n>15):
        raise ZlyRozmiar()
    if(l_mine>m_m*n_n-1 or l_mine<1):
        raise ZlyIloscMin()
    else:
        start_window.destroy()
        game_window(m_m,n_n,l_mine)
       




#przycisk rozpoczynający gre po wprowadzeniu danych 
b_start=Button(start_window,text="Graj",width='20',height='5',command=getvalue_start)
b_start.grid(column=0, row=8)

m=input_m.get()
n=input_n.get()
l_min=input_min.get()
start_window.mainloop()
