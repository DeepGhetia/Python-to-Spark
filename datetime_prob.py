from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

year = 2027
start = datetime.strptime(f'01-01-{year}','%d-%m-%Y')

def datetime_func(start) -> list:
    lt = []
    for i in range(1,13):
        end = (start + relativedelta(months=1)) - timedelta(days=1)
        for j in range(end.day,0,-1):
            today = datetime.strptime(f'{str(j).zfill(2)+'-'+str(i).zfill(2)+'-'+str(year)}','%d-%m-%Y')
            if today.strftime('%a')=='Fri':
                lt.append(today.strftime('%d-%b-%Y'))
                break
        start = end + timedelta(days=1)
    return lt

val = datetime_func(start)
print(val)