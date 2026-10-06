import matplotlib.pyplot as plt

def calculate_metrics(df):
    avg_shipping_cost = df['Shipping_Cost'].mean()
    print(f"Average Shipping Cost: {avg_shipping_cost:.2f}")

def analyze_delays(df):
    df['DeliveryDays'] = (df['Delivery_Date'] - df['Order_Date']).dt.days
    df['IsDelayed'] = df['DeliveryDays'] > 5
    delayed_orders = df[df['IsDelayed']]
    return delayed_orders['Customer_Region'].value_counts().head(5)

def plot_delays(delayed_cities, output_path):
    plt.figure(figsize=(10, 6))
    delayed_cities.plot(kind='bar', color='salmon')
    plt.title('Top 5 Regions with Deliveries > 5 Days')
    plt.xlabel('Region')
    plt.ylabel('Number of Delayed Deliveries')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Plot saved as {output_path}")
