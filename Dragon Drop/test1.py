from Focus_Roots import *


x = 100

def change():
    global x
    
    set_background(color_black)
    draw_circle(x=x,y=100,radius=50,width=0,color=color_emeraldgreen)

    x+=1



draw(change)