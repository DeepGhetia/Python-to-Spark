#this is very imp questions always gvies a good picture about the tough dict ques
dict1 = {
    'a': 1,
    'b': {'x': 10}
}
dict2 = {
    'b': {'y': 20},
    'c': 3
}

dic = {}

for i,j in dict1.items():
    if i not in dict2:
        dic[i] = j
    else:
        dic[i] = {key:val for a in [j,dict2[i]] for key,val in a.items()}

for i,j in dict2.items():
    if i not in dict1:
        dic[i] = j
    
print(dic)


###########
# data = {
#     "student1": ["CS101", "MATH"],
#     "student2": ["BIO", "CS101"],
#     "student3": ["ENG"]
# }

# # ❓Question: Create a new dictionary where each course is a key,
# # and the value is a list of students enrolled in it.
# lt = list(set([i for j in data.values() for i in j]))
# final = {}
# dic = []
# for i,j in data.items():
#     for k in j:
#         dic.append((i,k))
# print(dic)
# for i,j in dic:
#     if j in lt and j not in final.keys():
#         final[j] = [i]
#     else:
#         final[j] = final[j] + [i]     
# print(final)


# ###########
# You can use the sorted() function with a custom sorting key. Since you want to sort by number in descending order and then by alphabet in ascending order, you can use the following approach:

# python
# Copy
# Edit
# lt = [('b', 2), ('a', 3), ('c', 1), ('a', 2), ('b', 3)]

# sorted_lt = sorted(lt, key=lambda x: (-x[1], x[0]))

# print(sorted_lt)


data = {
    "apple": 1,
    "banana": 2,
    "cherry": 3,
    "date": 4
}

mapping = {
    1: 100,
    3: 300
}
def replace_values(data, mapping):
    for i,j in data.items():
        if j in mapping.keys():
            data[i] = mapping[j]
        else:
            data[i] = j
    return data
print(replace_values(data, mapping))


#################
words = ["listen", "silent", "enlist", "rat", "tar", "art", "evil", "vile", "live"]

def group_anagrams(s):
    lt = [''.join(sorted(i)) for i in s]
    dic = dict(zip(s,lt))
    res = {}
    for i,j in dic.items():
        first_key = i
        first_value = j
        if first_value not in res.keys():
            res[first_value] = [first_key]
        else:
            res[first_value] = res[first_value] + [first_key]
    return res
print(group_anagrams(words))

#################
data = {
    "apple": 10,
    "banana": 15,
    "cherry": 5,
    "date": 15,
    "elderberry": 8
}

def second_most_frequent_key(data):
    lt = sorted(set(data.values()),reverse=True)[1]
    print(lt)
    res = []
    for i,j in data.items():
        if j == lt:
            res.append(i)
    return res

print(second_most_frequent_key(data))

#####################
import statistics
scores = {
    "Alice": [85, 90, 88],
    "Bob": [70, 78, 82],
    "Charlie": [92, 95, 94]
}

def scoring(scores):
    lt = list(scores.keys())
    lt1 = list(map(statistics.mean,scores.values()))
    lt1 = [round(i,2) for i in lt1]
    return dict(zip(lt,lt1))
print(scoring(scores))

#################
students = {
    "Alice": {"Math": 85, "English": 90, "Science": 88},
    "Bob": {"Math": 70, "English": 78, "Science": 82},
    "Charlie": {"Math": 92, "English": 95, "Science": 94}
}
def average_scores(students):
    dic = {}
    for name, subjects in students.items():
        avg_score = round(sum(subjects.values()) / len(subjects), 2)
        dic[name] = avg_score
    return dic

##############
dic = {}
for i, j in data.items():
    lt = []  # Start with an empty list instead of [0]
    for k in j:
        if k % 2 == 0:
            lt.append(k)
    dic[i] = sum(lt)  # If no even numbers, sum([]) = 0 automatically
print(dic)

###############
data = {
    "Alice": [3, -8, 2, -10, 7],
    "Bob": [-7, -1, -9, -5],
    "Charlie": [4, 6, -8, 2, -3],
    "David": [-11, 13, -15, 7]
}
dic = {}
for i,j in data.items():
    lt = []
    for k in j:
        if k>0:
            lt.append(k)
    if len(lt) == 0:
        lt.append(0)
    dic[i] = lt
print(dic)
        
#################
dict1 = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88
}

dict2 = {
    "Alice": 90,
    "Bob": 82,
    "Charlie": 87,
    "Eve": 95
}
dic = {}
for i,j in dict1.items():
        if i in dict2:
            dic[i] = max(j,dict2[i])
print(dic)

###############
dict1 = {
    "apple": 5,
    "banana": 8,
    "orange": 3
}

