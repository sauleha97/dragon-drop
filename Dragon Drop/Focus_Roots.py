import pygame,sys
from pygame import mixer

pygame.init()
mixer.init()

screen_width = 500 #inital screen width
screen_height = 500 #inital screen height

clock = pygame.time.Clock()

"""
Initial color codes
"""
color_white = (255,255,255)
color_aqua=(0,255,255)
color_antiquewhite1=(255,239,219)
color_aquamarine=(127,255,212)
color_banana=(227,207,87)
color_bisque=(255,228,196)
color_black=(0,0,0)
color_blue=(0,0,255)
color_violet=(138,43,226)
color_brick=(156,102,31)
color_brown=(165,42,42)
color_emeraldgreen=(0,201,87)
color_firebrick=(255,48,48)
color_yellow =(255,215,0)
color_chocolate=(210,105,30)
color_light_salmon=(139,87,66)
color_burlywood=(205,170,125)
color_gray=(201,201,201)
color_sky_blue=(0,191,255)
color_orchid=(191,62,255)
color_dark_gold=(255,185,15)
color_khaki=(255,246,143)
color_skin=(255,228,181)
color_mid_night_blue=(25,25,112)
color_sea_green=(84,255,159)
color_violet_red=(255,130,171)
color_pale_green=(152,251,152)

bg_color = (255,255,255) #Initial Background color white


screen = pygame.display.set_mode((screen_width,screen_height)) #create screen

Mouse_x=0 #Initial mouse position for x
Mouse_y=0 #Initial mouse position for y
screen.fill(bg_color)

"""
Pygame key notation
"""
key_up=pygame.K_UP
key_down=pygame.K_DOWN
key_right=pygame.K_RIGHT
key_left=pygame.K_LEFT
key_w=pygame.K_w
key_a=pygame.K_a
key_s=pygame.K_s
key_d=pygame.K_d
key_space=pygame.K_SPACE

#Funtion keys pressed on keyboard
def get_keys_pressed():
    keys=pygame.key.get_pressed()
    return keys


def pause_music():
    mixer.music.pause()
#Funtion to play music
def play_music(loc,loop=1):
    """
    Funtion is build to play music
    Parameters:-
    1) loc:- Specify the absolute path where the music file is located
    2) loop:- Speciifes how many times you want to pay your music DEFAULT is 1 . If you pass parameter as -1 your music will be played infinitely
    """
    mixer.music.load(loc)
    mixer.music.play(loop)

def image(loc,scale_width,scale_length,x,y):

    """
    Funtion is display image
    Parameters:-
    1) loc:- Specify the absolute path where the image file is located
    2) scale_width:- Speciifes how many times you want to pay your music DEFAULT is 1 . If you pass parameter as -1 your music will be played infinitely
    """
    img = pygame.image.load(loc)
    img_scale =  pygame.transform.scale(img, (scale_width, scale_length))
    rect = img_scale.get_rect()
    rect.center = x,y
    screen.blit(img_scale, rect)
    return rect


def get_mouse_position():
    global Mouse_x,Mouse_y

    Mouse_x,Mouse_y=pygame.mouse.get_pos()

    return Mouse_x,Mouse_y

def set_background(colorORimg,isimage=0):
    if isimage==0:
        screen.fill(colorORimg)


# Function to display text on screen
def write_text(text,x,y,size=5,color=color_emeraldgreen):

    font = pygame.font.Font('freesansbold.ttf', size)
    text_obj = font.render(text, True, color , screen.get_alpha())
    textRect = text_obj.get_rect()
    textRect.center = (x,y)
    screen.blit(text_obj,textRect)
                    
    

def set_screen_size(width,height):
    global screen_width,screen_height

    screen_width = width
    screen_height = height
    screen = pygame.display.set_mode((screen_width,screen_height))


def draw_polygon(points,width=2,color=color_emeraldgreen):
    rect_obj=pygame.draw.polygon(screen, color, points, width)
    return rect_obj
    


def draw_circle(x,y,radius=5,width=2,color=color_emeraldgreen):
    rect_obj=pygame.draw.circle(screen,color,(x,y),radius,width=width)
    return rect_obj


def draw_line(start_pos,end_pos,width=2,color=color_emeraldgreen):
    rect_obj=pygame.draw.line(screen,color,start_pos,end_pos,width)
    return rect_obj


def draw_ellipse(top,left,width,height,draw_width=2,color=color_emeraldgreen):
    rect_obj = pygame.Rect(top,left,width,height)
    pygame.draw.ellipse(screen,color,rect_obj,width=draw_width)
    return rect_obj



def draw_rect(top,left,width,height,draw_width=2,color=color_emeraldgreen):
    rect_obj = pygame.Rect(top,left,width,height) # Draw Rectangle
    pygame.draw.rect(screen,color,rect_obj,width=draw_width)
    return rect_obj


def change2():
    pass
def draw(t):

    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            t()
            pygame.display.flip()
            clock.tick(60)