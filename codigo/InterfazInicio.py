"""
AVANCE 1 PROYECTO LABS UNAL
AUTORES: Andrés Felipe Ardila
         Jorge Andrés Hernández
         David Santiago Murcia
versión 2.0
"""
from tkinter import *   #libreria para crear la interfaz
from tkinter import messagebox
import time as tm
from datetime import  datetime
from math import fabs
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from random import randint

multas = 0
_USUARIO_ADMIN = "admin"
_PASS_ADMIN = "programacion"
rol = 0
usuario = ""
contraseña = ""
now = datetime.now()

root = Tk()  # Se crea una ventana
root.title("LABS UNAL")  # se le da titulo a la ventana
root.resizable(0, 0)  # no se permite que se alargue la ventana , con (1,1) se permite alargue vertical y horizontal
root.iconbitmap("../Imagenes/Icono/iconoUnal.ico")  # se busca la imagen del icono
logoUnal = PhotoImage(file="../Imagenes/Logos/logo.png")
demoUnal = PhotoImage(file="../Imagenes/Logos/demo.png")
bannerLab = PhotoImage(file="../Imagenes/Logos/BannerLab.png")
fuente = PhotoImage(file="../Imagenes/ImagenEquipos/fuente.png")
generador = PhotoImage(file="../Imagenes/ImagenEquipos/generador.png")
osciloscopio = PhotoImage(file="../Imagenes/ImagenEquipos/osciloscopio.png")
caiman = PhotoImage(file="../Imagenes/ImagenEquipos/caiman.png")
multimetro = PhotoImage(file="../Imagenes/ImagenEquipos/multimetro.png")
puntas = PhotoImage(file="../Imagenes/ImagenEquipos/puntas.png")
nombres = ["Multimetro","Osciloscopio","Sonda Osciloscopio", "Generador de Señales", "Cable Banana-Caiman","Fuente"]

sesion = -1
class DatosUsuarios:

    global sesion
    global indiceSesion
    global nombres
    def agregarUsuario(self,pUsuario,pContraseña,pNombre):
        usuarios.append(Usuarios(pUsuario,pContraseña,pNombre))
    def quitarUsuario(self,usuario):
        pass

    def validarContraseña(self,pUsuario, pContraseña): #metodo que valida si el usuario y la contraseña coinciden con los exixtentes en la base de datos
        global  sesion
        global indiceSesion
        self.retorno = False
        sesion = -1
        for i in usuarios:
            sesion += 1
            if i.darUsuario() == pUsuario and i.darContraseña() == pContraseña:
                self.retorno = True
                break
        indiceSesion = sesion
        return self.retorno



class Usuarios:   #clase para la creacion de usuarios
    usuario = ""
    contraseña = ""
    nombre =""
    cantida = 0
    multimetro = 0
    osciloscopio = 0
    sonda = 0
    generador = 0
    cable = 0
    fuente = 0
    horas = 0
    minutos = 0
    segundos = 0
    enPrestamo = 0
    multas = 0
    fecha = ""

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
    def usarEquipo(self, tipo):
        if tipo == "Generador de Señales":
            self.generador += 1
        elif tipo == "Multimetro":
            self.multimetro += 1
        elif tipo == "Osciloscopio":
            self.osciloscopio += 1
        elif tipo == "Sonda Osciloscopio":
            self.sonda += 1
        elif tipo == "Cable Banana-Caiman":
            self.cable += 1
        else:
            self.fuente += 1
        self.cantida += 1
    def cantidad(self):
        return self.cantida
    def cantidadEquipo(self, tipo):
        if tipo == "Generador de Señales":
            return  self.generador
        elif tipo == "Multimetro":
            return self.multimetro
        elif tipo == "Osciloscopio":
            return self.osciloscopio
        elif tipo == "Sonda Osciloscopio":
            return self.sonda
        elif tipo == "Cable Banana-Caiman":
            return  self.cable
        else:
            return  self.fuente
    def devolverEquipo(self, tipo):
        if tipo == "Generador de Señales":
            self.generador -= 1
        elif tipo == "Multimetro":
            self.multimetro -= 1
        elif tipo == "Osciloscopio":
            self.osciloscopio -= 1
        elif tipo == "Sonda Osciloscopio":
            self.sonda -= 1
        elif tipo == "Cable Banana-Caiman":
            self.cable -= 1
        else:
            self.fuente -= 1
        self.cantida -= 1
    def regresivo(self,hora):
        pass
    def darTiempo(self):
        return [self.horas, self.minutos, self.segundos]
    def asignarTiempo(self,hora,minuto,segundo):
        self.horas = hora
        self.minutos = minuto
        self.segundos = segundo
    def asignarFecha(self, fech):
        self.fecha = fech
    def darFecha(self):
        return  self.fecha
    def agregarEquiposAprestamo(self):
        self.enPrestamo = self.cantidad
    def darEquiposEnPrestamo(self):
        return self.enPrestamo
    def devolverPrestamo(self):
        self.enPrestamo = 0
    def agregarMulta(self):
        self.multas += 1
    def quitarMultas(self):
        self.multas = 0
    def darMultas(self):
        return self.multas
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
    def reservarEquipo(self):
        self.cantidad -=1
    def devolverEquipo(self):
        self.cantidad +=1
