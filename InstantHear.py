import pyttsx3
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Instant Hear")
root.iconbitmap("")#Type your file name


text=Entry(root,width=50,bg="white",fg="black",font=("arial","16"))
text.pack(padx=10,pady=20)

def Hear():
    pyttsx3.speak(text.get())
    

x = tk.StringVar()
b1 = tk.Button(root,text="Hear",fg="black",bg="lightgrey",command=Hear).pack()

root.mainloop()
