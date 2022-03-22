import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

sample_rate = 10000 # Hz

# create our Band Pass Filter array
h = [   -0.007556823672943045,
  -5.5586152510954474e-15,
  -0.03983643480317535,
  -1.7835253290583313e-15,
  0.21379181250492926,
  4.179969279202232e-15,
  -0.4593448330389809,
  -2.2570793273606466e-15,
  0.5799555976951902,
  -2.2570793273606466e-15,
  -0.4593448330389809,
  4.179969279202232e-15,
  0.21379181250492926,
  -1.7835253290583313e-15,
  -0.03983643480317535,
  -5.5586152510954474e-15,
  -0.007556823672943045
    ]

# plot the impulse response
plt.figure('impulse')
plt.plot(h, '.-')
plt.show()


# plot the frequency response
H = np.abs(np.fft.fft(h, 1024)) # take the 1024-point FFT and magnitude
H = np.fft.fftshift(H) # make 0 Hz in the center
w = np.linspace(-sample_rate/2, sample_rate/2, len(H)) # x axis
plt.figure('freq')
plt.plot(w, H, '.-')
plt.show()
