from Focus_Roots import *
import pygame

set_screen_size(700,700)


start = 0

dragon_x = 600
dragon_y = 650

obs1_x = 100
obs1_y = 550

obs2_x = 0
obs2_y = 400

obs3_x = 100
obs3_y = 150

obs4_x = 600
obs4_y = 200

obs5_x = 450
obs5_y = 300

obs6_x = 600
obs6_y = 200

obs7_x = 600
obs7_y = 200

game_over = False
game_won = -1 # 0 Lost 1 Won

win_music = 0
loose_music = 0

def change():
    image("D:/focus roots/focus roots/Games/Dragon Drop/Assets/images/background_1.jpg",700,700,350,350)
    global start, dragon_y, dragon_x, game_over, game_won, win_music, loose_music
    
    set_background(color_black)

    Mouse_x, Mouse_y = get_mouse_position()

    dragon = image("D:/focus roots/focus roots/Games/Dragon Drop/Assets/images/dragon.png",60, 60, dragon_x, dragon_y)

    chicken = image("D:/focus roots/focus roots/Games/Dragon Drop/Assets/images/chicken.png",30, 30, 630, 130)

    draw_rect(top=dragon.x,left=dragon.y,width=60,height=60,draw_width=2,color=color_brick)

    if dragon.collidepoint(Mouse_x, Mouse_y) and game_over==False:
        dragon_x = Mouse_x
        dragon_y = Mouse_y


    obstacle_1 = draw_rect(top=obs1_x,left=obs1_y,width=590,height=50,draw_width=0,color=color_brick)
    obstacle_2 = draw_rect(top=obs2_x,left=obs2_y,width=600,height=50,draw_width=0,color=color_brick)
    obstacle_3 = draw_rect(top=obs3_x,left=obs3_y,width=600,height=50,draw_width=0,color=color_brick)

    obstacle_4 = draw_rect(top=obs4_x,left=obs4_y,width=50,height=120,draw_width=0,color=color_brick)     
    obstacle_5 = draw_rect(top=obs5_x,left=obs5_y,width=50,height=180,draw_width=0,color=color_brick)
    obstacle_6 = draw_rect(top=250,left=150,width=50,height=180,draw_width=0,color=color_brick) 

    obstacle_7 = draw_rect(top=0,left=30,width=700,height=50,draw_width=0,color=color_brick)

    
    if dragon.collidelist([obstacle_1,obstacle_2,obstacle_3,obstacle_4,obstacle_5,obstacle_6,obstacle_7]) != -1:
        game_over = True
        game_won = 0


    if dragon.contains(chicken):
        game_over = True
        game_won = 1

    if game_over:

        if game_won == 0:
            dragon_y += 5
            write_text("You Failed", 300, 300, 90, color=color_aquamarine)
            if loose_music == 0:
                play_music("Assets/sounds/gameover1.wav")
                loose_music=1

        if game_won == 1:
            write_text("You Won", 300, 300, 90, color=color_aquamarine)
            if win_music == 0:
                play_music("Assets/sounds/collect.wav")
                win_music = 1

            del chicken


                          

draw(change)