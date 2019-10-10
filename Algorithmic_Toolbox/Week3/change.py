#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 22:55:34 2019

@author: chaoli
"""

import sys

def get_change(m):
    if m >= 10:
        return get_change(m-10) + 1
    elif m >= 5:
        return get_change(m-5) + 1
    else:
        return m

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))