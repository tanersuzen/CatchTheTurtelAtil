import turtle

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch the Turtle")
FONT = ("Arial",30,"normal")

#score turtle

score_turtle = turtle.Turtle()
score_turtle.color("dark blue")
score_turtle.write(arg="Score: 0", move=False,align="center",font=(FONT))





turtle.mainloop()

