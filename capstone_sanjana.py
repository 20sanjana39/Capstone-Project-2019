import turtle 
import random
import time 
import math

#create main window
wn = turtle.Screen()
wn.title("Jumping Avenger by Sanjana")
wn.setup(height = 800, width = 1200)
wn.register_shape("thor.gif")
wn.register_shape("rainbow_bridge2.gif")
wn.bgpic("rainbow_bridge2.gif")
wn.tracer(0)

#number of lives 
lives = 3

#set gravity 
GRAVITY = -0.3

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
		self.shape("thor.gif")
		self.shapesize(stretch_wid = 5, stretch_len=2, outline = None)
		self.color("red")
		self.speed(0)
		self.penup()
		self.direction = "Left"
		self.goto(0, -250)
		self.speed = 3
		self.state = "running"
		self.dy = 0
		self.width = 60
		self.height = 95
		self.number_of_lives = 3

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
		if self.xcor() > 360 or self.xcor() < -360: 
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

	def update_number_of_lives(self):
		pen.clear()
		pen.write("Lives: {}" .format(self.number_of_lives), align = "center", font = ("Times New Roman", 30, "normal"))
	
	def change_number_of_lives(self, lives): 
		self.number_of_lives -= lives
		self.update_number_of_lives()

obstacles = []

#CREATE OBSTACLE 
class Obstacle(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("square")
		self.color("white")
		self.speed = 0
		self.direction = "right"
		self.speed = random.randint(1,4)
		self.goto(random.randint(-300, -220), random.randint(-300, -200))
		self.setheading(0)
		self.width = 20
		self.height = 20
		
	def update_number_of_lives(self):
		pen.clear()
		pen.write("Lives: {}" .format(self.number_of_lives), align = "center", font = ("Times New Roman", 30, "normal"))
	
	def change_number_of_lives(self, lives):
			self.number_of_lives -= lives 
			self.update_number_of_lives
	
	def move(self):
		self.forward(self.speed) 
		
		if self.xcor() > 270:
			self.setx(-270)

#CREATE BONUS
class Bonus(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.shape("circle")
		self.color("red")
		self.speed = 0
		self.speed = random.randint(1,3)
		self.goto(random.randint(-250, 250), random.randint(250, 250))
		self.setheading(270)
		self.height = 20
		self.width = 20

	def update_number_of_lives(self):
		pen.clear()
		pen.write("Lives: {}" .format(self.number_of_lives), align = "center", font = ("Times New Roman", 24, "normal"))
	
	def change_number_of_lives(self, lives):
			self.number_of_lives == lives 
			self.update_number_of_lives
		
	def move(self):
		self.forward(self.speed) 
		
		if self.ycor() < - 270:
			self.sety(400)

#CREATE GAME 
class Game(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.penup()
		self.speed(0)
		self.color("white")
		self.speed = 0 
		self.goto(000,000)
		#continue this

#NUMBER OF LIVES
class Pen(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.hideturtle()
		self.write("Lives: {}" .format(lives), align = "center", font = ("Times New Roman", 30, "normal"))

#COLLISION
def is_collision(sprite_1, sprite_2):
	 #Axis Aligned Bounding Box
	a = (math.fabs(sprite_1.xcor() - sprite_2.xcor()) * 2) < (sprite_1.width + sprite_2.width)
	b = (math.fabs(sprite_1.ycor() - sprite_2.ycor()) * 2) < (sprite_1.height + sprite_2.height)
	return (a and b)
	
#CREATE INSTANCES
player = Player()
border = Border()
pen = Pen()
obstacles = []
bonuses = []
game = Game()
#get an extra life from above
	
#create loops 
for count in range(3):
	obstacles.append(Obstacle())

for count in range(2):
	bonuses.append(Bonus())

#KEYBOARD BINDING
wn.listen()	
wn.onkeypress(player.go_right, "Right")
wn.onkeypress(player.go_left, "Left")
wn.onkeypress(player.jump, "Up")
	
# if time passes more than 2 minutes, then player wins the game
# if lives equals zero, game over 
	
while True:
	wn.update()	
	player.move()
	player.dy += GRAVITY
	
	for obstacle in obstacles:
		obstacle.move()
		#check for falling off screen
		if obstacle.xcor() > 270:
			obstacle.setx(-270)
			
		#check for collision with obstacle
		if is_collision(obstacle, player):
			player.change_number_of_lives(+1)
			obstacle.goto(random.randint(-270, -220), random.randint(-270, -200))
			
	for bonus in bonuses: 
		bonus.move()
		# Check for falling off screen
		if bonus.ycor() < - 270:
			bonus.sety(400)

		# Check for collision with player
		if is_collision(bonus, player):
			player.change_number_of_lives(-1)
			bonus.goto(random.randint(-250, 250), random.randint(250, 250))
			
	
	#create code for the end of the game
	if player.number_of_lives <= 0: 
		wn.update()
		time.sleep(1)
		exit()

wn.mainloop()