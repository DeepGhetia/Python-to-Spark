# file handling - 
# A, W, R(BY DEFAULT), X(CREATE), t, b

s = '''Inspirational quote
Short story or scene
Poem (any style)
Dialogue between characters
Funny or sarcastic line
Mystery or horror snippet
Philosophical thought
Random facts or trivia
'''
# with open('C:/Users/hp/Desktop/python/read.txt') as file:
#     lt = [j for i in [i.split() for i in file.read().splitlines()] for j in i]
#     print(lt)

# with open('C:/Users/hp/Desktop/python/read.txt','a') as file:
#     lt = s.split('\n')
#     for i in lt:
#         file.write(f"{i}\n")

# with open('C:/Users/hp/Desktop/python/read.txt') as file:
#     for i in file.read().splitlines():
#         print(i)

# with open('C:/Users/hp/Desktop/python/read.txt') as f:
#     lt = f.readline().stirp().split(',') //string -> readline()
#     print(lt)
#     lt1 = [i.split(',') for i in f.read().splitlines()]
#     print(lt1)
#     for i in range(len(lt1)):
#         print(f"{lt[1]} : {lt1[i][1]}")

# with open('C:/Users/hp/Desktop/python/read.txt') as file:
#     lt = file.readline().strip().split(',')
#     print(lt)
#     lt1 = file.readlines()
#     print(lt1)
#     lt2 = []
#     for i in lt1:
#         lt2.append(i.strip())
#     final = [i.split(',') for i in lt2]
#     print(final)

# file.read() -> str
# file.read().splitlines() -> list with stripped data 
# file.readline() -> full string 1st file 
# file.readlines() -> list without stripped data

# with open('C:/Users/hp/Desktop/python/read.txt','at') as file:
#     file.write('\n')
#     file.write(s)