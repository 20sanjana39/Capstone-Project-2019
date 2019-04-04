import turtle 
import random

#create main window
wn = turtle.Screen()
wn.title("Jumping Avenger by Sanjana")
wn.setup(height = 600, width = 800)
wn.bgcolor("black")

#number of lives 
	
number_of_lives = 3

#establish avenger
class Player(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("triangle")
		self.color("blue")
		self.speed(0)
		self.penup()
		self.direction = "Left"
		self.goto(0, -250)
		self.speed = 3
		
#move avenger (left and right)
	def move(self): 
		if self.direction == "Left": 
			x = self.xcor()
			self.setx(x - self.speed)
			
		if self.direction == "Right":	
			x = self.xcor()
			self.setx(x + self.speed)
	
	def go_left(self): 
		self.direction = "Left"

	def go_right(self): 
		self.direction = "Right"

#move avenger (jump)

# Create instances
player = Player()

# Keyboard Binding
wn.listen()	
wn.onkeypress(player.go_right, "Right")
wn.onkeypress(player.go_left, "Left")

while True:
	player.move()



wn.mainloop()

