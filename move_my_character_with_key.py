from pico2d import *


open_canvas()
character = load_image('BODY_skeleton1.png')
ground = load_image('TUK_GROUND.png')


def handle_events():
    global running, dirX, dirY, x, y

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
            if dirX != 0:
                dirX = 0
            if dirY != 0:
                dirY = 0

def draw_character():
    global frame

    if dirX > 0:
        imageNum = 0
    elif dirX < 0:
        imageNum = 2
    elif dirY > 0:
        imageNum = 3
    else:
        imageNum = 1

    if imageNum == 0:
        if frame < 4:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        else:
            character.clip_draw((frame - 4) * 100, 0, 100, 100, x, y)
    else:
        character.clip_draw(frame * 64, 136 + imageNum * 64, 64, 64, x, y,100,100)


running = True
x = 800 // 2
y= 600 // 2
frame = 0
dirX = 0
dirY = 0


while running:
    clear_canvas()
    ground.clip_draw(0,0, 1280, 1024, 400, 300,800,600)
    draw_character()
    update_canvas()
    handle_events()
    frame = (frame + 1) % 9
    if 20 <= x + dirX * 5 <= 780:
        x += dirX * 5
    if 40 <= y + dirY * 5 <= 560:
        y += dirY * 5
    delay(0.05)

close_canvas()
