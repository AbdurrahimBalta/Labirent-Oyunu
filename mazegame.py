# Part 1: Setting up the maze

import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Fare oyunu")
wn.setup(700, 700)
wn.tracer(0)

# Register shapes
images = ["faresola.gif","fare.gif","duvar.gif","peynir.gif","fareyukari.gif","fareasagi.gif"]
for image in images:
    turtle.register_shape(image)

# Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("duvar.gif")
        self.color("white")
        self.penup()
        self.speed(0)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("fare.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0
        self.numberOfSteps = 0


    def go_up(self):
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

        player.numberOfSteps += 1

    def go_down(self):
        # Calculate the spot to move to
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        # Check if the space has a wall
        if(move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

        player.numberOfSteps += 1

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        
        player.numberOfSteps += 1

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

        player.numberOfSteps += 1

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle() 

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("peynir.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


class AImouse(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape("faresola.gif")
        self.color("red")
        self.penup()
        self.goto(x, y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx = 0
            dy = 24
            self.shape("fareyukari.gif")
        elif self.direction == "down":
            dx = 0
            dy = -24
            self.shape("fareasagi.gif")
        elif self.direction == "left":
            dx = -24
            dy = 0
            self.shape("faresola.gif")
        elif self.direction == "right":
            dx = 24
            dy = 0
        else:
            dx = 0
            dy = 0
        # Calculate the spot to move to
        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        # Check if the space has a wall
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            # Choose a different direction
            self.direction = random.choice(["up", "down", "right", "left"])
        
        # set timer to move next time
        turtle.ontimer(self.move, t=random.randint(100, 300))

        
    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

   
        


# Create levels list
levels = [""]

# Define levels list
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP              XXX   XXX",
    "XXXX   XXXXX    XXX   XXX",
    "XXXX    XXXXXXX XXX   XXX",
    "XXXXX                  XX",
    "XXXXXXXXXXXXXX   XXX  XXX",
    "XXX            XXXXXX  XX",
    "X  XX   XXXX    XX  XX  X",
    "X  XXX  XXXXX  XXX  XXXXX",
    "X  XXX   XXXX       X  XX",
    "X       XX     XXXXXX  XX",
    "X    X    XXX          XX",
    "X    XXXXXXX   XXXXXX  XX",
    "XXX  X  XX     X  XXXXXXX",
    "XXX  XXXXX  E X        XX",
    "XXX   XXXX      XXXXX  XX",
    "XXX            XXXX    XX",
    "XXXE XXXXXXXXXXXT    XXXX",
    "XXX XX  XXX   XXXX   XXXX",
    "XXXX   XX XXX        XXXX",
    "XXXT    XX     XXX    XXX",
    "XXXXXXX      XX    XXXXXX",
    "XX    XXXXXXXXX  XXXXXXXX",
    "XXX    XXXXX      XXXXXXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]
# Add a traseres list
treasures = []
# Add enemies list
enemies = []
# Add maze to mazes list
levels.append(level_1)

# Create Level Setup Function


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the character at each x,y coordinate
            # NOte the order of y and s in the next line
            character = level[y][x]
            # Calculate the screen x, y coodinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (representing a wall)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                # ADD coordinates to wall list
                walls.append((screen_x, screen_y))

            # Check if it is an P (representing a wall)
            if character == "P":
                player.goto(screen_x, screen_y)

            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
            #Check if it is an E (representing enemy) 
            if character == "E":
                enemies.append(AImouse(screen_x,screen_y))

# Create class instances
pen = Pen()
player = Player()

# Create wall coordinate list
walls = []

# Set up the level
setup_maze(levels[1])

# Keyboard Binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_down, "Down")
turtle.onkey(player.go_up, "Up")

# Turn off screen updates
wn.tracer(0)

#Start moving enemies
for enemy in enemies:
    turtle.ontimer(enemy.move, t=250)
    

# Main Game Loop
while True:
    turtle.listen()
    # Check for player collision with trasure
    # iterate through treasure list
    for treasure in treasures:
        if player.is_collision(treasure):
            # Add the treasure gold to the player gold
            player.gold += treasure.gold
            
            print("Player Gold : {}".format(player.gold))
            print("Player toplam adim sayisi : {}".format(player.numberOfSteps))
            # Destroy the treasure
            treasure.destroy()
            # Remove the treasure form the treasures list
            treasures.remove(treasure)

    for enemy in enemies:
        turtle.listen()
        if player.is_collision(enemy):
            player.gold = 0
            player.destroy()
            print("player dies")
            print("Player toplam adim sayisi : {}".format(player.numberOfSteps))

        if turtle.onkey(player.go_right,"Right"):
            print("Player toplam adim sayisi : {}".format(player.numberOfSteps))
            

        

     # Update screen
    wn.update()