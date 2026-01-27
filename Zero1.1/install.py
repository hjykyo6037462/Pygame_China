def run():
    name = input('请输入要安装文件名(不含.py后缀名)>')
    if not name:
        return
    import os
    path = os.path.dirname(os.path.abspath(__file__))
    a = os.path.join(path, 'images', f"{name}.png")
    if not os.path.exists(a):
        print('找不到png文件(文件可能不存在或格式为jpg等)')
        return
    app_path = os.path.join(path, f"{name}.py")
    with open(app_path, 'r', encoding='utf-8') as f:
        code = f.readline()[1:]
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "set_up.py")
    insert_code = '    '+code
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines.insert(6, insert_code)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('安装成功！')
    os._exit(0)
