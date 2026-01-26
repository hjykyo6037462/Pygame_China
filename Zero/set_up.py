import pgzrun
from pgzero.actor import Actor

def ima():
    l = {}
    l['install'] = Actor('install.png',(150,100))
    l['uninstall'] = Actor('uninstall',(150,300))
    return l
def run(name):
    exec('import '+name)
    exec(name+'.run()')