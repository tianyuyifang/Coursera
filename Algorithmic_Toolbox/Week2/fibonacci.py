#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:58:55 2019

@author: chaoli
"""

def calc_fib(n):
    if n <= 1:
        return n
    prev = 0
    cur = 1
    for _ in range(2,n+1):
        prev, cur = cur, prev + cur
    return cur

if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))