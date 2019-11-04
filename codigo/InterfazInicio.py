"""
AVANCE 1 PROYECTO LABS UNAL
AUTORES: Andrés Felipe Ardila
         Jorge Andrés Hernández
         David Santiago Murcia
versión 1.0
"""
import os
import sqlite3  #librería para bases de datos
from tkinter import *   #libreria para crear la interfaz
from tkinter import messagebox


nombreProducto = ""
marcaProducto = ""
modeloProducto =""
codigoProducto =""
disponibilidadProducto = ""
cantidadProductos = 0
tiempoUsoProductos = 0
multas = 0
agregarProductos = False

"""CREACION DE LA VENTANA"""

root = Tk()             #Se crea una ventana
root.title("LABS UNAL")   #se le da titulo a la ventana
root.resizable(0, 0)       # no se permite que se alargue la ventana , con (1,1) se permite alargue vertical y horizontal
root.iconbitmap("../Imagenes/Icono/iconoUnal.ico")        #se busca la imagen del icono
frame = Frame()         # se crea un frame
frame.pack()            # se coloca el frame dentro de la ventana
rol = IntVar()          #variable para almacenar lo que el usuario selecciona como rol( lo selecciona en la interfaz)
frame.config(width="800", height="500", bg="gray")  #se configura el frame ancho, alto y color de fondo


"""FUNCION CODIGO QUE VALIDA DATOS PARA INICIAR SESION"""
#APLICACION DE CICLOS PARA BUSQUEDA EN UNA LISTA
#APLICACION DE CONDICIONALES
#APLICACION OPERADORES ASIGNACIÓN, ARITMETICOS Y LÓGICOS

class Usuarios:   #clase para la creacion de usuarios
    usuario = ""
    contraseña = ""
    nombre =""

    def __init__(self,pUsuario, pContraseña,pNombre):
        self.usuario = pUsuario
        self.contraseña = pContraseña
        self.nombre = pNombre

    def darContraseña(self):
        return self.contraseña
    def darUsuario(self):
        return self.usuario
    def darNombre(self):
        return  self.nombre

class DatosUsuarios:  #Clase para la conexión y manipulación de datos de la base de datps
    conexion = None
    cursor = None

    """cursor.execute("CREATE TABLE ESTUDIANTES(USUARIO VARCHAR(50) PRIMARY KEY, PASSWORD VARCHAR(50), NOMBRE VARCHAR(50))")
    cursor.execute("INSERT INTO ESTUDIANTES VALUES('unal','programacion','predeterminado')")
    conexion.commit()"""

    def conectar(self): #metodo que conecta con la  base de datos
        r = os.path.dirname(__file__)
        source = r.replace('\\', "/") + "/BBDUsuarios"
        self.conexion = sqlite3.connect(source)
        self.cursor = self.conexion.cursor()

    def agregarUsuario(self,usuario): #metodo que agrega un usuario a la base de datos

        self.usuario = usuario.darUsuario()
        self.password = usuario.darContraseña()
        self.nombre = usuario.darNombre()
        self.expresion = str("INSERT INTO ESTUDIANTES VALUES('"+ self.usuario+"','"+self.password+"','"+self.nombre+"')")
        self.cursor.execute(self.expresion)
        self.conexion.commit()

    def quitarUsuario(self,usuario): #metodo que quita el usuario dado de la base de datos
        self.usuario = usuario.darUsuario()
        self.cursor.execute("DELETE FROM ESTUDIANTES WHERE USUARIO ='"+self.usuario+"'")
        self.conexion.commit()

    def validarContraseña(self,pUsuario, contraseña): #metodo que valida si el usuario y la contraseña coinciden con los exixtentes en la base de datos
                                                        #True si coincide, False si no
        self.retorno = None
        try:  #se captura una excepción en caso de que pUsuario no exista en la base de datos
            self.cursor.execute("SELECT * FROM ESTUDIANTES WHERE USUARIO = '" + pUsuario + "'") #selecciona toda la fila con los datos de pUsuario
            self.estudiante = self.cursor.fetchall()  #convierte en una lista con un elemento tupla la fila anterior- eje: [(e,l,e,m,e,n,t)]
            self.estudianteTupla = self.estudiante[0]  #de la anterior lista, selecciona elemento 0 que es la tupla
            if self.estudianteTupla[1]== contraseña:    #en la tupla se busca la contraseña que por el orden ingresado esta en 1 y se verifica si es igual a la dad como parametro
                self.retorno = True  #si coincide se retorna True
            else:
                self.retorno = False
        except:
            self.retorno = False   #retorna falso si se lanza el error por no existir el usuario


        return self.retorno



