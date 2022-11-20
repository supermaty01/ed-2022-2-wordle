from tkinter import Tk, Label, ttk, Button, Frame, Entry, messagebox, CENTER
import words
from random import choice
 
class Juego(Tk):
    colores = {'gris': '#787c7e', 'amarillo': '#c9b458', 'verde': '#6aaa64'}
    def __init__(self, dificultad, aciertos, fallos): 
        super().__init__() 
        self.title('Wordle Equipo 8') 
        self.minsize(1024, 640) 
 
        self.aciertos = aciertos 
        self.fallos = fallos 
        self.dificultad = dificultad
        self.gana = False 
        self.intento = 1 
 
        text = f'Aciertos: {aciertos}   Fallos: {fallos}' 
        titulo = Label(self, text = text, font = ('Helvetica', 24, 'bold')) 
        titulo.pack(pady = 20) 
        self.palabra_escogida = self.escoger()
        self.ejecutar() 
 
    def escoger(self): 
        return choice(words.palabras_dict[self.dificultad])
 
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
 
    def procesar_palabra(self, palabra_ingresada):
        resultados_palabra = []
        contador_amarillas = {}
        for i in range(int(self.dificultad)):
            if palabra_ingresada[i] in self.palabra_escogida:
                if self.palabra_escogida[i] == palabra_ingresada[i]:
                    resultados_palabra.append('verde')
                else:
                    if palabra_ingresada[i] not in contador_amarillas:
                        contador_amarillas[palabra_ingresada[i]] = 1
                        resultados_palabra.append('amarillo')
                    elif contador_amarillas[palabra_ingresada[i]] < self.palabra_escogida.count(palabra_ingresada[i]):
                        contador_amarillas[palabra_ingresada[i]] += 1
                        resultados_palabra.append('amarillo')
                    else:
                        resultados_palabra.append('gris')
            else:
                resultados_palabra.append('gris')
        return resultados_palabra

    def dibujar_palabra(self, evento): 
        palabra_ingresada = self.input.get() 
        self.input.delete(0, 'end')
              
        if len(palabra_ingresada) != int(self.dificultad):
            messagebox.showinfo(title="Error",message=f'La palabra que ingresó es no válida. Por favor ingrese una palabra de tamaño {self.dificultad}') 
            return 
        if palabra_ingresada not in words.palabras_set:
            messagebox.showinfo(title="Error",message='La palabra que ingresó es no válida. Por favor ingrese una palabra existente.') 
            return 
        if palabra_ingresada == self.palabra_escogida: 
            for i in range(int(self.dificultad)): 
                celda = Label(self.frame_intento, text = palabra_ingresada[i].upper(), width = 6, height = 3, bg = Juego.colores['verde'], fg='white', font=('Helvetica', 12, 'bold')) 
                celda.grid(row = self.intento, column = i, padx = 2, pady = 2)
                
            messagebox.showinfo(message="¡¡Ganaste!!", title="Partida terminada") 
            self.gana = True 
            self.otra_partida() 
            return 
        
        color_palabra = self.procesar_palabra(palabra_ingresada)
        
 
        for i in range(int(self.dificultad)): 
 
            celda = Label(self.frame_intento, text = palabra_ingresada[i].upper(), width = 6, height = 3, bg = Juego.colores[color_palabra[i]], fg='white', font=('Helvetica', 12, 'bold')) 
            celda.grid(row = self.intento, column = i, padx = 2, pady = 2) 
 
        self.intento += 1 
 
        if self.intento == 7: 
            messagebox.showinfo(message=f"Perdiste", title=f"Partida terminada. La palabra correcta es {self.palabra_escogida}") 
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