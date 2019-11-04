import os
import sqlite3  #librería para bases de datos
from tkinter import *   #libreria para crear la interfaz
from tkinter import messagebox

conexion = sqlite3.connect("Base Datos Estudiantes")
cursor = conexion.cursor()

#cursor.execute("CREATE TABLE ESTUDIANTES(USUARIO VARCHAR(10) PRIMARY KEY, PASSWORD VARCHAR(10), NOMBRE VARCHAR(10), TIEMPO INTEGER, MULTA INTEGER)")
#cursor.execute("INSERT INTO ESTUDIANTES VALUES('unal','programacion','predeterminado','100',0)")
#conexion.commit()