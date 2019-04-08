import turtle 
import random
import time 

#create main window
wn = turtle.Screen()
wn.title("Jumping Avenger by Sanjana")
wn.setup(height = 600, width = 800)
wn.bgcolor("brown")

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

	def draw_border(self):
		self.penup()
		self.goto(-300,-300)
		self.pendown()
		self.goto(-300, 300)
		self.goto(300,300)
		self.goto(300,-300)
		self.goto(-300, -300)
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
		self.write("Lives: {}" .format(lives), align = "center", font = ("Courier", 24, "normal"))

#move avenger
	def move(self): 
		# Left
		if self.direction == "Left": 
			x = self.xcor()
			self.setx(x - self.speed)
		
		# Right	
		if self.direction == "Right":	
			x = self.xcor()
			self.setx(x + self.speed)
	
		# Jump
		if self.state == "jumping":
			self.sety(self.ycor() + self.dy)
			
		# Border checking
		if self.xcor() > 290 or self.xcor() < -290: 
			self.speed = 0
		if self.ycor() > 290 or self.ycor() < -290:
			self.dy = 0 
			self.speed = 0
			self.right(90)
			
	def go_left(self): 
		self.direction = "Left"
		self.speed = 3 

	def go_right(self): 
		self.direction = "Right"
		self.speed = 3 

#move avenger (jump)
	def jump(self):
		self.state = "jumping"
		self.dy = 10

# Create instances
player = Player()
border = Border()
obstacles = []


# Keyboard Binding
wn.listen()	
wn.onkeypress(player.go_right, "Right")
wn.onkeypress(player.go_left, "Left")
wn.onkeypress(player.jump, "Up")

while True:
	player.move()
	player.dy += GRAVITY

wn.mainloop()