import tkinter as tk
from tkinter import simpledialog, messagebox
import math
import turtle
import time
import random
import string
from datetime import datetime
from tkinter import filedialog

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '  
}

def cl():
    num = simpledialog.askfloat("Ingresar número", "Por favor, ingresa un número:")
    if num is not None:
        logaritmo = math.log(num)
        messagebox.showinfo("Resultado", f"El logaritmo de {num} es {logaritmo:.2f}")

def cs():
    num = simpledialog.askfloat("Ingresar número", "Por favor, ingresa un número:")
    if num is not None:
        seno = math.sin(num)
        messagebox.showinfo("Resultado", f"El seno de {num} es {seno:.2f}")

def cc():
    num = simpledialog.askfloat("Ingresar número", "Por favor, ingresa un número:")
    if num is not None:
        coseno = math.cos(num)
        messagebox.showinfo("Resultado", f"El coseno de {num} es {coseno:.2f}")

def ct():
    num = simpledialog.askfloat("Ingresar número", "Por favor, ingresa un número:")
    if num is not None:
        tangente = math.tan(num)
        messagebox.showinfo("Resultado", f"La tangente de {num} es {tangente:.2f}")

def cf():
    num = simpledialog.askinteger("Ingresar número", "Por favor, ingresa un número:")
    if num is not None:
        r = 1
        i = 2
        while i <= num:
            r *= i
            i += 1
        messagebox.showinfo("Resultado", f"El factorial de {num} es {r:.2f}")

def cm():
    def texto_a_morse(texto):
        texto = texto.upper()
        morse = []
        for letra in texto:
            if letra in morse_code:
                morse.append(morse_code[letra])
            else:
                morse.append(' ')
        return ' '.join(morse)

    texto = simpledialog.askstring("Ingresar texto", "Por favor, ingresa un texto:")
    if texto is not None:
        codigo_morse = texto_a_morse(texto)
        messagebox.showinfo("Resultado", f"El código Morse de '{texto}' es: {codigo_morse}")

def cb(): 
    num = simpledialog.askinteger("Ingresar número", "Por favor, ingresa un número:") 
    if num is not None: 
        binario = bin(num)   
        messagebox.showinfo("Resultado", f"El número binario de {num} es {binario}") 
        
def ch(): 
    num = simpledialog.askinteger("Ingresar número", "Por favor, ingresa un número:") 
    if num is not None: 
        hexadecimal = hex(num) 
        messagebox.showinfo("Resultado", f"El número hexdecimal de {num} es {hexadecimal}") 

def co(): 
    num = simpledialog.askinteger("Ingresar número", "Por favor, ingresa un número:") 
    if num is not None: 
        octadecimal = oct(num) 
        messagebox.showinfo("Resultado", f"El número octadecimal de {num} es {octadecimal}")

def gr():
    ventana_ruleta = turtle.Screen()
    ventana_ruleta.title("Ruleta de 10 números")
    ruleta = turtle.Turtle()
    ruleta.speed(0)

    def girar_ruleta():
        ruleta.penup()
        ruleta.goto(0, 0)
        ruleta.pendown()
        for i in range(30):
            ruleta.clear()
            numero = random.randint(1, 30)
            ruleta.write(f"Número: {numero}", align="center", font=("Arial", 20, "normal"))
            ventana_ruleta.update()
            time.sleep(0.1)
        ruleta.clear()
        ruleta.write(f"Número: {numero}", align="center", font=("Arial", 20, "normal"))

    ruleta.penup()
    ruleta.goto(0, -200)
    ruleta.pendown()
    ruleta.circle(200)

    boton_girar = turtle.Turtle()
    boton_girar.penup()
    boton_girar.goto(0, -250)
    boton_girar.pendown()
    boton_girar.write("Girar", align="center", font=("Arial", 16, "normal"))

    def clic_girar(x, y):
        if -50 < x < 50 and -260 < y < -240:
            girar_ruleta()

    ventana_ruleta.onclick(clic_girar)
    ventana_ruleta.mainloop()

def agr():
    gr()

