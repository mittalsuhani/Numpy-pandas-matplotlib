
import matplotlib.pyplot as plt

# Years
years = list(range(2014, 2024))

# Hypothetical runs data
kohli_runs = [1050, 980, 1200, 1100, 950, 1300, 1250, 1150, 1000, 1080]
rohit_runs = [870, 920, 990, 1020, 1110, 980, 1200, 1170, 1090, 1130]
sehwag_runs = [750, 680, 720, 650, 700, 620, 590, 610, 580, 560]

# Create plot
plt.figure(figsize=(12, 6))

# Plot lines with different styles
plt.plot(
    years,
    kohli_runs,
    label="Virat Kohli",
    color="blue",
    linestyle="-",
    linewidth=2,
    marker="o"
)

plt.plot(
    years,
    rohit_runs,
    label="Rohit Sharma",
    color="green",
    linestyle="--",
    linewidth=2,
    marker="s"
)

# Custom style for Sehwag
plt.plot(
    years,
    sehwag_runs,
    label="Virender Sehwag",
    color="red",
    linestyle=":",
    linewidth=3,
    marker="D",
    markersize=8
)

# Labels and title
plt.xlabel("Years")
plt.ylabel("Runs Scored")
plt.title("Comparison of Hypothetical Runs: Kohli vs Rohit vs Sehwag")

# Legend
plt.legend()

# Grid
plt.grid(True)

# Show plot
plt.show()

