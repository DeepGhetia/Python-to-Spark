##### very imp#######
d1 = {'k1': {'a': 1, 'b': 2}, 'k2': 100, 'k4':[7,8]}
d2 = {'k1': {'b': 3, 'c': 4}, 'k3': 200, 'k4':[1,2]}
dic = {}

for i,j in d1.items():
    if i not in d2:
        dic[i] = [j]
    else:
        if isinstance(j,(int,str,tuple,float)):
            dic[i] = [j,d2[i]]
        elif isinstance(j,list):
            dic[i] = j + d2[i]
        else:
            temp = {}
            for home in [j,d2[i]]:
                for deep, ghetia in home.items():
                    if deep not in temp:
                        temp[deep] = ghetia
                    else:
                        temp[deep] = [temp[deep],ghetia]
            dic[i] = temp

for i,j in d2.items():
    if i not in d1:
        dic[i] = [j]

print(dic)

# data = {
#     "student1": ["CS101", "MATH"],
#     "student2": ["BIO", "CS101"],
#     "student3": ["ENG", "CS101"]
# }

# # ❓Question: Find the course that has the most students enrolled.
# # If there's a tie, return all such courses in a list.
# lt = list(set([j for i in data.values() for j in i]))
# lt1 = []
# dic = {}
# for i,j in data.items():
#     for k in j:
#         lt1.append((i,k))

# for i,j in lt1:
#     if j in lt and j not in dic.keys():
#         dic[j] = [i]
#     else:
#         dic[j] = dic[j] + [i]

# max_val = max(len(j) for i,j in dic.items())

# print([i for i,j in dic.items() if len(j) == max_val])

##############
data = {
    "student1": ["CS101", "MATH"],
    "student2": ["BIO", "CS101"],
    "student3": ["ENG"]
}

# ❓Question: Return a list of students who are enrolled in "CS101".
lt = list(set([j for i in data.values() for j in i]))
lt1 = []
dic = {}
for i,j in data.items():
    for k in j:
        lt1.append((i,k))

for i,j in lt1:
    if j in lt and j not in dic.keys():
        dic[j] = [i]
    else:
        dic[j] = dic[j] + [i]

print(list(j for i,j in dic.items() if i == 'CS101')[0])

#######
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for index,(j,k) in enumerate(list(dict_num.items()), start=1):
    print(j,k,index)

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for (i,j),k in zip(list(dict_num.items()),[i+1 for i in range(len(list(dict_num.items())))]):
    print(i,j,k)

#when you write abve codes it gives you conidence.
#also below codes
dic = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

lt = []
for i,j in dic.items():
    temp = []
    for a in j:
        temp.append((i,a))
    lt.append(temp)

final = []

for i,j in zip(lt[0],lt[1]):
    dic = {}
    dic[i[0]] = i[1]
    dic[j[0]] = j[1]
    final.append(dic)
print(final)


#######
d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
d2 = {'x': 300, 'y': 'Red', 'z': 600}

dic = {}

for i,j in d1.items():
    if i not in d2:
        dic[i] = [j]
    else:
        dic[i] = [j] + [b for a,b in d2.items() if i == a]

for i,j in d2.items():
    if i not in d1:
        dic[i] = [j]

print(dic)


##########
dic = {
    'Carla ': {
        'name': {
            'first': 'Carla ',
            'last': 'Russell'
        },
        'postIds': [1, 2, 3, 4, 5]
    }
}

lt = ['Carla ', 'postIds', 1]

val = dic['Carla ']
print(val)
for i in range(1,len(lt)):
    val = val[lt[i]]
    print(val)
print(val)

###
users = {
    'Theodore': {'user': 'Theodore', 'age': 45},
    'Roxanne': {'user': 'Roxanne', 'age': 15},
    'Mathew': {'user': 'Mathew', 'age': 21},
}

val = 'user'

dic = {}
for i,j in users.items():
    dic[i] = j[val]
print(dic)

#######3
student_data = {
    "Alice": {
        "grades": {
            "math": 85,
            "science": 90
        },
        "attendance": {
            "Jan": 20,
            "Feb": 18
        }
    },
    "Bob": {
        "grades": {
            "math": 78,
            "science": 88
        },
        "attendance": {
            "Jan": 22,
            "Feb": 20
        }
    }
}

path = ["Bob", "attendance", "Feb"]

if path[0] == 'Alice':
    val = student_data['Alice']
else:
    val= student_data['Bob']

for i in range(1,len(path)):
    val = val[path[i]]
print(val)

#########
d1 = {'a': [1, 2], 'b': {'x': 10, 'y': 20}, 'c': 100}
d2 = {'a': [3, 4], 'b': {'y': 30, 'z': 40}, 'd': 200}

dic = dict(d1)

for i,j in dic.items():
    if i not in d2:
        dic[i] = [j]
    else:
        if isinstance(j,(int,float,str,list,tuple)):
            dic[i] = dic[i] + d2[i]
        else:
            temp = {}
            for d in [dic[i], d2[i]]:
                for a,b in d.items():
                    if a not in temp:
                        temp[a] = b
                    else:
                        temp[a] = [temp[a], b]
            dic[i] = temp

for i,j in d2.items():
    if i not in dic:
        dic[i] = [j]

print(dic)