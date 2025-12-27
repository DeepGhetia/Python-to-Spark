import pandas as pd
from datetime import datetime,timedelta
# Users
users = pd.DataFrame({
    'user_id': [1, 2, 3, 4, 5, 6],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'country': ['US', 'US', 'UK', 'IN', 'IN', 'UK'],
    'signup_date': ['2025-01-01','2025-01-02','2025-01-03','2025-01-04','2025-01-05','2025-01-06']
})

# Orders
orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'user_id': [1, 2, 1, 3, 4, 5, 3, 6, 2, 5],
    'order_date': ['2025-02-01','2025-02-01','2025-02-05','2025-02-05','2025-02-07',
                   '2025-02-07','2025-02-10','2025-02-11','2025-02-12','2025-02-13'],
    'amount': [250, 450, 300, 150, 500, 200, 100, 300, 200, 100],
    'status': ['completed','completed','canceled','completed','completed','canceled','completed','completed','completed','completed'],
    'coupon_used': [True, False, True, True, False, False, True, False, True, True]
})

# Refunds
refunds = pd.DataFrame({
    'order_id': [103, 105, 110],
    'refund_amount': [300, 500, 100],
    'refund_date': ['2025-02-06','2025-02-08','2025-02-14']
})

df = pd.merge(users,orders,on='user_id',how='left')
df = pd.merge(df,refunds,on='order_id',how='left')
df['rn'] = df.groupby('user_id')['order_date'].rank(method='first',ascending=False).astype('int64')
df = df.sort_values(['user_id','order_date'])
df['next_order_date'] = df.groupby('user_id')['order_date'].shift(-1)

def func(y,x):
    return (y-x).days
df['days'] = df.apply(lambda x: func(pd.to_datetime(x['next_order_date']),pd.to_datetime(x['order_date'])), axis=1).round(1)
#agg
df = df.fillna({'refund_amount':0})
df['agg'] = df['amount'] - df['refund_amount']
df = df.sort_values(['country','order_date'])
df['cum_country_revenue'] = df.groupby('country')['agg'].cumsum()
print(df)
final = df.groupby('country').agg(
    top_users = ('user_id',lambda x: x[(df.loc[x.index,'rn']<=3) & (df.loc[x.index,'status']=='completed')].nunique()),
    coupon_revenue = ('agg',lambda x: x[(df.loc[x.index,'coupon_used']==True) & (df.loc[x.index,'status']=='completed')].sum()),
    avg_order_gap = ('days','mean')
).reset_index()


final = final[final['coupon_revenue']>400].sort_values('coupon_revenue',ascending=False)
print(final)