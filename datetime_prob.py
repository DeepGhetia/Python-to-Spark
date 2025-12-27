from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

year = '2023'
start = datetime.strptime('01-01-'+year,'%d-%m-%Y')
final = []

for _ in range(1,13):
    end = (start + relativedelta(months=1)) - timedelta(days=1)
    for j in range(end.day,start.day-1,-1):
        input = f'{str(j).zfill(2)}-{str(start.month).zfill(2)}-{start.year}'
        val = datetime.strptime(input,'%d-%m-%Y').strftime('%a')
        if val == 'Fri':
            final.append(input)
            break
    start = start + relativedelta(months=1)
print(final)