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
_USUARIO_ADMIN = "admin"
_PASS_ADMIN = "programacion"
rol = 0
usuario = ""
contraseña = ""

root = Tk()  # Se crea una ventana
root.title("LABS UNAL")  # se le da titulo a la ventana
root.resizable(0, 0)  # no se permite que se alargue la ventana , con (1,1) se permite alargue vertical y horizontal
root.iconbitmap("../Imagenes/Icono/iconoUnal.ico")  # se busca la imagen del icono
logoUnal = PhotoImage(file="../Imagenes/Logos/logo.png")
demoUnal = PhotoImage(file="../Imagenes/Logos/demo.png")
fuente = PhotoImage(file="../Imagenes/ImagenEquipos/fuente.png")
generador = PhotoImage(file="../Imagenes/ImagenEquipos/generador.png")
osciloscopio = PhotoImage(file="../Imagenes/ImagenEquipos/osciloscopio.png")
caiman = PhotoImage(file="../Imagenes/ImagenEquipos/caiman.png")
multimetro = PhotoImage(file="../Imagenes/ImagenEquipos/multimetro.png")
puntas = PhotoImage(file="../Imagenes/ImagenEquipos/puntas.png")


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
class Equipos:
    marca = ""
    modelo = ""
    nombre = ""
    cantidad = 0
    def __init__(self,pNombre, pMarca,pModelo,pCantidad):
        self.marca = pMarca
        self.modelo = pModelo
        self.nombre = pNombre
        self.cantidad = pCantidad

    def darNombre(self):
        return self.nombre
    def darModelo(self):
        return self.modelo
    def darMarca(self):
        return self.marca
    def darCantidad(self):
        return self.cantidad
class Laboratorio:

    equipos = []
    lab = 0
    a = Equipos("Multimetro", "fluke", "87-v", 20)
    b = Equipos("Osciloscopio", "Rigol", "DS1054", 15)
    c = Equipos("Sonda Osciloscopio", "Genérico 10X", "P4060", 25)
    d = Equipos("Generador de Señales", "Electroni", "FY3224S", 15)
    e = Equipos("Cable Banana-Caiman", "Genérico", "NA", 100)
    f = Equipos("Fuente", "Genérico", "NA", 100)
    equipos.append(a)
    equipos.append(b)
    equipos.append(c)
    equipos.append(d)
    equipos.append(e)
    equipos.append(f)
    nombre1 = ""
    def __init__(self, pNombre, lab):
        self.nombrel = pNombre
        self.lab = lab

    def darNombre(self):
        return self.nombrel
    def darCantidadPorNombre(self,pNombre):
        xCantidad = 0
        for i in self.equipos:
             if i.darNombre() == pNombre and i != None:
                xCantidad = i.darCantidad()
        return xCantidad
    def reservar(self,pNombre):
        reserva = False
        for i in self.equipos:
            if i.darNombre() == pNombre and i.darCantidad() > 0 and i != None:
                i.darCantidad -= 1
                reserva = True
        return reserva
    def devolver(self,pNombre):
        devuelve = False
        for i in self.equipos:
            if i.darNombre() == pNombre and i != None:
                i.darCantidad += 1
                devuelve = True
        return devuelve
class DatosUsuarios:  #Clase para la conexión y manipulación de datos de la base de datps
    conexion = None
    cursor = None

    def conectar(self): #metodo que conecta con la  base de datos
        r = os.path.dirname(__file__)
        source = r.replace('\\', "/") + "/Base Datos Estudiantes"
        self.conexion = sqlite3.connect(source)
        self.cursor = self.conexion.cursor()

    def agregarUsuario(self,usuario): #metodo que agrega un usuario a la base de datos
        self.conectar()
        self.usuario = usuario.darUsuario()
        self.password = usuario.darContraseña()
        self.nombre = usuario.darNombre()
        self.expresion = str("INSERT INTO ESTUDIANTES VALUES('"+ self.usuario+"','"+self.password+"','"+self.nombre+"')")
        self.cursor.execute(self.expresion)
        self.conexion.commit()
        self.conexion.close()

    def quitarUsuario(self,usuario): #metodo que quita el usuario dado de la base de datos
        self.conectar()
        self.usuario = usuario.darUsuario()
        self.cursor.execute("DELETE FROM ESTUDIANTES WHERE USUARIO ='"+self.usuario+"'")
        self.conexion.commit()
        self.conexion.close()

    def validarContraseña(self,pUsuario, pContraseña): #metodo que valida si el usuario y la contraseña coinciden con los exixtentes en la base de datos
                                                        #True si coincide, False si no
        self.retorno = None
        try:  #se captura una excepción en caso de que pUsuario no exista en la base de datos
            self.conectar()
            self.cursor.execute("SELECT * FROM ESTUDIANTES WHERE USUARIO = '" + pUsuario + "'") #selecciona toda la fila con los datos de pUsuario
            self.estudiante = self.cursor.fetchall()  #convierte en una lista con un elemento tupla la fila anterior- eje: [(e,l,e,m,e,n,t)]
            self.estudianteTupla = self.estudiante[0]  #de la anterior lista, selecciona elemento 0 que es la tupla
            if self.estudianteTupla[1]== pContraseña:    #en la tupla se busca la contraseña que por el orden ingresado esta en 1 y se verifica si es igual a la dad como parametro
                self.retorno = True  #si coincide se retorna True
            else:
                self.retorno = False
            self.conexion.close()
        except:
            self.retorno = False   #retorna falso si se lanza el error por no existir el usuario


        return self.retorno

