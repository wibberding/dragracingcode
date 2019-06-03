# import pygame module in this program 
import pygame 
import time

clock = pygame.time.Clock()
#Variables  
start_of_game_timer = time.clock()
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

left_lane_ready = False
right_lane_ready = False
left_lane_release_down = False
right_lane_release_down = False
ready_for_countdown = False

left_lane_disqualify = False
right_lane_disqualify = False


#List of functions needed for the game

def car_start_button_pressed(lane):
    global ready_for_countdown, left_lane_ready, right_lane_ready, green_left, green_right, stage_1_left, stage_2_left, stage_1_right, stage_2_right
    if ready_for_countdown == False:
        if lane == "left":
            left_lane_ready = True
            stage_1_left = True
            stage_2_left = True
        if lane == "right":
            right_lane_ready = True
            stage_1_right = True
            stage_2_right = True
    if ready_for_countdown == True:
        if lane == "left":
            if green_left == True:
                release_car(lane)
        if lane == "right":
            if green_right == True:
                release_car(lane)

def finish_line_crossed(lane):
    pass

def start_timer():
    pass

def start_race():
    pass

def release_car(lane):
    pass

def countdown_ready():
    global left_lane_ready, right_lane_ready, ready_for_countdown
    if left_lane_ready == True and right_lane_ready == True:
        ready_for_countdown = True
    else:
        ready_for_countdown = False


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
image = pygame.image.load('images/mustang.jpg') 
  
# infinite game loop 
while True : 
    
    # completely fill the surface object 
    # with white colour 
    display_surface.fill(black) 
  
    # copying the image surface object 
    # to the display surface object at 
    # (0, 0) coordinate. 
    display_surface.blit(image, (0, 0)) 

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
  

    #Code for game logic
    countdown_ready()


    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                car_start_button_pressed("left")
            if event.key == pygame.K_w:
                car_start_button_pressed("right")

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