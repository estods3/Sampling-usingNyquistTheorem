# Sampling using Nyquist Theorem
This simulation is a useful demonstration of how an input signal can be sampled to collect and store data in a digital system. The simulator generates a an input signal of a randomized frequency and allows the user to select a sampling frequency to read the input signal and then recreate it in the output based on the samples.

![Alt text](https://github.com/estods3/Sampling-usingNyquistTheorem/blob/master/screenshots/sampling.gif?raw=true "Sampling")


The simulation demonstrates the importance of the Nyquist–Shannon Sampling Theorem in determining what sampling frequency should be selected for a data collection system.

## System Requirements

You will need Python to run this program. I tested it with Python 2.7.15+ 64 bit.
You will also need a few Python modules. You can install these by typing 

`pip install -r requirements.txt`

in your cloned directory of this repository.

## Example:

Clone or download the code and navigate to its directory in a terminal.
Run the program by typing the following in a terminal: 

`python src/runSimulation.py`

A pygame window will appear with the simulator: an input signal window, an output signal window, and a slider at the top to select a sampling frequency.

Drag the slider to select a frequency to sample the input signal. The corresponding output will show on the right. If the sampling frequency is less than the minimum Nyquist frequency (2 X Max. Input Frequency) the output signal will look very different from the input due to aliasing. The estimated frequency (displayed in the terminal) will also be inaccurate.
![Alt text](/screenshots/FrequencyLowerThanDoubleInput.png?raw=true "Sampling Frequency Less than Nyquist")

If the sampling frequency is greater than the Nyquist frequency, the output signal will more closely mirror the input and the estimated frequency (displayed in the terminal) will also be accurate. This means the signal can be reconstructed and its frequency approximated without aliasing.
![Alt text](/screenshots/FrequencyGreaterThanNyquist.png?raw=true "Sampling Frequency Greater than Nyquist")

Note, because the ouput signal is drawn using lines rather than a sinusoid, the output signal will not match the input unless the sampling frequency is an order of magnitude higher than the input frequency as shown below. 
![Alt text](/screenshots/FrequencyHighResolution.png?raw=true "Sampling Frequency Significantly Greater than Nyquist")

## Resources:
https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
