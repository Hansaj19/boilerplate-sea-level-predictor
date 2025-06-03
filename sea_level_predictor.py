import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (using all data)
    # Get slope and y-intercept for the entire dataset
    linregress_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope_all = linregress_all.slope
    intercept_all = linregress_all.intercept

    # Create x-values for the line from the start year to 2050
    x_pred_all = pd.Series([i for i in range(df['Year'].min(), 2051)])
    y_pred_all = slope_all * x_pred_all + intercept_all
    ax.plot(x_pred_all, y_pred_all, color='red', label='Fit (1880-2050)')

    # Create second line of best fit (using data from year 2000 onwards)
    # Filter data from year 2000
    df_2000 = df[df['Year'] >= 2000]

    # Get slope and y-intercept for data from year 2000 onwards
    linregress_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    slope_2000 = linregress_2000.slope
    intercept_2000 = linregress_2000.intercept

    # Create x-values for the line from 2000 to 2050
    x_pred_2000 = pd.Series([i for i in range(2000, 2051)])
    y_pred_2000 = slope_2000 * x_pred_2000 + intercept_2000
    ax.plot(x_pred_2000, y_pred_2000, color='green', label='Fit (2000-2050)')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend() # Display legend for the lines

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()