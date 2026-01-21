import pgzrun
import pygame
import math
import sys
import time

WIDTH = 960
HEIGHT = 720
bj = Actor('bj.png', (480, 360))
r = Actor('r.png', (-1100, 360))
my = Actor('my.png', (480, 360))
red = Actor('red.png',(360,360))
f = None
n = 1
t = 0
c = False
def draw():
    global f,t
    bj.draw()
    r.draw()
    my.draw()
    if t == 1:
        time.sleep(2)
        sys.exit()
    if f == True:
        red.draw()
        if my.colliderect(red):
            screen.draw.text('碰到红色/边缘了！游戏失败！', (20, 300), fontsize=70, color="yellow", fontname='simhei.ttf')
            t = 1
        else:
            screen.draw.text('游戏成功！', (50, 250), fontsize=200, color="yellow", fontname='simhei.ttf')
            t = 1
    if f == False:
        screen.draw.text('碰到红色/边缘了！游戏失败！', (20, 300), fontsize=70, color="yellow", fontname='simhei.ttf')
        t = 1
def update():
    global f,c
    if keyboard.up:
        my.y -= 10
    if keyboard.down:
        my.y += 10
    if keyboard.left:
        my.x -= 5
    if keyboard.right:
        my.x += 5
    local_x = int(my.x - r.x + r.width/2)  # 基于图像中心的偏移计算
    local_y = int(my.y - r.y + r.height/2)
    
    # 2. 检查坐标是否在r图像范围内
    if 0 <= local_x < r.width and 0 <= local_y < r.height:
        # 3. 获取该位置的颜色
        color = r._orig_surf.get_at((local_x, local_y))[:3]
        if color[1] < 25 and color[2] < 25:
            f = False
    if (my.x < 0 or my.x > 960) or (my.y < 0 or my.y > 720):
        f = False
    if r.x > 2000 and c == False:
        c = True
        f = True
def m():
    global n
    r.x += n
    n += 2
clock.schedule_interval(m,0.5)   
pgzrun.go()