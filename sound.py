import pygame

pygame.mixer.init()


def play_sound(file_path):
    """
    Spielt eine Sounddatei ab.
    :param file_path: Pfad zur Sounddatei
    """
    try:
        sound = pygame.mixer.Sound(file_path)
        sound.play()
    except pygame.error as e:
        print("Fehler beim Abspielen des Sounds:", e)
