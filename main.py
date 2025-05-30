from spiketraingen.SpikeTrainGenerator import SpikeTrainGenerator
from spiketraingen.SpikeTrainPlotter import SpikeTrainPlotter

if __name__ == "__main__":
    duration_ms = 1000  # Duration of the spike train in milliseconds which equates to 1 second

    # Create an instance of the generator
    gen = SpikeTrainGenerator(
        duration_ms=duration_ms,    # 1-second spike train
        jitter_std=2.0,             # add ±2ms noise to spike timing
        frequency=10.0,             # 10 Hz frequency
        amplitude=3,                # 3 spikes per cycle	
        output_dir="data"           # Directory to save the spike train
    )

    spikes_binary = gen.generate_binary_train() # Generate a spike train in binary mode 
    spikes_event = gen.generate_event_train()   # Generate a spike train in event mode 

    plotter = SpikeTrainPlotter(
        duration_ms=duration_ms,    # 1-second spike train
        output_dir="plots"          # Directory to save the plots
    )

    plotter.plot_binary(spikes_binary)  # Plot the binary spike train
    plotter.plot_event(spikes_event)    # Plot the event-based spike train