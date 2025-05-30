import numpy as np
import os

class SpikeTrainGenerator:
    def __init__(self, duration_ms, jitter_std, frequency, amplitude, output_dir='data'):
        """
        Initializes the spike train generator.

        Parameters:
        - duration_ms (int): Duration of the spike train in milliseconds.
        - jitter_std (float): Standard deviation of Gaussian timing noise (ms).
        - frequency (float): Frequency in Hz.
        - amplitude (int): Number of spikes per cycle.
        - output_dir (str): Directory where the spike train will be saved.
        """
        self.duration_ms = duration_ms
        self.jitter_std = jitter_std
        self.frequency = frequency
        self.amplitude = amplitude
        self.output_dir = output_dir

        self.interval = 1000 / frequency # Duration of one cycle in milliseconds
        self.num_cycles = int(self.duration_ms / self.interval) # How many cycles fit in the total duration

        os.makedirs(self.output_dir, exist_ok=True)

    def generate_binary_train(self):
        """
        Generate and save a single binary spike train.

        Paramaters:
        - None

        Returns:
        - spikes (np.ndarray): A NumPy array representing the binary spike train, where 1 indicates a spike and 0 indicates no spike.
        """
        # Create a binary vector of 0s and 1s with 1s marking spike positions
        spikes = np.zeros(self.duration_ms, dtype=int)
        for cycle in range(self.num_cycles):
            base_time = int(cycle * self.interval)
            for _ in range(self.amplitude):
                # Add noise and round to nearest millisecond
                spike_time = int(base_time + np.random.normal(0, self.jitter_std))

                # Only include spikes within the total duration
                if 0 <= spike_time < self.duration_ms:
                    # Mark spike occurrence
                    spikes[spike_time] = 1
        
        # Save the train to the output directory
        self._save(spikes, 'binary')

        return spikes

    def generate_event_train(self):
        """
        Generate and save a single event-based spike train.

        Paramaters:
        - None

        Returns:
        - spikes (np.ndarray): A NumPy array representing the spike train consisting of spike times in milliseconds.
        """
        # Generate event-based spike times with Gaussian jitter
        spikes = []
        for cycle in range(self.num_cycles):
            base_time = cycle * self.interval
            for _ in range(self.amplitude):
                # Add noise to each spike time
                spike_time = base_time + np.random.normal(0, self.jitter_std)

                # Only include spikes within the total duration
                if 0 <= spike_time < self.duration_ms:
                    spikes.append(spike_time)

        # Convert list to chronologically sorted NumPy array
        spikes = np.sort(np.array(spikes))

        # Save the train to the output directory
        self._save(spikes, 'event')

        return spikes

    def _save(self, spikes, mode):
        """
        Save the generated spike train to output directory.

        Parameters:
        - spikes (np.ndarray): The spike train to save (either binary or event-based).
        - mode (string): The type of spike train ('binary' or 'event').

        Returns:
        - None
        """
        # Construct a descriptive filename
        filename = f"spike_f{int(self.frequency)}_a{self.amplitude}_{mode}.npy"
        filepath = os.path.join(self.output_dir, filename)

        # Save the spike train as .npy
        np.save(filepath, spikes)
        print(f"Saved: {filepath}")
