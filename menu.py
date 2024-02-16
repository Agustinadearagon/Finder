import tkinter as tk
import subprocess

def ejecutar_sirla():
    try:
        subprocess.run(["python", "media/lbsnredes/COMPARTIDO/HERRAMIENTAS/sirla.py"])
    except FileNotFoundError:
        print("El archivo sirla.py no se encontró en la ruta especificada.")

def ejecutar_hacha():
    try:
        subprocess.run(["python", "media/lbsnredes/COMPARTIDO/HERRAMIENTAS/hacha.py"])
    except FileNotFoundError:
        print("El archivo hacha.py no se encontró en la ruta especificada.")

def ejecutar_conversor():
    try:
        subprocess.run(["python", "media/lbsnredes/COMPARTIDO/HERRAMIENTAS/conversor.py"])
    except FileNotFoundError:
        print("El archivo conversor.py no se encontró en la ruta especificada.")

def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Menú de Herramientas")
ventana.geometry("800x600")  # Establece el tamaño de la ventana (ancho x alto)

btn_sirla = tk.Button(ventana, text="Sirla", command=ejecutar_sirla, height=4, width=20)
btn_hacha = tk.Button(ventana, text="Hacha", command=ejecutar_hacha, height=4, width=20)
btn_conversor = tk.Button(ventana, text="Conversor", command=ejecutar_conversor, height=4, width=20)
btn_salir = tk.Button(ventana, text="Salir", command=salir, height=4, width=20)

btn_sirla.pack(pady=10)
btn_hacha.pack(pady=10)
btn_conversor.pack(pady=10)
btn_salir.pack(pady=10)

ventana.mainloop()
