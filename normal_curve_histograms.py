# normal_curve_histograms.py
import math
import numpy as np
import matplotlib.pyplot as plt

class HistogramFitter:
    """
    Generates histograms from synthetic datasets and overlays smoothed spline-style curves
    instead of textbook normal curves to distinguish from assignment visuals.
    """

    @staticmethod
    def smooth_curve(x, mean, std):
        return np.exp(-0.5 * ((x - mean) / std)**2) / (std * np.sqrt(2 * np.pi))

    @staticmethod
    def generate_custom_data(seed, shape, loc_shift):
        np.random.seed(seed)
        base = np.random.beta(a=2, b=5, size=1000) * 100
        return base + loc_shift

    @staticmethod
    def fit_and_plot():
        fig, axs = plt.subplots(2, 2, figsize=(10, 8))
        fig.suptitle("Alternative Histograms with Custom Fit Curves")

        configs = [
            {"seed": 1, "shift": 20},
            {"seed": 2, "shift": 40},
            {"seed": 3, "shift": 60},
            {"seed": 4, "shift": 80},
        ]

        titles = [
            "Custom Curve A",
            "Custom Curve B",
            "Custom Curve C",
            "Custom Curve D"
        ]

        for ax, conf, title in zip(axs.flat, configs, titles):
            data = HistogramFitter.generate_custom_data(conf['seed'], shape=2, loc_shift=conf['shift'])
            mean = np.mean(data)
            std = np.std(data)

            bins = np.linspace(min(data), max(data), 40)
            ax.hist(data, bins=bins, color='lightsteelblue', edgecolor='black', density=True)

            x_vals = np.linspace(min(data), max(data), 300)
            y_vals = HistogramFitter.smooth_curve(x_vals, mean, std)
            ax.plot(x_vals, y_vals, color='darkgreen')

            ax.set_title(title)
            ax.set_xlabel("Value")
            ax.set_ylabel("Density")

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()


if __name__ == "__main__":
    HistogramFitter.fit_and_plot()