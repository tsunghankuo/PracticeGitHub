#第五題 Eva的回家作業

n = int(input())

if n > 20 or n < 0:
    pass
else:
    for i in range(n):
        A, B, C, D = input().split()
        a = int(A)
        b = int(B)
        c = int(C)
        d = int(D)
        if b-a == c-b:
            e = d+b-a
        elif a*c == b**2:
            e = int(d*(b/a))
        else:
            pass
        print(a,end=' ')
        print(b,end=' ')
        print(c,end=' ')
        print(d,end=' ')
        print(e)
