import turtle
import random
import tkinter
scr = turtle.Screen()
scr.bgcolor("light gray")
scr.title("Catch The Turtle Game")
FONT = ('Haveltica', 15, 'bold')
turtle_list = []
score = 0
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
play_again_btn = tkinter.Button(bg="dark gray")
game_over = False

def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.penup()
    top_height = scr.window_height() / 2
    y = top_height * 0.9
    score_turtle.setpos(0, y)
    score_turtle.color("black")
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)
def make_turtle():
    t = turtle.Turtle()
    def handle_click(x, y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("#001853")
    t.setposition(random.randint(-250, 250), random.randint(-250, 250))
    turtle_list.append(t)

def setup_turtles():
    for i in range(20):
        make_turtle()


def play_again():
    global game_over, score
    game_over = False
    score = 0
    score_turtle.clear()
    countdown_turtle.clear()
    start_game_up()
    play_again_btn.pack_forget()


def show_turtles_randomly():
    global game_over
    global score
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        scr.ontimer(show_turtles_randomly, 500)
    else:
        hide_turtles()
        if game_over:
            play_again_btn.config(text="Play again", height=5, width=15, command=play_again)
            play_again_btn.pack()

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = scr.window_height() / 2
    y = top_height * 0.7
    countdown_turtle.setposition(0, y)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time Remaining: {time}", move=False, align="center", font=FONT)
        scr.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        if score < 10:
            countdown_turtle.clear()
            countdown_turtle.write(arg=f"Game Over!!: {score}", move=False, align="center", font=FONT)
        elif score >= 10 and score <= 20:
            countdown_turtle.clear()
            countdown_turtle.write(arg=f"You can do better: {score}", move=False, align="center", font=FONT)
        elif score > 20:
            countdown_turtle.clear()
            countdown_turtle.write(arg=f"Congratulations. You win: {score}", move=False, align="center", font=FONT)
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()
def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(5)
    turtle.tracer(1)
start_game_up()
hide_turtles()

turtle.mainloop()
