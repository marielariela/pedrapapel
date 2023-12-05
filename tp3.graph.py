import tkinter as tk
from tkinter import ttk
import tp3_back as back

#back.derrotas
juego = back.PPT()

ventana = tk.Tk()
ventana.title("Juego de Piedra-Papel-Tijera")
ventana.config(width=400, height=300)
etiqueta_principal = ttk.Label(text="Elegí tu jugada.")
etiqueta_principal.place(x=20, y=20)
str_resultado = tk.StringVar()

def elijo_piedra():
    resul = juego.jugar_con_piedra()
    print("Resultado:",resul)
    str_resultado.set(resul)
def elijo_papel():
    resul = juego.jugar_con_papel()
    print("Resultado:",resul)
    str_resultado.set(resul)
def elijo_tijera():
    resul = juego.jugar_con_tijera()
    print("Resultado:",resul)
    str_resultado.set(resul)
def elijo_finalizar():
    juego.finalizar()


#str_resultado.set("")

text_resultado = ttk.Label(ventana, textvariable = str_resultado)
text_resultado.place(x=20,y=60)
boton_piedra = ttk.Button(text="Piedra", command=elijo_piedra)
boton_piedra.place(x=20, y=160)
boton_papel = ttk.Button(text="Papel", command=elijo_papel)
boton_papel.place(x=100, y=160)
boton_tijera = ttk.Button(text="Tijera", command=elijo_tijera)
boton_tijera.place(x=180, y=160)
boton_finalizar = ttk.Button(text="Finalizar", command=elijo_finalizar)
boton_finalizar.place(x=260, y=160)


#agrrego una barra de texto que muestre el historial de resultados en el programa grafico y no en el termina
texto_puntaje=tk.StringVar()
barra_puntaje=tk.Label(ventana, text=texto_puntaje, padx=5, pady=5,justify="center")
altura=ventana.cget("height")
anchura=ventana.cget("width")
barra_puntaje.place(x=anchura/5, y=altura-40)

#funcion que actualiza la barra de puntaje
def actualizar_barra_estado():
    try:
        usuario=juego.puntaje_us
        maquina=juego.puntaje_pc
        texto_estado = f"Puntaje Usuario: {usuario}     |       Puntaje Maquina: {maquina}"
        barra_puntaje.config(text=texto_estado)
        ventana.after(500, actualizar_barra_estado)
    except Exception as e:
        barra_puntaje.config(text=f"Error: {str(e)}")


actualizar_barra_estado()
ventana.mainloop()

