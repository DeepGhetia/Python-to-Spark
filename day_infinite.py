lt = [1,2,3,4,5,6]
print([(lt[i],lt[j],lt[k]) for i in range(len(lt)) for j in range(i+1,len(lt)) for k in range(j+1,len(lt))])
print([lt[i:i+2] for i in range(0,len(lt),2)])
for i,v in enumerate(lt,start=0):
    print(i,v)

