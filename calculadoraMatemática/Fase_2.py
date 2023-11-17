from tkinter import Tk, StringVar, W, E, N, S
from tkinter import ttk
import math


def alternarModoOscuro():
    global modo_oscuro

    if modo_oscuro:
        # MODO CLARO
        root.configure(bg="#F1F1DD")  # Cambia el fondo a un tono claro
        estilos.configure('mainframe.TFrame', background="#F1F1DD")  # Cambia el color del frame principal al modo claro

        # ESTILO BOTONES
        estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", foreground="#121212", width=5, relief="flat", background="#EBE4E4")
        estilos_botones_numeros.map('Botones_numeros.TButton', foreground=[('active', '#E66F00')], background=[('active','#D5CCCC')])

            # ESTILOS BOTON BORRAR
        estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 22",foreground="#d76600", width=5, relief="flat", background="#d6cdcd")
        estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', '#EFEFDB')], background=[('active', '#E66F00')])

            # ESTILO RESTO DE BOTONES
        estilos_botones_restantes.configure('Botones_restantes.TButton', font="arial 22",foreground="#d76600", width=5, relief="flat", background="#d6cdcd")
        estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active','#C2C2A4')])

            # ESTILOS LABELS
        estilos_label1.configure('Label1.TLabel', font="arial 16", foreground="#CF6C0F", anchor= "e", background="#F1F1DD")
        estilos_label2.configure('Label2.TLabel', font="arial 40", foreground="#DE6C01", anchor="e", background="#F1F1DD")

            # ESTILOS BOTON IGUAL
        estilos_boton_igual.configure('Boton_igual.TButton', font="Arial 22",foreground="#d76600", width=5, relief="flat", background="#d6cdcd")
        estilos_boton_igual.map('Boton_igual.TButton', foreground=[('active', '#EFEFDB')], background=[('active', '#E66F00')])

        # MODO OSCURO DESACTIVADO
        modo_oscuro = False
    else:
            # Cambiar a modo oscuro
        root.configure(bg="#303030")  # Cambia el fondo a un tono oscuro
        estilos.configure('mainframe.TFrame', background="#1e1e1e")  # Cambia el color del frame principal al modo oscuro
            
            # ESTILO BOTONES
        estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22",foreground="#d6d6d6", width=5, relief="flat", background="#303030")
        estilos_botones_numeros.map('Botones_numeros.TButton', foreground=[('active', '#d76600')], background=[('active','#4f4f4f')])

            # ESTILOS BOTON BORRAR
        estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 22",foreground="#d76600", width=5, relief="flat", background="#444444")
        estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', '#EFEFDB')], background=[('active', '#E66F00')])

            # ESTILO RESTO DE BOTONES
        estilos_botones_restantes.configure('Botones_restantes.TButton', font="arial 22",foreground="#d76600", width=5, relief="flat", background="#444444")
        estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active','#C2C2A4')])

            # ESTILOS LABELS
        estilos_label1.configure('Label1.TLabel', font="arial 16", foreground="#CF6C0F", anchor= "e", background="#1e1e1e")
        estilos_label2.configure('Label2.TLabel', font="arial 40", foreground="#DE6C01", anchor="e", background="#1e1e1e")

            # ESTILOS BOTON IGUAL
        estilos_boton_igual.configure('Boton_igual.TButton', font="Arial 22",foreground="#d76600", width=5, relief="flat", background="#444444")
        estilos_boton_igual.map('Boton_igual.TButton', foreground=[('active', '#EFEFDB')], background=[('active', '#E66F00')])

        # MODO OSCURO ACTIVADO
        modo_oscuro = True

# Inicialización de variables
modo_oscuro = False

# Función para manejar la entrada de variables
def ingresarVariable(tecla):
    global ecuacion

    # Manejo de dígitos, paréntesis y punto decimal
    if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
        if (
            tecla == '('
            and entrada2.get() and entrada2.get()[-1] not in "+-*/^"
        ):
            # Agrega automáticamente un operador '*' antes del paréntesis de apertura
            entrada2.set(entrada2.get() + '*' + tecla)
        elif (
            tecla >= '0' and tecla <= '9' and entrada2.get() and entrada2.get()[-1] == ')'
        ):
            # Agrega automáticamente un operador '*' después del paréntesis de cierre
            entrada2.set(entrada2.get() + '*' + tecla)
        else:
            entrada2.set(entrada2.get() + tecla)


    # Manejo de operadores

    if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-' or tecla == '^':
        if not entrada2.get() or entrada2.get()[-1] in "+-*/^":
            # Si entrada2 está vacío o termina con un operador, no agregamos otro operador.
            return

        # Agrega automáticamente un paréntesis de apertura después del '^'
        if tecla == '^':
            entrada2.set(entrada2.get() + tecla + '(')
        else:
            entrada2.set(entrada2.get() + tecla)


    # Manejo de comparación mayor que ('>')
    if tecla == '>':
        if entrada2.get() and entrada2.get()[-1] not in "+-*/" and not entrada2.get().endswith(">"):
            entrada2.set(entrada2.get() + tecla)
            partes = entrada2.get().split(">")
            if len(partes) == 2:
                # Realiza la comparación cuando ambas partes de la comparación están presentes
                expresion1 = eval(partes[0])
                expresion2 = eval(partes[1])
                resultado_comparacion = expresion1 > expresion2
                entrada2.set(str(resultado_comparacion))
            else:
                # No se tienen ambas partes de la comparación, establece la entrada2 en "False"
                entrada2.set("False")


    # Manejo de comparación menor que ('<')
    if tecla == '<':
        if entrada2.get() and entrada2.get()[-1] not in "+-*/" and not entrada2.get().endswith("<"):
            entrada2.set(entrada2.get() + tecla)
            partes = entrada2.get().split("<")
            if len(partes) == 2:
                # Realiza la comparación cuando ambas partes de la comparación están presentes
                expresion1 = eval(partes[0])
                expresion2 = eval(partes[1])
                resultado_comparacion = expresion1 < expresion2
                entrada2.set(str(resultado_comparacion))
            else:
                # No se tienen ambas partes de la comparación, establece la entrada2 en "False"
                entrada2.set("False")


