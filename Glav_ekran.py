import pygame
from tkinter import *
from tkinter import filedialog


pygame.init()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Моноэтажка")


background_image = pygame.image.load("background.jpg")
button_image = pygame.image.load("button.png")


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def choose_background_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        return pygame.image.load(file_path)
    else:
        return None


def choose_button_image():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        return pygame.image.load(file_path)
    else:
        return None


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(background_image, (0, 0))


    screen.blit(button_image, (SCREEN_WIDTH // 2 - button_image.get_width() // 2, 200))
    screen.blit(button_image, (SCREEN_WIDTH // 2 - button_image.get_width() // 2, 300))
    screen.blit(button_image, (SCREEN_WIDTH // 2 - button_image.get_width() // 2, 400))


    font = pygame.font.Font(None, 36)
    draw_text("Начать", font, WHITE, screen, SCREEN_WIDTH // 2 - 50, 220)
    draw_text("Настройки", font, WHITE, screen, SCREEN_WIDTH // 2 - 70, 320)
    draw_text("Выход", font, WHITE, screen, SCREEN_WIDTH // 2 - 50, 420)


    pygame.display.flip()


pygame.quit()
