import os
import re
import time
import json
from datetime import datetime
from lib import selectstrings


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
    os.system('cat /proc/cpuinfo| grep "processor"| wc -l > n_core.log')
    time.sleep(0.1)
    with open('n_core.log', 'r') as f:
        n_core = f.read()[:-1]
        print('    核数: {}'.format(n_core))
    # 内存
    os.system('free -m > free.log')
    time.sleep(0.1)
    with open('free.log', 'r') as f:
        line = f.readlines()[1]
        name, total, used, free, shared, buff_cache, available, _ = re.split(r'\s+', line)
        print('    可用内存: {:.2f}G / {:.2f}G'.format(float(available)/1024.0, float(total)/1024.0))
        #TODO detect per seconds, and generate reports per hour/day?
#       import pdb; pdb.set_trace()


orders = [
    {'name': 'detect', 'func': detect, 'comment': "监控机器使用情况"},
    {'name': 'restart', 'func': restart, 'comment': "重启工作环境"},
]

def ui():
    while True:
        print('> 你要做什么：')
        for info in orders:
            print('    {:<10}: {}'.format(info['name'], info['comment']))
        print('> ', end='')
        sc = str(input())
        rs = selectstrings(orders, "name", sc)
        if len(rs) == 0:
            print("no match, input again")
        elif len(rs) == 1:
            rs[0]['func']()
            break
        else:
            print('此任务不存在，请重新输入')
        print()

ui()