def cp():

    monto_factura = simpledialog.askfloat("Monto de la Factura", "Ingrese el monto de la factura:")
    if monto_factura is None:
        return "No se a ingresado el valor"
    

    porcentaje_propina = simpledialog.askfloat("Porcentaje de Propina", "Ingrese el porcentaje de propina:")
    if porcentaje_propina is None:
        return "No se a ingresado el valor"
    propina = (monto_factura * porcentaje_propina) / 100
    
    
    total = monto_factura + propina
    
    
    mensaje = f"Subtotal: ${monto_factura:.2f}\nPropina ({porcentaje_propina}%): ${propina:.2f}\nTotal a pagar: ${total:.2f}"
    messagebox.showinfo("Resultado", mensaje)

def t():
    segundos = simpledialog.askinteger("Configurar Temporizador", "Ingresa la duración del temporizador (segundos):")
    if segundos is None:
        return

    ventana_temporizador = tk.Toplevel()
    ventana_temporizador.title("Temporizador")

    tiempo_restante_label = tk.Label(ventana_temporizador, text=f"Tiempo restante: {segundos} segundos", font=("Arial", 16))
    tiempo_restante_label.pack(padx=20, pady=20)

    for i in range(segundos, -1, -1):
        minutos_restantes = i // 60 
        segundos_restantes = i % 60
        mensaje = f"Tiempo restante: {minutos_restantes} minutos {segundos_restantes} segundos"
        tiempo_restante_label.config(text=mensaje)
        ventana_temporizador.update()
        time.sleep(1)

    mensaje = "¡Tiempo agotado!"
    tiempo_restante_label.config(text=mensaje)
    ventana_temporizador.update()
    time.sleep(2)
    ventana_temporizador.destroy()

def gc():
    longitud = simpledialog.askinteger("tamaño de la contraseña", "Ingrese la longitud de la contraseña:")
    if longitud is not None:
        contrasena = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longitud))
        messagebox.showinfo("Contraseña generada", f"Contraseña generada: {contrasena}")

def p():
    def es_palindromo(palabra):
        palabra = palabra.lower()
        return palabra == palabra[::-1]

    palabra = simpledialog.askstring("Palabra", "Ingrese la palabra:")

    if es_palindromo(palabra):
        messagebox.showinfo("Palabra",f"La palabra {palabra} es palindromo")
    else:
        messagebox.showinfo("Palabra",f"La palabra {palabra} no es palindromo")


def cdm():
    try:
        num = simpledialog.askinteger("número", "Ingrese el número:")
        
        medida_en_centimetros = num * 100
        medida_en_kilometros = num / 1000
        medida_en_millas = num * 0.000621371
        medida_en_milimetros = num * 1000
        
        messagebox.showinfo("conversion",f"La medida en metros {num} en centimetros es {medida_en_centimetros}")
        messagebox.showinfo("conversion",f"La medida en metros {num} en kilometros es {medida_en_kilometros}")
        messagebox.showinfo("conversion",f"La medida en metros {num} en millas es {medida_en_millas}")
        messagebox.showinfo("conversion",f"La medida en metros {num} en milimetros es {medida_en_milimetros}")
        
    
    except ValueError:
        messagebox.showinfo("Error",f"ingrese bien los datos")

def cde():     
    year_actual = datetime.now().year

    while True:
        try:
            year_nacimiento = simpledialog.askinteger("Ingrese año de nacimiento","Por favor, ingresa tu año de nacimiento (ejemplo: 1990): ")
            break
        except ValueError:
            messagebox.showinfo("Entrada no válida","Ingresa un año válido.")

    edad = year_actual - year_nacimiento
    messagebox.showinfo("edad",f"Tienes {edad} años.")

    
lista = "Elige una opción:\n1. Piedra\n2. Papel\n3. Tijera"

def get_user_choice():
    user_choice = simpledialog.askinteger("Elige una opción", lista)
    return user_choice

def get_computer_choice():
    return random.randint(1, 3)

def play_game():
    user_choice = get_user_choice()
    if user_choice is not None and 1 <= user_choice <= 3:
        options = ["piedra", "papel", "tijera"]
        User = options[user_choice - 1]

        computer_choice = get_computer_choice()
        Computer = options[computer_choice - 1]

        messagebox.showinfo("Elecciones", f"Tú eliges: {User}\nPC eligió: {Computer}\n...")

        if User == Computer:
            messagebox.showinfo("Resultado", "Empate")
        elif (User == "piedra" and Computer == "tijera") or (User == "papel" and Computer == "piedra") or (User == "tijera" and Computer == "papel"):
            messagebox.showinfo("Resultado", "Ganaste")
        else:
            messagebox.showinfo("Resultado", "Perdiste")
    else:
        messagebox.showwarning("Error", "Debes elegir una opción válida (1, 2 o 3)")

