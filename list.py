#note down that list in w3resources from 50-80 for now are eye opening questions

########
s = 'The quick brown fox.'
val = 10
for i in [s[i:i+val] for i in range(0,len(s),val)]:
    print(i)

#simple que but effective
lt = [1, 2, 3, 4]

final = []
total = 0
for i in lt:
    total+=i
    final.append(total)
print(final)

#flattern the lst recursion - 
lt = [1, [2], [[3], [4], 5], 6]

def func(lt):
    result = []
    for i in lt:
        if isinstance(i,list):
            result.extend(func(i))
        else:
            result.append(i)
    return result

print(func(lt))

# 1. getting the scond key not from what we want
lt1 = [4.1]
lt2 = [2.3, 4.3]

from math import floor
temp = {i:floor(i) for i in lt1}
temp1 =  {i:floor(i) for i in lt2}

print(temp, temp1)

final = []
for i,j in temp1.items():
    if j in temp.values():
        val = [a for a,b in temp.items() if j == b]
        final.append(val)
print([j for i in final for j in i])

# 2.

lt = [[1], [2, 4, 4], [1, 2], [4]]

max_val = max([len(i) for i in lt])

final = []
for i in lt:
    if len(i) == max_val:
        final.append(i)
    else:
        final.append(i + [0 for _ in range(max_val - len(i))])

print([sum(i) for i in zip(*final)])


my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
for i in my_list:
    print(i['key']['subkey']) # this is right because we are accessing dict inside list

#always open your eyes and visualize


#two common things in list and tup is index() and count()
# lt = [1,2,3,4,5,-1]
# print(sorted(lt,key =lambda x:-x)[0])

#######
# pythonic ay to check if lis tis empty
# lt = []
# if not lt:
#     print('list is empty')

############
# copy a list 
# lt = [10, 22, 44, 23, 4]
# lt1 = list(lt)
# print(lt1)

###########below is unique que find uncommen b/w 2 list
# list1 = [1, 3, 5, 7, 9]

# # Define another list 'list2' containing different numbers
# list2 = [1, 2, 4, 6, 7, 8]

# a = list(set(list1).difference(set(list2)))
# b = list(set(list2).difference(set(list1)))
# print(a+b)

######
# always note issubset will always give true or flase only 
# ex:
# def func(lt,b):
#     return set(b).issubset(set(lt))
# print(func(lt,b))

#########
lt = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']
dic = {}
for i in sorted(lt):
    val = i[0]
    if val not in dic.keys():
        dic[val] = [i]
    else:
        dic[val] = dic[val] + [i]
print(dic)


###########
n = 20
dic = {}
for i in range(1,n+1):
        dic[i] = []
print(dic)

##########nested dict
lt = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print(sorted(lt, key=lambda x: -x['key']['subkey']))

##########
lt = [1, 1, 1, 0, 0, 0, 2, -2, -2]
print(sorted(list(set(lt)),key=lambda x:-x[0])[1])

#below is the example of using brian \
# lt= ['p', 'q']
# n = 4
# final = sorted([(i,str(j)) for i in lt for j in range(1,n+1)],key=lambda x:x[1])
# print([i+j for i,j in final])            - not a right way to Code 

# lt= ['p', 'q']
# n = 4
# print([j+str(i) for i in range(1,n+1) for j in lt])   - good way to code always visualize the code and output

##########
color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

color_name = [('color_name',i) for i in color_name]
color_code = [('color_code',i) for i in color_code]
lt = list(zip(color_name,color_code))
final = []
for i, j in lt:
    dic = {}
    dic[i[0]] = i[1]
    dic[j[0]] = j[1]
    final.append(dic)
print(final)

##########3
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print(sorted(my_list, key=lambda x: -x['key']['subkey']))

###########
lt = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]
print([{j:k for j,k in i.items() if j != 'key1'} for i in lt])

#########3
color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

lt = [{'color_name':i} for i in color_name]
lt1 = [{'color_code':i} for i in color_code]
final = []
good = list(zip(lt,lt1))

