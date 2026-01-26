import pgzrun
import set_up

WIDTH = 2500
HEIGHT = 1500

l = {}
def draw():
    global l
    l = set_up.ima()
    for i in l:
        l[i].draw()
def on_mouse_down(pos):
    global l
    for i in l:
        if l[i].collidepoint(pos):
            set_up.run(i)
pgzrun.go()