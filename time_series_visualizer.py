import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig("line_plot.png")
    return fig

def draw_bar_plot():
    # Prepare data for bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    df_bar = df_bar.groupby(["year", "month"])["value"].mean().unstack()

    fig = df_bar.plot(kind="bar", figsize=(12, 6), legend=True).figure
    plt.title("Average Daily Page Views per Month")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", 
               labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    fig.savefig("bar_plot.png")
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box["year"] = df_box.index.year
    df_box["month"] = df_box.index.month_name()

    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x="month", y="value", 
                data=df_box, ax=axes[1], 
                order=["January", "February", "March", "April", "May", "June", "July", 
                       "August", "September", "October", "November", "December"])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    fig.savefig("box_plot.png")
    return fig

# For testing purposes
draw_bar_plot()
draw_line_plot()
draw_box_plot()