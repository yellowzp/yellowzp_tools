#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Vesper Huang
"""
import psutil
import os


KILL_LIST = [
    'iOACloudRtp.exe',
    'iOACloudGuard.exe',
    'iOACloudClient.exe',
    'iOAGui.exe'
]


if __name__ == "__main__":
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() in KILL_LIST:
            print('pid: %s, pname: %s' % (pid, p.name()))
            # cmd_str = 'taskkill /F /IM %s' % p.name()
            # os.system(cmd_str)