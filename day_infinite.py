from functools import reduce
lt = [1,2,3,4,5]

print(list(map(lambda x: x%2==0,lt))) #transformation
print(list(filter(lambda x: x%2==0,lt))) #filtering (select/project)
print(reduce(lambda x,y:x*y,lt)) #aggregation