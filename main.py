from spiketraingen.SpikeTrainGenerator import SpikeTrainGenerator
from spiketraingen.SpikeTrainPlotter import SpikeTrainPlotter

if __name__ == "__main__":
    # Duration of the spike train in milliseconds which equates to 1 second:
    # This gives a long enough window to observe divergence or steady behavior
    duration_ms = 1000

    # Frequencies to test neuron behavior:
    # This range tests whether proximity to or distance from resonance triggers exploding spiking
    frequencies = [5.0, 10.0, 15.0, 20.0]

    # Amplitudes to control number of spikes per cycle
    amplitudes = [1, 2, 5, 10, 15]

    # No jitter for deterministic controlled experiments:
    # This ensures any exploding behavior is due to the neuron's internal dynamics,
    # not variability in the input spike timing
    jitter_std = 0.0

    for f in frequencies:
        for a in amplitudes:
            # Create an instance of the generator
            gen = SpikeTrainGenerator(
                duration_ms=duration_ms,
                jitter_std=jitter_std,
                frequency=f,
                amplitude=a,
                output_dir="data"
            )

            spikes_binary = gen.generate_binary_train() # Generate a spike train in binary mode
            spikes_event = gen.generate_event_train()   # Generate a spike train in event mode 

            # Create an instance of the plotter
            plotter = SpikeTrainPlotter(
                duration_ms=duration_ms,
                frequency=f,
                amplitude=a,
                output_dir="plots"
            )

            plotter.plot_binary(spikes_binary)  # Plot the binary spike train
            plotter.plot_event(spikes_event)    # Plot the event-based spike train