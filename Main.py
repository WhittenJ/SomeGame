import pygame
import random

pygame.init()

display_width = 800
display_height = 600

# Colors, RGB
black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

# Setting up the surface of the game window
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Title Here')
clock = pygame.time.Clock()

# Player Icons
img = pygame.image.load('C:\\Users\\jwhitten\\Documents\\Python\\Top Down Racing\\sonic_r.png')
(img_width, img_height) = img.get_rect().size  # Get img's size

# Set Icon for game window
icon_img = pygame.image.load('C:\\Users\\jwhitten\\Documents\\Python\\Top Down Racing\\sonic_icon.png')
pygame.display.set_icon(icon_img)

# Setting sounds and music
# crash_sound = pygame.mixer.Sound('C:\\Users\\jwhitten\\Documents\\Python\\Top Down Racing\\crash.wav')
# pygame.mixer.music.load('C:\\Users\\jwhitten\\Documents\\Python\\Top Down Racing\\background_music.mp3')

def main_menu():
    menu = True
    while menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #  Move menu cursor left
                    1
                elif event.key == pygame.K_RIGHT:
                    #  Move menu cursor right
                    1
                elif event.key == pygame.K_UP:
                    #  Move menu cursor up
                    1
                elif event.key == pygame.K_DOWN:
                    #  Move menu cursor down
                    1
                elif event.key == pygame.K_p:
                    #  Pause game
                    pause = True
                    # game_pause()
