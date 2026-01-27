import pgzrun
import set_up

WIDTH = 2500
HEIGHT = 1500
l = {}
input_text = ''
key = False
aBc = False
def on_key_down(key):
    """按键按下事件：处理所有输入逻辑（字母/数字/空格/退格/Shift大小写）"""
    global input_text,aBc
    # 仅当键盘激活时处理输入
    if not key:
        return
    
    key_name = key.name  # 获取当前按下的按键名称
    if key_name == 'CAPSLOCK':
        if aBc == False:
            aBc = True
            print('已开启大写模式')
        else:
            aBc = False
            print('已开启小写模式')
        return
    # 1. 处理字母键（根据Shift切换大小写）
    if key_name.isalpha() and len(key_name) == 1:
        if aBc:
            input_text += key_name # 大写
        else:
            input_text += key_name.lower()  # 小写
    # 2. 处理数字键（PGZero数字键名是k_1/k_2等，提取最后一位）
    elif key_name.startswith('K_') and len(key_name) == 3:
        num = key_name[-1]
        input_text += num
    # 3. 处理空格
    elif key_name == 'SPACE':
        input_text += ' '
    # 4. 处理回车
    elif key_name == 'RETURN':
        with open('input_f.txt', 'w', encoding='utf-8') as file:
            file.write(input_text)
        input_text = ''
    # 5. 处理退格（删除最后一个字符）
    elif key_name == 'BACKSPACE' and len(input_text) > 0:
        input_text = input_text[:-1]
def draw():
    global l,input_text,key
    screen.clear()
    l = set_up.ima()
    for i in l:
        l[i].draw()
    if key == True:
        screen.draw.text('Zero_Users>'+input_text+'|',(10, 1400),fontsize=50,color=(255, 255, 255))
def on_mouse_down(pos):
    global l,key,input_text
    for i in l:
        if l[i].collidepoint(pos):
            if i == 'in_keyboard' and key != None:
                if key == False:
                    input_text = ''
                    key = True
                    print('已开启输入法')
                else:
                    key = False
                    print('已关闭输入法')
            else:
                set_up.run(i)
pgzrun.go()