class Laboratorio:
    global indiceSesion
    lab = 0
    nombre1 = ""

    def __init__(self, pNombre, lab):
        self.nombrel = pNombre
        self.lab = lab

    def darNombre(self):
        return self.nombrel
    def darNombreEquipo(self,indice):
        return equipos[indice].darNombre()
    def darCantidadPorNombre(self,pNombre):
        xCantidad = 0
        for i in equipos:
             if i.darNombre() == pNombre :
                xCantidad = i.darCantidad()
        return xCantidad
    def reservar(self,pNombre):
        reserva = False
        for i in range(len(equipos)):
            if equipos[i].darNombre() == pNombre and equipos[i].darCantidad() > 0:
                equipos[i].reservarEquipo()
                usuarios[indiceSesion].usarEquipo(self.darNombreEquipo(i))
                reserva = True
        return reserva
    def devolver(self,pNombre):
        devuelve = False
        for i in equipos:
            if i.darNombre() == pNombre and  usuarios[indiceSesion].cantidadEquipo(i.darNombre())> 0:
                i.devolverEquipo()
                usuarios[indiceSesion].devolverEquipo(pNombre)
                devuelve = True
        return devuelve
    def devolverTodoUsuario(self):
        retorno = False
        for i in equipos:
            for j in range(usuarios[indiceSesion].cantidadEquipo(i.darNombre())):
                retorno = self.devolver(i.darNombre())
        return retorno
    def darEquipoPorNombre(self,pNombre):
        equip = None
        for i in equipos:
            if i.darNombre() == pNombre:
                equip = i
        return equip
    def prestarAUsuario(self,indice, tiempo):
        usuarios[indice].regresivo(tiempo)

usuarios = []
equipos = []
usuariosPrestamos = []
usuariosMultas = []
datos = DatosUsuarios()
indiceSesion = sesion

usuarios.append(Usuarios("jhernandezga","unal","Jorge Andrés Hernández"))
usuarios.append(Usuarios("anardilaa","unal","Andrés Ardila"))
usuarios.append(Usuarios("dmurcia","unal","David Murcia"))

equipos.append(Equipos("Generador de Señales", "Electroni", "FY3224S", 25))
equipos.append(Equipos("Osciloscopio", "Rigol", "DS1054", 15))
equipos.append(Equipos("Fuente", "Genérico", "NA", 100))
equipos.append(Equipos("Cable Banana-Caiman", "Genérico", "NA", 100))
equipos.append(Equipos("Sonda Osciloscopio", "Genérico 10X", "P4060", 25))
equipos.append(Equipos("Multimetro", "fluke", "87-v", 20))

labElectronica = Laboratorio("Laboratiorio de Ingeniería Eléctrica y Electrónica",1)
time1 = ''
dia = ''

def ventanaAdmin3():
    frame = Frame()
    frame.config(bg="white")
    frame.pack()
    print(len(usuariosMultas))

    def anterior():
        frame.destroy()
        ventanaAdmin1()

    def quitarMulta(indice):
        usuariosMultas[indice].quitarMultas()
        messagebox.showinfo("Info", "Se eliminaron las multas del usuario")
        usuariosMultas.remove(usuariosMultas[indice])
        frame.destroy()
        ventanaAdmin3()
    for i in range(len(usuariosMultas)):

        labelUsuariosM1 = Label(frame, text= usuariosMultas[i].darMultas())
        labelUsuariosM1.config(font=("Berlin Sans FB", 16), fg="#96D646", bg="White")
        labelUsuariosM1.grid(row=i+4, column=2)

        labelUsuarios1 = Label(frame, text=usuariosMultas[i].darNombre())
        labelUsuarios1.config(font=("Berlin Sans FB", 16), fg="#96D646", bg="White")
        labelUsuarios1.grid(row=i+4, column=1)

        multaButton = Button(frame, text="Quitar Multa", width=20, height=1, activeforeground="#96D646",
                                activebackground="white", command = lambda :quitarMulta(i))
        multaButton.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                              fg="white")
        multaButton.grid(row=i+4, column=3)

    if len(usuariosMultas) == 0:
        labelMultas2 = Label(frame, text="No hay usuarios con multas")
        labelMultas2.config(font=("Berlin Sans FB", 20), fg="#96D646", bg="White")
        labelMultas2.grid(row=4, column=1, columnspan = 3)


    labelMultas= Label(frame, text="Usuarios con Multas")
    labelMultas.config(font=("Berlin Sans FB", 35), fg="#540C21", bg="White")
    labelMultas.grid(row=2, column=1)

    labelUsuariosM = Label(frame, text="Multas")
    labelUsuariosM.config(font=("Berlin Sans FB", 19), fg="#540C21", bg="White")
    labelUsuariosM.grid(row=3, column=2)

    labelUsuarios = Label(frame, text="Usuarios")
    labelUsuarios.config(font=("Berlin Sans FB", 19), fg="#540C21", bg="White")
    labelUsuarios.grid(row=3, column=1)

    anteriorButton = Button(frame, text="<<", width=20, height=1, activeforeground="#96D646",
                            activebackground="white", command=anterior)
    anteriorButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                          fg="white")
    anteriorButton.grid(row=12, column=1)