labElectronica = Laboratorio("Laboratiorio de Ingeniería Eléctrica y Electrónica",1)

def ventanaUsuario3():

    frame = Frame()
    frame.pack()

    def anterior():
        ventanaUsuario2()
        frame.destroy()
    anteriorButton = Button(frame, text="Anterior", width=20, height=1, activeforeground="#96D646",
                             activebackground="white",
                             command=anterior)  # command es para que llame a la funcion cuando se presione el boton
    anteriorButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    anteriorButton.grid(row=7, column=1, columnspan=2, pady=20)  # se coloca en la grilla o tabla
    labelImagen1 = Label(frame, image=demoUnal)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelImagen1.config(bg="White")
    labelImagen1.grid(row=1, column=1)

def ventanaUsuario2():

    frame = Frame()
    frame.pack()
    labElectronica.darNombre()
    def siguiente():
        ventanaUsuario3()
        frame.destroy()

    siguienteButton = Button(frame, text="Siguiente1", width=20, height=1, activeforeground="#96D646",
                          activebackground="white",
                          command=siguiente)  # command es para que llame a la funcion cuando se presione el boton
    siguienteButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                        fg="white")  # se configura el relieve colore y fuente
    siguienteButton.grid(row=7, column=2, columnspan=2, pady=20)  # se coloca en la grilla o tabla

    labelgenerador = Label(frame, image= generador ) # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelgenerador.config(bg="White")
    labelgenerador.grid(row=2, column=1)

    buttonGenerador = Button(frame, text="Añadir", width=20, height=1, activeforeground="#96D646",
                             activebackground="white")  # command es para que llame a la funcion cuando se presione el boton
    buttonGenerador.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonGenerador.grid(row=3, column=1, pady=5)  # se coloca en la grilla o tabla

    labelOsciloscopio = Label(frame, image=osciloscopio) # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelOsciloscopio.config(bg="White")
    labelOsciloscopio.grid(row=2, column=2)

    buttonOsciloscopio = Button(frame, text="Añadir", width=20, height=1, activeforeground="#96D646",
                             activebackground="white")  # command es para que llame a la funcion cuando se presione el boton
    buttonOsciloscopio.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonOsciloscopio.grid(row=3, column=2, pady=5,padx = 10)  # se coloca en la grilla o tabla


    labelFuente = Label(frame, image=fuente)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelFuente.config(bg="White")
    labelFuente.grid(row=2, column=3)

    buttonFuente = Button(frame, text="Añadir", width=20, height=1, activeforeground="#96D646",
                             activebackground="white")  # command es para que llame a la funcion cuando se presione el boton
    buttonFuente.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonFuente.grid(row=3, column=3,  pady=5,padx =10)  # se coloca en la grilla o tabla

    labelCaiman = Label(frame, image=caiman)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelCaiman.config(bg="White")
    labelCaiman.grid(row=5, column=1)

    buttonCaiman = Button(frame, text="Añadir", width=20, height=1, activeforeground="#96D646",
                             activebackground="white")  # command es para que llame a la funcion cuando se presione el boton
    buttonCaiman.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonCaiman.grid(row=6, column=1,  pady=5,padx =10)  # se coloca en la grilla o tabla

    labelPuntas = Label(frame, image=puntas)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelPuntas.config(bg="White")
    labelPuntas.grid(row=5, column=2)

    buttonPuntas = Button(frame, text="Añadir", width=20, height=1, activeforeground="#96D646",
                             activebackground="white")  # command es para que llame a la funcion cuando se presione el boton
    buttonPuntas.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonPuntas.grid(row=6, column=2, pady=5)  # se coloca en la grilla o tabla

    labelMultimetro = Label(frame, image= multimetro)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelMultimetro.config(bg="White")
    labelMultimetro.grid(row=5, column=3)

    buttonMultímetro = Button(frame, text="Añadir", width=20, height=1, activeforeground="#96D646",
                             activebackground="white")  # command es para que llame a la funcion cuando se presione el boton
    buttonMultímetro.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonMultímetro.grid(row=6, column=3, pady=5)  # se coloca en la grilla o tabla