# Manejo del operador igual ('=')
    if tecla == '=':
        if entrada2.get():
            ecuacion = entrada2.get()
            # Reemplaza '**' con '^' para mostrar en Label_entrada1
            ecuacion_display = ecuacion.replace('**', '^')
            # Reemplaza '^' con '**' para la exponenciación y luego evalúa
            ecuacion = ecuacion.replace('^', '**')
            resultado = eval(ecuacion)
            entrada1.set(ecuacion_display)  # Establece la ecuación en entrada1
            entrada2.set(str(resultado))
        else:
            entrada1.set('')
            entrada2.set('')
            ecuacion = ""

# Función para borrar toda la entrada
def borrarTodo():
    entrada1.set('')
    entrada2.set('')
    global ecuacion
    ecuacion = ""

# Función para borrar un elemento de la entrada
def borrarPorElemento():
    ecuacion_actual = entrada2.get()
    if ecuacion_actual:
        ecuacion_actual = ecuacion_actual[:-1]  # Remove the last character
        entrada2.set(ecuacion_actual)


# Inicialización de variables
ecuacion = ""
raiz_cuadrada = False

# Creación de la ventana principal
root = Tk()
root.title("MathLion")
root.geometry("+500+80")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

# ESTILOS
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#F1F1DD")

    # ESTILO BOTONES
estilos_botones_numeros = ttk.Style()
estilos_botones_numeros.configure('Botones_numeros.TButton', font="arial 22", width=5, relief="flat", background="#EBE4E4")
estilos_botones_numeros.map('Botones_numeros.TButton', foreground=[('active', '#E66F00')], background=[('active','#D5CCCC')])

    # ESTILOS BOTON BORRAR
estilos_botones_borrar = ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton', font="arial 22",foreground="#d76600", width=5, relief="flat", background="#d6cdcd")
estilos_botones_borrar.map('Botones_borrar.TButton', foreground=[('active', '#EFEFDB')], background=[('active', '#E66F00')])

    # ESTILO RESTO DE BOTONES
estilos_botones_restantes = ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton', font="arial 22",foreground="#d76600", width=5, relief="flat", background="#d6cdcd")
estilos_botones_restantes.map('Botones_restantes.TButton', background=[('active','#C2C2A4')])

    # ESTILOS LABELS
estilos_label1 = ttk.Style()
estilos_label1.configure('Label1.TLabel', font="arial 16", foreground="#CF6C0F", anchor= "e", background="#F1F1DD")

estilos_label2 = ttk.Style()
estilos_label2.configure('Label2.TLabel', font="arial 40", foreground="#DE6C01", anchor="e", background="#F1F1DD")

    # ESTILOS BOTON IGUAL
estilos_boton_igual = ttk.Style()
estilos_boton_igual.configure('Boton_igual.TButton', font="Arial 22",foreground="#d76600", width=5, relief="flat", background="#d6cdcd")
estilos_boton_igual.map('Boton_igual.TButton', foreground=[('active', '#EFEFDB')], background=[('active', '#E66F00')])


# ADAPTAVILIDAD DE CALCULADORA
mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))

mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)
mainframe.rowconfigure(7, weight=1)


    # Escuchar la tecla "o" para alternar el modo oscuro
root.bind('o', lambda event: alternarModoOscuro())

    # PANTALLA SUPERIOR
entrada1 = StringVar()
Label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
Label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

    # PANTALLA INFERIOR
entrada2 = StringVar()
Label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style="Label2.TLabel")
Label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))


     # BOTONES NUMEROS
