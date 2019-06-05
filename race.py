# import pygame module in this program 
import pygame 
import time
from gpiozero import LED, Button

left_button = Button(26)
right_button = Button(16)
left_finish_line = Button(4, pull_up=False)
right_finish_line = Button(14, pull_up=False)

#Variables  
start_of_game_timer = time.clock()
race_start_time = 0
countdown_started = False #When christmas tree starts
time_christmas_tree_started = 0.0

left_lane_start_time = 0
left_lane_end_time = 0
left_lane_reaction_time = 0.00
left_lane_total_time = 0.00

right_lane_start_time = 0
right_lane_end_time = 0
right_lane_reaction_time = 0.00
right_lane_total_time = 0.00

#Light states

#Left lights
stage_1_left = False
stage_2_left = False
yellow_1_left = False
yellow_2_left = False
yellow_3_left = False
green_left = False
red_left = False

#right lights
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

left_car_released = False
left_car_release_time = 0.0
right_car_released = False
right_car_release_time = 0.0

left_car_finished = False
left_car_finish_time = 0.0
right_car_finished = False
right_car_finish_time = 0.0

race_ended = False


#List of functions needed for the game

def car_start_button_pressed(button):
    global ready_for_countdown, left_lane_ready, right_lane_ready, green_left, green_right, stage_1_left, stage_2_left, stage_1_right, stage_2_right, red_right, red_left, left_car_released, right_car_released
   
    if ready_for_countdown == False:
        if button.pin.number == 26: # left lane
            left_lane_ready = True
            stage_1_left = True
            stage_2_left = True
            print("left lane ready for countdown")
        if button.pin.number == 16: #right lane
            right_lane_ready = True
            stage_1_right = True
            stage_2_right = True
            print("right lane ready for countdown")

    if countdown_started == True:
        if button.pin.number == 26: #left lane
            if green_left == True and red_left == False:
                release_car("left")
                print("left lane released")
            else:
                if left_car_released == False:
                    red_left = True
                    left_car_released = True
                    finish_line_crossed("left")
                    print("left disqualified")

        if button.pin.number == 16: #right lane
            if green_right == True and red_right == False:
                release_car("right")
                print("right lane released")
            else:
                if right_car_released == False:
                    red_right = True
                    right_car_released = True
                    finish_line_crossed("right")
                    print("right disqualified")
    if race_ended == True:
        reset_game()

def finish_line_crossed(button):
    global left_car_finished, left_car_finish_time, right_car_finished, right_car_finish_time
    if button.pin.number == 4: #left lane
        if left_car_finished == False:
            left_car_finished = True
            left_car_finish_time = time.clock()
            print("Left car finished")
    if button.pin.number == 14: #right lane
        if right_car_finished == False:
            right_car_finished = True
            right_car_finish_time = time.clock()
            print("Right car finished")
    

def start_countdown():
    global countdown_started, time_christmas_tree_started, race_start_time
    countdown_started = True
    time_christmas_tree_started = time.clock()
    race_start_time = time_christmas_tree_started + 2
    print("countdown is starting")
    #reset times

def release_car(lane):
    global left_car_released, left_car_release_time, right_car_released, right_car_release_time
    
    if lane == "left":
        if left_car_released == False:
            left_car_released = True
            left_car_release_time = time.clock()
            print(lane + " car released")
    if lane == "right":
        if right_car_released == False:
            right_car_released = True
            right_car_release_time = time.clock()
            print(lane + " car released")

def countdown_ready():
    global left_lane_ready, right_lane_ready, ready_for_countdown
    if left_lane_ready == True and right_lane_ready == True:
        ready_for_countdown = True
    else:
        ready_for_countdown = False

def gate_control():
    global left_lane_release_down, right_lane_release_down
    if left_lane_release_down == True:
        print("Left lane gate open")
    else:
        print("Left lane gate closed")
    if right_lane_release_down == True:
        print("Right lane gate open")
    else:
        print("Right lane gate closed")

def countdown_control():
    #control the light countdown
    global time_christmas_tree_started, yellow_1_left, yellow_1_right, yellow_2_left, yellow_2_right, yellow_3_left, yellow_3_right, green_left, green_right, red_left, red_right
    if countdown_started == True:
        time_now = time.clock()
        interval_between_lights = 0.5

        if ((interval_between_lights *1) + time_christmas_tree_started) < time_now:
            yellow_1_left = True
            yellow_1_right = True

        if ((interval_between_lights * 2) + time_christmas_tree_started) < time_now:
            yellow_2_left = True
            yellow_2_right = True

        if ((interval_between_lights * 3) + time_christmas_tree_started) < time_now:
            yellow_3_left = True
            yellow_3_right = True

        if ((interval_between_lights * 4) + time_christmas_tree_started) < time_now:
            if red_left == False:
                green_left = True
            if red_right == False:
                green_right = True


