import pygame
import game_config as gc

from pygame import display, event, image
from time import sleep
from demon import Demon

def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TILES_SIDE + col
    return row, col, index
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        #get cilck
        pos = pygame.mouse.get_pos()

        #chech clicked:
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
                
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button
        screen.blit(self.image, self.rect)
        
        return action
pygame.init()
display.set_caption('My Game')
screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))
matched = image.load('other_assets/matched.png')
background = image.load('other_assets/backgroundx.png')
start = image.load('other_assets/start_btn.png')
exit = image.load('other_assets/exit_btn.png')
running = True
tiles = [Demon(i) for i in range(0, gc.NUM_TILES_TOTAL)]
current_images_displayed = []
score = 0
RED = (255, 45, 123)
frame_count = 0
frame_rate = 60
start_time = 20
game_over = 0
exit_button = Button(450,450,exit) 
while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
        if start_time >= 0 :

            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row, col, index = find_index_from_xy(mouse_x, mouse_y)
                if index not in current_images_displayed:
                    if len(current_images_displayed) > 1:
                        current_images_displayed = current_images_displayed[1:] + [index]
                    else:
                        current_images_displayed.append(index)
       
    # Display 
    screen.fill((0, 0, 0))
    screen.blit(background ,(100,300))
    total_skipped = 0
    # Score   
    myfont = pygame.font.SysFont("GG25", 35)
    scoretext = myfont.render("Score = "+str(score),1,(255, 45, 123))
    screen.blit(scoretext, (40, 800))
    #Time
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 35)
    total_seconds = start_time - (frame_count // frame_rate)
    if total_seconds < 0:
        total_seconds = 0
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    output_string = "Time End: {0:02}:{1:02}".format(minutes, seconds)    
    text = font.render(output_string, True, RED)
    screen.blit(text, [500, 800])
    frame_count += 1
    clock.tick(frame_rate)
    if total_seconds == 0 :
        game_over = 1
    #Button
    exit_button.draw()
   
   
   
    #
    for i, tile in enumerate(tiles):
        current_image = tile.image if i in current_images_displayed else tile.box
        if not tile.skip:
            screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped += 1
    display.flip()

    # Check for matches
    
    if game_over == 0:
        if len(current_images_displayed) == 2:
            idx1, idx2 = current_images_displayed
       
            if tiles[idx1].name == tiles[idx2].name:
                score += 1
                tiles[idx1].skip = True
                tiles[idx2].skip = True
        
            # display matched message
                sleep(0.2)
                screen.blit(matched, (100, 200))
                display.flip()
                sleep(0.5)
                current_images_displayed = []

    #text option
    #   

        if total_skipped == len(tiles):
            running = False

print('Goodbye!')
