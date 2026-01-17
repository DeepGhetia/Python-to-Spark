s = '''Name~|Age
Brayan,gomez~|25
John,Cleark~|30
Sumit,Sen~|31
'''
lt = list(map(lambda x: x.replace('~',''),s.splitlines()[1:]))
with open('C:/Users/hp/Desktop/python/Python-to-Spark/read.txt','wt') as file:
    for i in lt:
        file.write(f'{i}\n')