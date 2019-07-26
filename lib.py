#-*- coding: utf8 -*-
import os
import time
import pprint

def split():
    print("---------------------------------------------------------------------------------")

def look(x, to_file=False, without_split=False):
    if not to_file:
        if not without_split:
            split()
        pprint.pprint(x)
    else:
        return pprint.pformat(x)

def timing():
    start = pre = time.time()
    yield None
    while True:
        now = time.time()
        yield float('%.3f' % (now-pre))
        pre = now

def add_key(d, key, debug=False):
    if debug:
        print('d={}'.format(d))
        print('key={}'.format(key))
    d[key] = key in d and d[key]+1 or 1

def prettylen(s):
    n = 0
    for c in s:
        if '\u4e00' <= c <= '\u9fff' or c=='（' or c=='）' or c=='，' or c=='：':
            n = n + 2
        else:
            n = n + 1
    return n

def to_yaml(inf, level=0):
    output = ""
    if isinstance(inf, list):
        if level > 0:
            output += '\n'
        for value in inf:
            output += "{}- {}".format(level*4*' ', to_yaml(value, level+1))
    elif isinstance(inf, dict):
        if level > 0:
            output += '\n'
        for key, value in inf.items():
            output += "{}{}: {}".format(level*4*' ', key, to_yaml(value, level+1))
    else:
        output += "{}\n".format(inf)
    return output

def prettyprint(infs):
    interval = 10
    maxlens = {}
    for inf in infs:
        for key, value in inf.items():
            if maxlens.__contains__(key) and prettylen(value) <= maxlens[key]:
                continue
            maxlens[key] = prettylen(value)
    print("---------------------------------------------------------------------")
    lastkey = ""
    for inf in infs:
        for key, value in inf.items():
            lastkey = key
        break
    for inf in infs:
        for key, value in inf.items():
            if key != lastkey:
                print(value + (interval+maxlens[key]-prettylen(value))*' ', end='')
            else:
                print(value, end='')
        print('')
    print("---------------------------------------------------------------------")

def selectstrings2(sc, lines):
    rs = []
    for line in lines:
        if line.find(sc) != -1:
            rs.append(line)
    return rs

def selectstrings(infs, key, sc):
    rs = []
    for inf in infs:
        if inf[key].find(sc) != -1:
            rs.append(inf)
    return rs
