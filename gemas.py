import turtle
import random
#Configurar pantalla
pantalla = turtle.Screen()
pantalla.title("Videojuego")
pantalla.bgpic("ingresar_ruta")
pantalla.setup(width=800,height=600)

#Crear personaje
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("green")
tortuga.penup()
pantalla.mainloop()
