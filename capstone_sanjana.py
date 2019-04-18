import turtle 
import random
import time 
import math

#create main window
wn = turtle.Screen()
wn.title("Jumping Avenger by Sanjana")
wn.setup(height = 800, width = 1200)
wn.bgcolor("darkblue")
wn.tracer(0)

#number of lives 
lives = 3

#set gravity 
GRAVITY = -0.4

#ESTABLISH BORDER
class Border(turtle.Turtle):
	def __init__(self): 
		turtle.Turtle.__init__(self)
		self.penup()
		self.hideturtle()
		self.speed(0)
		self.pensize(5)

#ESTABLISH AVENGER
class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.shapesize(stretch_wid = 5, stretch_len=2, outline = None)
		self.color("red")
		self.speed(0)
		self.penup()
		self.direction = "Left"
		self.goto(0, -250)
		self.speed = 3
		self.state = "running"
		self.dy = 0
		self.width = 40
		self.height = 100

#move avenger
	def move(self): 
		self.goto(self.xcor(), self.ycor())

		# Left
		if self.direction == "Left": 
			x = self.xcor()
			self.speed = 3
			self.setx(x - self.speed)
		
		# Right	
		if self.direction == "Right":	
			x = self.xcor()
			self.speed = 3
			self.setx(x + self.speed)
	
		# Jump
		if self.state == "jumping":
			self.sety(self.ycor() + self.dy)
			# Check for landing
			if self.ycor() <= -250:
				self.sety(-250)
				self.state = "running"
				self.dy = 0
			
		# Border checking
		if self.xcor() > 150 or self.xcor() < -150: 
			self.speed = 0
			self.direction = "none"

	def go_left(self): 
		self.direction = "Left"
		self.speed = 3 

	def go_right(self): 
		self.direction = "Right"
		self.speed = 3 

#move avenger (jump)
	def jump(self):
		if self.state != "jumping": 
			self.state = "jumping"
			self.dy = 10		

obstacles = []

#CREATE FIRST OBSTACLE 
class Obstacle(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("square")
		self.color("white")
		self.speed = 0
		self.direction = "right"
		self.speed = random.randint(1,3)
		self.goto(random.randint(-270, -220), random.randint(-240, -220))
		self.setheading(0)
		self.width = 20
		self.height = 20
		
		#make if statement to get the obstacles coming out from the left side
		if self.goto == -270 or self.goto  == -240: 
			self.goto(random.randint(-270, -220), random.randint(-240, -220))
	

	def move(self):
		self.forward(self.speed) 
		
		if self.ycor() < -250:
			self.sety(50)

#CREATE SECOND OBSTACLE 
#class Obstacle1(turtle.Turtle):
#	def __init__(self):
#		turtle.Turtle.__init__(self)
#		self.shape("square")
#		self.color("grey")

#NUMBER OF LIVES
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.write("Lives: {}" .format(lives), align = "center", font = ("Courier", 24, "normal"))

#COLLISION
def is_collision(self, sprite_1, sprite_2):
	# Axis Aligned Bounding Box
	x_collision = (math.fabs(sprite_1.xcor() - sprite_2.xcor()) * 2) < (sprite_1.width + sprite_2.width)
	y_collision = (math.fabs(sprite_1.ycor() - sprite_2.ycor()) * 2) < (sprite_1.height + sprite_2.height)
	return (x_collision and y_collision)


#CREATE INSTANCES
player = Player()
border = Border()
pen = Pen()
obstacles = []

#get an extra life from above

#create loops 
for count in range(6):
	obstacles.append(Obstacle())

#KEYBOARD BINDING
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


wn.mainloop()