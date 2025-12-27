import pandas as pd

data = {
    "order_id": [101,102,103,104,105,106,107,108,109,110,111,112],
    "customer_id": [1,1,2,2,3,3,3,4,5,5,6,6],
    "region": ["US","US","EU","EU","US","US","EU","EU","US","EU","US","EU"],
    "product": ["A","B","A","C","B","C","A","B","A","C","B","A"],
    "quantity": [2,5,3,4,1,2,5,3,4,2,6,1],
    "price": [100,200,150,300,200,250,150,200,100,400,250,120],
    "order_date": pd.to_datetime([
        "2023-01-01","2023-01-05","2023-01-07","2023-01-08",
        "2023-02-01","2023-02-03","2023-02-04","2023-02-10",
        "2023-03-01","2023-03-05","2023-03-10","2023-03-11"
    ])
}

df = pd.DataFrame(data)


df['revenue'] = df['quantity']*df['price']
df['month'] = df['order_date'].dt.strftime('%m')
revenue_per_order = df[['order_id','customer_id','region','product','revenue','month']]
# print(revenue_per_order)

customer_monthly = revenue_per_order.groupby(['customer_id','region','month']).agg(
    total_revenue = ('revenue','sum'),
    unique_products = ('product','nunique'),
    revenue_A = ('revenue', lambda x: x[revenue_per_order.loc[x.index,'product'] == 'A'].sum()),
    revenue_B = ('revenue', lambda x: x[revenue_per_order.loc[x.index,'product'] == 'B'].sum()),
    revenue_C = ('revenue', lambda x: x[revenue_per_order.loc[x.index,'product'] == 'C'].sum())
).reset_index()

# print(customer_monthly)

region_summary = customer_monthly.groupby(['region','month']).agg(
    avg_revenue_per_customer = ('total_revenue','mean'),
    max_unique_products = ('unique_products','max'),
    customers_bought_A = ('revenue_A', lambda x: x.apply(lambda y: 1 if y > 0 else 0).sum()),
    customers_pref_B = ('region', lambda x: (customer_monthly.loc[x.index,'revenue_B']>customer_monthly.loc[x.index,'revenue_C']).sum()),
    total_region_revenue = ('total_revenue','sum')
).reset_index()

# print(region_summary)

final_summary = region_summary.groupby(['region',
        'month',
        'avg_revenue_per_customer',
        'max_unique_products',
        'customers_bought_A',
        'customers_pref_B',
        'total_region_revenue']).agg(
            pct_customers_bought_A = ('region','count')
        ).reset_index()

final_summary['pct_customers_bought_A'] = (100*(final_summary['customers_bought_A']/final_summary['pct_customers_bought_A'])).round(2)

print(final_summary.sort_values(['region','month'], ascending=[False,False]).reset_index(drop=True))