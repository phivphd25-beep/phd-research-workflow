import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# Plot 1: score plot
plt.figure()
df["experiment_score"].plot(kind="bar")
plt.title("Experiment Score")
plt.xlabel("Index")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("results/score_plot.png")
plt.close()

# Plot 2: temperature and humidity plot
plt.figure()
plt.plot(df["temperature"], marker="o", label="Temperature")
plt.plot(df["humidity"], marker="s", label="Humidity")
plt.title("Temperature and Humidity")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.tight_layout()
plt.savefig("results/temperature_humidity_plot.png")
plt.close()

print("Plots saved successfully")