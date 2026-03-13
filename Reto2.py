import turtle
#no se puede hacer con 4 y 6, porque seria un cuadrado y un hexagono no una estrella
def estrella(puntas, tamano):
    t = turtle.Turtle()
    t.speed(5)
    
    if puntas % 2 != 0:
        angulo = 180 - (180 / puntas) #formula para tener los angulos y que salga la estrella
    else:
        angulo = 135 

    for _ in range(puntas):
        t.forward(tamano)
        t.right(angulo)
    
    turtle.done()

num_puntas = int(input("Introduce el número de puntas: "))
estrella(num_puntas, 200)