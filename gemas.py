import turtle
import random

#Crear Pantalla
pantalla = turtle.Screen()
pantalla.title("Videojuego")
pantalla.bgpic("C:/Users/Lab.Computacion/Desktop/Codigo_Futuro/francisco 3b/videojuego/fondo.png")
pantalla.setup(width=800,height=600)

#Crear personaje
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("green")
tortuga.penup()

#Crear gemas
gemas = []
num_gemas = 6
for i in range(num_gemas):
    gema = turtle.Turtle()
    gema.shape("circle")
    gema.color("blue")
    gema.penup()
    gema.goto(random.randint(-300,300),random.randint(-150,70))
    gemas.append(gema)

obstaculos = []
num_obstaculos = 10
for i in range(num_obstaculos):
    obstaculo = turtle.Turtle()
    obstaculo.shape("square")
    obstaculo.color("red")
    obstaculo.penup()
    obstaculo.goto(random.randint(-300,300),random.randint(-150,70))
    obstaculos.append(obstaculo)

score = 0
game_over = False
def mover_tortuga():
    global score
    tortuga.forward(20)
    score = score + 1
def mover_izq():
    tortuga.left(30)
def mover_der():
    tortuga.right(30)
pantalla.onkeypress(mover_tortuga,"Up")
pantalla.onkeypress(mover_izq,"Left")
pantalla.onkeypress(mover_der, "Right")
pantalla.listen()
pantalla.mainloop()