dict2 = {
    "banana": 4,
    "grape": 6,
    "orange": 2
}
dic = {}
for i,j in dict1.items():
    if i in dict2.keys():
        dic[i] = j + dict2[i]
    else:
        dic[i] = j
for i,j in dict2.items():
    if i not in dict1.keys():
        dic[i] = j
print(dic)

##############
dict1 = {"A": [1, 2, 3], "B": [4, 5], "C": [6, 7, 8]}
dict2 = {"A": [1, 2, 4], "B": [4, 5], "C": [6, 7, 9]}

dic = {}
for i,j in dict1.items():
    if i in dict2.keys():
        dic[i] = (sum(j),) + (sum(dict2[i]),)
print({i:j for i,j in list(dic.items()) if j[0] != j[1]})

# 4. Merge Two Dictionaries But Keep Only the Last 3 Values in Lists for Common Keys
# 📌 Task:

# Given two dictionaries where values are lists, merge them.

# If a key exists in both, store only the last 3 values in the final list.

# Example Input:
# python
# Copy
# Edit
# dict1 = {"A": [1, 2, 3], "B": [4, 5], "C": [6, 7, 8]}
# dict2 = {"A": [4, 5, 6, 7], "B": [8, 9, 10], "D": [11, 12]}
# Expected Output:
# python
# Copy
# Edit
# {
#     "A": [5, 6, 7],  # Merge [1,2,3] + [4,5,6,7] → Keep last 3
#     "B": [5, 8, 9],  # Merge [4,5] + [8,9,10] → Keep last 3
#     "C": [6, 7, 8],  # Only in dict1, keep as is
#     "D": [11, 12]    # Only in dict2, keep as is
# }
# this is th most imp question above it teaches you to openyour eyes ans solve any questiion


#111111
# 1.1. Merge Two Dictionaries and Keep Only the First 3 Unique Values in Lists
# 📌 Task:
# You have two dictionaries where values are lists. Merge them so that:

# If a key exists in both, merge the lists and keep only the first 3 unique values (in order).

# If a key exists in only one dictionary, keep it unchanged.

# Example Input:
# python
# Copy
# Edit
# dict1 = {"A": [1, 2, 3], "B": [4, 5], "C": [6, 7, 8]}
# dict2 = {"A": [3, 4, 5, 6], "B": [5, 6, 7], "D": [9, 10]}
# Expected Output:
# python
# Copy
# Edit
# {
#     "A": [1, 2, 3],  # Merge [1,2,3] + [3,4,5,6] → Keep first 3 unique
#     "B": [4, 5, 6],  # Merge [4,5] + [5,6,7] → Keep first 3 unique
#     "C": [6, 7, 8],  # Only in dict1, keep as is
#     "D": [9, 10]  # Only in dict2, keep as is
#
# dic = {}

# for i,j in dict1.items():
#     if i not in dict2.keys():
#         dic[i] = j
#     else:
#         dic[i] = j+dict2[i]

# for i,j in dict2.items():
#     if i not in dict1.keys():
#         dic[i] = j

# for i, j in dic.items():
#     lt = []
#     if len(j) > 3:
#         for a in j:
#             if a not in lt:
#                 lt.append(a)
#         dic[i] = lt[:3]
#     else:
#         dic[i] = j
        
# print(dic)
# 
#  }

#######2
# 2. Find Keys Where Sum of List Values is Prime
# 📌 Task:

# Given a dictionary where values are lists of numbers, return a new dictionary with only the keys where the sum of the list is a prime number.

# Example Input:
# python
# Copy
# Edit
# data = {"X": [2, 3], "Y": [4, 6], "Z": [5, 5, 5]}
# Expected Output:
# python
# Copy
# Edit
# {
#     "X": [2, 3],  # Sum = 5 (prime)
#     "Z": [5, 5, 5]  # Sum = 15 (not prime, so ignored)
# }
# (Note: Only "X" is included because 5 is prime.)


############3
dict1 = {'listen': 3, 'silent': 2, 'enlist': 5}  
dict2 = {'tinsel': 4, 'banana': 6, 'letsin': 1}

lt = [(i,''.join(sorted(i))) for i,j in dict1.items()]
lt1 = [(i,''.join(sorted(i))) for i,j in dict2.items()]
print(lt,lt1)
final = [(lt[i][0], lt1[j][0]) for i in range(len(lt)) for j in range(len(lt1)) if lt[i][1] == lt1[j][1]]
# print(final)


# #############
# 1️⃣ Reverse Map Merging with Frequency Count
# Given two dictionaries with different values but overlapping keys, create a dictionary where the values become keys and the keys become values in a list.

