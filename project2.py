import turtle

def draw_rectangle():
    window = turtle.Screen()
    window.bgcolor("blue")

    tres = turtle.Turtle()
    tres.shape("turtle")
    tres.color("yellow")
    tres.speed(10)
    for i in range(1,40):
        tres.forward(200)
        tres.left(90)
        tres.forward(100)
        tres.left(90)
        tres.forward(200)
        tres.left(90)
        tres.forward(100)
        tres.left(90)
        tres.left(10)


    #xyz = turtle.Turtle()
    #xyz.shape("arrow")
    #xyz.color("red")
    #xyz.circle(100)
    

    window.exitonclick()

draw_rectangle()

