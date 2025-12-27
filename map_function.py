#think logically pleae incase of list, tup, dic, set

#true / false is everything in python/pandas/spark
#only == and != can work for string
#using multiple for loops is the key remeber that
#'deep'*2 = 'deepdeep' similarly lt = [2], lt*2, [2,2]
#whenever you use range() in for always rmeeber upper range or just a sngle num in range is always equal to no of iterations
# more important null in python means None singleton object
# be it any method/func comp will yield true/false and rest will yield value (comaprison ops gona yield you true/flase with even writing if else block)

#return statement and comparison operator compliment each other.
# def func->int: #good way to use func

# ** is represented as power
#abs method is also cu=rucial.
#sorting cannot take place for int and str together at once *** //homogenous ele only
#also avoid sorting noumbers in string format****

#one of the good observation is 
# 1. type(val) == int
# 2. isinstance(val, int)
# might not be same as bool is a sub type of int hence becoming true if you want to follow strict ness always go for type(val).

########
# good example for lambda
# # syntax
# lambda is one liner no () braces = lambda = sedha
# x = lambda param1, param2, param3: param1 + param2 + param2
# lambda arguments: value_if_true if condition else value_if_false
# print(x(arg1, arg2, arg3)) // the main job of lambda is to evaluate the expression and output the result based on th exp

######
# in func always remeber if not return type func returns none also if just return statement it also returns None
# and pass has nothing to do with func can be used without func use case of pass - just a place holder doing nothing.

# **************@always note any vaue will be active strictly inside the loop only
#always note if using 2 lt or dict or tup simultanously each value then go for for i,j in zip(lt,lt1)
# or if requirement is first ele and multiple values in second list then go for for for multiple for's'

####
# always remeber uneven lists or tuples in zip method will output equal values and other extra values will be ignored.

# In Python:

# True is treated as the integer 1

# False is treated as the integer 0

#bool and int are bro's

s='3'
if 3 == s:
    print(True)
else:
    print(False)

# Operator | Use it when you want to...
# == | Check if values or contents are equal
# is | Check if two variables reference the same object

#always keep in mind for any question regarding repettion always go for dictionary logic where in get the value as count
# #big thing to note is while using if == or in note in works only for iterable not on integers so if you have
# condition int equating to int then alsways go for int == int not int in int that is for string in string

#when using in always note somethin should be iterable 
# This is fine: list is iterable
2 in [1, 2, 3]  # True

# This is fine: string is iterable
'a' in "apple"  # True

# This is fine: dict is iterable (over keys)
'b' in {'a': 1, 'b': 2}  # True

# This will raise a TypeError: int is not iterable
3 in 5  # ❌ TypeError

# i was saying this - 
# Summary
# Data Type	in Works?	Example   #always note type should be same iside int = int not string
# String	✅ Yes	"a" in "apple" → True
# List	✅ Yes	2 in [1, 2, 3] → True
# Tuple	✅ Yes	5 in (1, 2, 3) → False
# Set	✅ Yes	10 in {10, 20, 30} → True
# Dictionary (keys)	✅ Yes	"Alice" in {"Alice": 'a'} → True
# Dictionary (values)	✅ Yes	'a' in {"Alice": 'a'}.values() → True
# Integer	❌ No	2 in 12345 → TypeError

# map metod takes 2 input 1st is func can be int str or even lambda secnond is iterable
# always note while using dic in for loop left hand data before = always menas key and right hand data after = always means values
#always keep note that for swapping alays go or a,b = b,a

lt = [1,2,3,4,5]
# deep = map(lambda a:a+1, lt)
# print(list(deep))s
# also note len doesnt work for float and int
#always note in for loop string, list etc etc is iterable and int is not so always
# try to convert int to str and ten iterate using for loop pleae note this

