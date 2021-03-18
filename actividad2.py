"Este juego es el juego de la vibora"
"Autores: Alejandro Torre, Daniel Flores"
from turtle import *
from random import randrange
from freegames import square, vector

a = randrange(-200,100,10)
b = randrange(-200,100,10)
food = vector(a,b)
"Agrego variables a y b para que pasen por un randrange para que cada vez que se inicie el juego la comida no estara en el mismo lugar."

snake = [vector(10, 0)]
aim = vector(0, -10)

c= randrange(1,5)

"Genero una variable aleatoria para despues adignarle un color dependiendo del numero con funciones '/if/'"

    
if c==1:
    c="black"
if c==2:
    c="green"
if c==3:
    c="blue"
if c==4:
    c="magenta"
if c==5:
    c="cyan"
        
a= randrange(1,5)

"Genero una variable aleatoria para despues adignarle un color dependiendo del numero con funciones '/if/'"
    
if a==1:
    a="black"
if a==2:
    a="green"
if a==3:
    a="blue"
if a==4:
    a="magenta"
if a==5:
    a="cyan"

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    
    

    for body in snake:
        square(body.x, body.y, 9, c)
    
    

    square(food.x, food.y, 9, a)
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()