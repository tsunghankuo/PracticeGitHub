#第三題 兩光法師占卜術
import sys

for s in sys.stdin:
    nums = s.split(' ')
    month, date = nums
    fortune = (int(month) * 2 + int(date)) % 3

    if fortune == 0:
        print('普通')
    elif fortune == 1:
        print('吉')
    else:
        print('大吉')