# ✅ Quick Trick for Any Code
# 🔹 Read inside-out: Start with the deepest function (inside () first).
# 🔹 Read left to right for functions on the same level.
# 🎯 Key Takeaways for Execution Order
# Innermost function runs first (inside-out execution).
# String modifications (upper(), replace(), split()) happen before joining.

#remeber when you have join split and multiple other functions then always read from s. function calling
#remeber strip method only strips at starting and ending if you want in between then use replace menthod.
# deep = map(str,lt)
# print(", ".join(deep))

# small in big 
# split() and slit(' ') where 1st is prpersplit 2nd is split first space and other spaces are included
# join can take anything not only list 
# imp keep note of all the string func they are usefull to core

lt = [1,2,3,4,5]
print(', '.join(map(str,lt)))

print(' '.join(str(lt))) # this is wrong u cannot apply any function or conversion in join method on a list

print(', '.join(str(i) for i in range(1,6)))

# What is the output of split()?
# The split() method always returns a list of strings.

# It takes a string and splits it into a list, using a specified separator (default is whitespace).

# What is the Output of join()?
# ✅ The join() method always returns a string by joining elements of an iterable (like a list or tuple) with a specified separator.

# leap year logic 4 se ya 400 se but 4 se ho raha hai toh 100 se nahi
#always remeber the flow please
#evertime it is not necessary to use i from for loop example case is count the no of integer in a number
#u cannot iterate the integer only string is possible - remeber it
#u cannot use lt[i] while appneding values to list if there is no indexing with other value in the sme 
# list - always go for append method while doing this or ad the dummy vlues before hand.

#sting functions
# a.isalpha(), isnumeric()
#anything in delete string always go for replace.

# Yes, exactly! 🔥
# .zfill(length of string) pads zeros on the left side of a string until it reaches the length you specify.

#strip(), splitlines(), find(), index(), for in, split(), join(), upper(), lower(), replace(',',' '), s.startswiht('c'), rfind, find, isdigit()
# isalpha, rindex, rfind, endswith('b'), isupper(), islower(), isalnum(), title() -> capitalize the words i.e. "Deep", count()
#always keep substring logic handy
#break, pass, True, False

#always note there is diff b/w s.strip() and s.strip(' ')

####
# Use the rstrip() method to remove trailing whitespace characters, including the newline character.
# Then, print the modified 'str1' with trailing whitespace removed.
# print(str1.rstrip()) 

#works only with int
# x = 123456789
# print(f"{x:,}")

# y = -0.25
# print(f"{x*100:.2f}%")

#iterable items in pytohn are string, list etc etc
# ✅ Common Iterable Types in Python
# Iterable Type	Example
# Strings	"hello" → ['h', 'e', 'l', 'l', 'o']
# Lists	[1, 2, 3, 4]
# Tuples	(10, 20, 30)
# Dictionaries	{"a": 1, "b": 2} (Keys are iterable)
# Sets	{1, 2, 3}
# Range Objects	range(5) → [0, 1, 2, 3, 4]
# Files	open('file.txt') (Iterates line by line)

# ✅ Examples of Non-Iterable Objects
# Non-Iterable Type	Example
# Integers (int)	num = 10
# Floats (float)	pi = 3.14
# Booleans (bool)	flag = True
# Complex Numbers (complex)	z = 2 + 3j
# NoneType (None)	value = None

#always not max and min func can take individual arguemants sch as max(a,b) but other
# thn max and min for sum, mean, med we have to pass iterable items only

#passing singl column - to below
# sum()	List, Tuple, Set	sum([1, 2, 3]) → 6
# min()	List, Tuple, Multiple Numbers	min(4, 2, 8) → 2
# max()	List, Tuple, Multiple Numbers	max(4, 2, 8) → 8
# avg (manual)	List, Tuple	sum(nums) / len(nums)
# mean()	List, Tuple	statistics.mean([3, 6, 9]) → 6.0
# median()	List, Tuple	statistics.median([3, 5, 7]) → 5

