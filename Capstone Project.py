#SANJANA RAPETA - CAPSTONE PROJECT 
import os
import turtle 
import random
import time 
import math

#main window 
wn = turtle.Screen()
wn.title("Jumping Avenger by Sanjana")
wn.setup(height = 750, width = 1300)
wn.bgpic("splash_screen.gif")
wn.update()
time.sleep(6)
wn.bgpic("background.gif")
wn.tracer(0)

wn.register_shape("background.gif")
wn.register_shape("thor.gif")
wn.register_shape("obstacle.gif")
wn.register_shape("lightning.gif")

#number of lives 
lives = 3

#gravity 
GRAVITY = -0.18

#establish border
class Border(turtle.Turtle):
	def __init__(self): 
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.pensize(5)

#establish player
class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("thor.gif")
		self.shapesize(stretch_wid = 5, stretch_len=2, outline = None)
		self.color("red")
		self.speed(0)
		self.penup()
		self.direction = "Left"
		self.goto(170, -170)
		self.speed = 5
		self.state = "running"
		self.dy = 0
		self.width = 150
		self.height = 130
		self.number_of_lives = 3

#move player
	def move(self): 
		self.goto(self.xcor(), self.ycor())

		if self.direction == "Left": 
			x = self.xcor()
			self.speed = 3
			self.setx(x - self.speed)

		if self.direction == "Right":	
			x = self.xcor()
			self.speed = 3
			self.setx(x + self.speed)
	
		if self.state == "jumping":
			self.sety(self.ycor() + self.dy)
			if self.ycor() <= -175:
				self.sety(-175)
				self.state = "running"
				self.dy = 0
			
		if self.xcor() > 500 or self.xcor() < -550: 
			self.speed = 0
			self.direction = "none"

	def go_left(self): 
		self.direction = "Left"
		self.speed = 3 

	def go_right(self): 
		self.direction = "Right"
		self.speed = 3 

	def jump(self):
		if self.state != "jumping": 
			self.state = "jumping"
			self.dy = 10		

	def update_number_of_lives(self):
		pen.clear()
		pen.write("Lives: {}" .format(self.number_of_lives), align = "center", font = ("Times New Roman", 30, "normal"))
	
	def change_number_of_lives(self, lives): 
		self.number_of_lives -= lives
		self.update_number_of_lives()

#establish obstacle 
class Obstacle(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("obstacle.gif")
		self.speed = 0
		self.direction = "right"
		self.speed = random.randint(1,6)
		self.goto(random.randint(-1400, -700), -190), (random.randint(-1200, -700), -190), (random.randint(-1600, -700), -190)
		self.setheading(0)
		self.width = 100	
		self.height = 110
		
	def update_number_of_lives(self):
		pen.clear()
		pen.write("Lives: {}" .format(self.number_of_lives), align = "center", font = ("Times New Roman", 30, "normal"))
	
	def change_number_of_lives(self, lives):
			self.number_of_lives -= lives 
			self.update_number_of_lives
	
	def move(self):
		self.forward(self.speed) 
		
		if self.xcor() > 800:	
			self.setx(-1600)

#establish bonus
class Bonus(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("lightning.gif")
		self.speed = 0
		self.speed = random.randint(1,3)
		self.goto(random.randint(-250, 250), random.randint(250, 250))
		self.setheading(270)
		self.height = 25
		self.width = 20

	def update_number_of_lives(self):
		pen.clear()
		pen.write("Lives: {}" .format(self.number_of_lives), align = "center", font = ("Times New Roman", 24, "normal"))
	
	def change_number_of_lives(self, lives):
			self.number_of_lives == lives 
			self.update_number_of_lives
		
	def move(self):
		self.forward(self.speed) 
		
		if self.ycor() < -270:
			self.sety(400)

#establish game
class Game(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.color("white")
		self.speed = 0 
		self.ht()
	
	def play_sound(self,filename):
		("afplay {}&".format(filename))

#establish number of lives
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.hideturtle()
		self.write("Lives: {}" .format(lives), align = "center", font = ("Times New Roman", 30, "normal"))

#bounding box collision
def is_collision(sprite_1, sprite_2):
	a = (math.fabs(sprite_1.xcor() - sprite_2.xcor()) * 2) < (sprite_1.width + sprite_2.width)
	b = (math.fabs(sprite_1.ycor() - sprite_2.ycor()) * 2) < (sprite_1.height + sprite_2.height)
	return (a and b)
	
#instances
border = Border()
player = Player()
obstacles = []
bonuses = []
game = Game()
pen = Pen()

#loops
for count in range(4):
	obstacles.append(Obstacle())

for count in range(1):
	bonuses.append(Bonus())

#keyboard binding
wn.listen()	
wn.onkeypress(player.go_right, "Right")
wn.onkeypress(player.go_left, "Left")
wn.onkeypress(player.jump, "Up")
	
while True:
	wn.update()	
	player.move()
	player.dy += GRAVITY
	
	for obstacle in obstacles:
		obstacle.move()
		
		if obstacle.xcor() > 600:
			obstacle.setx(-1000)
			
		if is_collision(obstacle, player):
			player.change_number_of_lives(+1)
			os.system("afplay obstacle.mp3&")
			obstacle.goto(random.randint(-1400, -700), -190), (random.randint(-1800, -700), -190), (random.randint(-1700, -700), -190)
			
	for bonus in bonuses: 
		bonus.move()
		if bonus.ycor() < -270:
			bonus.sety(400)
		if is_collision(bonus, player):
			os.system("afplay bonus.mp3&")
			player.change_number_of_lives(-1)
			bonus.goto(random.randint(-250, 600), random.randint(250, 600))

	if player.number_of_lives == 0: 
		wn.bgpic("game_over.gif")
		wn.update()
		pen.hideturtle()
		time.sleep(2)
		exit()
	
	if player.number_of_lives == 10: 
		wn.bgpic("you_win.gif")
		wn.update()
		time.sleep(2)
		exit()
		
wn.mainloop()