def end_race():
    global left_car_finished, right_car_finished, race_start_time, left_car_release_time, right_car_release_time, left_car_finish_time, right_car_finish_time, left_reaction, right_reaction, left_elapsed, right_elapsed, race_ended, left_lane_total_time, right_lane_total_time, left_lane_reaction_time, right_lane_reaction_time, left_car_release_time, right_car_release_time
    if left_car_finished == True and right_car_finished == True and race_ended == False:
        print("Race ended")
        race_ended = True
        #Calculate times
        left_lane_total_time = left_car_finish_time - race_start_time
        right_lane_total_time = right_car_finish_time - race_start_time
        left_lane_reaction_time = left_car_release_time - race_start_time
        right_lane_reaction_time = right_car_release_time - race_start_time
        print(left_elapsed)
        print(right_elapsed)
        #reset variables

def reset_game():
    global start_of_game_timer, race_start_time, countdown_started, time_christmas_tree_started
    start_of_game_timer = time.clock()
    race_start_time = 0
    countdown_started = False #When christmas tree starts
    time_christmas_tree_started = 0.0

    global left_lane_start_time, left_lane_end_time, left_lane_reaction_time, left_lane_total_time
    left_lane_start_time = 0
    left_lane_end_time = 0
    left_lane_reaction_time = 0.00
    left_lane_total_time = 0.00

    global right_lane_start_time, right_lane_end_time, right_lane_reaction_time, right_lane_total_time
    right_lane_start_time = 0
    right_lane_end_time = 0
    right_lane_reaction_time = 0.00
    right_lane_total_time = 0.00

    #Light states

    #Left lights
    global stage_1_left, stage_2_left, yellow_1_left, yellow_2_left, yellow_3_left, green_left, red_left
    stage_1_left = False
    stage_2_left = False
    yellow_1_left = False
    yellow_2_left = False
    yellow_3_left = False
    green_left = False
    red_left = False

    #right lights
    global stage_1_right, stage_2_right, yellow_1_right, yellow_2_right, yellow_3_right, green_right, red_right
    stage_1_right = False
    stage_2_right = False
    yellow_1_right = False
    yellow_2_right = False
    yellow_3_right = False
    green_right = False
    red_right = False

    global left_lane_ready, right_lane_ready, left_lane_release_down, right_lane_release_down, ready_for_countdown 
    left_lane_ready = False
    right_lane_ready = False
    left_lane_release_down = False
    right_lane_release_down = False
    ready_for_countdown = False

    global left_car_released, left_car_release_time, right_car_released, right_car_release_time
    left_car_released = False
    left_car_release_time = 0.0
    right_car_released = False
    right_car_release_time = 0.0

    global left_car_finished, left_car_finish_time, right_car_finished, right_car_finish_time, race_ended
    left_car_finished = False
    left_car_finish_time = 0.0
    right_car_finished = False
    right_car_finish_time = 0.0

    race_ended = False
    
    
right_button.when_pressed = car_start_button_pressed
left_button.when_pressed = car_start_button_pressed
left_finish_line.when_pressed = finish_line_crossed
right_finish_line.when_pressed = finish_line_crossed
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
    left_elapsed= font_big.render(str(round(left_lane_total_time,3)), True, white)
    display_surface.blit(left_elapsed, (50,350)) 
                                                                                      
    right_elapsed_title = font.render('Elasped Time', True, white)
    display_surface.blit(right_elapsed_title, (580,300)) 
    right_elapsed= font_big.render(str(round(right_lane_total_time,3)), True, white)
    display_surface.blit(right_elapsed, (580,350)) 

    left_reaction_time_title = font.render('Reaction Time', True, white)
    display_surface.blit(left_reaction_time_title, (50,600)) 
    left_reaction= font_big.render(str(round(left_lane_reaction_time,3)), True, white)
    display_surface.blit(left_reaction, (50,650))  

    right_reaction_time_title = font.render('Reaction Time', True, white)
    display_surface.blit(right_reaction_time_title, (580,600))
    right_reaction= font_big.render(str(round(right_lane_reaction_time,3)), True, white)
    display_surface.blit(right_reaction, (580,650)) 
  

    #Code for game logic
    countdown_control()
    countdown_ready()
    if ready_for_countdown == True and countdown_started == False:
        start_countdown()
    end_race()


    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                car_start_button_pressed("left")
            if event.key == pygame.K_w:
                car_start_button_pressed("right")
            if event.key == pygame.K_a:
                finish_line_crossed("left")
            if event.key == pygame.K_s:
                finish_line_crossed("right")

        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
  
    # Draws the surface object to the screen.   
    pygame.display.flip()  
