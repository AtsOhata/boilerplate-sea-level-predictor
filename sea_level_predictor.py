import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    year = df['Year']
    sea_level = df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(10, 6))
    plt.scatter(year, sea_level, label='Data Points', color='blue')
    slope, intercept, r_value, p_value, std_err = linregress(year, sea_level)
    
    # Create first line of best fit
    all_year = list(range(1880, 2051))
    predicted_sea_levels = [intercept + slope * y for y in all_year]
    plt.plot(all_year, predicted_sea_levels, color='red', label='Line of Best Fit')

    # Create second line of best fit
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    future_years = list(range(2000, 2051))
    predicted_sea_levels = [intercept_recent + slope_recent * y for y in future_years]
    plt.plot(future_years, predicted_sea_levels, linestyle='--', color='green', label='Prediction to 2050')

    x_ticks = list(range(1850, 2100, 25))
    x_tick_labels = [f'{tick}.0' for tick in x_ticks]
    plt.xticks(x_ticks, x_tick_labels)
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()