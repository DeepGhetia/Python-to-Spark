from datetime import datetime,timedelta
from dateutil.relativedelta import relativedelta

start = datetime.strptime('01-01-2025','%d-%m-%Y')
lt = []
for _ in range(1,13):
    end = (start + relativedelta(months=1)) - timedelta(days=1)
    for val in range(end.day,start.day-1,-1):
        inter = f'{str(val).zfill(2)+'-'+str(end.month).zfill(2)+'-'+str(end.year)}'
        temp = datetime.strptime(inter,'%d-%m-%Y').strftime('%a')
        if temp=='Thu':
            lt.append(inter)
            break
    start = end + timedelta(days=1)
print(lt)