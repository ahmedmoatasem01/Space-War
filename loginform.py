import pygame

pygame.init()


screen_width = 400
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))


pygame.display.set_caption("Game Menu")
pygame.display.set_caption("Space War")
icon = pygame.image.load('warship.png')
pygame.display.set_icon(icon)
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))


font = pygame.font.SysFont('Arial', 25)

username = "username"
password = "password"


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
cyan=(64,224,208)


username_box = pygame.Rect(150, 150, 200, 32)
password_box = pygame.Rect(150, 250, 200, 32)

login_button = pygame.Rect(150, 300, 80, 40)
close_button = pygame.Rect(270, 300, 80, 40)


username_input = ""
password_input = ""


message = ""
message_color = black


def display_message(text, color):
    global message, message_color
    message = text
    message_color = color


def check_login():
    global username_input, password_input
    if username_input == username and password_input == password:
        display_message("Login Successful!", green)
    else:
        display_message("Incorrect Username or Password", red)


def draw_screen():
    # Draw the background image
    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, white, username_box, 2)
    pygame.draw.rect(screen, white, password_box, 2)
    pygame.draw.rect(screen, cyan, login_button, 2)
    pygame.draw.rect(screen, red, close_button, 2)

    text_surface = font.render("Username:", True, white)
    screen.blit(text_surface, (20, 150))
    text_surface = font.render("Password:", True, white)
    screen.blit(text_surface, (20, 250))

    text_surface = font.render(username_input, True, black)
    screen.blit(text_surface, (username_box.x + 10, username_box.y + 5))
    text_surface = font.render(password_input, True, black)
    screen.blit(text_surface, (password_box.x + 10, password_box.y + 5))

    text_surface = font.render("Login", True, white)
    screen.blit(text_surface, (login_button.x + 16, login_button.y + 3))
    text_surface = font.render("Close", True, red)
    screen.blit(text_surface, (close_button.x + 16, close_button.y + 4))

    text_surface = font.render(message, True, message_color)
    screen.blit(text_surface, (10, 350))
    pygame.display.update()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if username_box.collidepoint(event.pos):
                username_input = ""
            if password_box.collidepoint(event.pos):
                password_input = ""
            if login_button.collidepoint(event.pos):
                check_login()
            if close_button.collidepoint(event.pos):
                running = False

        if event.type == pygame.KEYDOWN:
            if username_box.collidepoint(event.pos):
                if event.key == pygame.K_RETURN:
                    check_login()
                else:
                    username_input += event.unicode
            if password_box.collidepoint(event.pos):
                if event.key == pygame.K_RETURN:
                    check_login()
                else:
                    password_input += event.unicode

    draw_screen()

pygame.quit()