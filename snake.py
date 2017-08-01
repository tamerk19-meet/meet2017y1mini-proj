def up():
    global direction
    direction=UP
    print('you pressed up key')
def down():
    global direction
    direction=DOWN
    print('you pressed down key')
def right():
    global direction
    direction=RIGHT
    print('you pressed right key')
def left():
    global direction
    direction=LEFT
    print('you pressed left key')
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print('you moved right!')
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print('you moved left!')
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print('you moved down!')
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print('you moved up!')

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)

    if snake.pos()in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamps(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('You Have Eaten The Food!')
        
        
    
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    

    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos>=RIGHT_EDGE:
        print('you hit the right edge! GAME OVER!')
        quit()
    if new_x_pos<=LEFT_EDGE:
        print('you hit the left edge! GAME OVER!')
        quit()
    if new_y_pos>=UP_EDGE:
        print('you hit the up edge! GAME OVER!')
        quit()
    if new_y_pos<=DOWN_EDGE:
        print('you hit the down edge! GAME OVER!')
        quit()
      
    turtle.ontimer(move_snake,TIME_STEP)
     
##########################################################################
import turtle
import random
turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=7

pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

snake=turtle.clone()
snake.shape('square')

turtle.hideturtle()
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)
    pos_list.append(my_pos)

    stamp1=snake.stamp()
    stamp_list.append(stamp1)

UP_ARROW='Up'
LEFT_ARROW='Left'
DOWN_ARROW='Down'
RIGHT_ARROW='Right'

TIME_STEP=100
SPACEBAR='space'

UP=0
DOWN=1
LEFT=2
RIGHT=3
direction = UP
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE = 400
LEFT_EDGE = -400

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.listen()

move_snake()

turtle.register_shape('trash.gif')
food=turtle.clone()
food.shape('trash.gif')
food_pos=[(100,100),(-100,100),(-100,-100),(100,-100)]
food_stamps=[]
food.hideturtle()
for this_food_pos in food_pos:
    food.goto(this_food_pos)
    my_food_stamp=food.stamp()
    food_stamps.append(my_food_stamp)
    

