import os
os.system("clear")


import turtle
import random
import math
import time

wn = turtle.Screen()
wn.bgcolor("pink")
wn.title("Gintama Game by Alice Park")
wn.bgpic("background.gif")
wn.register_shape("character 2.gif")
wn.register_shape("bonus.gif")
wn.register_shape("enemy.gif")
wn.register_shape("bonus 2.gif")
turtle.bgpic("ss.gif")
turtle.update()
time.sleep(5)
wn.bgpic("background.gif")

class Player(turtle.Turtle):
	def __init__(self):
			turtle.Turtle.__init__(self)
			self.penup()
			self.shape("character 2.gif")
			self.color("white")
			self.speed(0)
			self.speed = 5
			self.goto(0,-250)
			self.pensize(3)

	def move(self):
		self.forward(self.speed)
	
		if self.xcor() > 290 or self.xcor() < -290:
			self.left(180)
		if self.ycor() > 290 or self.ycor() < -290:
			self.left(180)
		
	def turnleft(self):
		self.setheading(180)
		
	def turnright(self):
		self.setheading(0)

		
class Border(turtle.Turtle):
	

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color("white")
		self.pensize(5)
		
	def draw_border(self):
		self.penup()
		self.goto(-300,-300)
		self.pendown()
		self.goto(-300,300)
		self.goto(300,300)
		self.goto(300,-300)
		self.goto(-300,-300)
		
		
class Enemy(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("enemy.gif")
		self.speed = 0
		self.speed = random.randint(1,3)
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(270)

	def move(self):
		self.forward(self.speed) 
		
		if self.ycor() < - 270:
			self.sety(400)
			
	def jump(self):
		self.goto(random.randint(-250, 250), 360)
		self.setheading(270)
		
		
	def update_score(self):
		self.clear()
		self.write("Score: {}".format(self.score), False, align = "left", font = ("Arial",14,"normal"))	
		
	def change_score(self, points):
		self.score -= points 
		self.update_score()


class Goal(turtle.Turtle):

	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("bonus.gif")
		self.speed = 0
		self.speed = random.randint(1,3)
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(270)
		

	def move(self):
		self.forward(self.speed) 
		
		if self.ycor() < - 270:
			self.sety(400)
			
	def jump(self):
		self.goto(random.randint(-250, 250), 360)
		self.setheading(270)

class Bonus(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("bonus 2.gif")
		self.color("red")
		self.speed = 0
		self.speed = random.randint(1,4)
		self.goto(random.randint(-250, 250), random.randint(-250, 250))
		self.setheading(270)

	def move(self):
		self.forward(self.speed) 
		
		if self.ycor() < - 270:
			self.sety(400)
			
	def jump(self):
		self.goto(random.randint(-250, 250), 360)
		self.setheading(270)
		
		
	def update_score(self):
		self.clear()
		self.write("Score: {}".format(self.score), False, align = "left", font = ("Arial",14,"normal"))	
		
	def change_score(self, points):
		self.score == points 
		self.update_score()
			
class Game(turtle.Turtle):
	
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.color("white")
		self.goto(-290, 310)
		self.score = 0
		
	def update_score(self):
		self.clear()
		self.write("Score: {}".format(self.score), False, align = "left", font = ("Arial",14,"normal"))	
		
	def change_score(self, points):
		self.score += points 
		self.update_score()
		
	def play_sound(self,filename):
		os.system("afplay {}&".format(filename))
		
	
		
def isCollision(t1, t2):
	a = t1.xcor()-t2.xcor()
	b = t1.ycor()-t2.ycor()
	distance = math.sqrt((a ** 2) + (b ** 2))

		
	if distance < 40:
		return True
	else:
		return False

	
player = Player()
border = Border()
enemies = []
goals = []
bonuses = []
game = Game()

for count in range(6):
	goals.append(Goal())
	
for count in range(6):
	enemies.append(Enemy())
	
for count in range(3):
	bonuses.append(Bonus())
	
border.draw_border()

turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")


wn.tracer(0)
while True:

	wn.update()
	player.move()
	
	for goal in goals:
		goal.move()
	
	
		if isCollision(player, goal):
			goal.jump()				
			game.change_score(10)
			if game.ycor() < - 270:
				game.sety(400)
				
	for enemy in enemies:
		enemy.move()
	
	
		if isCollision(player, enemy):
			enemy.jump()				
			game.change_score(-50)
			if game.ycor() < - 270:
				game.sety(400)
				
	for bonus in bonuses:
		bonus.move()
	
	
		if isCollision(player, bonus):
			bonus.jump()	
			game.play_sound("collision.mp3")			
			game.change_score(+20)
			if game.ycor() < - 270:
				game.sety(400)
				
				
	#Check for end of game.
		if game.score < 0:
			wn.bgpic("Game Over.gif")
			wn.update()
			time.sleep(3)
			exit()

			

			

		
					