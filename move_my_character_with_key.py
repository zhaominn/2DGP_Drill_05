from pico2d import *


open_canvas()
character = load_image('BODY_skeleton.png')
ground = load_image('TUK_GROUND.png')


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
    pass


frame = 0
running = True

while running:
    clear_canvas()
    ground.draw(400,300)
    character.clip_draw(frame*64,64,64,64,400,300)
    update_canvas()
    handle_events()
    frame = (frame+1) % 9
    delay(0.05)

close_canvas()
