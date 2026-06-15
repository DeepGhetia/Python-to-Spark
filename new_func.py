import functools 
def filtered(lt)->int:
    return functools.reduce(lambda x,y: x+y,lt)
