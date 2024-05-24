import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def test_environment():
    print("NumPy version:", np.__version__)
    print("Pandas version:", pd.__version__)

    # Simple plot to test matplotlib
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Test Plot")
    plt.savefig("test_plot.png")
    print("Plot saved as test_plot.png")


if __name__ == "__main__":
    test_environment()
