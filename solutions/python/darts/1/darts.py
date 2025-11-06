def score(x, y):
    if (0<=x<=1 or -1<=x<=0 ) and (0<=y<=1 or -1<=y<=0) and x**2+y**2<=1:
        score=10
    elif (0<=x<=1 or -1<=x<=0 ) and (0<=y<=1 or -1<=y<=0) and x**2+y**2>1:
        score=5
    elif (1<=x<=5 or -5<=x<=1 or x==0) and (1<=y<=5 or -5<=y<=1) and x**2+y**2<=5**2:
       score=5
    elif (1<=x<=5 or -5<=x<=1 or x==0) and (1<=y<=5 or -5<=y<=1) and x**2+y**2>5**2:
       score=1
    elif (5<=x<=10 or -10<=x<=-5 or x==0) and (5<=y<=10 or -10<=y<=-5 ) and x**2+y**2<=10**2:
       score=1
    else:
        score=0
    
    
    return score
