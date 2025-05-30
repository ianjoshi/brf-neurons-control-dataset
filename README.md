# Control Dataset Generator for Resonate-and-Fire Neurons
This repository generates a synthetic control dataset of spike trains designed to test **exploding spiking behavior** in **standard Resonate-and-Fire (RF) neurons** introduced by Izhikevich:
> Izhikevich, E. M. (2001). *Resonate-and-Fire Neurons*. Neural Netw., 14(6-7), 883-94. 
> doi:10.1016/s0893-6080(01)00078-8

The experiment is inspired by and directly tests a claim made in:
> Higuchi, S., Kairat, S., Bohte, S. M., & Otte, S. (2024). *Balanced Resonate-and-Fire Neurons*. 
> https://arxiv.org/abs/2402.14603

## What This Repository Does
1. Generates spike trains by sweeping over different frequencies.
2. Saves each spike train in both **binary** (0/1 vector) and **event-based** (spike times) format.
3. Plots and saves visualizations for each spike train.
4. Organizes everything in structured output directories for use in RF simulations.

## Local Setup Instructions
### 1. Clone the repository
```bash
git clone https://github.com/ianjoshi/brf-neurons-control-dataset
cd brf-neurons-control-dataset
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv brfc-venv
brfc-venv\Scripts\activate          # On Windows
```

### 3. Install required packages
```bash
pip install -r requirements.txt
```

## How to Run
Run the main script to generate the dataset:
```bash
python main.py
```

This will:
- Generate a set of spike trains for a grid of (frequency, amplitude) pairs,
- Save the data to `data/`,
- Save plots to `plots/`.

## Dataset Parameters
These parameters are swept to generate the control dataset:
| Parameter   | Values                                                           |
| ----------- | ---------------------------------------------------------------- |
| `frequency` | `[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60]` (Hz)               |
| `amplitude` | `5` spikes per cycle                                             |
| `duration`  | `1000` ms (1 second per spike train)                             |
| `jitter`    | `0.0` (no noise for clean control input)                         |

Each (frequency, amplitude) pair produces two spike trains:
- A binary train (0/1 vector, 1 ms resolution),
- An event train (list of spike times).

## Experimental Use Case
This dataset is designed to be used as input to simulated Resonate-and-Fire neurons under varying internal parameters. By applying the same input across different parameter regimes, you can isolate whether divergence (exploding spiking) is caused by:
- The input spike pattern (e.g. frequency or energy),
- Or the neuron's internal instability.
This forms the basis of a controlled experiment to validate claims in the *Balanced Resonate-and-Fire Neurons* paper.

## License
This project is licensed under the MIT License. You are free to use, modify, and share it for academic and research purposes.

## References
1. Izhikevich, E. M. (2001). *Resonate-and-Fire Neurons*. Neural Netw., 14(6-7), 883-94. doi:10.1016/s0893-6080(01)00078-8
2. Higuchi, S., Kairat, S., Bohte, S. M., & Otte, S. (2024). *Balanced Resonate-and-Fire Neurons*. https://arxiv.org/abs/2402.14603