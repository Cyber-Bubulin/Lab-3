from random import sample
import numpy as np
import tkinter as tk
from tkinter import Text
from tkinter import Entry
from tkinter import Button
import re

def clicked():
    n = format(input_entry.get())
    if  (re.search('[a-zA-Zа-яА-ЯёЁ]', n)==None) and  len(n)==3:
        n = int(n)
        a = 'ABCDEFGHIJKLMNOPKRSTUVWXYZ0123456789'
        b = sample(a,5)
        third = n%10
        n = n//10
        second = n%10
        n = n//10
        first = n%10
        result= [*b, '-',*np.roll(b, first)[:4], '-', *np.roll(b, -second)[:3], '-', *np.roll(b, third)[:2]]
        s_result = ' '.join(result).replace(' ', '')
        lbl = tk.Label(window, text=s_result, font=24)
        lbl.pack()
        
    else: 
        lbl = tk.Label(window, text='Неверный формат ввода', font=24)
        lbl.pack()
        

if __name__=="__main__":
    window = tk.Tk()
    window.geometry('800x600')
    bg_img = tk.PhotoImage(file='smeshariki.png')

    window.title("Key Generator")

    lbl_bg = tk.Label(window, image=bg_img)
    lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

    lbl_text = tk.Label(window, text="Введите трёхзначное десятичное число:", font=("Arial", 16))
    lbl_text.pack()

    input_entry = Entry(window)
    input_entry.pack(ipady=15)



    submit_button = Button(window, text="Generate", command=clicked)
    submit_button.pack()

    window.mainloop()