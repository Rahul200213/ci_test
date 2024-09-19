def area(length:int|float)->int|float:
    """ 
    fucntion to calculate araer of the square """
    if not isinstance(length,(int,float)) or length <=0:
        raise TypeError("Length must be a postive ")
    
    return length * length
