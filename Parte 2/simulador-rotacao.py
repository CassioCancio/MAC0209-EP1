import pygame as pyg
import importlib
modelador = importlib.import_module("modelador-circular")

class Experiment_Data:
    g = 9.807
    loop_radius = 0.145
    circle_radius = 0.008705

    @classmethod
    def get_proportions(screen_size):
        #aqui loop radius = scalar
        w, h = screen_size
        scalar = min(w,h)
        circle = int(scalar*self.circle_radius/self.loop_radius)
        gravity = scalar*self.g/self.loop_radius
        return gravity, scalar, circle



def update_drawing(screen):
    pass

def update_physics(screen, elements,dt):
    pass

def event_handler(event, running):
    if event.type == pyg.QUIT:
        running = False


def main():
    experiment_index = 2 
    data = modelador.Experiment_Handler(experiment_index)
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
        pyg.display.update()


if __name__=="__main__":
    main()