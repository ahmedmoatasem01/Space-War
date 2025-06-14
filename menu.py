import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("Game Menu")
pygame.display.set_caption("Space War")
icon = pygame.image.load('warship.png')
pygame.display.set_icon(icon)

# Set up colors
background = pygame.image.load('Background.jpg')
background_color = (0, 0, 0)
text_color = (255, 255, 255)
button_color = (50, 50, 50)
button_hover_color = (100, 100, 100)

# Set up fonts
title_font = pygame.font.Font(None, 60)
menu_font = pygame.font.Font(None, 40)

# Set up texts
title_text = title_font.render("Game Menu", True, text_color)
login_text = menu_font.render("Login", True, text_color)
start_text = menu_font.render("Start", True, text_color)
options_text = menu_font.render("Options", True, text_color)
exit_text = menu_font.render("Exit", True, text_color)

# Set up button dimensions
button_width = 200
button_height = 50

login_button_rect = pygame.Rect(
    (window_width - button_width) // 2,
    window_height // 2.5 - button_height // 2,
    button_width,
    button_height
)

start_button_rect = pygame.Rect(
    (window_width - button_width) // 2,
    window_height // 2 - button_height // 2,
    button_width,
    button_height

)

options_button_rect = pygame.Rect(
    (window_width - button_width) // 2,
    window_height // 1.7 - button_height // 2,
    button_width,
    button_height
)

exit_button_rect = pygame.Rect(
    (window_width - button_width) // 2,
    window_height // 1.4 - button_height // 2,
    button_width,
    button_height
)

def draw_menu():
    # Update the screen
    window.fill(background_color)
    window.blit(background,(0,0))
    window.blit(title_text, (window_width // 2 - title_text.get_width() // 2, window_height // 4))

    # Draw buttons
    pygame.draw.rect(window, button_color, login_button_rect)
    pygame.draw.rect(window, button_color, start_button_rect)
    pygame.draw.rect(window, button_color, options_button_rect)
    pygame.draw.rect(window, button_color, exit_button_rect)

    # Check if mouse is hovering over buttons and change color accordingly
    if login_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(window, button_hover_color, login_button_rect)
    if start_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(window, button_hover_color, start_button_rect)
    if options_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(window, button_hover_color, options_button_rect)
    if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(window, button_hover_color, exit_button_rect)

    # Draw button text
    window.blit(login_text, login_button_rect.move(65, 10))
    window.blit(start_text, start_button_rect.move(65, 10))
    window.blit(options_text, options_button_rect.move(45, 10))
    window.blit(exit_text, exit_button_rect.move(75, 10))

    pygame.display.update()

def handle_menu_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if login_button_rect.collidepoint(mouse_pos):
                print("Login selected")

                # Add your login code here
            elif start_button_rect.collidepoint(mouse_pos):
                print("Start selected")
                # Add your start code here
            elif options_button_rect.collidepoint(mouse_pos):
                print("Options selected")

                # Add your options code here
            elif exit_button_rect.collidepoint(mouse_pos):
                sys.exit()

def menu_screen():
    running = True
    while running:
        draw_menu()
        handle_menu_events()

# Run the menu screen
menu_screen()

# Quit the game
pygame.quit()