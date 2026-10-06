# E-Commerce Delivery Optimization

![E-Commerce Banner](banner.jpg)

## Business Problem
In the highly competitive e-commerce landscape, especially during peak Indian festive sales, optimizing logistics is critical. Delivery delays directly impact customer satisfaction, brand loyalty, and operational costs. This project aims to identify and flag delayed deliveries (taking more than 5 days) and highlight the cities experiencing the most significant logistical bottlenecks. By understanding these patterns, the business can proactively route shipments, allocate more regional delivery partners, and set realistic delivery expectations for customers.

## Tech Stack
* **Python**: Core programming language.
* **Pandas**: For robust data manipulation and time-series date processing.
* **Matplotlib**: For generating clear, professional data visualizations.

## Methodology
1. **Data Ingestion**: The script loads the raw sales data.
2. **Data Transformation**: Order and delivery dates are converted into datetime objects to calculate the exact delivery duration in days.
3. **Metric Calculation**: The script calculates the Average Order Value across the dataset to provide a baseline financial metric.
4. **Anomaly Detection**: Deliveries taking more than 5 days are flagged as "Delayed".
5. **Visualization**: The top 5 cities with the highest count of delayed deliveries are extracted and visualized using a bar chart, saved as `delayed_cities_plot.png`.

## Business Impact
By identifying the top 5 delayed cities, the supply chain management team can immediately investigate local bottlenecks. The impact includes:
* Reduced customer churn by addressing recurring delays.
* Optimized logistics costs by predicting regional volume spikes.
* Better resource allocation during high-demand festive seasons.

## Setup Instructions
**Prerequisites:**
You must provide the dataset `ecommerce_sales.csv` in the root of this directory. The CSV must contain the following columns: `OrderID`, `City`, `OrderDate`, `DeliveryDate`, and `OrderValue_INR`.

**Execution:**
Run the analysis script using the following command:
```bash
python main.py
```
This will output the average order value to the console and generate a plot of the delayed cities.
