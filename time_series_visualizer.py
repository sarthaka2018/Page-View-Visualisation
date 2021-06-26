import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col="date", parse_dates=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    ax.plot(df)
    ax.set(xlabel='Date', ylabel='Page Views', title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    sns.lineplot(x='date', y='value', data=df, ax=ax)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar.reset_index(inplace=True)
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.month
    df_bar = df_bar.groupby(['year', 'month']).mean().reset_index()

    labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

    # Draw bar plot
    fig, ax = plt.subplots()
    sns.barplot(x='year', y='value', hue='month', data=df_bar, ax=ax, hue_order=labels)
    ax.set(xlabel='Years', ylabel='Average Page Views')
    ax.legend(loc='upper left', title='Months')




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1, fliersize=3.5)
    df_box.reindex(labels)
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, fliersize=3.5, order=labels)

    ax1.set(title='Year-wise Box Plot (Trend)', xlabel='Year', ylabel='Page Views')
    ax2.set(title='Month-wise Box Plot (Seasonality)', xlabel='Month', ylabel='Page Views')




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
