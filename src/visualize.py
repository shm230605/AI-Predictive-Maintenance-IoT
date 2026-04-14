import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder automatically
os.makedirs("images", exist_ok=True)

def plot_temperature(df):
    plt.figure()
    plt.plot(df['temperature'])
    plt.title("Temperature Trend")
    plt.xlabel("Index")
    plt.ylabel("Temperature")
    plt.savefig("images/temperature.png")
    plt.close()

def plot_failure_distribution(df):
    plt.figure()
    sns.countplot(x='failure', data=df)
    plt.title("Failure Distribution")
    plt.savefig("images/failure.png")
    plt.close()