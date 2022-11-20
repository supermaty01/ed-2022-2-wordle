from tkinter import Tk, Label, ttk, Button 
 
class Inicio(Tk): 
    def __init__(self, aciertos, fallos): 
        super().__init__() 
        self.title('Wordle Equipo 8') 
        self.aciertos = aciertos 
        self.fallos = fallos 
        self.minsize(1024, 640) 
 
        text = f'Aciertos: {aciertos}   Fallos: {fallos}'
        titulo = Label(self, text = text, font = ('Helvetica', 24, 'bold')) 
        titulo.pack(pady = 20) 
 
        titulo = Label(self, text = 'Wordle - Equipo #3', font = ('Helvetica', 24, 'bold')) 
        titulo.pack(pady = 20) 
 
        titulo = Label(self, text = 'Por favor seleccione una dificultad', font = ('Helvetica', 12, 'bold')) 
        titulo.pack(pady = 30) 
         
        self.combo = ttk.Combobox(self, values=["4","5","6","7","8"], state='readOnly', ) 
        self.combo.set("4") 
        self.combo.pack() 
 
        boton1 = Button(self, text = "Continuar") 
        boton1.pack(anchor = 'c', pady=20) 
        boton1.bind("<Button-1>", self.crearJuego) 
 
    def crearJuego(self, evento): 
        from Juego import Juego 
        dificultad = self.combo.get() 
        self.destroy() 
        ventana = Juego(dificultad, self.aciertos, self.fallos) 
        ventana.mainloop() 
 
         
 
 
 
if __name__ == '__main__': 
    ventana = Inicio(0,0) 
    ventana.mainloop() 
    