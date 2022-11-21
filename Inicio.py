from tkinter import Tk, Label, ttk, Button, Frame


class Inicio(Tk):
    def __init__(self, aciertos, fallos):
        # Configuracion basica de la pantall
        super().__init__()
        self.title('Wordle Equipo 8')
        self.minsize(960, 540)

        # Se guarda la cantidad de aciertos y de fallos, luego se presentan en la ventana
        self.aciertos = aciertos
        self.fallos = fallos
        text = f'Aciertos: {aciertos}              Fallos: {fallos}'
        Label(self, text=text, font=('Helvetica', 15, 'bold')).pack(
            pady=10, padx=20, anchor='w')

        # Se pone el titulo principal del Juego
        Label(self, text='Wordle - Equipo #8',
              font=('Helvetica', 24, 'bold')).pack(pady=20)

        # Seleccion de la dificultad del juego
        Label(self, text='Por favor seleccione una dificultad',
              font=('Helvetica', 12, 'bold')).pack(pady=30)

        # Combobox para la seleccion de la dificultad
        self.combo = ttk.Combobox(
            self, values=["4", "5", "6", "7", "8"], state='readOnly', height=2, width=15, font=('Helvetica', 11, 'bold'))
        self.combo.set("4")
        self.combo.pack()

        # Boton para iniciar el juego
        boton1 = Button(self, text="Continuar", bg='dodger blue', height=2,
                        width=10, font=('Helvetica', 11, 'bold'), fg='white')
        boton1.pack(anchor='c', pady=20)
        boton1.bind("<Button-1>", self.crearJuego)

    def crearJuego(self, evento):
        '''Funcion para inicializar la ventana de creacion del juego'''
        from Juego import Juego

        # Se obtiene la dificultad seleccionada por el usuario
        dificultad = self.combo.get()

        # Se destruye la ventana actual
        self.destroy()

        # Se inicializa la ventana del juego
        ventana = Juego(dificultad, self.aciertos, self.fallos)
        ventana.mainloop()


if __name__ == '__main__':
    ventana = Inicio(0, 0)
    ventana.mainloop()