for i,j in good:
    dic = {}
    dic['color_name'] = i['color_name']
    dic['color_code'] = j['color_code']
    final.append(dic)
print(final)

##########
num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(max(num,key=sum))

###########
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
lt = []
for i in num:
    if i not in lt:
        lt.append(i)
print(lt)

#######3
lt = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 3, 4]
final = [0]
for i in range(len(lt)):
    start = lt[i]
    if i == len(lt)-1:
        end = lt[i]
    else:
        end = lt[i+1]
    if end != start:
        final.append(end)
print(final)

#######3
lt  = [[2], [0], [1, 3], [0, 7], [13, 15, 17], [9, 11]]
print(sorted(sorted(lt), key=lambda x:len(x)))

#########
lt = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
start = 13
end = 17
print([i for i in lt if all(start<=j<=end for j in i)])

#######3
# one of the good questions - consecutive list ke liye ye he logic hai important
lt = [0, 1, 2, 3, 4, 5, 6]
final = []
if len(lt)%2 == 0:
    for i in range(0, len(lt), 2):
        start = lt[i]
        end = lt[i+1]
        final.append(end)
        final.append(start)
else:
    for i in range(0, len(lt)-1, 2):
        start = lt[i]
        end = lt[i+1]
        final.append(end)
        final.append(start)
    final.append(lt[-1])
print(final)
########## - very imp from here
lt =  ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
c = ['#', 'color', '@']
final = []
for i in lt:
    s=i
    for j in c:
        s = s.replace(j,'').strip()
    final.append(s)
print(final) #this is very imp question reassigning is very imp note that 

#########
lt = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
final = []
n = 3
for i in lt:
    temp = []
    for j in range(len(i)):
        if j!=n-1:
            temp.append(i[j])
    final.append(temp)
print(final)

#########
lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
lt1 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
final = []
for i in lt1:
    temp = []
    for j in i:
        if j in lt:
            temp.append(j)
    final.append(temp)
print(final)

########
lt = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
temp = lt[0]
for i in range(len(lt)-1):
    temp = set(temp).intersection(set(lt[i+1]))
    temp = list(temp)
print(temp)

#good confidence code
lt = [2, 4, 7, 0, 5, 8]
lt1 = [2, 5, 8]
lt2 = [0, 1]
lt3 = [3, 3, -1, 7]

ele = max(len(lt),len(lt1),len(lt2),len(lt3))

def pad(lt, ele):
    if len(lt) == ele:
        return list(lt)
    else:
        return lt + [[] for _ in range(0,ele - len(lt))]
    
f1 = pad(lt,ele)
f2 = pad(lt1,ele)
f3 = pad(lt2,ele)
f4 = pad(lt3,ele)

print([i for i in [j for i in zip(f1,f2,f3,f4) for j in i] if isinstance(i,int)])

#####33
lt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
size = 4
val = 'b'
final = []
for i in range(0,len(lt),size):
    final.append(lt[i:i+size])
    if i+size<len(lt):
        final.append([val])

print([j for i in final for j in i])


#########
lt = [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]

final = []
for i in lt:
    s = ''
    for j in i:
        s+=f"{j} "
    final.append(s.strip())
print(final)

#
print([' '.join(i) for i in lt])

#######
lt = [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
print([len(lt)], [max(len(row) for row in lt)])

#2
print([len(lt)], [len(lt[0])])

#######
lt = [[1], [2, 4, 4], [1, 2], [4]]

final = []

max_val = max([len(i) for i in lt])
for i in lt:
    if len(i) == max_val:
        final.append(i)
    else:
        final.append(i + [0 for _ in range(max_val - len(i))])

print([sum(i) for i in zip(*final)])

######
lt = ['red', 'green', 'white', 'black']

for i in range(len(lt)-1, -1, -1):
    print(lt[i])

for i in reversed(lt):
    print(i)

for i,v in reversed(list(enumerate(lt))):
    print(i,v)