# Example:
# python
# Copy
# Edit
# dict1 = {'a': 10, 'b': 20, 'c': 10}  
# dict2 = {'b': 20, 'c': 30, 'd': 40}
# 🔹 Expected Output:

# python
# Copy
# Edit
# {10: ['a', 'c'], 20: ['b'], 30: ['c'], 40: ['d']}
# 📌 Twist: The same value should map to a list of all corresponding keys.

###########
words = ['apple', 'bat', 'banana', 'cherry', 'grape', 'kiwi']
le = sorted(set([len(i) for i in words]))
print(le)
dic = {}

for i in words:
    for j in le:
        if len(i) == j:
            if j not in dic.keys():
               dic[j] = []
            dic[j] = dic[j] + [i]
print(dic)

##########
dict1 = {'a': [1, 2], 'b': [3, 4, 5], 'c': [6, 7, 8, 9]}
dic = {}
for i,j in dict1.items():
    dic[i] = len(j)
print(dic)

val = sorted(dic.items(), key = lambda x:x[1], reverse=True)[0][0]

lt = []
for i,j in dict1.items():
    if i==val:
        lt.append(i)
        lt.append(j)

print(tuple(lt))

###########
# 8️⃣ Rotate Dictionary by Keys (Right Shift)
# You are given a dictionary and a number n. Your task is to rotate the dictionary's keys by n positions in a right shift, meaning each key will be moved n positions forward, and the keys that "fall off" the end should wrap around to the beginning.

# Example:
# python
# Copy
# Edit
# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# n = 2
# Expected Output:
# python
# Copy
# Edit
# {'c': 3, 'd': 4, 'a': 1, 'b': 2}


########## - string question
# Swap commas and dots in a string.

# Write a Python program to swap commas and dots in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"


##########3
s = "aabbcc"
dic = {}
for i in s:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] = dic[i] + 1
lt = list(dic.items())
lt = sorted(lt,key = lambda x: (x[1], x[0]))[0][0]
print(lt)

##############
dict1 = {
    "Anna": ["Apples", "Bananas"],
    "Brian": ["Grapes", "Oranges"]
}

dict2 = {
    "Anna": ["Apples", "Mangoes"],
    "Brian": ["Grapes", "Oranges"]
}

# Question: Find the keys with different list values between dict1 and dict2.
lt = []
for i,j in dict1.items():
    if i in dict2.keys():
        if j != dict2[i]:
            lt.append(i)
print(lt)

############
employee_projects = {
    "E001": ["Project A", "Project B"],
    "E002": ["Project C"],
}
employee_projects['E002'] = employee_projects['E002'] + ['Project D']
# Question: Add "Project D" to E002's list of projects.
print(employee_projects)


############
dict1 = {
    "user1": ["apple", "banana", "kiwi"],
    "user2": ["grape", "mango"],
    "user3": ["peach"]
}

dict2 = {
    "user1": ["banana", "orange"],
    "user2": ["mango", "cherry"],
    "user3": ["plum"]
}

# ❓Question: Create a list of keys where at least one item in the lists is common between dict1 and dict2.
lt = []
for i,j in dict1.items():
    if i in dict2.keys():
        for k in j:
            if k in dict2[i]:
                lt.append(i)
                break
print(lt)

##########
a = {
    "group1": ["a", "b"],
    "group2": ["c", "d"]
}

b = {
    "group2": ["d", "e"],
    "group3": ["f"]
}

# ❓Question: Find the total number of unique values across both dictionaries’ lists.
lt = [k for i,j  in a.items() for k in j]
lt1 = [k for i,j  in b.items() for k in j]
print(len(set(lt).union(set(lt1))))

###########
x = {
    "id1": ["A", "B"],
    "id2": ["C"]
}

y = {
    "id1": ["X", "Y"],
    "id3": ["Z"]
}

# ❓Question: For keys that exist in both `x` and `y`, swap their list values.
dic = {}
for i,j in x.items():
    if i in y.keys():
        x[i], y[i] = y[i], x[i]

final = {}
for i,j in x.items():
    if len(j) > 1:
        final[i] = j

final1 = {}
for i,j in y.items():
    if len(j) > 1:
        final1[i] = j
print(final, final1)


##############3
dict1 = {
    "k1": ["a", "b"],
    "k2": ["c"],
    "k3": ["x", "y"]
}

dict2 = {
    "k1": ["a", "b", "c"],
    "k2": ["c", "d"],
    "k3": ["y"]
}

# ❓Question: Print keys where all items in dict1[key] are also in dict2[key].
dic = {}
for i,j in dict1.items():
    if i in dict2.keys():
        dic[i] = list(set(j).difference(set(dict2[i])))

for i,j in dic.items():
    if len(j) == 0:
        print(i)