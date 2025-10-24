def steps(number):
    count=0
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number>1:
            if number%2==0:
                number=number/2
                count=count+1
            else:
                number=(number*3)+1
                count=count+1
    return count
    
        
     