__author__ = 'zhanghengyang'


from fabric.api import run

def host_type():
    run('uname -s')