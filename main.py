from tkinter import mainloop
from tkinter import messagebox
import customtkinter
from customtkinter import *

customtkinter.set_appearance_mode("dark")

def ktmi():
    k = int(entr.get())
    mi = k * 0.621371
    messagebox.showinfo("result",message=f"{k} kilometres is equal to {mi} miles.")

def mitk():
    mi = int(entr.get())
    k = mi / 0.621371
    messagebox.showinfo("result",message=f"{mi} miles is equal to {k} kilometres.")

def mtf():
    m = int(entr.get())
    f = m * 3.28084
    messagebox.showinfo("result",message=f"{m} metres is equal to {f} feet.")

def ftm():
    f = int(entr.get())
    m = f / 3.28084
    messagebox.showinfo("result",message=f"{f} feet is equal to {m} metres.")

def itc():
    i = int(entr.get())
    c = i * 2.54
    messagebox.showinfo("result",message=f"{i} inches is equal to {c} centimetres.")

def cti():
    c = int(entr.get())
    i = c / 2.54
    messagebox.showinfo("result",message=f"{c} centimetres is equal to {i} inches.")

main = CTk()
main = CTk(fg_color= "#6fefef")
main.geometry("500x500")
main.title("Unit Converter")


lbl = customtkinter.CTkLabel( main,
                             text="Unit Converter",
                             font= ("Helvetica",18),
                             width=140,
                             height=35,
                             bg_color="#b2faf3",
                             fg_color=("black","black"),
                             corner_radius=10)
lbl.pack(pady=18)

entr = customtkinter.CTkEntry(main,
                              placeholder_text="Enter numerical value",
                              width=145
                              )
entr.pack(pady=18)

lngth = customtkinter.CTkScrollableFrame(main,
                                         orientation="vertical",
                                         label_text="Length converter",
                                         label_fg_color="#5ad6ec",
                                         label_text_color="black")
lngth.pack(pady=18)

buttons1= [
    ("km to mile", ktmi),
    ("mile to km", mitk),
    ("m to ft", mtf),
    ("ft to m", ftm),
    ("in to cm", itc),
    ("cm to in", cti),
]

for text, command in buttons1:
    customtkinter.CTkButton(lngth, text=text, command=command).pack(pady=10)

main.mainloop()