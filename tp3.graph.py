import tkinter as tk
from tkinter import ttk
import ppt_back as back

#back.derrotas
juego = back.PPT()

ventana = tk.Tk()
ventana.title("Juego de piedra-papel-tijera")
ventana.config(width=400, height=300)
etiqueta_principal = ttk.Label(text="Eligí tu jugada")
etiqueta_principal.place(x=20, y=20)
str_resultado = tk.StringVar()

def elijo_piedra():
    resul = juego.jugar_con_piedra()
    print("Resultado",resul)
    str_resultado.set(resul)
def elijo_papel():
    resul = juego.jugar_con_papel()
    print("Resultado",resul)
    str_resultado.set(resul)
def elijo_tijera():
    resul = juego.jugar_con_tijera()
    print("Resultado",resul)
    str_resultado.set(resul)

#x= 0

#def tijera():
#    global x
#    x+=1
#    str_resultado.set(f"Hola {x}")
str_resultado.set("")

text_resultado = ttk.Label(ventana, textvariable = str_resultado)
text_resultado.place(x=20,y=60)
boton_piedra = ttk.Button(text="Piedra", command=elijo_piedra)
boton_piedra.place(x=20, y=160)
boton_papel = ttk.Button(text="Papel", command=elijo_papel)
boton_papel.place(x=100, y=160)
boton_tijera = ttk.Button(text="Tijera", command=elijo_tijera)



boton_tijera.place(x=180, y=160)


ventana.mainloop()