def ventanaAdmin2():
    frame = Frame()
    frame.config(bg="white")
    frame.pack()

    def anterior():
        ventanaAdmin1()
        frame.destroy()
    def crearUsuario():

        if nombreEntry.get() == "":
            messagebox.showinfo("Info", "Escriba un nombre")
        elif usuarioEntry.get() == "":
            messagebox.showinfo("Info", "Escriba un nombre de usuario")
        elif passEntry.get() == "":
            messagebox.showinfo("Info", "Escriba una contraseña")
        else:
            crear = True
            for i in range(len(usuarios)):
                if usuarioEntry.get() == usuarios[i].darUsuario():
                    crear = False
                    break
            if crear:
                usuarios.append(Usuarios(usuarioEntry.get(),passEntry.get(),nombreEntry.get()))
                messagebox.showinfo("Info", "Usuario creado")
            else:
                messagebox.showinfo("Info", "El usuario ya existe")


    banLabel = Label(frame,
                        text="Creación de Usuarios")
    banLabel.config(font=("Berlin Sans FB", 30), bg="white",
                       fg="#96D646", justify ="center")
    banLabel.grid(row=1, column=1, padx=20, pady=20, columnspan = 2)

    nombreLabel = Label(frame,
                         text="Nombre:")
    nombreLabel.config(font=("Berlin Sans FB", 15), bg="white",
                        fg="gray")
    nombreLabel.grid(row=2, column=1, padx=20, pady=20,
                      sticky="e")

    nombreEntry = Entry(frame)
    nombreEntry.config(justify="center", fg="#7CD325",
                        font=("Berlin Sans FB", 15))
    nombreEntry.grid(row=2, column=2, padx=10, pady=20, sticky="w")

    usuarioLabel = Label(frame,
                         text="Usuario:")
    usuarioLabel.config(font=("Berlin Sans FB", 15), bg="white",fg="gray")
    usuarioLabel.grid(row=3, column=1, padx=20, pady=20,
                      sticky="e")

    usuarioEntry = Entry(frame)
    usuarioEntry.config(justify="center", fg="#7CD325",
                        font=("Berlin Sans FB", 15))
    usuarioEntry.grid(row=3, column=2, padx=10, pady=20, sticky="w")

    passLabel = Label(frame, text="Contraseña:")
    passLabel.config(bg="white", fg="gray", font=("Berlin Sans FB", 15))
    passLabel.grid(row=4, column=1, padx=10, pady=20, sticky="e")

    passEntry = Entry(frame)
    passEntry.config(justify="center", show="*", fg="#7CD325", font=("Berlin Sans FB", 15))
    passEntry.grid(row=4, column=2, padx=10, pady=20, sticky="w")

    cierraButton = Button(frame, text="<<", width=20, height=1, activeforeground="#540C21",
                          activebackground="white",
                          command=anterior)  # command es para que llame a la funcion cuando se presione el boton
    cierraButton.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                        fg="white")  # se configura el relieve colore y fuente
    cierraButton.grid(row=10, column=1, columnspan=2, pady=20)  # se coloca en la grilla o tabla

    crearButton = Button(frame, text="Crear", width=20, height=1, activeforeground="#540C21",
                          activebackground="white",
                          command=crearUsuario)  # command es para que llame a la funcion cuando se presione el boton
    crearButton.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                        fg="white")  # se configura el relieve colore y fuente
    crearButton.grid(row=10, column=3, columnspan=2, pady=20)  # se coloca en la grilla o tabla