def calcular_imc(peso, altura):
    try:
        altura_metros = altura / 100
        imc = peso / (altura_metros ** 2)
        return imc
    except ZeroDivisionError:
        return "Altura no válida"

def calcular():
    try:
        peso = simpledialog.askfloat("Calcular IMC", "Ingrese su peso en kilogramos:")
        altura = simpledialog.askfloat("Calcular IMC", "Ingrese su altura en centímetros:")
        imc = calcular_imc(peso, altura)

        if isinstance(imc, float):
            messagebox.showinfo("Resultado", "Su índice de masa corporal (IMC) es {:.2f}".format(imc))
        else:
            messagebox.showwarning("Resultado", imc)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para peso y altura.")



AHORCADO = ['''
  +---+
  |     |
        |
        |
        |
        |
=========''',
'''
  +---+
  |     |
  O     |
        |
        |
        |
=========''',
'''
  +---+
  |     |
  O     |
  |     |
        |
        |
=========''',
'''
  +---+
  |     |
  O     |
 /|     |
        |
        |
========='''
'''
  +---+
  O     |
 /|\    |
        |
        |
=========''',
'''
  +---+
  |     |
  O     |
 /|\    |
 /      |
        |
=========''',
'''
  +---+
  |     |
  O     |
 /|\    |
 / \    |
        |
=========''']

palabras = 'valoracion aprenderpython pneumonoultramicroscopicsilicovolcanoconiosis comida juego python web imposible variable curso volador cabeza reproductor mirada escritor billete lapicero celular valor revista gratuito disco voleibol anillo estrella'.split()

def buscarPalabraAleat(listaPalabras):
    palabraAleatoria = random.randint(0, len(listaPalabras) - 1)
    return listaPalabras[palabraAleatoria]

def displayBoard(palabraSecreta, letraIncorrecta, letraCorrecta):
    ahorcado_idx = min(len(letraIncorrecta), len(AHORCADO) - 1)
    ahorcado = AHORCADO[ahorcado_idx]

    display = ahorcado + "\n\n"
    display += f"Letras incorrectas: {' '.join(letraIncorrecta)}\n\n"

    for letra in palabraSecreta:
        if letra in letraCorrecta:
            display += letra + ' '
        else:
            display += '_ '

    return display

def elijeLetra(letrasElegidas):
    while True:
        letra = simpledialog.askstring("Adivina una letra", "Elige una letra:")
        letra = letra.lower()

        if len(letra) != 1:
            messagebox.showwarning("Error", "Por favor, ingresa una sola letra.")
        elif letra in letrasElegidas:
            messagebox.showwarning("Error", "Ya has elegido esa letra. Intenta con otra.")
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            messagebox.showwarning("Error", "Por favor, elige una letra del alfabeto.")
        else:
            return letra

def jugar():
    palabraSecreta = buscarPalabraAleat(palabras)
    letraIncorrecta = ""
    letraCorrecta = ""
    finJuego = False

    while True:
        display = displayBoard(palabraSecreta, letraIncorrecta, letraCorrecta)
        messagebox.showinfo("Ahorcado", display)

        letra = elijeLetra(letraIncorrecta + letraCorrecta)

        if letra in palabraSecreta:
            letraCorrecta += letra
            letrasEncontradas = all(letra in letraCorrecta for letra in palabraSecreta)

            if letrasEncontradas:
                mensaje = f"¡Muy bien! La palabra secreta es '{palabraSecreta}'. ¡Has ganado!"
                messagebox.showinfo("Ahorcado", mensaje)
                finJuego = True
        else:
            letraIncorrecta += letra

            if len(letraIncorrecta) == len(AHORCADO) - 1:
                display = displayBoard(palabraSecreta, letraIncorrecta, letraCorrecta)
                messagebox.showinfo("Ahorcado", display)
                mensaje = f"¡Te has quedado sin letras! La palabra era '{palabraSecreta}'."
                messagebox.showinfo("Ahorcado", mensaje)
                finJuego = True

        if finJuego:
            respuesta = messagebox.askyesno("Ahorcado", "¿Quieres jugar de nuevo?")
            if respuesta:
                palabraSecreta = buscarPalabraAleat(palabras)
                letraIncorrecta = ""
                letraCorrecta = ""
                finJuego = False
            else:
                break

