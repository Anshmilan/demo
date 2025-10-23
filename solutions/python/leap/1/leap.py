def leap_year(year):
    leap=year%4
    leap1=year%400
    leap2=year%100
    if leap==0:
        if leap2 !=0 or leap1 ==0:
            x = True
        else:
            x = False
    else:
        x = False
    return x