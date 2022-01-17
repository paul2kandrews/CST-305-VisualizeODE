# Brett Silvey & Paul Andrews
# CST-305
# Visualize ODE with Scipy
# We certify that this is our own work and the code for the project is our own.

import numpy as np   # import numpy for array space
from scipy.integrate import odeint  # will return the value of the derivative of the function
import matplotlib.pyplot as plt # allows for function to be plotted

# function that returns db/dr
def model(F, res, band, pix):
    dfdr = -band / ((res * pix)**2) # derivative of the original function
    return dfdr

F0 = 50 # set initial value of graph
samples = 50 # set number of samples we want on the x-axis
res_s = np.linspace(1024*576,2160*3840, samples) # set the range of the x-axis a.k.a resolution space

pix = 24 # set color depth a.k.a. bits per pixel

band = 2 * 10**9 # set signal bandwith in Gbps
F2 = odeint(model, F0, res_s, args=(band, pix,)) # solve the ODE
plt.plot(res_s,F2,'r-',linewidth=2,label=f'Bandwidth   = {band * 1*10**-9} Gbps\nColor Depth = {pix} bits') # plot the result

band = 1 * 10**9 # set signal bandwith in Gbps
F1 = odeint(model, F0, res_s, args=(band, pix,)) # solve the ODE
plt.plot(res_s,F1,'g-',linewidth=2,label=f'Bandwidth   = {band * 1*10**-9} Gbps\nColor Depth = {pix} bits') # plot the result

band = 0.5 * 10**9 # set signal bandwith in Gbps
F3 = odeint(model, F0, res_s, args=(band, pix,)) # solve the ODE
plt.plot(res_s,F3,'b-',linewidth=2,label=f'Bandwidth   = {band * 1*10**-9} Gbps\nColor Depth = {pix} bits') # plot the result

plt.xlabel('Resolution (total pixel count)') # label the x-axis
plt.ylabel('Frame Rate (frames/second)') # label the y-axis
plt.title('Frame Rate vs. Resolution') # label the graph
plt.legend() # show the legend
plt.show() # render the graph