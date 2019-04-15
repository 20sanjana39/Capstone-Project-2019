import turtle 
import random
import time 

#create main window
wn = turtle.Screen()
wn.title("Jumping Avenger by Sanjana")
wn.setup(height = 700, width = 1000)
wn.bgcolor("brown")
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
		self.color("black")
		self.pensize(5)

#ESTABLISH AVENGER
class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("triangle")
		self.color("yellow")
		self.speed(0)
		self.penup()
		self.direction = "Left"
		self.goto(0, -250)
		self.speed = 3
		self.state = "running"
		self.dy = 0 

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
		if self.xcor() > 50 or self.xcor() < -50: 
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

#CREATE OBSTACLE 
class Obstacle(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("circle")
		self.color("black")
		self.speed = 0
		self.speed = random.randint(1,3)
		self.goto(random.randint(-250, 250), random.randint(-250, -250))
		self.setheading(5)

	def move(self):
		self.forward(self.speed) 
		
		if self.ycor() < - 270:
			self.sety(400)
	
	
#NUMBER OF LIVES
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.write("Lives: {}" .format(lives), align = "center", font = ("Courier", 24, "normal"))

#CREATE INSTANCES
player = Player()
border = Border()
pen = Pen()
obstacles = []

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