def ventanaAdmin1():
    frame = Frame()
    frame.config(bg="white")
    frame.pack()
    def cerrar():
        ventanaInicio()
        frame.destroy()

    def crear():
        ventanaAdmin2()
        frame.destroy()
    def multas():
        ventanaAdmin3()
        frame.destroy()

    for i in range(len(usuariosPrestamos)):

        labelNombre = Label(frame, text=usuariosPrestamos[i].darNombre())
        labelNombre.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
        labelNombre.grid(row=i + 3, column=1)

        labeltiempo = Label(frame, text=":".join(list(map(str,usuariosPrestamos[i].darTiempo()))))
        labeltiempo.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
        labeltiempo.grid(row=i + 3, column=3)

        labelt = Label(frame, text=str(usuariosPrestamos[i].cantidad()))
        labelt.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
        labelt.grid(row=i + 3, column=2)

    if len(usuariosPrestamos) == 0:
        labelPresta2 = Label(frame, text="No hay préstamos")
        labelPresta2.config(font=("Berlin Sans FB", 20), fg="#540C21", bg="White")
        labelPresta2.grid(row=4, column=1, columnspan=3)


    labelUsuarios = Label(frame, text = "Usuario")
    labelUsuarios.config(font=("Berlin Sans FB", 16), fg="#96D646", bg="White")
    labelUsuarios.grid(row=2, column=1)

    labelCantidad = Label(frame, text= "Equipos en Préstamo")
    labelCantidad.config(font=("Berlin Sans FB", 16), fg="#96D646", bg="White")
    labelCantidad.grid(row=2, column=2)

    labelEntrega = Label(frame, text="Hora de Entrega")
    labelEntrega.config(font=("Berlin Sans FB", 16), fg="#96D646", bg="White")
    labelEntrega.grid(row=2, column=3)

    cierraButton = Button(frame, text="Cerrar Sesión", width=20, height=1, activeforeground="#96D646",
                          activebackground="white",
                          command=cerrar)  # command es para que llame a la funcion cuando se presione el boton
    cierraButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                        fg="white")  # se configura el relieve colore y fuente
    cierraButton.grid(row=10, column=1, pady=20)  # se coloca en la grilla o tabla

    crearButton = Button(frame, text="Crear Usuario", width=20, height=1, activeforeground="#96D646",
                          activebackground="white",
                          command=crear)  # command es para que llame a la funcion cuando se presione el boton
    crearButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                        fg="white")  # se configura el relieve colore y fuente
    crearButton.grid(row=10, column=3,  pady=20)  # se coloca en la grilla o tabla

    multasButton = Button(frame, text="Multas Usuarios", width=20, height=1, activeforeground="#96D646",
                         activebackground="white",
                         command=multas)
    multasButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                       fg="white")
    multasButton.grid(row=10, column=2, pady=20)

def ventanaUsuario5():
    frame = Frame()
    frame.config(bg="white")
    frame.pack()

    def cerrar():
        ventanaInicio()
        frame.destroy()

    labelHoras = Label(frame, text = "Tiene multas, por favor comuniquese con el administrador")
    labelHoras.config(font=("Berlin Sans FB", 25), fg="#540C21", bg="White")
    labelHoras.grid(row=2, column=1)

    cierraButton = Button(frame, text="Cerrar Sesión", width=20, height=1, activeforeground="#96D646",
                          activebackground="white",
                          command=cerrar)  # command es para que llame a la funcion cuando se presione el boton
    cierraButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                        fg="white")  # se configura el relieve colore y fuente
    cierraButton.grid(row=10, column=1, columnspan=2, pady=20)  # se coloca en la grilla o tabla