# Key Differences:
# Feature	sort()	sorted()
# Modifies Original List?	✅ Yes	❌ No
# Returns a New List?	❌ No (Returns None)	✅ Yes
# Works on Other Iterables?	❌ No (Lists only)	✅ Yes (Lists, tuples, strings, etc.)
# Performance	Faster (In-place sorting)	Slightly slower (Creates a new list)

# sort() for list is to be used in single line also we can add reverse=True
# sorted for list can be used in single line while printing or has to be assigned to a new list also we can add reverse = true

# reverse()
# we can reverse a list just like sort again in single line.
# reversed()
# reversed method for it returns a itrator which then has to be converted to list again

#note for string sort and reverse() method does not work only 
# because string is immutable same string can not be changed just like tuple

# sorted(string) - when you use srted method it returns list hnce needs to be joined
# reversed(string) - same to what sorted does to string

#if wan to remove duplicates always go for set method simple

#unpacking the tup when u use * u get a list
# we can dicrectly pass tup in join mehod in string

# list comprehension - logic
# only if 
# lt = [a for a in b if a > 0]
# if and else both
# lt = [a if a > 0 else 'haha' for a in b]

#note to use break statements logically whenever needed
# u cannot directly pass a tuple in a dict - u need to add the tup in a list frst and then to dic

#set union intersection issubset

# #FOR DATTIME 
# Y-2024
# y-24
# m-01
# b-Jan
# B-JANUARY
# H,M,S(24 format)
# I,M,S(12 format)
# p (AM/PM)
#A (weekday name)
#u (weekday no)
##### anyting to add in dates use timedelta or relative delta
#### also note today().day, month, year
# timedelta, relativedelta - days
# normal datetime - day, month, year, weekday
# normal days ka diff directly hojata hai but in days and sec as output is in timedelta
# we can also use relativedelta(d1,d2).days or months or years to get datefdeiff
# and to add dates always go for timedelta and reltivedelta
# we can also create date and datetime using date(y,m,d) and datetime(y,m,d,h,m,s) this is similar to make_date() and make_timestamp() in spark

# zip method outputs tuples
# whenevr yu se nested things always go for for for in comprehension

# #dict
# dic.key() - list of keys in dictionary aslo under list()

# tuples inside list can be converted to dict 
# in smilar wy list(dic.items()) - gives list of tuples

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# lt=[]
# for i,j in myfamily.items():
#     print(myfamily[i]['name'])

# dic = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}
# lt1 = list(dic.items())
# lt1 = sorted(lt1,key=lambda x:x[1], reverse=True)
# print(dict(lt1))

lt = [1, 2, 3, 4, 5]
lt1 = [6, 7, 8, 9, 0]

# # Dictionary comprehension to merge lists
# merged_dict = {k: v for k, v in zip(lt, lt1)}

# # print(merged_dict)
# dic = {'1':1}
# dic1 = {'2':2}
# print(dic1 | dic)
# dic = {'apple': '5', 'banana': '2', 'cherry': '8', 'date': '3'}
# dic1 = {j:i for i,j in dic.items()}
# print(dic1)


#things to note when converting list to dic and tup to idic is dic[lt] is necessary i.e wrappig up is necesary

# #the most imp ques - 
# Write a program to update the value of a key in a dictionary if it exists, otherwise add the key with a specified value.
# if key was there then it would have been updated with latest value if not key and value worould have been added

#this condtiion works right "n in range(2,6)" it gives true"

#when you try to pass or aooend a list in ist or tuple in list always not use list() or tuple() just go for [] or ()

#best example to sort multiple times
# lt = sorted(lt,key=lambda x:(x[1],x[0]))

    # number = avg[0]  - code to get the list to integer type
    # print(f'{number:.2f}') - flaoting point 2 digit fixed 

# in a function pass has to be written as only pass return is not mandatory remember this.