def inicioSesion():   # funcion que dice si se inicio o no sesion(comprueba usuario y contraseña)

        if rol.get() == 1:    # si el rol seleccionado es 1(para estudiantes) se ejecuta
            usuario = usuarioEntry.get()   #se obtiene lo que se introdujo en la casilla de usuario en la interfaz
            contraseña = passEntry.get()   #se obtiene lo que se introdujo en la casilla de contraseña en la interfaz
            inicio = False  # se inicializa variable el falso
            contador = 0       # el contador va a subir +1 cada ver que se itere
            for i in listaUsuarios:     # recorre cada elemento de de la lista con i
                if i == usuario:        # comprueba si algun elemento de la lista es igual a lo que se introdujo en la casilla
                    if listaContraseñas[contador] == contraseña: #comprueba si la contraseña introducida esta en la lista en la posicion que dice el contador
                        inicio = True                   #si coincide inicio cambia de false a true
                contador+=1  #aumenta el contador en cada iteracion

            if inicio:   # si inicio es verdadero se ejecuta(si es verdadero significa que coinciden los datos)
                messagebox.showinfo("Info", "Se inició sesión correctamente")  #funcion que manda una alerta con un mensaje
            else:
                messagebox.showinfo("Info", "Usuario o contraseña incorrectos")


        elif rol.get() == 2:  #si el rol es 2 (para administrador ) se ejecuta

            #comprueba si lo que se introdujo en las casillas es igual a user y pass predeterminado para el administrador
            if usuarioEntry.get() == _USUARIO_ADMIN and passEntry.get() == _PASS_ADMIN:
                messagebox.showinfo("Info", "Se inició sesión correctamente como ADMINISTRADOR") #alerta con mensaje
            else:
                messagebox.showinfo("Info", "Usuario o contraseña de ADMINISTRADOR incorrectos")

        else: # se muestra si no se selecciona el rol
            messagebox.showinfo("Info", "Seleccione un Rol")



"""CREACION DE WIDGETS DE LA INTERFAZ"""

usuarioLabel = Label(frame, text="Usuario:")    # se crea una label(para colocar texto o imagenes) y se coloca en el frame
usuarioLabel.config(font=("Berlin Sans FB", 18), bg="gray", fg="white")  #se configura fuente, bg color fondo y fg color letra
usuarioLabel.grid(row=3, column=1, padx=20, pady=20, sticky="e")  #se ubica en una grilla creada en la interfaz en fila 3 columna 1
                                                                  #padx y y son para espaciado entre el cudrado de grilla

usuarioEntry = Entry(frame)     #crea un entry(caja para colocar texto) y se coloca en el frame
usuarioEntry.config(justify="center", fg="#7CD325", font=("Berlin Sans FB", 15)) #Se configura  justify es para justiificar el texto
usuarioEntry.grid(row=3, column=2, padx=10, pady=20, sticky="w")  #se ubica en grilla

passLabel = Label(frame, text="Contraseña:")
passLabel.config(bg="gray", fg="white", font=("Berlin Sans FB", 18))
passLabel.grid(row=4, column=1, padx=10, pady=20, sticky="e")

passEntry = Entry(frame)
passEntry.config(justify="center", show="*", fg="#7CD325", font=("Berlin Sans FB", 15))
passEntry.grid(row=4, column=2, padx=10, pady=20, sticky="w")

logoUnal = PhotoImage(file="../Imagenes/Logos/logo.png") #busca una imagen en la ruta dada y la almacena en logoUnal
labelImagen1 = Label(frame, image=logoUnal)  #Se crea un label y se le dice que va a contener la imagen logoUnal
labelImagen1.config(bg="White")
labelImagen1.grid(row=1, column=1)

demoUnal = PhotoImage(file="../Imagenes/Logos/demo.png")
labelImagen2 = Label(frame, image=demoUnal)
labelImagen2.config(bg="White")
labelImagen2.grid(row=1, column=2)

rolLabel = Label(frame, text="Seleccione su rol: ")
rolLabel.config(bg="gray", fg="white", font=("Berlin Sans FB", 18))
rolLabel.grid(row=5, column=1, padx=20, pady=20, sticky="e")

radioEstudiante = Radiobutton(frame, text="Estudiante", variable = rol, value = 1) #se crea radiobutton(el circulo para seleccionar rol)
radioEstudiante.config(bg="gray", font=("Berlin Sans FB", 15), activebackground="gray",
                               activeforeground="#7CD325", fg ="#7CD325")
radioEstudiante.grid(row=5, column=2, sticky="w")

radioAdministrador = Radiobutton(frame, text="Administrador", variable = rol, value = 2)
radioAdministrador.config(bg="gray",activebackground="gray", activeforeground="#7CD325",
                                  font=("Berlin Sans FB", 15), fg = "#7CD325")
radioAdministrador.grid(row=6, column=2, sticky="w")

inicioButton = Button(frame, text="Iniciar Sesión", width=20, height=1, activeforeground="#96D646",  #se crea un boton, se le configura el texto, tamaño y color
                              activebackground="white", command=inicioSesion)    # command es para que llame a la funcion cuando se presione el boton
inicioButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15), fg="white") #se configura el relieve colore y fuente
inicioButton.grid(row=7, column=1, columnspan=2, pady=20)# se coloca en la grilla o tabla

root.mainloop()  #debe colocarse para que la interfaz se mantenga en ejecucion y no se cierre


"""usuario1 =Usuarios("jhernandezga","unal","Jorge Hernandez")
data = DatosUsuarios()
data.conectar()
data.agregarUsuario(usuario1)"""
#data.quitarUsuario(usuario1)









