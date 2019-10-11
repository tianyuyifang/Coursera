# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(char=next, position=i))
        if next in ")]}":
            if not are_matching(opening_brackets_stack.pop().char, next):
                return i+1
    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack.pop().position + 1


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
