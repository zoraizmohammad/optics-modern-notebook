import numpy as np
import matplotlib.pyplot as plt

# Parameters for the exponential distribution
mu = 1.5  # mean rate (events per unit time)

# Generate simulated data using exponential distribution
num_samples = 10000
inter_event_times = np.random.exponential(scale=1/mu, size=num_samples)

# Plot histogram of simulated data
plt.figure(figsize=(10, 6))
count, bins, ignored = plt.hist(inter_event_times, bins=50, density=True, alpha=0.6, label='Simulated Data (Histogram)')

# Overlay the theoretical PDF
x = np.linspace(0, np.max(inter_event_times), 1000)
pdf = mu * np.exp(-mu * x)
plt.plot(x, pdf, 'r--', label=r'Theoretical PDF: $\mu e^{-\mu t}$')

# Labels and legend
plt.title("Histogram of Simulated Inter-Event Times vs. Exponential PDF")
plt.xlabel("Time between events (t)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()
