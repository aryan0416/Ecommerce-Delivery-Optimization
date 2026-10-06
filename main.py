from src.data_loader import load_data
from src.analysis import calculate_metrics, analyze_delays, plot_delays

def main():
    df = load_data('data/ecommerce_sales.csv')
    calculate_metrics(df)
    delayed_cities = analyze_delays(df)
    plot_delays(delayed_cities, 'delayed_cities_plot.png')

if __name__ == "__main__":
    main()
