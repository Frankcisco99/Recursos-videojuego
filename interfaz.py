import tkinter 
from tkinter import ttk

ventana = tkinter.Tk()
ventana.title("Codigo errores")
ventana.geometry("300x200")
ventana.resizable(0,0)

texto = ttk.Label(ventana, text="Ingresa el codigo",font= "Calibri 16 bold")
texto.pack(pady=10)

codigo_entry = ttk.Entry(ventana)
codigo_entry.pack()

btn_buscar = ttk.Button(ventana, text="Buscar codigo")
btn_buscar.pack(pady=10)
ventana.mainloop() #todo antes del mainloop