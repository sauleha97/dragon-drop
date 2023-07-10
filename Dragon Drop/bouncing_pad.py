
from Focus_Roots import *
import random

x_y = [10,15]
pad_x = 225
ball_x = 250
ball_y = 250
ball_speed_x = 2
ball_speed_y = 2 
brick_num = 0
brick_list = []
ball = draw_circle(ball_x,ball_y,5,0)
brick_rect_list = []



    



def bricks_creation(x,y):
    per_row_brick_count = 500/20 

    brick_length=17
    brick_space=2.5
    for brick in range(int(per_row_brick_count)):
            brick_x = x
            brick_y = y
            brick_length=17

            x+=brick_length + brick_space

            brick_data=dict()
            brick_data["brick_x"] =  brick_x
            brick_data["brick_y"] =  brick_y
            brick_data["brick_length"] =  brick_length
            brick_data["brick_rect_obj"] =  '00'

            brick_list.append( brick_data ) 

row_count=5

x=x_y[0]
y=x_y[1]
for row in range(row_count):
    

    bricks_creation(x,y)

    y+=10+5







def display_bricks():

    global brick_list

    for brick_index in range(len(brick_list)):

        print(brick_list[brick_index])
        brick_rect = draw_rect(brick_list[brick_index]["brick_x"],brick_list[brick_index]["brick_y"],brick_list[brick_index]["brick_length"],10,0,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        brick_list[brick_index]["brick_rect_obj"]=brick_rect

    
def bounce(brick_cd = False):
    global ball_x,ball_y,ball_speed_x,ball_speed_y

    if brick_cd == False:
        if ball_x == 10 or ball_x >= 490 :
            ball_speed_x *= -1
        if ball_y == 10:
            ball_speed_y*= -1  
        

        ball_x -= ball_speed_x 
        ball_y += ball_speed_y 

    else:
       ball_speed_x *= -1
       ball_speed_y*= -1
       ball_x += ball_speed_x 
       ball_y += ball_speed_y 

def cd():
    global brick_list,ball,ball_speed_x,ball_speed_y
    
    for brick in brick_list:

        if ball.colliderect(brick["brick_rect_obj"]):
            brick_list.remove(brick)
            ball_speed_x = random.randint(2,3)
            #play_music('point.mp3',1)
            #ball_speed_y = random.randint(1,3)
            
            bounce(brick_cd = True)
            print("Collision happened")


def change():
    global pad_x,ball_speed_x,ball_speed_y,x_y,ball
    set_background(color_black)
    
    ball = draw_circle(ball_x,ball_y,5,0)
    
    keys = get_keys_pressed()
    if keys[key_left]:
        pad_x -= 5
        
    if keys[key_right]:
        pad_x += 5
    pad = draw_rect(pad_x,350,100,15,0,color=color_aqua)

    

    if ball.colliderect(pad):
        ball_speed_y *=-1
        bounce()
    bounce()
    display_bricks()
    cd()

    

draw(change)
