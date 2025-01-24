import matplotlib as plt


def plot_distribution(df, column):
    sns.histplot(df[column], kde=True)
    plt.title(f"{column} Distribution")
    plt.show()
