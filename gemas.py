import turtle
import random
#Configurar pantalla
pantalla = turtle.Screen()
pantalla.title("Videojuego")
pantalla.bgpic("C:/Users/Lab.Computacion/Desktop/Codigo_Futuro/francisco 4e/videojuego/fondo.png")
pantalla.setup(width=800,height=600)

#Crear personaje
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("green")
tortuga.penup()

score = 0
game_over = False

def mover_tortuga():
    global score
    tortuga.forward(20)
    score += 1
pantalla.onkeypress(mover_tortuga,"Up")
pantalla.listen()

pantalla.mainloop()