def ventanaUsuario4():
    frame = Frame()
    frame.config(bg="white")
    frame.pack()
    var = StringVar()
    multas = StringVar()
    multas.set(usuarios[indiceSesion].darMultas())
    def reloj():
        global time1
        time2 = tm.strftime('%H:%M:%S')
        if time2 != time1:
            time1 = time2
            labelHoras.configure(text=time2)
            if list(map(int,time1.split(":"))) == usuarios[indiceSesion].darTiempo():
                messagebox.showinfo("Info", "Tiene una multa")
                usuarios[indiceSesion].agregarMulta()
                multas.set(usuarios[indiceSesion].darMultas())
                usuariosMultas.append(usuarios[indiceSesion])
        labelHoras.after(500, reloj)

    def tiempoEntrega():
        hora = usuarios[indiceSesion].darTiempo()[0]
        if hora > 23:
            hora = int(fabs(hora-24))

        local = "{}:{}:{}".format(hora, usuarios[indiceSesion].darTiempo()[1],usuarios[indiceSesion].darTiempo()[2])
        return local
    var.set(tiempoEntrega())

    def generarReciboUsuario( indice):
        global nombres
        w, h = A4
        user = usuarios[indice].darUsuario()
        name = usuarios[indice].darNombre()
        multas = usuarios[indice].darMultas()
        objetosTipo = 0
        objetos = [0]
        cantidad = [0]
        for i in nombres:
            if usuarios[indice].cantidadEquipo(i) > 0:
                objetos.append(i)
                cantidad.append(usuarios[indice].cantidadEquipo(i))
                objetosTipo += 1
        y_offset = 70
        xlist = [100, 300, 500]
        ylist = [h - y_offset - (n * 35 + 45) for n in range(1, objetosTipo + 3)]
        a = user + str(randint(0, 1000))
        c = canvas.Canvas(a + ".pdf", pagesize=A4)
        c.setFont("Times-Roman", 28)
        c.drawString(100, h - 50, "Recibo de devolución LABS UNAL")
        c.line(60, h - 70, w - 60, h - 70)
        c.setFont("Times-Roman", 15)
        c.drawString(60, h - 100, "Usuario:" + user)
        c.drawString(60, h - 120, "Nombre:" + name)
        c.drawString(300, h - 100, "Laboratorio: Electrónica")
        c.line(60, h - 125, w - 60, h - 125)
        c.setFont("Times-Roman", 20)
        c.drawString(230, h - 145, "Equipos Devueltos")
        c.grid(xlist, ylist)
        c.setFont("Times-Roman", 15)
        c.drawString(170, h - y_offset - 100, "Equipo")
        c.drawString(370, h - y_offset - 100, "Cantidad")
        for i in range(1, len(ylist) - 1):
            for j in range(len(xlist) - 1):
                if j == 1:
                    c.drawString(xlist[j] + 80, ylist[i] - 20, str(cantidad[i]))
                else:
                    c.drawString(xlist[j] + 40, ylist[i] - 20, objetos[i])
        c.drawString(60, ylist[len(ylist) - 1] - 30, "Multas: " + str(multas))

        c.drawString(60, ylist[len(ylist) - 1] - 50, "Hora de y fecha  devolución:                      "+ time1+"      "+ str(now.date()))
        c.drawString(60, ylist[len(ylist) - 1] - 70,
                     "Hora de y fecha  devolución programada: " + var.get() + "      " +usuarios[indiceSesion].darFecha() )
        if multas > 0:
            c.setFont("Times-Roman", 18)
            c.drawString(60, ylist[len(ylist) - 1] - 105, "Nota:")
            c.setFont("Times-Roman", 12)
            c.drawString(50, ylist[len(ylist) - 1] - 120,
                         "Tiene multas, por favor comuníquese con el administrador para poder realizar otro préstamo")
        c.line(60, 90, w - 60, 90)
        c.setFont("Times-Roman", 10)
        c.drawString(60, 80, "jhernandezga@unal.edu.co")
        c.drawString(60, 70, "anardilaa@unal.edu.co")
        c.drawString(60, 60, "dmurciac@unal.edu.co")
        c.line(60, 50, w - 60, 50)
        c.save()

    def devolvera():
        generarReciboUsuario(indiceSesion)
        if labElectronica.devolverTodoUsuario():

            messagebox.showinfo("Devolución", "Los equipos fueron devueltos. Se ha generado su recibo")
            usuariosPrestamos.remove(usuarios[indiceSesion])
            if usuarios[indiceSesion].darMultas() == 0:
                frame.destroy()
                ventanaUsuario2()
            else:
                frame.destroy()
                ventanaUsuario5()

    labelHoras = Label(frame)
    labelHoras.config(font=("Berlin Sans FB", 50), fg="#540C21", bg="White")
    labelHoras.grid(row=2, column=2)

    labelEntrega = Label(frame, textvariable = var)
    labelEntrega.config(font=("Berlin Sans FB", 50), fg="#540C21", bg="White")
    labelEntrega.grid(row=3, column=2)

    def cerrar():
        ventanaInicio()
        frame.destroy()

    reloj()
    labelTiempoAc = Label(frame, text = "Hora Actual:" )
    labelTiempoAc.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelTiempoAc.grid(row=2, column=1, sticky = "e")

    labelMultas1 = Label(frame, text = "Multas:")
    labelMultas1.config(font=("Berlin Sans FB", 20), fg="#96D646", bg="White")
    labelMultas1.grid(row=2, column=3)

    labelMultas = Label(frame, textvariable = multas )
    labelMultas.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelMultas.grid(row=2, column=4 )

    labelTiempoEntrega = Label(frame, text = "Hora de entrega:" )
    labelTiempoEntrega.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelTiempoEntrega.grid(row=3, column=1, sticky ="e")

    cerrarButton = Button(frame, text="Cerrar Sesión", width=20, height=1, activeforeground="#96D646",
                            activebackground="white", command=cerrar)
    cerrarButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                          fg="white")
    cerrarButton.grid(row=5, column=1, pady=10)

    devolverButton = Button(frame, text="Devolver", width=20, height=1, activeforeground="#96D646",
                            activebackground="white", command=devolvera)
    devolverButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                          fg="white")
    devolverButton.grid(row=5, column=2, pady=10)

