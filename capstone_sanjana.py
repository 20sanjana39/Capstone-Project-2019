import turtle 
import random
import time 

#create main window
wn = turtle.Screen()
wn.title("Jumping Avenger by Sanjana")
wn.setup(height = 600, width = 800)
wn.bgcolor("brown")

#number of lives 
	
number_of_lives = 3

#set gravity 
GRAVITY = -0.2

#establish avenger
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
		
#move avenger (left and right)
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
			
		
	def go_left(self): 
		self.direction = "Left"

	def go_right(self): 
		self.direction = "Right"

#move avenger (jump)
	def jump(self):
		self.state = "jumping"
		self.dy = 6

#create obstacle
class Obstacle(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("circle")
		self.color("red")
		self.speed = random.randint(1,3)
		#the goto has to only

# Create instances
player = Player()


# Keyboard Binding
wn.listen()	
wn.onkeypress(player.go_right, "Right")
wn.onkeypress(player.go_left, "Left")
wn.onkeypress(player.jump, "Up")

while True:
	player.move()
	player.dy += GRAVITY
		

#idea = balls falling out of the sky like bouncing balls for the third obstacle 
#but will that make the movement weird then???

wn.mainloop()

