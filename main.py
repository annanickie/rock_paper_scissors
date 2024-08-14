import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock, Paper, Scissors")

# Colors
black = (0, 0, 0)
bg_color = (255, 255, 204)  # Light yellow background
button_color = (255, 160, 122)
hover_color = (255, 218, 185)

# Load images
opening_img = pygame.image.load('opening.jpeg')
opening_img = pygame.transform.scale(opening_img, (screen_width, screen_height))

rock_img = pygame.image.load('rock.png')
paper_img = pygame.image.load('paper.png')
scissors_img = pygame.image.load('scissors.png')

# Scale game images
img_size = (150, 150)
rock_img = pygame.transform.scale(rock_img, img_size)
paper_img = pygame.transform.scale(paper_img, img_size)
scissors_img = pygame.transform.scale(scissors_img, img_size)

# Button dimensions
button_width = 150
button_height = 50

# Game text
font = pygame.font.Font(None, 36)
result_text = ''

# Function to display text on the screen
def display_text(text, center_x, center_y, color=black):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, center_y))
    screen.blit(text_surface, text_rect)

# Draw a button with text and hover effect
def draw_button_with_text(text, x, y, width, height, color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    display_text(text, x + width // 2, y + height // 2)

# Draw image with label
def draw_image_with_label(image, label, x, y):
    screen.blit(image, (x, y))
    display_text(label, x + img_size[0] // 2, y + img_size[1] + 20)

# Main game logic
def game_result(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    global result_text
    result_text = f"Computer chose: {computer_choice}"

    if user_choice == computer_choice:
        outcome = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        outcome = "You Win!"
    else:
        outcome = "You Lose!"

    result_text += f" - {outcome}"
    show_result_page()

# Page handlers
def show_opening_page():
    screen.blit(opening_img, (0, 0))
    draw_button_with_text("Start Game", (screen_width - button_width) // 2, screen_height - 100, button_width, button_height, button_color, show_game_page)

def show_game_page():
    global page
    page = "game"

def show_result_page():
    global page
    page = "result"

def reset_game():
    global page, result_text
    result_text = ''
    page = "opening"

# Main loop
page = "opening"  # Start on the opening page
running = True
while running:
    if page == "opening":
        show_opening_page()
    elif page == "game":
        screen.fill(bg_color)
        # Draw images with labels
        draw_image_with_label(rock_img, "Rock", 50, 100)
        draw_image_with_label(paper_img, "Paper", 225, 100)
        draw_image_with_label(scissors_img, "Scissors", 400, 100)
        
        # Button positions
        draw_button_with_text("Rock", 50, 260, button_width, button_height, button_color, lambda: game_result('Rock'))
        draw_button_with_text("Paper", 225, 260, button_width, button_height, button_color, lambda: game_result('Paper'))
        draw_button_with_text("Scissors", 400, 260, button_width, button_height, button_color, lambda: game_result('Scissors'))
    elif page == "result":
        screen.fill(bg_color)
        display_text(result_text, screen_width // 2, screen_height // 2 - 20)
        draw_button_with_text("Play Again", (screen_width - button_width) // 2, screen_height - 100, button_width, button_height, button_color, reset_game)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
