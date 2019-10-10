#Uses python3

import sys
import functools

def greaterThan(a, b):
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    return ab - ba

def largest_number(a):
    
    b = sorted(a, key=functools.cmp_to_key(greaterThan), reverse=True)
    return int("".join(map(str,b)))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
