#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: Vesper Huang
"""

import sys
import os
import re
import time

if __name__ == "__main__":
    dirs = os.listdir("../")
    path = os.getcwd()
    for dire in dirs:
        if os.path.isfile(dire):
            if re.search(r".*\.null$", dire):
                new_name = re.sub(r"\.null", ".mp4", dire)
                print "rename %s to %s" % (dire, new_name)
                os.rename(os.path.join(path, dire), os.path.join(path, new_name))
    # s = raw_input("press any key to end")
    time.sleep(1)