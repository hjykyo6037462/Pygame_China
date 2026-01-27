def run():
    name = input('请输入要卸载的文件(不含.py后缀名)>')
    if not name:
        return
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    py_file = os.path.join(current_dir, f"{name}.py")
    with open(py_file, 'r', encoding='utf-8') as f:
        code = f.readline()[1:]
    os.remove(py_file)
    png_file = os.path.join(current_dir, 'images', f"{name}.png")
    os.remove(png_file)
    set_up_file = os.path.join(current_dir, 'set_up.py')
    with open(set_up_file, 'r', encoding='utf-8') as f:
        l = f.readlines()
    new_l = []
    for i in l:
        if code not in i:
            new_l.append(i)
    with open(set_up_file, 'w', encoding='utf-8') as f:
        f.writelines(new_l)
    print('卸载成功！')
    os._exit(0)
