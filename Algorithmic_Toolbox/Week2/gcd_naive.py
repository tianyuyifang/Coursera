#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:15:37 2019

@author: chaoli
"""

import sys

def gcd_naive(a, b):
    a,b = max(a, b), min(a, b)
    if b == 0:
        return a
    else:
        return gcd_naive(b, a % b)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))