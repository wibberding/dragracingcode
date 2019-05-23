# import pygame module in this program 
import pygame 


#Variables  
timer = 0
race_start_time = 0

left_lane_start_time = 0
left_lane_end_time = 0
left_lane_reaction_time = 0.00
left_lane_total_time = 0.00

right_lane_start_time = 0
right_lane_end_time = 0
right_lane_reaction_time = 0.00
right_lane_total_time = 0.00

#Light states
stage_1_left = True
stage_2_left = True
yellow_1_left = True
yellow_2_left = True
yellow_3_left = True
green_left = True
red_left = True

stage_1_right = True
stage_2_right = True
yellow_1_right = True
yellow_2_right = True
yellow_3_right = True
green_right = True
red_right = True

#List of functions needed for the game

def car_start_button_pressed(lane):
    pass

def finish_line_crossed(lane):
    pass

def start_timer():
    pass

def start_race():
    pass


# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
  
# define the RGB value 
# for colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
  
# assigning values to X and Y variable 
X = 800 
Y = 800
  
# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y )) 
  
# set the pygame window name 
pygame.display.set_caption('Race') 
  
# create a surface object, image is drawn on it. 
#image = pygame.image.load('images/mustang.jpg') 
  
# infinite game loop 
while True : 
  
    # completely fill the surface object 
    # with white colour 
    display_surface.fill(black) 
  
    # copying the image surface object 
    # to the display surface object at 
    # (0, 0) coordinate. 
    #display_surface.blit(image, (0, 0)) 

    #Draw lights in correct state
    if stage_1_left == True:
        pygame.draw.circle(display_surface, white, (190,50), 30)
    else:
        pygame.draw.circle(display_surface, white, (190,50), 30, 2)

    if stage_1_right == True:
        pygame.draw.circle(display_surface, white, (610,50), 30)
    else:
        pygame.draw.circle(display_surface, white, (610,50), 30, 2)

    if stage_2_left == True:
        pygame.draw.circle(display_surface, white, (255,50), 30)
    else:
        pygame.draw.circle(display_surface, white, (255,50), 30, 2)

    if stage_2_right == True:
        pygame.draw.circle(display_surface, white, (545,50), 30)
    else:
        pygame.draw.circle(display_surface, white, (545,50), 30, 2)

    if yellow_1_left == True:
        pygame.draw.circle(display_surface, yellow, (345,70), 50)
    else:
        pygame.draw.circle(display_surface, yellow, (345,70), 50, 2)

    if yellow_1_right == True:
        pygame.draw.circle(display_surface, yellow, (455,70), 50)
    else:
        pygame.draw.circle(display_surface, yellow, (455,70), 50, 2)
    
    if yellow_2_left == True:
        pygame.draw.circle(display_surface, yellow, (345,175), 50)
    else:
        pygame.draw.circle(display_surface, yellow, (345,175), 50, 2)

    if yellow_2_right == True:
        pygame.draw.circle(display_surface, yellow, (455,175), 50)
    else:
        pygame.draw.circle(display_surface, yellow, (455,175), 50, 2)

    if yellow_3_left == True:
        pygame.draw.circle(display_surface, yellow, (345,280), 50)
    else:
        pygame.draw.circle(display_surface, yellow, (345,280), 50, 2)

    if yellow_3_right == True:
        pygame.draw.circle(display_surface, yellow, (455,280), 50)
    else:
        pygame.draw.circle(display_surface, yellow, (455,280), 50, 2)
    
    if green_left == True:
        pygame.draw.circle(display_surface, green, (345,385), 50)
    else:
        pygame.draw.circle(display_surface, green, (345,385), 50, 2)

    if green_right == True:
        pygame.draw.circle(display_surface, green, (455,385), 50)
    else:
        pygame.draw.circle(display_surface, green, (455,385), 50, 2)
    
    if red_left == True:
        pygame.draw.circle(display_surface, red, (345,490), 50)
    else:
        pygame.draw.circle(display_surface, red, (345,490), 50, 2)

    if red_right == True:
        pygame.draw.circle(display_surface, red, (455,490), 50)
    else:
        pygame.draw.circle(display_surface, red, (455,490), 50, 2)
    
    
    #Draw titles
    font = pygame.font.Font(None, 40)
    font_big = pygame.font.Font(None, 72)

    left_elapsed_title = font.render('Elasped Time', True, white)
    display_surface.blit(left_elapsed_title, (50,300)) 
    left_elapsed= font_big.render(str(left_lane_total_time), True, white)
    display_surface.blit(left_elapsed, (50,350)) 

    right_elapsed_title = font.render('Elasped Time', True, white)
    display_surface.blit(right_elapsed_title, (580,300)) 
    right_elapsed= font_big.render(str(right_lane_total_time), True, white)
    display_surface.blit(right_elapsed, (580,350)) 

    left_reaction_time_title = font.render('Reaction Time', True, white)
    display_surface.blit(left_reaction_time_title, (50,600)) 
    left_reaction= font_big.render(str(left_lane_reaction_time), True, white)
    display_surface.blit(left_reaction, (50,650))  

    right_reaction_time_title = font.render('Reaction Time', True, white)
    display_surface.blit(right_reaction_time_title, (580,600))
    right_reaction= font_big.render(str(right_lane_reaction_time), True, white)
    display_surface.blit(right_reaction, (580,650)) 
  
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
  
        # Draws the surface object to the screen.   
        pygame.display.update()  