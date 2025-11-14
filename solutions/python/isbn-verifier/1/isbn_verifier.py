def is_valid(isbn):
    isbn_new=isbn.replace("-","")
    isbn_list=list(isbn_new)
    count=10
    sum=0
    if len(isbn_list)!=10:
        return False
        
    for i in isbn_list:
        if i=="X" and count==1:
            i=10
            value=i*count
        else:
            try:
                isinstance(int(i),int)
            except ValueError as e:
                return False
            value=int(i)*count
        sum=sum+value
        count=count-1
    valid=sum%11
    if valid==0:
        return True
    else:
        return False
            
            
    
