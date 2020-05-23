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

#Głowne okno gry 
def game_window(m,n,l_min):

    x_width=n*52
    y_height=m*42
    
    game_window=Tk()
    game_window.geometry(str(x_width)+"x"+str(y_height))
    game_window.title("SAPER GRA")
#wporwadzanie obrazków na przyciski     
    photo = PhotoImage(file = r"img/pole.png")
    bomb=PhotoImage(file = r"img/bomb1.png")
    jeden=PhotoImage(file = r"img/jeden.png")
    dwa=PhotoImage(file = r"img/dwa.png")
    trzy=PhotoImage(file = r"img/trzy.png")
    cztery=PhotoImage(file = r"img/cztery.png")
    piec=PhotoImage(file = r"img/piec.png")
    szesc=PhotoImage(file = r"img/szesc.png")
    siedem=PhotoImage(file = r"img/siedem.png")
    osiem=PhotoImage(file = r"img/osiem.png")
    block=PhotoImage(file = r"img/block.png")
    flag=PhotoImage(file = r"img/pole_f.png")
    dark_pole=PhotoImage(file = r"img/dark_pole.png")

    tab_l_click=[]


    # funkcjia opisujaca kilkniecie lewym przyciskiem myszki na przycisk 
    def l_click(x,y):
        print("x",x)
        print("y",y)
        tmp_tabg=[]
        tmp_tabg.append(x)
        tmp_tabg.append(y)
        # dodanie do tablicy kilknietych przycisków
        tab_l_click.append(tmp_tabg)
        print(tmp_tabg)   
        if tmp_tabg in list_min:
            print("boom")
            pole[x][y].configure(image=bomb)
            #wyswietlenie informacji o przegranej i zamkniecie gry
            msend=messagebox.showerror(title="Przegrałeś",message="Trafiłeś na mine koniec gry")
            exit()     
        #wywołanie funkcji sprawdzajacej czy w sąsiednich polach jest mina: zwraca liczbe min

        count_mine=count_near_mine(x,y)
        #ustanianie odpowiedniego obrazka dla konkretnego przycisku oraz sprawdzenie czy prycisk nie jest miną
        if(count_mine==1 and tmp_tabg not in list_min):
            pole[x][y].configure(image=jeden)
            

        if(count_mine==2 and tmp_tabg not in list_min):
            pole[x][y].configure(image=dwa)
            
        if(count_mine==3 and tmp_tabg not in list_min):
            pole[x][y].configure(image=trzy)
        if(count_mine==4 and tmp_tabg not in list_min):
            pole[x][y].configure(image=cztery)
        if(count_mine==5 and tmp_tabg not in list_min):
            pole[x][y].configure(image=piec)
        if(count_mine==6 and tmp_tabg not in list_min):
            pole[x][y].configure(image=szesc)
        if(count_mine==7 and tmp_tabg not in list_min):
            pole[x][y].configure(image=siedem)

        if(count_mine==8 and tmp_tabg not in list_min):
            pole[x][y].configure(image=osiem)
            
        if(count_mine==0 and tmp_tabg not in list_min):
            pole[x][y].configure(image=block)
            

            
        print(tab_l_click)    
            

    
    #Funkcja zliczajaca ilosc min do okoła pojedyniczego przycisku
    def count_near_mine(x,y):
        #ilośc bobm w sasi
        suma_min_s=0
        # lewy gorny
        tmp_tab=[]
        tmp_tab.append(x-1)
        tmp_tab.append(y-1)
        if tmp_tab in list_min:
            suma_min_s+=1
            
         #gorny
        tmp_tab=[]
        tmp_tab.append(x)
        tmp_tab.append(y-1)
        if tmp_tab in list_min:
            suma_min_s+=1       
         # prawy gorny
        tmp_tab=[]
        tmp_tab.append(x+1)
        tmp_tab.append(y-1)
        if tmp_tab in list_min:
            suma_min_s+=1
         # lewy 
        tmp_tab=[]
        tmp_tab.append(x-1)
        tmp_tab.append(y)
        if tmp_tab in list_min:
           
            suma_min_s+=1
         # prawy
        tmp_tab=[]
        tmp_tab.append(x+1)
        tmp_tab.append(y)
        if tmp_tab in list_min:
            suma_min_s+=1
            
         # lewy dol
        tmp_tab=[]
        tmp_tab.append(x-1)
        tmp_tab.append(y+1)
        if tmp_tab in list_min:
            suma_min_s+=1
            
         # dol
        tmp_tab=[]
        tmp_tab.append(x)
        tmp_tab.append(y+1)
        if tmp_tab in list_min:
            suma_min_s+=1
            
         # prawy dol
        tmp_tab=[]
        tmp_tab.append(x+1)
        tmp_tab.append(y+1)
        if tmp_tab in list_min:
            suma_min_s+=1
            
        print("suma sąsiednich min =",suma_min_s)
        return suma_min_s
    
         


    pole=[]
   
    
    #losowanie pozycji min
    list_min=[]
    tmp_l_min=l_min
    while(tmp_l_min!=0):
        min=[]
        x_random_min=random.randint(0,m-1)
        y_random_min=random.randint(0,n-1)
        min.append(x_random_min)
        min.append(y_random_min)
        #sprawdzenie czy nie wylosowaliśmy 2 razy tej samej pozycji
        if min not in list_min:
            list_min.append(min)
            tmp_l_min-=1
    
#generowanie siatki przycisków    
    for x in range(m):
        pole.append([])
        
        for y in range(n):
            
            pole[x].append(Button(game_window,width='45',height='35',image=photo,command=lambda x=x, y=y: l_click(x,y)))
            
            pole[x][y].grid(row=x, column=y)
    

    game_window.mainloop()

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
