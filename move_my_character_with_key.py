from pico2d import *


open_canvas()
character = load_image('BODY_skeleton.png')
ground = load_image('TUK_GROUND.png')


def handle_events():
    global running, dirX, dirY

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dirX += 1
            elif event.key == SDLK_LEFT:
                dirX -= 1
            elif event.key == SDLK_UP:
                dirY += 1
            elif event.key == SDLK_DOWN:
                dirY -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type==SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirX-=1
            elif event.key == SDLK_LEFT:
                dirX+=1
            elif event.key == SDLK_UP:
                dirY-=1
            elif event.key == SDLK_DOWN:
                dirY+=1

running = True
x = 800 // 2
y= 600 // 2
frame = 0
dirX = 0
dirY = 0


while running:
    clear_canvas()
    ground.clip_draw(0,0, 1280, 1024, 400, 300,800,600)
    character.clip_draw(frame * 64, 64, 64, 64, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 9
    x += dirX * 5
    y += dirY * 5
    delay(0.05)

close_canvas()
