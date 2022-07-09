import turtle
import os
import math
import random
# import winsound
#176th line
import pyautogui
from subprocess import call

# 1 set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
#25. 
wn.bgpic("ik.png")
#29.
wn.tracer(0)


#26. register the shapes
turtle.register_shape("player.gif")
turtle.register_shape("enemy.gif")
turtle.register_shape("yellowlaser.gif")
turtle.register_shape("p01.gif")
turtle.register_shape("p02.gif")
turtle.register_shape("gameover.gif")

#23. set score 0 
score = 0
# draw score
score_pen = turtle.Turtle()
score_pen.speed(0)  # 0 fastest
score_pen.penup()
score_pen.setposition(-610, 20)
scorestring = "%s" %score
score_pen.write(scorestring, False, align="left", font=("horta", 34, "bold"))
score_pen.hideturtle()

#23. set death 0 
death = 0
# draw score
death_pen = turtle.Turtle()
death_pen.speed(0)  # 0 fastest
death_pen.penup()
death_pen.setposition(740, 20)
deathstring = "%s" %death
death_pen.write(deathstring, False, align="left", font=("horta", 34, "bold"))
death_pen.hideturtle()

# 4 Create a player turtle
player = turtle.Turtle()

#27.
#(4) player.shape("triangle")
player.shape("player.gif")

#4
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
playerspeed = 25

last01 = turtle.Turtle()
last01.shape("p01.gif")
last01.penup()
last01.speed(0)
last01.setposition(-2, -150)
last01.hideturtle()

last02 = turtle.Turtle()
last02.shape("p02.gif")
last02.penup()
last02.speed(0)
last02.setposition(-2, 150)
last02.hideturtle()

gameover = turtle.Turtle()
gameover.shape("gameover.gif")
gameover.shapesize(0.5,0.5)
gameover.penup()
gameover.speed(0)
gameover.setposition(-2, -10)
gameover.hideturtle()


# 15.choose no. of enemies
no_of_enemies = 10
#create an empty list
enemies = []
# add enemies to list
for i in range(no_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("enemy.gif")
    #15.
    enemy.penup()
    enemy.speed(0)
    #16. random positions
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x, y)
enemyspeed = 0.2

# 8 create bullet
bullet = turtle.Turtle()
bullet.shape("yellowlaser.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
bulletspeed = 5

# bullet states
# ready = ready to fire
# fire  = bullet is firing
bulletstate = "ready"  # coz on start of game we got bulletstate as ready

# 5a. movement of player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def move_up():
    y = player.ycor()
    y += playerspeed
    if y > -150:
        y = -150
    player.sety(y)

def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < -280:
        y = -280
    player.sety(y)

# 9.
def fire_bullet():
    # declare bulletstate as a global if it needs changed
    global bulletstate

    if bulletstate == "ready":
        bulletstate = "fire"
        # winsound.PlaySound("paddle.wav",winsound.SND_ASYNC)
        # move bullet just above player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()

def move_last01():
    x = last01.xcor()
    y = last01.ycor() + 5
    if y > 20:
        y = 20
    last01.setposition(x, y)
    last01.showturtle()
    
def move_last02():
    x = last02.xcor()
    y = last02.ycor() - 5
    if y < 10:
        y = 10
    last02.setposition(x, y)
    last02.showturtle()

# 12.for collosion
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 30: 
        xo = t2.xcor()
        yo = t2.ycor() - 10
        return True
    else: return False

# 5b. create controls
turtle.listen()
# when i push left key it's gonna implement the above function
turtle.onkeypress(move_left, "Left")
# when i push left key it's gonna implement the above function
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(move_up, "Up")
turtle.onkeypress(move_down, "Down")
# 10.
turtle.onkeypress(fire_bullet, "space")

# to maximize the window
pyautogui.hotkey("win","up")

# 7 main game loop
while True:
    
    #30.
    wn.update()
    # 18. will make them indented
    for enemy in enemies:
        #7a move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #7b enemy limit
        if enemy.xcor() > 280:
            #21.(to move all the enimies down) and change each enemy to e
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            #22. and change each enemy to e
            for e in enemies:
                y = e.ycor()
                y -= 20
                e.sety(y)
            enemyspeed *= -1

        #19. check for collision (indented for all the enemies)
        if isCollision(bullet, enemy):
            # reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
            # reset the enemy
            #20. randon respawning
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy.setposition(x, y)

            death += 1
            deathstring = "%s" %death
            death_pen.clear()
            death_pen.write(deathstring, False, align="left", font=("horta", 34, "normal"))

            #24. update score
            score += 5
            scorestring = "%s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("horta", 34, "normal"))

        for e in enemies:
            if e.ycor() < -260:
                player.hideturtle()
                for e in enemies:
                    e.hideturtle()
                score_pen.clear()
                death_pen.clear()
                move_last01()
                move_last02()
        
            if last01.ycor() == 20 and last02.ycor() == 10:
                gameover.showturtle()
        
        # 14.
        if isCollision(player, enemy):
            player.hideturtle()
            for e in enemies:
                e.hideturtle()
            score_pen.clear()
            death_pen.clear()
            move_last01()
            move_last02()
        
        if last01.ycor() == 20 and last02.ycor() == 10:
            gameover.showturtle()

    # 11.move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 280:
        bullet.hideturtle()
        bulletstate = "ready"