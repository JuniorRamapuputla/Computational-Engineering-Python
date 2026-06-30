#Plotting both sine and cosine waveforms on different axis

import matplotlib.pyplot as plt
from numpy import pi, sin, cos, arange

#create a time vector from 0 to 1 seconds, spaced by delta seconds
delta = 0.01
t = arange(0.0, 1.0, delta)

#create sine and cosine vectors
y1 = sin(2*pi*t)
y2 = cos(2*pi*t)

#plot the functions
fig, axs = plt.subplots(1,2,sharey=True)
axs[0].plot(t, y1, 'tab:grey') #Plot the sine function (y1) in grey
axs[1].plot(t, y2, 'tab:grey') #Plot the cosine function (y2) in grey

#Set Y label only for the left plot
axs[0].set(ylabel = 'Amplitude (V)')
axs[0].set(title = 'sin(2 $\ pi $ t)')
axs[1].set(title = 'cos(2 $\ pi $ t)')

#Set styles common to both plots: X and Y limits, X label
for ax in axs:
    ax.set(xlim = (0,1), ylim = (-1,1))
    ax.set(xlabel = 'Time (s)')
    ax.grid(True)

#set the plot title
fig.suptitle('FIgure showing sin(2$ \pi $t) and cos(2$ \pi $t) as subplots', fontweight = 'bold')    

plt.show()