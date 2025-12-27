# # # Python: Remove leading zeros from an IP address
# # # Python: Find maximum length of consecutive 0’s in a given binary string
# # # Python: Find all the common characters in lexicographical order from two given lower case strings
# # # Python: Create two strings from a given string


# # always note if you want the string after spliing in same order then always go for this logic
# # s = 'Python Exercises Practice Solution Exercises'
# # lt = []
# # for i in s.split():
# #     if i not in lt:
# #         lt.append(i)
# # print(' '.join(lt))

# ########count
# s = 'mississippi'
# s1 = 'iss'
# count = 0
# for i in range(0,len(s)-2):
#     if s1 == s[i:i+3]:
#         count+=1
# print(count)

# What this code does:
# You’re checking a sentence to see if each word has all unique characters (i.e., no repeating letters in any word). If any word has a repeated character, you print 'false' and break. If all words pass the test, you print 'true'.

# Let’s fix and clarify it step-by-step:

s = 'i am out'
all_unique = True

for word in s.split():
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    max_occurrence = max(char_count.values())
    if max_occurrence > 1:
        print('false')
        all_unique = False
        break

if all_unique == True:
    print('true')

#######
s = 'Red Green White'
final = []
for i in s.split():
    lt = []
    for j in i:
        if j not in lt:
            lt.append(j)
    final.append(''.join(lt))
print(' '.join(final))

