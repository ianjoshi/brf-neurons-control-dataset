import numpy as np
import matplotlib.pyplot as plt
import os

class SpikeTrainPlotter:
    def __init__(self, duration_ms, frequency, output_dir='plots'):
        """
        Initializes the plotter.

        Parameters:
        - duration_ms: Duration of the spike train in milliseconds.
        - frequency (float): Frequency in Hz.
        - output_dir: Directory to save plots.
        """
        self.duration_ms = duration_ms
        self.frequency = frequency
        self.output_dir = output_dir

        # Set default plot style
        plt.rcParams['font.family'] = 'serif'

        os.makedirs(self.output_dir, exist_ok=True)
    
    def plot_binary(self, spike_vector, title="Binary Spike Train"):
        """
        Plot and save a binary spike train.

        Parameters:
        - spike_vector (np.ndarray): Numpy array of 0s and 1s (length = duration_ms).
        - title (str): Title for the plot and filename.

        Returns:
        - None
        """
        full_title = f"{title} - Freq: {self.frequency}Hz"
        plt.figure(figsize=(10, 2))
        time_axis = np.arange(len(spike_vector))
        plt.step(time_axis, spike_vector, where='post', linewidth=0.8)
        plt.ylim(-0.2, 1.2)
        plt.xlim(0, self.duration_ms)
        plt.xlabel("Time (ms)")
        plt.ylabel("Spike (0/1)")
        plt.title(full_title)
        plt.tight_layout()
        self._save(title, mode='binary')

    def plot_event(self, spike_times, title="Event-Based Spike Train"):
        """
        Plot and save an event-based spike train.

        Parameters:
        - spike_times (np.ndarray): List or array of spike times (in ms).
        - title (str): Title for the plot and filename.
        """
        full_title = f"{title} - Freq: {self.frequency}Hz"
        plt.figure(figsize=(10, 2))
        for spike_time in spike_times:
            plt.axvline(x=spike_time, color='black', linewidth=0.8)
        plt.ylim(0, 1)
        plt.xlim(0, self.duration_ms)
        plt.xlabel("Time (ms)")
        plt.ylabel("Spike")
        plt.title(full_title)
        plt.tight_layout()
        self._save(title, mode='event')

    def _save(self, title, mode):
        """
        Save the generated plot to output directory.

        Parameters:
        - title (str): Title used to generate filename.
        - mode (str): The type of spike train ('binary' or 'event').
        """
        mode_dir = os.path.join(self.output_dir, mode)
        os.makedirs(mode_dir, exist_ok=True)

        filename = f"{title.replace(' ', '_').lower()}_f{self.frequency}.png"
        filepath = os.path.join(mode_dir, filename)
        plt.savefig(filepath)
        print(f"Saved plot to: {filepath}")