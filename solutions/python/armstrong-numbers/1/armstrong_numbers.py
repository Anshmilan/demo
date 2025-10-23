def is_armstrong_number(number):
    list_num=list(str(number))
    length=len(list_num)
    sum_num=0
    for num in list_num:
        sum_num=sum_num+(int(num))**length
    if sum_num==number:
        return True
    else:
        return False
        
        
