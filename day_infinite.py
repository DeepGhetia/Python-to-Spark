from functools import reduce
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

today = (datetime.today().date().replace(day=1) - relativedelta(days=1)).strftime('%d-%m-%Y %p')
print(today)

var = [1,2,3,4,5,6,7,8,9]
print([i for i in var if i%2==0])