def bdn():

    def guardar_archivo():
        contenido = texto.get("1.0", "end-1c")
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

        if archivo:
            with open(archivo, "w") as file:
                file.write(contenido)

    def abrir_archivo():
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

        if archivo:
            with open(archivo, "r") as file:
                contenido = file.read()
                texto.delete("1.0", tk.END)
                texto.insert(tk.END, contenido)

    v = tk.Tk()
    v.title("Bloc de Notas")

    texto = tk.Text(v)
    texto.pack()

    gby = tk.Button(v, text="Guardar", command=guardar_archivo)
    gby.pack()

    aby = tk.Button(v, text="Abrir", command=abrir_archivo)
    aby.pack()

    v.mainloop()

def cdt():
    def convertir():
        try:
            valor = float(ev.get())
            unidad_origen = cuo.get()
            unidad_destino = cud.get()

            if unidad_origen == unidad_destino:
                resultado = valor
            elif unidad_origen == "Celsius" and unidad_destino == "Fahrenheit":
                resultado = (valor * 9/5) + 32
            elif unidad_origen == "Celsius" and unidad_destino == "Kelvin":
                resultado = valor + 273.15
            elif unidad_origen == "Fahrenheit" and unidad_destino == "Celsius":
                resultado = (valor - 32) * 5/9
            elif unidad_origen == "Fahrenheit" and unidad_destino == "Kelvin":
                resultado = (valor + 459.67) * 5/9
            elif unidad_origen == "Kelvin" and unidad_destino == "Celsius":
                resultado = valor - 273.15
            elif unidad_origen == "Kelvin" and unidad_destino == "Fahrenheit":
                resultado = (valor * 9/5) - 459.67
            else:
                lr.config(text="Seleccione unidades válidas")

            lr.config(text=f"{valor} {unidad_origen} son {resultado} {unidad_destino}")
        except ValueError:
            lr.config(text="Ingrese un valor válido")

    v = tk.Tk()
    v.title("Conversor de Temperatura")

    f = tk.Frame(v)
    f.pack(padx=20, pady=20)

    lv = tk.Label(f, text="Valor:")
    lv.pack()

    ev = tk.Entry(f)
    ev.pack()

    cuo = tk.StringVar()
    cuo.set("Celsius")

    cud = tk.StringVar()
    cud.set("Fahrenheit")

    o = ["Celsius", "Fahrenheit", "Kelvin"]
    mdo = tk.OptionMenu(f, cuo, *o)
    mdo.pack()

    mdd = tk.OptionMenu(f, cud, *o)
    mdd.pack()

    bc = tk.Button(f, text="Convertir", command=convertir)
    bc.pack()

    lr = tk.Label(f, text="")
    lr.pack()

    v.mainloop()

def ldt():
    def agregar_tarea():
        tarea = entry_tarea.get()
        if tarea:
            lista_tareas.insert(tk.END, tarea)
            entry_tarea.delete(0, tk.END)

    def eliminar_tarea():
        seleccion = lista_tareas.curselection()
        if seleccion:
            lista_tareas.delete(seleccion)

    v = tk.Tk()
    v.title("Gestión de Tareas")

    frame = tk.Frame(v)
    frame.pack(padx=20, pady=20)

    entry_tarea = tk.Entry(frame, width=30)
    entry_tarea.grid(row=0, column=0, padx=5, pady=5)

    boton_agregar = tk.Button(frame, text="Agregar Tarea", command=agregar_tarea)
    boton_agregar.grid(row=0, column=1, padx=5, pady=5)

    boton_eliminar = tk.Button(frame, text="Eliminar Tarea", command=eliminar_tarea)
    boton_eliminar.grid(row=0, column=2, padx=5, pady=5)

    lista_tareas = tk.Listbox(frame, width=40, height=10)
    lista_tareas.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

    v.mainloop()

