# import pygame module in this program 
import pygame 


#Variables  
timer = 0
race_start_time = 0

left_lane_start_time = 0
left_lane_end_time = 0
left_lane_reaction_time = 0
left_lane_total_time = 0

right_lane_start_time = 0
right_lane_end_time = 0
right_lane_reaction_time = 0
right_lane_total_time = 0

#Light states
stage_1_left = False
stage_2_left = False
yellow_1_left = False
yellow_2_left = False
yellow_3_left = False
green_left = False
red_left = False

stage_1_right = False
stage_2_right = False
yellow_1_right = False
yellow_2_right = False
yellow_3_right = False
green_right = False
red_right = False

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
# for white colour 
black = (0,0,0) 
  
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
        pygame.draw.circle(display_surface, (255,255,0), (190,50), 30)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (190,50), 30, 2)

    if stage_1_right == True:
        pygame.draw.circle(display_surface, (255,255,0), (610,50), 30)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (610,50), 30, 2)

    if stage_2_left == True:
        pygame.draw.circle(display_surface, (255,255,0), (255,50), 30)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (255,50), 30, 2)

    if stage_2_right == True:
        pygame.draw.circle(display_surface, (255,255,0), (545,50), 30)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (545,50), 30, 2)

    if yellow_1_left == True:
        pygame.draw.circle(display_surface, (255,255,0), (345,70), 50)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (345,70), 50, 2)

    if yellow_1_right == True:
        pygame.draw.circle(display_surface, (255,255,0), (455,70), 50)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (455,70), 50, 2)
    
    if yellow_2_left == True:
        pygame.draw.circle(display_surface, (255,255,0), (345,175), 50)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (345,175), 50, 2)

    if yellow_2_right == True:
        pygame.draw.circle(display_surface, (255,255,0), (455,175), 50)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (455,175), 50, 2)

    if yellow_3_left == True:
        pygame.draw.circle(display_surface, (255,255,0), (345,280), 50)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (345,280), 50, 2)

    if yellow_3_right == True:
        pygame.draw.circle(display_surface, (255,255,0), (455,280), 50)
    else:
        pygame.draw.circle(display_surface, (255,255,0), (455,280), 50, 2)
    
    if green_left == True:
        pygame.draw.circle(display_surface, (0,255,0), (345,385), 50)
    else:
        pygame.draw.circle(display_surface, (0,255,0), (345,385), 50, 2)

    if green_right == True:
        pygame.draw.circle(display_surface, (0,255,0), (455,385), 50)
    else:
        pygame.draw.circle(display_surface, (0,255,0), (455,385), 50, 2)
    
    if red_left == True:
        pygame.draw.circle(display_surface, (255,0,0), (345,490), 50)
    else:
        pygame.draw.circle(display_surface, (255,0,0), (345,490), 50, 2)

    if red_right == True:
        pygame.draw.circle(display_surface, (255,0,0), (455,490), 50)
    else:
        pygame.draw.circle(display_surface, (255,0,0), (455,490), 50, 2)
    
    
    
    
  
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