def ventanaUsuario3():

    frame = Frame()
    frame.config(bg = "white")
    frame.pack()
    global nombres
    mostrar1 = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
    total = StringVar()
    total.set("Total: " + str(usuarios[indiceSesion].cantidad()))
    tiempo = IntVar()
    tiempo.set(-1)
    tiemposPrestamo = [1,2,3,4,5,0]

    for i in range(len(mostrar1)):
        mostrar1[i].set(usuarios[indiceSesion].cantidadEquipo(nombres[i]))

    def anterior():
        ventanaUsuario2()
        frame.destroy()
    def devolver(indice):
        labElectronica.devolver(nombres[indice])
        usuarios[indiceSesion].devolverPrestamo()
        mostrar1[indice].set(usuarios[indiceSesion].cantidadEquipo(nombres[indice]))
        total.set("Total: " + str(usuarios[indiceSesion].cantidad()))
    def confirmarPrestamo():
        dt = datetime.now()
        usuarios[indiceSesion].asignarFecha(str(dt.date()))
        if tiempo.get() == -1:
            messagebox.showinfo("Info", "Selecciones el tiempo de uso")
        elif usuarios[indiceSesion].cantidad() == 0:
            messagebox.showinfo("Info", "Agregue equipos al préstamo")
        else:
            usuarios[indiceSesion].agregarEquiposAprestamo()
            usuarios[indiceSesion].asignarTiempo(dt.hour+tiemposPrestamo[tiempo.get()], dt.minute, dt.second)
            usuariosPrestamos.append(usuarios[indiceSesion])
            frame.destroy()
            ventanaUsuario4()


    for i in range(6):
        labelNombreOs = Label(frame, text = nombres[i])
        labelNombreOs.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
        labelNombreOs.grid(row=i+1, column=2)

    labelNombreOs1 = Label(frame, textvariable = mostrar1[0] )
    labelNombreOs1.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelNombreOs1.grid(row=1, column=1)

    labelNombreOs2 = Label(frame, textvariable = mostrar1[1])
    labelNombreOs2.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelNombreOs2.grid(row= 2, column=1)

    labelNombreOs3 = Label(frame, textvariable = mostrar1[2])
    labelNombreOs3.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelNombreOs3.grid(row= 3, column=1)

    labelNombreOs4 = Label(frame, textvariable = mostrar1[3])
    labelNombreOs4.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelNombreOs4.grid(row= 4, column=1)

    labelNombreOs5 = Label(frame, textvariable = mostrar1[4])
    labelNombreOs5.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelNombreOs5.grid(row= 5, column=1)

    labelNombreOs6 = Label(frame, textvariable = mostrar1[5])
    labelNombreOs6.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelNombreOs6.grid(row= 6, column=1)

    labelTotal= Label(frame, textvariable=total)
    labelTotal.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelTotal.grid(row=7, column=1)
    labelTotall = Label(frame, textvariable=tiempo)
    labelTotall.config(font=("Berlin Sans FB", 16), fg="#540C21", bg="White")
    labelTotall.grid(row=9, column=1)


    anteriorButton = Button(frame, text="<<", width=20, height=1, activeforeground="#96D646",
                             activebackground="white", command = anterior)
    anteriorButton.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")
    anteriorButton.grid(row=12, column=1, pady=10)

    quitar1 = Button(frame, text="Quitar", width=20, height=1, activeforeground="#540C21",
                             activebackground="white", command = lambda: devolver(0) )
    quitar1.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")
    quitar1.grid(row=1, column=3 )


    quitar2 = Button(frame, text="Quitar", width=20, height=1, activeforeground="#540C21",
                     activebackground="white", command = lambda: devolver(1) )
    quitar2.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                   fg="white")
    quitar2.grid(row=2, column=3)

    quitar3 = Button(frame, text="Quitar", width=20, height=1, activeforeground="#540C21",
                     activebackground="white", command = lambda: devolver(2) )
    quitar3.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                   fg="white")
    quitar3.grid(row=3, column=3)

    quitar4 = Button(frame, text="Quitar", width=20, height=1, activeforeground="#540C21",
                     activebackground="white", command = lambda: devolver(3) )
    quitar4.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                   fg="white")
    quitar4.grid(row=4, column=3)

    quitar5 = Button(frame, text="Quitar", width=20, height=1, activeforeground="#540C21",
                     activebackground="white", command = lambda: devolver(4) )
    quitar5.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                   fg="white")
    quitar5.grid(row=5, column=3)

    quitar6 = Button(frame, text="Quitar", width=20, height=1, activeforeground="#540C21",
                     activebackground="white", command = lambda: devolver(5) )
    quitar6.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                   fg="white")
    quitar6.grid(row=6, column=3)

    confirmar = Button(frame, text="Confirmar", width=20, height=1, activeforeground="#540C21",
                     activebackground="white", command = lambda: confirmarPrestamo())
    confirmar.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                          fg="white")
    confirmar.grid(row=12, column=3, columnspan = 2)

    tiempoLabel = Label(frame, text="Seleccione el tiempo de uso máximo (Horas): ")
    tiempoLabel.config(bg="white", fg="#7CD325", font=("Berlin Sans FB", 18))
    tiempoLabel.grid(row=7, column=2, padx=20, pady=20, sticky="e")

    radioTiempo1 = Radiobutton(frame, text=tiemposPrestamo[0],value=0, variable=tiempo
                                  )
    radioTiempo1.config(bg="white", font=("Berlin Sans FB", 15), activebackground="white",
                           activeforeground="#7CD325", fg="#540C21")
    radioTiempo1.grid(row=7, column=3, sticky="w")

    radioTiempo2 = Radiobutton(frame, text=tiemposPrestamo[1], value=1,variable=tiempo
                               )
    radioTiempo2.config(bg="white", font=("Berlin Sans FB", 15), activebackground="white",
                        activeforeground="#7CD325", fg="#540C21")
    radioTiempo2.grid(row=8, column=3, sticky="w")

    radioTiempo3 = Radiobutton(frame, text=tiemposPrestamo[2], value=2,variable=tiempo
                               )
    radioTiempo3.config(bg="white", font=("Berlin Sans FB", 15), activebackground="white",
                        activeforeground="#7CD325", fg="#540C21")
    radioTiempo3.grid(row=9, column=3, sticky="w")

    radioTiempo4 = Radiobutton(frame, text=tiemposPrestamo[3],  value=3,variable=tiempo,
                              )
    radioTiempo4.config(bg="white", font=("Berlin Sans FB", 15), activebackground="white",
                        activeforeground="#7CD325", fg="#540C21")
    radioTiempo4.grid(row=10, column=3, sticky="w")

    radioTiempo5 = Radiobutton(frame, text=tiemposPrestamo[4], value=4,variable=tiempo,
                               )
    radioTiempo5.config(bg="white", font=("Berlin Sans FB", 15), activebackground="white",
                        activeforeground="#7CD325", fg="#540C21")
    radioTiempo5.grid(row=11, column=3, sticky="w")

    radioTiempo6 = Radiobutton(frame, text=tiemposPrestamo[5], value=5, variable=tiempo,
                               )
    radioTiempo6.config(bg="white", font=("Berlin Sans FB", 15), activebackground="white",
                        activeforeground="#7CD325", fg="#540C21")
    radioTiempo6.grid(row=8, column=2, sticky="w")
