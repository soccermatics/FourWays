"""
All of the life
===============


"""

import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 12/2.54, 2/2.54

##############################################################################
#
# First we set up functions which allow us to run sellular automata.

def show_grid(ax,grid,make_animation):
        if make_animation:
            frame = ax.imshow(grid, cmap=plt.get_cmap('Blues'), interpolation='nearest',animated=True)
        else:
            frame = ax.imshow(grid, cmap=plt.get_cmap('Blues'), interpolation='nearest')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.set_ylim(0,N)
        ax.set_xlim(0,N)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axis('equal')
        
        return frame
	
def iterate(grid):
    N=np.size(grid,1)
    new_grid = np.zeros((N, N), dtype="int")
    for i in range(N):
        for j in range(N):
            new_grid[i,j]=new_value(i, j,grid)
    return new_grid, grid
 

##############################################################################
# Set up the rules
# ----------------
#
# Now we set up the cellular automata 
#

def new_value(i, j,grid):
	
    neighbours = grid[i, (j-1)%N] + grid[i, (j+1)%N] + grid[(i-1)%N, j] + grid[(i+1)%N, j] +grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] + grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]
    
    # Apply rules
    if grid[i, j]  == 1:
        if (neighbours < 2) | (neighbours > 3):
            return 0
    else:
        if neighbours == 3:
            return 1
        
    return grid[i, j]


#############################################################################
#
# Now we set up the initial shape the model printing out every step
#


def initialize(grid):
    init_pattern = ["111",
			"001",
			"010"]
    for i, line in enumerate(init_pattern):
	    for j, char in enumerate(line):
		    grid[i+int(N/2)-2, j+int(N/2)-2] = int(char)
    return grid

N=8
STEPS = 10

grid = np.zeros((N, N), dtype="int")
grid = initialize(grid)

#############################################################################
#
# Now simulate
#


fig,axs=plt.subplots(1,STEPS)
for step in range(STEPS):
    grid, old_grid = iterate(grid) # Iterate & swap the two grids
    show_grid(axs[step],old_grid,0)

    
plt.show()



##############################################################################
# Animate the game of life on a larger grid

import matplotlib.animation as animation

rcParams['figure.figsize'] = 12/2.54, 12/2.54

make_animation=0

N=40
STEPS = 400


if make_animation:
    grid = np.random.choice([0, 1], size=(N,N), p=[1./3, 2./3])

    img = [] # some array of images
    frames = [] # for storing the generated imagesfig, ax = plt.subplots()
    fig,ax=plt.subplots(1)
    for step in range(STEPS):
        grid, old_grid = iterate(grid) # Iterate & swap the two grids
        im = show_grid(ax,old_grid,1)
        frames.append([im])


    ani = animation.ArtistAnimation(fig, frames, interval=50, blit=True,
                                repeat_delay=1000)

    # set output file
    writer = animation.FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    ani.save("Game_of_life_movie.mp4", writer=writer)


##############################################################################
# Here is a video of the output of this function.
#
# ..  youtube:: JoJck23OR38
#   :width: 640
#   :height: 349
