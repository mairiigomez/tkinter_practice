import tkinter as tk

ventana = tk.Tk()
ventana.title("Primer ventana")
# Ancho por alto 
ventana.geometry('380x300')
#color de fondo de la ventana 
ventana.configure(background='dark turquoise')
#etiquetas recibir texto o desplegar 
etiqueta1=tk.Label(ventana,text="Python",bg='red',fg='white')
#etiqueta1.pack(fill=tk.X)
etiqueta1.pack(padx=20, pady=20,side=tk.LEFT)

etiqueta1=tk.Label(ventana,text="Tkinter",bg='pink',fg='white')
#etiqueta1.pack(padx=20,pady=10,ipadx=50,ipady=20)
#etiqueta1.pack(padx=20,pady=50)
etiqueta1.pack(padx=20, pady=20,side=tk.LEFT)

etiqueta1=tk.Label(ventana,text="Aprender",bg='gold',fg='black')
#etiqueta1.pack(side=tk.LEFT)
etiqueta1.pack(padx=20, pady=20,side=tk.LEFT)

ventana.mainloop()