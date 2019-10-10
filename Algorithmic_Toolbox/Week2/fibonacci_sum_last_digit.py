#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 23:13:45 2019

@author: chaoli
"""

import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    arr = [0,1]

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current + 1) % 10
        arr.append(current)
        if previous == 0 and current == 1:
            size = len(arr) - 2
            return arr[n % size]

    return current

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))