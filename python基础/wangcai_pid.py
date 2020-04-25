#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2019/11/19 10:09
# @Author : "zhy"

import psutil
import time
import re, sys


def processinfo(x):
    p = psutil.process_iter()
    tlp = 0
    try:
        for r in p:
            aa = str(r)
            f = re.compile(x, re.I)
            if f.search(aa):
                tlp = int(aa.split('pid=')[1].split(',')[0])
                # 检索pid列表并获取传入值的pid
                return tlp
    except (psutil.NoSuchProcess):
        print('Ransomware process is caught, but the process does '
              'not exist (PID: %d)' % aa.pid)


def getinfo(tlp):
    p = psutil.Process(tlp)
    cpu_list = []
    for i in range(10):
        p_cpu = p.cpu_percent(interval=0.1)
        cpu_list.append(p_cpu)
        cpu = 0.00
        cpu = float(sum(cpu_list)) / len(cpu_list) / 10
        # 循环10次cpu使用值并取平均值
    try:
        pid = p.pid
        name = p.name()
        Memory = p.memory_percent(memtype="rss") / 2
        localtime = time.strftime('%H:%M:%S', time.localtime(time.time()))
        # 取进程pid 进程名 进程内存
    except IOError as e:
        print(e)
    else:
        # return pid, name, Memory, cpu, time
        print("Time:%s" % (localtime), "PID:%s" % (pid), "Name:%s" % (name),
              "Memory=%.3f%%" % (Memory), "CPU=%.2f%%" % (cpu * 2))


if __name__ == "__main__":
    while 0 < 1:
        time.sleep(10)
        s = processinfo('wangcai_main.exe')
        getinfo(s)
        if False:
            print("打开程序")
        else:
            continue