def ventanaUsuario2():

    frame = Frame()
    frame.config(bg = "White")
    frame.pack()
    nombre = []
    mostrar = [StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]

    for i in range(len(mostrar)):
        nombre.append(labElectronica.darNombreEquipo(i))

    for i in range(len(mostrar)):
        mostrar[i].set("Disponibles: "+ str(labElectronica.darCantidadPorNombre(nombre[i])))
    def siguiente():
        ventanaUsuario3()
        frame.destroy()
    def quitarACantidad(indice):
        labElectronica.reservar(nombre[indice])
        mostrar[indice].set("Disponibles: " + str(labElectronica.darCantidadPorNombre(nombre[indice])))

    def cerrar():
        ventanaInicio()
        frame.destroy()
        labElectronica.devolverTodoUsuario()

    labelBanner = Label(frame, image= bannerLab)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelBanner.config(bg="White")
    labelBanner.grid(row=1, column=1 , columnspan = 3)

    labelNombreGen = Label(frame, text=nombre[0])
    labelNombreGen.config( font=("Berlin Sans FB", 16), fg = "#540C21", bg ="White")
    labelNombreGen.grid(row=2, column=1)

    labelNombreOs = Label(frame, text=nombre[1])
    labelNombreOs.config( font=("Berlin Sans FB", 16), fg = "#540C21", bg ="White")
    labelNombreOs.grid(row=2, column=2)

    labelNombreFu = Label(frame, text=nombre[2])
    labelNombreFu.config( font=("Berlin Sans FB", 16), fg = "#540C21", bg ="White")
    labelNombreFu.grid(row=2, column=3)

    labelNombreCa = Label(frame, text=nombre[3])
    labelNombreCa.config( font=("Berlin Sans FB", 16), fg = "#540C21", bg ="White")
    labelNombreCa.grid(row=6, column=1)

    labelNombreSo = Label(frame, text=nombre[4])
    labelNombreSo.config( font=("Berlin Sans FB", 16), fg = "#540C21", bg ="White")
    labelNombreSo.grid(row=6, column=2)

    labelNombreMu = Label(frame, text=nombre[5])
    labelNombreMu.config( font=("Berlin Sans FB", 16), fg = "#540C21", bg ="White")
    labelNombreMu.grid(row=6, column=3)

    labelCantidadGen = Label(frame, textvariable=mostrar[0])
    labelCantidadGen.config(font=("Berlin Sans FB", 12), fg = "#96D646", bg = "White")
    labelCantidadGen.grid(row=4, column=1)

    labelCantidadOs = Label(frame, textvariable=mostrar[1])
    labelCantidadOs.config(font=("Berlin Sans FB", 12), fg = "#96D646", bg = "White")
    labelCantidadOs.grid(row=4, column=2)

    labelCantidadFu = Label(frame, textvariable=mostrar[2])
    labelCantidadFu.config(font=("Berlin Sans FB", 12), fg = "#96D646", bg = "White")
    labelCantidadFu.grid(row=4, column=3)

    labelCantidadCa = Label(frame, textvariable=mostrar[3])
    labelCantidadCa.config(font=("Berlin Sans FB", 12), fg = "#96D646", bg = "White")
    labelCantidadCa.grid(row=8, column=1)

    labelCantidadSo = Label(frame, textvariable=mostrar[4])
    labelCantidadSo.config(font=("Berlin Sans FB", 12), fg = "#96D646", bg = "White")
    labelCantidadSo.grid(row=8, column=2)

    labelCantidadMu = Label(frame, textvariable=mostrar[5])
    labelCantidadMu.config(font=("Berlin Sans FB", 12), fg = "#96D646", bg = "White")
    labelCantidadMu.grid(row=8, column=3)

    siguienteButton = Button(frame, text="Siguiente", width=20, height=1, activeforeground="#540C21",
                          activebackground="white",
                          command=siguiente)  # command es para que llame a la funcion cuando se presione el boton
    siguienteButton.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                        fg="white")  # se configura el relieve colore y fuente
    siguienteButton.grid(row=10, column=2, columnspan=2, pady=20)  # se coloca en la grilla o tabla

    cierraButton = Button(frame, text="Cerrar Sesión", width=20, height=1, activeforeground="#540C21",
                             activebackground="white",
                             command=cerrar ) # command es para que llame a la funcion cuando se presione el boton
    cierraButton.config(bg="#540C21", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    cierraButton.grid(row=10, column=1, columnspan=2, pady=20)  # se coloca en la grilla o tabla


    labelgenerador = Label(frame, image= generador ) # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelgenerador.config(bg="White")
    labelgenerador.grid(row=3, column=1)

    buttonGenerador = Button(frame, text="Reservar", width=20, height=1, activeforeground="#96D646",
                             activebackground="white", command = lambda :quitarACantidad(0))  # command es para que llame a la funcion cuando se presione el boton
    buttonGenerador.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonGenerador.grid(row=5, column=1, pady=5)  # se coloca en la grilla o tabla

    labelOsciloscopio = Label(frame, image=osciloscopio) # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelOsciloscopio.config(bg="White")
    labelOsciloscopio.grid(row=3, column=2)

    buttonOsciloscopio = Button(frame, text="Reservar", width=20, height=1, activeforeground="#96D646",
                             activebackground="white", command = lambda :quitarACantidad(1))  # command es para que llame a la funcion cuando se presione el boton
    buttonOsciloscopio.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonOsciloscopio.grid(row=5, column=2, pady=5,padx = 10)  # se coloca en la grilla o tabla


    labelFuente = Label(frame, image=fuente)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelFuente.config(bg="White")
    labelFuente.grid(row=3, column=3)

    buttonFuente = Button(frame, text="Reservar", width=20, height=1, activeforeground="#96D646",
                             activebackground="white", command = lambda :quitarACantidad(2))  # command es para que llame a la funcion cuando se presione el boton
    buttonFuente.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonFuente.grid(row=5, column=3,  pady=5,padx =10)  # se coloca en la grilla o tabla

    labelCaiman = Label(frame, image=caiman)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelCaiman.config(bg="White")
    labelCaiman.grid(row=7, column=1)

    buttonCaiman = Button(frame, text="Reservar", width=20, height=1, activeforeground="#96D646",
                             activebackground="white", command = lambda :quitarACantidad(3))  # command es para que llame a la funcion cuando se presione el boton
    buttonCaiman.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonCaiman.grid(row=9, column=1,  pady=5,padx =10)  # se coloca en la grilla o tabla

    labelPuntas = Label(frame, image=puntas)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelPuntas.config(bg="White")
    labelPuntas.grid(row=7, column=2)

    buttonPuntas = Button(frame, text="Reservar", width=20, height=1, activeforeground="#96D646",
                             activebackground="white", command = lambda :quitarACantidad(4))  # command es para que llame a la funcion cuando se presione el boton
    buttonPuntas.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonPuntas.grid(row=9, column=2, pady=5)  # se coloca en la grilla o tabla

    labelMultimetro = Label(frame, image= multimetro)  # Se crea un label y se le dice que va a contener la imagen logoUnal
    labelMultimetro.config(bg="White")
    labelMultimetro.grid(row=7, column=3)

    buttonMultímetro = Button(frame, text="Reservar", width=20, height=1, activeforeground="#96D646",
                             activebackground="white", command = lambda :quitarACantidad(5))  # command es para que llame a la funcion cuando se presione el boton
    buttonMultímetro.config(bg="#96D646", borderwidth=0, relief="flat", font=("Berlin Sans FB", 15),
                           fg="white")  # se configura el relieve colore y fuente
    buttonMultímetro.grid(row=9, column=3, pady=5)  # se coloca en la grilla o tabla

def ventanaInicio():

    def inicioSesion():
        usuario = usuarioEntry.get()
        contraseña = passEntry.get()
        rol = rola.get()

        if rol == 1:  # si el rol seleccionado es 1(para estudiantes) se ejecuta

            validar =datos.validarContraseña(usuario, contraseña)
            if validar:  # si inicio es verdadero se ejecuta(si es verdadero significa que coinciden los datos)
                if usuarios[indiceSesion].cantidad() > 0:
                    frame.destroy()
                    ventanaUsuario4()
                elif usuarios[indiceSesion].darMultas() > 0:
                    frame.destroy()
                    ventanaUsuario5()
                else:
                    ventanaUsuario2()
                    frame.destroy()
            else:
                messagebox.showinfo("Info", "Usuario o contraseña incorrectos")

        elif rol == 2:  # si el rol es 2 (para administrador ) se ejecuta

            # comprueba si lo que se introdujo en las casillas es igual a user y pass predeterminado para el administrador
            if usuario == _USUARIO_ADMIN and contraseña == _PASS_ADMIN:
                frame.destroy()
                ventanaAdmin1()
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
    labelImagen1 = Label(frame, image=logoUnal)  #Se crea un label y se le dice que va a contener la imagen logoUnal
    labelImagen1.config(bg="White")
    labelImagen1.grid(row=1, column=1)

    labelImagen2 = Label(frame, image=demoUnal)
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

ventanaInicio()
root.mainloop()













