from tkinter import Tk, Label, ttk, Button, Frame, Entry, messagebox 
 
class Juego(Tk): 
    def __init__(self, dificultad, aciertos, fallos): 
        super().__init__() 
        self.title('Wordle Equipo 8') 
        self.minsize(1024, 640) 
 
        self.aciertos = aciertos 
        self.fallos = fallos 
        self.dificultad = int(dificultad) 
        self.gana = False 
        self.intento = 1 
 
        text = f'Aciertos:{aciertos} Fallos:{fallos}' 
        titulo = Label(self, text = text, font = ('Helvetica', 24, 'bold')) 
        titulo.pack(pady = 20) 
        self.palabra_escogida = self.escoger() 
        self.ejecutar() 
 
    def escoger(self): 
        return 'hola' 
 
    def ejecutar(self): 
        # Elementos de la ventana 
        titulo = Label(self, text = 'Escribe la palabra:', font = ('Helvetica', 16, 'bold')) 
        titulo.pack(pady = 20) 
 
        self.input = Entry(self, font =('Helvetica', 12)) 
        self.input.pack(fill='x', padx = 50) 
 
        # Botón para hacer un intento 
        boton_intento = Button(self, text = 'Intentar', font = ('Helvetica', 12, 'bold'), bg='dodger blue', fg='white') 
        boton_intento.pack(pady = 10) 
        boton_intento.bind("<Button-1>", self.dibujar_palabra) 
 
        # Espacio donde saldrán los resultados 
        self.frame_intento = Frame(self, width = 400, height=400) 
        self.frame_intento.pack(pady = 10) 
 
        # Botón para hacer un intento 
        boton_termina = Button(self, text = 'Terminar partida', font = ('Helvetica', 12, 'bold'), bg='red3', fg='white') 
        boton_termina.pack(pady = 10) 
        boton_termina.bind("<Button-1>", self.otra_partida) 
 
    def intentar_palabra(self): 
        pass 
 
    def dibujar_palabra(self, evento): 
        palabra = self.input.get() 
 
        if len(palabra) != self.dificultad: 
            messagebox.showinfo(title="Error",message=f'La palabra que ingresó es no válida. Por favor ingrese una palabra de tamaño {self.dificultad}') 
            return 
 
        #colores = self.intentar_palabra(palabra) 
        color_palabra = ['gris','gris','gris','gris','gris'] 
 
        tam_grid = 30//self.dificultad 
 
        for i in range(self.dificultad): 
            colores = {'gris': 'gray', 'amarillo': 'orange', 'verde': 'lime green'} 
 
            celda = Label(self.frame_intento, text = palabra[i].upper(), width = tam_grid, height = 3, bg = colores[color_palabra[i]], fg='white', font=('Helvetica', 12, 'bold')) 
            celda.grid(row = self.intento, column = i, padx = 2, pady = 2) 
 
        self.intento += 1 
 
        if palabra == self.palabra_escogida: 
            messagebox.showinfo(message=f"¡¡Ganaste!!", title="Partida terminada") 
            self.gana = True 
            self.otra_partida() 
            return 
         
        if self.intento == 7: 
            messagebox.showinfo(message=f"Perdiste", title="Partida terminada") 
            self.otra_partida() 
            return        
 
    def otra_partida(self, evento = None): 
        from Inicio import Inicio 
        self.destroy() 
        if self.gana: 
            ventana = Inicio(self.aciertos+1, self.fallos) 
        else: 
            ventana = Inicio(self.aciertos, self.fallos+1) 
        ventana.mainloop()     
 
 
if __name__ == '__main__': 
    ventana = Juego(4,0,0) 
    ventana.mainloop()