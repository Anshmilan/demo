def convert(number):
    div_3=number%3
    div_5=number%5
    div_7=number%7
    result=''
    if div_3==0:
        result=result+'Pling'
    if div_5==0:
        result=result+'Plang'
    if div_7==0:
        result=result+'Plong'
    if div_3!=0 and div_5!=0 and div_7!=0:
        return str(number)
    return result
            
            
        
