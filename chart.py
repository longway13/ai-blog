# Creating individual charts for each distribution overlayed on the True Space with enhanced colors
import numpy as np
import matplotlib.pyplot as plt

# Loop over each configuration to generate individual plots with more vivid colors
fig, axes = plt.subplots(1, 3, figsize=(18, 6))
configs = []
for ax, config in zip(axes, configs):
    # Generate data points based on each configuration's std_dev
    x_data = np.random.normal(0, config["std_dev"], 100)
    y_data = np.random.normal(0, config["std_dev"], 100)
    
    # Plot the True Space in light grey as a base
    ax.scatter(x_true_space, y_true_space, color="darkgrey", alpha=0.6, s=15, label="True Space")
    
    # Plot the overlay for the current state with a more vivid color
    ax.scatter(x_data, y_data, color=config["color"], alpha=0.8, s=20, label=config["label"])
    
    # Set title and adjust axis limits
    ax.set_title(config["title"], fontsize=14)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    
    # Hide axis for a cleaner look
    ax.axis('off')
    
    # Add legend
    ax.legend(loc="upper right", fontsize=10)

# Show the plots
plt.tight_layout()
plt.show()
