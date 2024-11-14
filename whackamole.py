import pygame
import random

BOARD_ROWS = 16
BOARD_COLS = 20
LINE_WIDTH = 1
WIDTH = 640
HEIGHT = 512
SQUARE_SIZE = 32
LINE_COLOR = (0, 0, 0)

mole_image = pygame.image.load("mole.png")

screen = pygame.display.set_mode((640, 512))


def draw_grid():
    for i in range(1, BOARD_ROWS + 1):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )
    for i in range (1, BOARD_COLS+ 1):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i*SQUARE_SIZE, 0),
            (i*SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

def place_mole(x_coordinate, y_coordinate):
    mole_image_rect = mole_image.get_rect()
    mole_image_rect.topleft = (x_coordinate, y_coordinate)
    screen.blit(mole_image, mole_image_rect)

def move_mole():

    x_position = random.randrange(0, BOARD_COLS)
    y_position = random.randrange(0, BOARD_ROWS)
    x_coordinate = x_position * SQUARE_SIZE
    y_coordinate = y_position * SQUARE_SIZE
    print(x_coordinate, y_coordinate)
    return x_coordinate, y_coordinate

    # mole_image_rect = mole_image.get_rect()
    # mole_image_rect.center = (x_coordinate, y_coordinate)
    # screen.blit(mole_image, mole_image_rect)


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        #screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))

        x_coordinate = 0
        y_coordinate = 0
        p_x = 0
        p_y = 0

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    print (x, y)
                    if x <= x_coordinate + SQUARE_SIZE and x >= x_coordinate - SQUARE_SIZE and  y <= y_coordinate + SQUARE_SIZE and y >= y_coordinate - SQUARE_SIZE:
                        x_coordinate, y_coordinate = move_mole()
            screen.fill("light green")
            draw_grid()
            place_mole(x_coordinate, y_coordinate)
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