# #avg 
# sum(lt)//len(lt)
#sometimes try to use map and lambda they are deadly duo
#yaad rakho hamesha aakh khula rakhkar sochna aur dekhna chahiye - ex - a list of dictionaries and returns a list of the values for a specified key.
#greatest common divisor (GCD) - divisiblitiy ceck of both number and then go for common and then go for highest no.


#point to not is one on one iterators dont work so for any function we need to pass complete iterator say map fun

# one thing to not in set is during update method it updates existig main set
#big breakthrough sorted and reversed also works for dic

#dic by default means dic.keys 
#enum
# dic = {
#     "apple": 5,
#     "banana": 3,
#     "cherry": 8,
#     "date": 2,
#     "elderberry": 10
# }

# for index, (key, value) in enumerate(dic.items(), start=1):
#     print(f"{index}. {key}: {value}")

# s = 'deep, ghetia is good to watch-out, for is this  right   or wrong'
# print('#'.join(s.replace(',','').split(' ')))
# print('#'.join([i.strip(',') for i in s.split()]))

# @keep this problem in mind 
# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 15, 'c': 25, 'd': 40}

# def merge_dicts(dict1, dict2):
#     for i,j in dict2.items():
#         if i not in dict1.keys():
#             dict1[i] = j
#         else:
#             dict1[i] = dict1[i] + dict2[i]
#     return dict1
# print(merge_dicts(dict1, dict2))

############
# the most imp question of Python
# lt = ["banana", "apple", "cherry", "date"]  # List with four words

# sorted_lt = sorted(lt)  # Sort the list alphabetically

# # Modify each word directly in the list
# for i in range(len(sorted_lt)):
#     sorted_lt[i] = sorted_lt[i][0].upper() + sorted_lt[i][1:-1] + sorted_lt[i][-1].upper()

# print(sorted_lt)

############
# one of the greatest logic
# s = "python exercises practice solution"
# s = s.replace(' ',', ')
# s1 = ''
# for i in s.split():
#     for j in range(len(i)):
#         if j%2==0:
#             s1+=i[j].upper()
#         else:
#             s1+=i[j]
# print(s1.replace(',',' '))

# | Type    | Ordered | Indexed | Mutable(add/remove) | Allows Duplicates | Key-Based Access |
# | ------- | ------- | ------- | ------- | ----------------- | ---------------- |
# | `list`  | ✅ Yes   | ✅ Yes   | ✅ Yes   | ✅ Yes             | ❌ No             |
# | `tuple` | ✅ Yes   | ✅ Yes   | ❌ No    | ✅ Yes             | ❌ No             |
# | `set`   | ❌ No    | ❌ No    | ✅ Yes   | ❌ No              | ❌ No             |
# | `dict`  | ✅ Yes\* | ✅ Yes\* | ✅ Yes   | ❌ (Keys unique)   | ✅ Yes (by key)   |


##########
# map vs filter - 
# lt = [1,2,3,4,5]
# print(tuple(filter(lambda x: x%2==0,lt)))
# print(tuple(map(lambda x: x%2,lt)))

# file handling - 
# A, W, R(BY DEFAULT), X(CREATE), t, b

# | Purpose                              | Function to Use              | What It Does                                           | Example Idea                     |
# | ------------------------------------ | ---------------------------- | ------------------------------------------------------ | -------------------------------- |
# | **Transform each item**    (transform)         | `map(function, iterable)`    | Applies a function to every item, returns new iterable | Convert all strings to uppercase |
# | **Select items by condition**    (select)    | `filter(function, iterable)` | Keeps only items where function(item) is True          | Keep only even numbers           |
# | **Combine all items into one value**   (group)  | `reduce(function, iterable)` | Repeatedly combines items to produce one result        | Sum all numbers, find max        |

#questions like 2341 from LC are good one's to solve also LC 2697 two pointer q
#remember that to find the max number use sorted max or if neg numbers pleae use first neg and last max