def cps():
    def clasificar_palabra():
        palabra = entrada_palabra.get().strip().lower()
        num_silabas = contar_silabas(palabra)

        if num_silabas > 3:
            resultado.config(text="Sobreesdrújula")
        elif num_silabas == 3:
            resultado.config(text="Esdrújula")
        elif num_silabas == 2 and palabra[-1] in "aeiouáéíóú":
            resultado.config(text="Grave (Llana)")
        elif num_silabas == 1 and (palabra[-1] in "nrs" or palabra[-2:] in ["st", "sp", "ck"]):
            resultado.config(text="Aguda")
        else:
            resultado.config(text="Grave (Llana)")

    def contar_silabas(palabra):
        vocales = "aeiouáéíóú"
        silabas = 0
        i = 0

        while i < len(palabra):
            if palabra[i] in vocales:
                silabas += 1
                while i < len(palabra) and palabra[i] in vocales:
                    i += 1
            else:
                i += 1

        return silabas

    ventana = tk.Tk()
    ventana.title("Clasificador de Palabras")

    etiqueta = tk.Label(ventana, text="Ingrese una palabra:")
    etiqueta.pack()

    entrada_palabra = tk.Entry(ventana)
    entrada_palabra.pack()

    boton_clasificar = tk.Button(ventana, text="Clasificar", command=clasificar_palabra)
    boton_clasificar.pack()

    resultado = tk.Label(ventana, text="")
    resultado.pack()

    ventana.mainloop()

def ctt():
    def calcular_tipo_triangulo():
        angulo1 = float(angulo1_entry.get())
        angulo2 = float(angulo2_entry.get())
        angulo3 = float(angulo3_entry.get())
    
        if angulo1 + angulo2 + angulo3 == 180:
            if angulo1 == angulo2 == angulo3:
                resultado_label.config(text="Es un triángulo equilátero")
            elif angulo1 == angulo2 or angulo1 == angulo3 or angulo2 == angulo3:
                resultado_label.config(text="Es un triángulo isósceles")
            else:
                resultado_label.config(text="Es un triángulo escaleno")
        else:
            resultado_label.config(text="No es un triángulo válido")

    ventana = tk.Tk()
    ventana.title("Tipo de Triángulo")

    angulo1_label = tk.Label(ventana, text="Ángulo 1:")
    angulo1_label.pack()
    angulo1_entry = tk.Entry(ventana)
    angulo1_entry.pack()

    angulo2_label = tk.Label(ventana, text="Ángulo 2:")
    angulo2_label.pack()
    angulo2_entry = tk.Entry(ventana)
    angulo2_entry.pack()

    angulo3_label = tk.Label(ventana, text="Ángulo 3:")
    angulo3_label.pack()
    angulo3_entry = tk.Entry(ventana)
    angulo3_entry.pack()

    calcular_button = tk.Button(ventana, text="Calcular", command=calcular_tipo_triangulo)
    calcular_button.pack()

    resultado_label = tk.Label(ventana, text="")
    resultado_label.pack()

    ventana.mainloop()



ventana = tk.Tk()
ventana.title("Proyecto SENA")

ventana.geometry("1359x900")

marco_botones = tk.Frame(ventana)
marco_botones.pack(expand=True)

mensajes = [
    "Logaritmo",
    "Seno",
    "Coseno",
    "Tangente",
    "Factorial",
    "Código Morse",
    "Número Hexadecimal",
    "Número Binario",
    "Número Octadecimal",
    "Programa aleatorio",
    "Calcular Propina",
    "Temporarizador",
    "Generador-contraseña",
    "Palindromo",
    "Conversor desde metros",
    "Conversor de edad",
    "Piedra, papel o tijera",
    "Calcular IMC",
    "Ahorcado",
    "Bloc de notas",
    "Conversor de temperatura",
    "Lista de Tareas",
    "Clasificador de palabras",
    "Calcular tipo de triangulo"
    

]

funciones = [
    cl,
    cs,
    cc,
    ct,
    cf,
    cm,
    ch,
    cb,
    co,
    agr,
    cp,
    t,
    gc,
    p,
    cdm,
    cde,
    play_game,
    calcular,
    jugar,
    bdn,
    cdt,
    ldt,
    cps,
    ctt,

]

fila_actual = 0
columna_actual = 0

for mensaje, funcion in zip(mensajes, funciones):
    boton = tk.Button(marco_botones, text=mensaje, font=("Arial", 14), command=funcion)
    boton.grid(row=fila_actual, column=columna_actual, padx=10, pady=10)
    columna_actual += 1
    if columna_actual == 3:
        columna_actual = 0
        fila_actual += 1

ventana.mainloop()