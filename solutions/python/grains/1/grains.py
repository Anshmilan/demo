def square(number):
    if 0<number <=64:
        return 2**(number-1)
    else:
       raise ValueError("square must be between 1 and 64") 


def total():
    total_fin=0
    for index in range(64):
        index1=index+1
        total=square(index1)
        total_fin=total_fin+total
    return total_fin
