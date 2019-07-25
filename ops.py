import os
import time
import json
from datetime import datetime


def restart_docker_compose(port, path):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H%M%S_%f')
    os.chdir(path)
    os.system("docker-compose restart 2>&1 | tee /data/luqi/log/{}_restart_docker_compose_{}.log &".format(timestamp, port))
    print('restart_docker_compose done.')

def restart():
    with open('/home/zijie0/ops/port_info.json', 'r') as f:
        Port2Space = json.load(f)
    print('你要重启哪个端口：（输入q直接退出）')
    for port, info in Port2Space.items():
        print('    {}: {}'.format(port, info))
    print('注意：重启前请一定确认相关人员工作可以被打断！')
    # 输入一次，重启某端口
    port = str(input())
    if port == 'q':
        return
    elif port in Port2Space:
        restart_docker_compose(port, Port2Space[port]['path'])
    else:
        print('此端口不存在')


def detect():
    os.system('free -m > free.log')
    time.sleep(1)
    with open('free.log', 'r') as f:
        print(f.read())


Tasks = {
    'detect': {'func': detect, 'comment': "监控机器使用情况"},
    'restart': {'func': restart, 'comment': "重启工作环境"},
    'q': {'func': None, 'comment': "退出"},
    '<Return>': {'func': None, 'comment': "直接回车，刷新一下"},
}

def ui():
    while True:
        print('> 你要做什么：')
        for name, info in Tasks.items():
            print('    {:<10}: {}'.format(name, info['comment']))
        print('> ', end='')
        order = str(input())
        if order == 'q':
            break
        elif order == '':
            pass
        elif order in Tasks:
            Tasks[order]['func']()
        else:
            print('此任务不存在，请重新输入')

ui()
