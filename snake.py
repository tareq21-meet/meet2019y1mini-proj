import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7
TIME_STEP = 200

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("circle")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Function to draw a part of the snake on the screen
def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos) 
    #snake.stamp() returns a stamp ID. Save it in some variable         
    snake_stamp = snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(snake_stamp)
#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for a in range(START_LENGTH):
    x_pos=snake.xcor() #Get x-position with snake.pos()[0]
    y_pos=snake.ycor()

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp)#erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position


UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400
snake.direction = "Right"
def up():
    snake.direction="Up" #Change direction to up
    print("You pressed the up key!")
def down():
    snake.direction="Down" #Change direction to up
     #Update the snake drawing 
    print("You pressed the down key!")
def left():
    snake.direction="Left" #Change direction to up
     #Update the snake drawing 
    print("You pressed the left key!")

def right():
    snake.direction="Right" #Change direction to up
    #Update the snake drawing 
    print("You pressed the right key!")
#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(down, "Down")

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, "Up") # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.onkeypress(left, "Left")

turtle.onkeypress(right, "Right")

turtle.listen()
turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 
#Locssations of food
food_pos = []
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    a = food.stamp()
    food_stamps.append(a)
    ####WRITE YOUR CODE HERE!!
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x, food_y)
    food_pos.append((food_x, food_y))
    stm=food.stamp()
    food_stamps.append(stm)


def move_snake():

    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    print(snake.pos())
    print(snake.direction)
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction == "Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")
    elif snake.direction == "Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved Right!")
    elif snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    new_stamp()
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
    else:
        remove_tail()
    if snake.pos() in pos_list [:-1]:
        print(pos_list)
        print(snake.pos())
        print("you have eaten your self!!!! game over :(")
        quit()
    
    # The next three lines check if the snake is hitting the 
    # right edge
    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    if new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()
    if new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    if new_y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         quit()
     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE

    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE


    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this

    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)

    if len(food_stamps) <= 2 :
    			make_food()

    turtle.ontimer(move_snake,TIME_STEP)
move_snake()
turtle.mainloop()
