def equilateral(sides):
    #sides=[2,2,3]
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if (a==b==c) and a>0 and b>0 and c>0 :
        return True
    else:
        return False

def isosceles(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if (a==b or a==c or b==c) and (a+b>=c and b+c>=a and a+c>=b):
        return True
    else:
        return False


def scalene(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    if (a!=b!=c) and (a!=c) and (a+b>=c and b+c>=a and a+c>=b):
        return True
    else:
        return False
