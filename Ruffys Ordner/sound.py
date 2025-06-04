import pygame

pygame.init()
click_sound = 'click.wav'

def play_click_sound():
    try:
        pygame.mixer.music.load(click_sound)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"Fehler beim Abspielen des Sounds: {e}")