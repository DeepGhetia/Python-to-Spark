lt = [(1,'a'),(3,'c'),(2,'d'),(5,'a')]
print(sorted(lt,key = lambda x: (x[1],-x[0])))