Button0 = ttk.Button(mainframe, text="0", style="Botones_numeros.TButton", command=lambda: ingresarVariable('0'))
Button1 = ttk.Button(mainframe, text="1", style="Botones_numeros.TButton", command=lambda: ingresarVariable('1'))
Button2 = ttk.Button(mainframe, text="2", style="Botones_numeros.TButton", command=lambda: ingresarVariable('2'))
Button3 = ttk.Button(mainframe, text="3", style="Botones_numeros.TButton", command=lambda: ingresarVariable('3'))
Button4 = ttk.Button(mainframe, text="4", style="Botones_numeros.TButton", command=lambda: ingresarVariable('4'))
Button5 = ttk.Button(mainframe, text="5", style="Botones_numeros.TButton", command=lambda: ingresarVariable('5'))
Button6 = ttk.Button(mainframe, text="6", style="Botones_numeros.TButton", command=lambda: ingresarVariable('6'))
Button7 = ttk.Button(mainframe, text="7", style="Botones_numeros.TButton", command=lambda: ingresarVariable('7'))
Button8 = ttk.Button(mainframe, text="8", style="Botones_numeros.TButton", command=lambda: ingresarVariable('8'))
Button9 = ttk.Button(mainframe, text="9", style="Botones_numeros.TButton", command=lambda: ingresarVariable('9'))

    # BOTONES PARA BORRAR
Button_borrar = ttk.Button(mainframe, text= chr(9003), style="Botones_borrar.TButton", command=lambda: borrarPorElemento())
Button_borrar_todo = ttk.Button(mainframe, text="C", style="Botones_borrar.TButton", command=lambda: borrarTodo())

    # PARENTESIS
Button_parentesis1 = ttk.Button(mainframe, text="(", style="Botones_restantes.TButton", command=lambda: ingresarVariable('('))
Button_parentesis2 = ttk.Button(mainframe, text=")", style="Botones_restantes.TButton", command=lambda: ingresarVariable(')'))

    # BOTON PUNTO
Button_punto = ttk.Button(mainframe, text=".", style="Botones_restantes.TButton", command=lambda: ingresarVariable('.'))

    # BOTON OPERADORES
Button_division = ttk.Button(mainframe, text=chr(247), style="Botones_restantes.TButton", command=lambda: ingresarVariable('/'))
Button_multiplicacion = ttk.Button(mainframe, text="X", style="Botones_restantes.TButton", command=lambda: ingresarVariable('*'))
Button_resta = ttk.Button(mainframe, text="-", style="Botones_restantes.TButton", command=lambda: ingresarVariable('-'))
Button_suma = ttk.Button(mainframe, text="+", style="Botones_restantes.TButton", command=lambda: ingresarVariable('+'))
Button_potencia = ttk.Button(mainframe, text="^", style="Botones_restantes.TButton", command=lambda: ingresarVariable('^'))

     # BOTON IGUAL
Button_igual = ttk.Button(mainframe, text="=", style="Boton_igual.TButton", command=lambda: ingresarVariable('='))

    # BOTON MAYOR QUE Y MENOR QUE
Button_menor = ttk.Button(mainframe, text="<", style="Botones_restantes.TButton", command=lambda: ingresarVariable('<'))
Button_mayor = ttk.Button(mainframe, text=">", style="Botones_restantes.TButton", command=lambda: ingresarVariable('>'))



# BOTONES EN PANTALLA

    # primera fila de botones
Button_parentesis1.grid(column=0,row=2, sticky=(W, N, E, S))
Button_parentesis2.grid(column=1, row=2, sticky=(W, N, E, S))
Button_borrar_todo.grid(column=2, row=2, sticky=(W, N, E, S))
Button_borrar.grid(column=3, row=2, sticky=(W, N, E, S))

    # segunda fila de botones
Button7.grid(column=0, row=3, sticky=(W, N, E, S))
Button8.grid(column=1, row=3, sticky=(W, N, E, S))
Button9.grid(column=2, row=3, sticky=(W, N, E, S))
Button_division.grid(column=3, row=3, sticky=(W, N, E, S))

    # tercer fila de botones
Button4.grid(column=0, row=4, sticky=(W, N, E, S))
Button5.grid(column=1, row=4, sticky=(W, N, E, S))
Button6.grid(column=2, row=4, sticky=(W, N, E, S))
Button_multiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

    # cuarta fila de botones
Button1.grid(column=0, row=5, sticky=(W, N, E, S))
Button2.grid(column=1, row=5, sticky=(W, N, E, S))
Button3.grid(column=2, row=5, sticky=(W, N, E, S))
Button_suma.grid(column=3, row=5, sticky=(W, N, E, S))

    # quinta fila de botones
Button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
Button_punto.grid(column=2, row=6, sticky=(W, N, E, S))
Button_resta.grid(column=3, row=6, sticky=(W, N, E, S))

    # Sexta fila de botones
Button_igual.grid(column=0, row=7, sticky=(W, N, E, S))
Button_potencia.grid(column=1, row=7, sticky=(W, N, E, S))
Button_menor.grid(column=2, row=7, sticky=(W, N, E, S))
Button_mayor.grid(column=3, row=7, sticky=(W, N, E, S))

for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)


root.mainloop()


