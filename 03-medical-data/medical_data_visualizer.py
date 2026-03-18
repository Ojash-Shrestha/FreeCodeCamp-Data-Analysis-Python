import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25 ).astype(int)

# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    """
    Creates a categorical plot that shows the counts of good and bad outcomes
    for various health indicators, split by cardiovascular disease status.
    The function transforms the data into long format and groups it to
    visualize the distribution of cholesterol, glucose, smoking, alcohol,
    activity, and overweight status across cardio=0 and cardio=1 patients.

    Returns:
        matplotlib.figure.Figure: The figure object containing the categorical plot.
    """
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7
    g = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )

    #8
    fig = g.fig

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    """
    Cleans the medical data by filtering out blood pressure anomalies and
    extreme height/weight outliers, then generates a correlation heatmap.
    Correlations are calculated across all 14 variables including age,
    blood pressure, cholesterol, and lifestyle factors. The heatmap uses
    a mask to hide the upper triangle for better readability and displays
    the correlation coefficients between all variables.

    Returns:
        matplotlib.figure.Figure: The figure object containing the heatmap.
    """
    # 11
    df_heat = df[
    (df['ap_lo'] <= df['ap_hi']) &
    (df['height'] >= df['height'].quantile(0.025)) &
    (df['height'] <= df['height'].quantile(0.975)) &
    (df['weight'] >= df['weight'].quantile(0.025)) &
    (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        ax=ax
    )

    # 16
    fig.savefig('heatmap.png')
    return fig