#第六題  一元二次方程式
import math

def RootOfQuadatic(a, b, c):

    discr = pow(b, 2)-4*a*c
    if a != 0 and discr > 0:
        x1 = (-b+math.sqrt(discr))/(2*a)
        x2 = (-b-math.sqrt(discr))/(2*a)
        result = 'Two different roots x1 = {}, x2 = {}.'.format(x1, x2)
        return result
    elif a != 0 and discr == 0:
        x = -(-b/(2*a))
        result = 'Two same roots x = {}.'.format(x)
        return result
    elif a != 0 and discr < 0:
        x1 = str(-b/(2*a)) + "+" + str(math.sqrt(-discr)/(2*a)) + "i"
        x2 = str(-b/(2*a)) + "-" + str(math.sqrt(-discr)/(2*a)) + "i"
        result = 'Two different virtual roots x1 = {}, x2 = {}.'.format(x1, x2)
        return result
    elif a == 0 and b != 0:
        x = -c/b
        result = 'The answer is {}.'.format(x)
        return result
    else:
        return 'No Solution'
if __name__=="__main__":
    a=input()
    b=input()
    c=input()
    print(RootOfQuadatic(int(a),int(b),int(c)))
