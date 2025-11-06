def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number>0:
        fact=[]
        for i in range(1,number):
            y=number%i
            if y==0:
                fact.append(i)
    
        total_sum=sum(fact)
        if total_sum==number:
            type="perfect"
        elif number<total_sum:
            type="abundant"
        elif number>total_sum:
            type="deficient"
        return type
    else:
        raise ValueError("Classification is only possible for positive integers.")
    
        
        
