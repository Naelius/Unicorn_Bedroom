import pygame

pygame.mixer.init()

klick_sound = pygame.mixer.Sound('click.mp3')

def play_click_sound():
    klick_sound.play()