import sys

for s in sys.stdin:
    nums = s.split(' ')
    a, b = nums

    a, b = int(a), int(b)
    print(a + b)
