"""
TITLE: Vehicle Speed and Distance
DESCRIPTION: A time vector t of evenly spaced values from 0s to 1s is created using the arange function, 
            which will serve as the x-axis of the plot. For each x-axis value, a corresponding y-axis value
            is calculated for a sine wave of frequency 2pi * 1 hz
AUTHOR: [Junior Ramapuputla]
DATE: 2026/06/27
"""


import matplotlib.pyplot as plt
from numpy import pi, sin, cos, arange


#The time spacing between time samples 
delta = 0.01

#create a time vector from 0 to 1, spaced by delta seconds
t = arange(0.0, pi, delta)

#create a sine & cosine wave vector
y1 = sin(2*pi*t)
y2 = cos(2*pi*t)


#Plot the functions
plt.figure(1) # 1 identifies the plot as figure 1
plt.plot(t,y1) # same as plot(x,y)
plt.plot(t,y2)

#Customize the plt
#set the axis limits
plt.xlim(0,1)
plt.ylim(-1,1)

#set the axis labels of the plot
plt.xlabel('Time(s)')
plt.ylabel('Amplitude (V)')

#Set the plot title
plt.title('Graph showing both sin(2$pi$t) and cos(2$pi$t)')
 
#Turn on the plot grid
plt.grid(True)

#Add a legend to the plot
plt.legend(['sin(2$\pi$t)','cos(2$\pi$t)'])

#Show the plot
plt.show()
