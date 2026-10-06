import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ecommerce_sales.csv')
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'])

avg_order_value = df['OrderValue_INR'].mean()
print(f"Average Order Value: {avg_order_value}")

df['DeliveryDays'] = (df['DeliveryDate'] - df['OrderDate']).dt.days
df['IsDelayed'] = df['DeliveryDays'] > 5

delayed_orders = df[df['IsDelayed']]
delayed_cities = delayed_orders['City'].value_counts().head(5)

plt.figure(figsize=(10, 6))
delayed_cities.plot(kind='bar', color='salmon')
plt.title('Top 5 Cities with Deliveries > 5 Days')
plt.xlabel('City')
plt.ylabel('Number of Delayed Deliveries')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('delayed_cities_plot.png')
plt.show()
