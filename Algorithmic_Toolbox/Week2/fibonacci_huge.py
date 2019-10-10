#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:57:02 2019

@author: chaoli
"""

import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    arr = [0,1]

    for _ in range(n-1):
        previous, current = current % m, (previous + current) % m
        arr.append(current)
        if previous == 0 and current == 1:
            size = len(arr) - 2
            return arr[n % size ]
    return current


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))