def ventanaInicio(logo, logo2):
    def inicioSesion():

        usuario = usuarioEntry.get()
        contraseña = passEntry.get()
        rol = rola.get()

        if rol == 1:  # si el rol seleccionado es 1(para estudiantes) se ejecuta

            valida = DatosUsuarios()
            validar = valida.validarContraseña(usuario, contraseña)
            if validar:  # si inicio es verdadero se ejecuta(si es verdadero significa que coinciden los datos)
                ventanaUsuario2()
                frame.destroy()
            else:
                messagebox.showinfo("Info", "Usuario o contraseña incorrectos")

        elif rol == 2:  # si el rol es 2 (para administrador ) se ejecuta

            # comprueba si lo que se introdujo en las casillas es igual a user y pass predeterminado para el administrador
            if usuario == _USUARIO_ADMIN and contraseña == _PASS_ADMIN:
                messagebox.showinfo("Info", "Se inició sesión correctamente como ADMINISTRADOR")  # alerta con mensaje
            else:
                messagebox.showinfo("Info", "Usuario o contraseña de ADMINISTRADOR incorrectos")

        else:  # se muestra si no se selecciona el rol
            messagebox.showinfo("Info", "Seleccione un Rol")

    frame = Frame()  # se crea un frame

    frame.pack()  # se coloca el frame dentro de la ventana
    rola = IntVar()  # variable para almacenar lo que el usuario selecciona como rol( lo selecciona en la interfaz)
    frame.config(width="800", height="500", bg="gray")  # se configura el frame ancho, alto y color de fondo

    usuarioLabel = Label(frame, text="Usuario:")    # se crea una label(para colocar texto o imagenes) y se coloca en el frame
    usuarioLabel.config(font=("Berlin Sans FB", 18), bg="gray", fg="white")  #se configura fuente, bg color fondo y fg color letra
    usuarioLabel.grid(row=3, column=1, padx=20, pady=20, sticky="e")  #se ubica en una grilla creada en la interfaz en fila 3 columna 1                                                                      #padx y y son para espaciado entre el cudrado de grilla

    usuarioEntry = Entry(frame)     #crea un entry(caja para colocar texto) y se coloca en el frame
    usuarioEntry.config(justify="center", fg="#7CD325", font=("Berlin Sans FB", 15)) #Se configura  justify es para justiificar el texto
    usuarioEntry.grid(row=3, column=2, padx=10, pady=20, sticky="w")  #se ubica en grilla

    passLabel = Label(frame, text="Contraseña:")
    passLabel.config(bg="gray", fg="white", font=("Berlin Sans FB", 18))
    passLabel.grid(row=4, column=1, padx=10, pady=20, sticky="e")

    passEntry = Entry(frame)
    passEntry.config(justify="center", show="*", fg="#7CD325", font=("Berlin Sans FB", 15))
    passEntry.grid(row=4, column=2, padx=10, pady=20, sticky="w")

     #busca una imagen en la ruta dada y la almacena en logoUnal
    labelImagen1 = Label(frame, image=logo)  #Se crea un label y se le dice que va a contener la imagen logoUnal
    labelImagen1.config(bg="White")
    labelImagen1.grid(row=1, column=1)

    labelImagen2 = Label(frame, image=logo2)
    labelImagen2.config(bg="White")
    labelImagen2.grid(row=1, column=2)

    rolLabel = Label(frame, text="Seleccione su rol: ")
    rolLabel.config(bg="gray", fg="white", font=("Berlin Sans FB", 18))
    rolLabel.grid(row=5, column=1, padx=20, pady=20, sticky="e")

    radioEstudiante = Radiobutton(frame, text="Estudiante", variable = rola, value = 1) #se crea radiobutton(el circulo para seleccionar rol)
    radioEstudiante.config(bg="gray", font=("Berlin Sans FB", 15), activebackground="gray",
                                       activeforeground="#7CD325", fg ="#7CD325")
    radioEstudiante.grid(row=5, column=2, sticky="w")

    radioAdministrador = Radiobutton(frame, text="Administrador", variable = rola, value = 2)
    radioAdministrador.config(bg="gray",activebackground="gray", activeforeground="#7CD325",
                                          font=("Berlin Sans FB", 15), fg = "#7CD325")
    radioAdministrador.grid(row=6, column=2, sticky="w")

    inicioButton = Button(frame, text="Iniciar Sesión", width=20, height=1, activeforeground="#96D646",  #se crea un boton, se le configura el texto, tamaño y color
                                      activebackground="white", command=inicioSesion)    # command es para que llame a la funcion cuando se presione el boton
    inicioButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15), fg="white") #se configura el relieve colore y fuente
    inicioButton.grid(row=7, column=1, columnspan=2, pady=20)# se coloca en la grilla o tabla


ventanaInicio(logoUnal, demoUnal)
root.mainloop()  #debe colocarse para que la interfaz se mantenga en ejecucion y no se cierre












