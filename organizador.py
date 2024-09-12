import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organizar_archivos(directorio):
    # Obtener la lista de archivos en el directorio
    archivos = os.listdir(directorio)

    # Crear un diccionario para almacenar los archivos según su extensión
    archivos_por_extension = {}

    # Iterar sobre cada archivo
    for archivo in archivos:
        # Obtener la extensión del archivo
        _, extension = os.path.splitext(archivo)
        # Eliminar el punto de la extensión
        extension = extension[1:]

        # Crear un directorio para la extensión si aún no existe
        if extension not in archivos_por_extension:
            os.makedirs(os.path.join(directorio, extension), exist_ok=True)

        # Mover el archivo al directorio correspondiente
        shutil.move(os.path.join(directorio, archivo), os.path.join(directorio, extension, archivo))

    print("Archivos organizados correctamente.")

def seleccionar_directorio():
    directorio = filedialog.askdirectory()
    if directorio:
        organizar_archivos(directorio)

# Crear la ventana principal
root = tk.Tk()
root.title("Organizador de Archivos")

# Crear un botón para seleccionar el directorio
btn_seleccionar_directorio = tk.Button(root, text="Seleccionar Directorio", command=seleccionar_directorio)
btn_seleccionar_directorio.pack(pady=20)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
