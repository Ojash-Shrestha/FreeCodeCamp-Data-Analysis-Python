import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    """
    Visualizes historical sea level data and predicts future sea level rise
    through the year 2050 using linear regression.

    This function reads dataset 'epa-sea-level.csv', generates a scatter plot
    of the 'CSIRO Adjusted Sea Level' by 'Year', and overlays two lines of best fit:
    1. A historical trend line based on all available data (from 1880 to 2050).
    2. A modern trend line based only on data from the year 2000 onwards to
       2050, to illustrate recent increase in sea level rise.

    Returns:
    matplotlib.axes.Axes: The axes object containing the final plot,
    returned for testing purposes.
    """
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure()
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x_all = df['Year']
    y_all = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x_all, y_all)

    x_pred = range(1880, 2051)
    y_pred = [slope * x + intercept for x in x_pred]
    plt.plot(x_pred, y_pred)

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    slope2, intercept2, r_value, p_value, std_err = linregress(x_recent, y_recent)

    x_pred2 = range(2000, 2051)
    y_pred2 = [slope2 * x + intercept2 for x in x_pred2]
    plt.plot(x_pred2, y_pred2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
