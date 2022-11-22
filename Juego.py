from tkinter import Tk, Label, ttk, Button, Frame, Entry, messagebox, CENTER, W
import words
from random import choice


class Juego(Tk):
    colores = {'gris': '#787c7e', 'amarillo': '#c9b458', 'verde': '#6aaa64'}

    def __init__(self, dificultad, aciertos, fallos):
        # Configuracion basica de la pantalla
        super().__init__()
        self.title('Wordle Equipo 8')

        # Pantalla completa
        self.minsize(1024, 700)

        # Se guardan caracteristicas basicas de la partida
        self.aciertos = aciertos
        self.fallos = fallos
        self.dificultad = dificultad
        self.gana = False
        self.intento = 1

        # Se muestran los aciertos y fallos
        text = f'Aciertos: {aciertos}              Fallos: {fallos}'
        Label(self, text=text, font=('Helvetica', 15, 'bold')).pack(
            pady=10, padx=20, anchor='w')

        # Se escoge una palabra al azar
        self.palabra_escogida = self.escoger()
        #print(self.palabra_escogida)

        self.ejecutar()

    def escoger(self):
        return choice(words.palabras_dict[self.dificultad])

    def ejecutar(self):
        # Elementos de la ventana
        Label(self, text='Escribe la palabra:',
              font=('Helvetica', 16, 'bold')).pack(pady=10)

        self.input = Entry(self, font=('Helvetica', 12),
                           justify='center', width=50)
        self.input.pack(ipady=3)

        # Botón para hacer un intento
        boton_intento = Button(self, text='Intentar', font=(
            'Helvetica', 12, 'bold'), bg='dodger blue', fg='white', activebackground='dodger blue', activeforeground='white', command=lambda: self.dibujar_palabra())
        boton_intento.pack(pady=10)

        # Espacio donde saldrán los resultados
        self.frame_intento = Frame(self)
        self.frame_intento.pack(pady=10)

        # Botón para hacer un intento
        boton_termina = Button(self, text='Terminar partida', font=(
            'Helvetica', 12, 'bold'), bg='red3', fg='white', activebackground='red3', activeforeground='white', command=lambda: self.otra_partida())
        boton_termina.pack(pady=10)

    def procesar_palabra(self, palabra_ingresada):
        '''Funcion para determinar los colores de cada letra teniendo en cuenta la palabra escogida'''
        # Se van agregando los colores de cada letra
        resultados_palabra = []
        # Sirve para determinar la cantidad de letras amarillas que se han agregado
        contador_amarillas = {}
        #

        # Se itera sobre el tamaño de la palabra
        for i in range(int(self.dificultad)):

            # Si la letra de la palabra ingresada se encuentra en la palabra escogida, en caso contrario se agrega el color gris a la lista
            if palabra_ingresada[i] in self.palabra_escogida:
                # Si la letra es igual a la letra que esta en la misma posicion de la palabra elegida
                if self.palabra_escogida[i] == palabra_ingresada[i]:
                    resultados_palabra.append('verde')
                else:
                    # Si es la primera vez que se encuentra esa letra en la palabra escogida
                    if palabra_ingresada[i] not in contador_amarillas:
                        contador_amarillas[palabra_ingresada[i]] = 1
                        resultados_palabra.append('amarillo')

                    # Si todavia se pueden pintar mas letras de color amarillo
                    elif contador_amarillas[palabra_ingresada[i]] < self.palabra_escogida.count(palabra_ingresada[i]):
                        contador_amarillas[palabra_ingresada[i]] += 1
                        resultados_palabra.append('amarillo')
                    else:
                        resultados_palabra.append('gris')
            else:
                resultados_palabra.append('gris')

        return resultados_palabra

    def dibujar_palabra(self):
        '''Funcion para dibujar la palabra y ingresada y el color de cada letra'''
        # Obtener palabra y limpiar input
        palabra_ingresada = self.input.get().lower()
        self.input.delete(0, 'end')

        # Si la palabra es más grande o más pequeña se le pide que ingrese una nueva palabra
        if len(palabra_ingresada) != int(self.dificultad):
            messagebox.showinfo(
                title="Error", message=f'La palabra que ingresó es no válida. Por favor ingrese una palabra de tamaño {self.dificultad}')
            return

        # Si la palabra ingresada no está en el lemario elegido
        if palabra_ingresada not in words.palabras_set:
            messagebox.showinfo(
                title="Error", message='La palabra que ingresó es no válida. Por favor ingrese una palabra existente.')
            return

        # Si la palabra ingresada corresponde a la palabra elegida
        if palabra_ingresada == self.palabra_escogida:

            # Poner toda la palabra en verde
            for i in range(int(self.dificultad)):
                celda = Label(self.frame_intento, text=palabra_ingresada[i].upper(
                ), width=6, height=3, bg=Juego.colores['verde'], fg='white', font=('Helvetica', 12, 'bold'))
                celda.grid(row=self.intento, column=i, padx=2, pady=2)

            # Mostrar mensaje de que gano la partida
            messagebox.showinfo(message="¡Ganaste!",
                                title="Partida terminada")

            # Gana la partida y lo envia a la pantalla de inicio para que seleccione nuevamente la dificultad
            self.gana = True
            self.otra_partida()
            return

        # Retorna los colores de cada letra de la palabra
        color_palabra = self.procesar_palabra(palabra_ingresada)

        for i in range(int(self.dificultad)):
            #
            celda = Label(self.frame_intento, text=palabra_ingresada[i].upper(
            ), width=6, height=3, bg=Juego.colores[color_palabra[i]], fg='white', font=('Helvetica', 12, 'bold'))
            celda.grid(row=self.intento, column=i, padx=2, pady=2)

        # Se aumenta un intento
        self.intento += 1

        # Si ya completo todos lo intentos muestra mensaje de error
        if self.intento == 7:
            messagebox.showinfo(
                message=f"Partida terminada. La palabra correcta es {self.palabra_escogida}", title=f'Perdiste')
            self.otra_partida()
            return

    def otra_partida(self):
        '''Funcion para jugar otra partida'''
        from Inicio import Inicio
        # Destruye la ventana actual
        self.destroy()

        # Si gano, aumenta unoa los aciertos, si pierde aumenta uno a los fallos
        if self.gana:
            ventana = Inicio(self.aciertos+1, self.fallos)
        else:
            ventana = Inicio(self.aciertos, self.fallos+1)

        ventana.mainloop()
