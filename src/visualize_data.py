import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned data
df = pd.read_csv("data/cleaned_data.csv")

# Plot 1: experiment_score
plt.figure()
df["experiment_score"].plot(kind="bar")
plt.title("Experiment Scores")
plt.xlabel("Index")
plt.ylabel("Score")
plt.tight_layout()
plt.savefig("results/experiment_score_plot.png")
plt.close()

# Plot 2: temperature
plt.figure()
df["temperature"].plot(kind="line", marker="o")
plt.title("Temperature")
plt.xlabel("Index")
plt.ylabel("Temperature")
plt.tight_layout()
plt.savefig("results/temperature_plot.png")
plt.close()

print("Plots saved in results folder")