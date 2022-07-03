import pygame as pyg

def update_drawing(screen):
    pass

def update_physics(screen, elements,dt):
    pass

def event_handler(event, running):
    if event.type == pyg.QUIT:
        running = False


def main():
    WIDTH, HEIGHT = (500,500)
    BACKGROUNG_COLOR = (100,100,100)
    screen = pyg.display.set_mode((WIDTH, HEIGHT))
    clock = pyg.time.Clock()
    elements = []
    t = 0

    running = True
    while running:
        clock.tick(60)
        for event in pyg.event.get():
            event_handler(event, running)

        screen.fill(BACKGROUNG_COLOR)
        update_physics(screen, elements, clock.get_time()/1000)
        pyg.display.update(screen)
        pyg.display.update()


if __name__=="__main__":
    main()