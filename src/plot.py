import numpy as np
import matplotlib.pyplot as plt

def plot(horizontal, graphs):
    fig, ax = plt.subplots()

    for graph in graphs:
        ax.plot(horizontal, graph, linewidth=2.0)

    ax.set(xlim=(np.min(horizontal), np.max(horizontal)),  ylim=(np.min(graphs), np.max(graphs)))

    plt.show()