"""
.. _cellularchaos:

Cellular chaos
==============

"""

import numpy as np


def generate_ca(rule, steps, input_string='', size=50,print_output=1):
    # Initialize the list of cells with a single "on" cell in the middle
    if input_string=='':
        cells = [0] * size
        cells[size // 2] = 1
    else:
        cells=list(map(int, [*input_string]))
        size=len(input_string)
    
    #Store the middle column
    middle_column=[cells[size // 2]]
    
    
    # Create a dictionary for mapping inputs to outpute 
    patterns = {
        (1, 1, 1): rule[0],
        (1, 1, 0): rule[1],
        (1, 0, 1): rule[2],
        (1, 0, 0): rule[3],
        (0, 1, 1): rule[4],
        (0, 1, 0): rule[5],
        (0, 0, 1): rule[6],
        (0, 0, 0): rule[7]
    }
    
    # Generate the specified number of steps
    for i in range(steps):
        # Copy the current state of the cells
        new_cells = [0] * size
        
        # Loop over every cell and update its state based on the neighboring cells
        for j in range(size):
            # Get the pattern of the cell and its neighbors
            if j == 0:
                pattern = (cells[size-1], cells[0], cells[1])
            elif j == size-1:
                pattern = (cells[size-2], cells[size-1], cells[0])
            else:
                pattern = (cells[j-1], cells[j], cells[j+1])
            
            # Update the cell's state based on the pattern
            new_cells[j] = patterns[pattern]
        
        string=''.join([str(item) for item in cells])
        if print_output:
            print(string)
        
        # Update the cells with the new state
        cells = new_cells
    
        # Update middle column
        middle_column.append(cells[size // 2]) 
    
    middle_string = ''.join([str(item) for item in middle_column])
    
    # Return the final state of the cells
    return middle_string

##############################################################################
# We can rewrite Esther's rule in the form of the outputs it produces for 
# a particular output.

rule = [1, 0, 1, 1, 0, 0, 1, 0] 
size = 50
steps = 30

generate_ca(rule, steps,size=size,print_output=1)


##############################################################################
# The fractal generating rule is

rule = [0, 0, 0, 1, 0, 1, 1, 0] 
size = 50
steps = 30

generate_ca(rule, steps,size=size,print_output=1)

##############################################################################
# The random rule is

rule = [0, 0, 0, 1, 1, 1, 1, 0] 
size = 50
steps = 30

middle_string = generate_ca(rule, steps,size=size,print_output=1)

print('\n')
print('The middle string is: ' + middle_string)

##############################################################################
# Random number generators
# ------------------------
#
# First we run the cellular automata for 20 steps 

rule = [0, 0, 0, 1, 1, 1, 1, 0] 
size = 20
steps = 20

middle_string = generate_ca(rule, steps,size=size,print_output=1)

print('\n')
print('The middle string is: ' + middle_string)


##############################################################################
# Convert to decimal number

def string_to_decimal(string):

    decimal=np.array(0)
    for i,c in enumerate(list(map(int, [*string]))):
        decimal=decimal + c*np.power(np.array(2, dtype=np.float128),-np.array(i+1, dtype=np.float128)) 

    return decimal

decimal=string_to_decimal(middle_string)
print('In decimal form this is: %f\n'%decimal)



##############################################################################
# 
# Then we rerun it with the middle string as input
#

middle_string = generate_ca(rule, steps, input_string=middle_string,print_output=1)

print('\n')
print('The middle string is: ' + middle_string)
decimal=string_to_decimal(middle_string)
print('In decimal form this is: %f\n'%decimal)


##############################################################################
# 
# And again
#

middle_string = generate_ca(rule, steps, input_string=middle_string,print_output=1)

print('\n')
print('The middle string is: ' + middle_string)
decimal=string_to_decimal(middle_string)
print('In decimal form this is: %f\n'%decimal)


##############################################################################
# 
# Now lets repeat this without printing out the whole cellular automata
#

random_decimals=[]
N=100

for i in range(N):
    middle_string = generate_ca(rule, steps, input_string=middle_string,print_output=0)
    random_decimals.append(string_to_decimal(middle_string))

print(random_decimals)



##############################################################################
# 
# Lets make these in to a graph over time
#

import matplotlib.pyplot as plt
from pylab import rcParams
import matplotlib
rcParams['figure.figsize'] = 12/2.54, 6/2.54
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)

def formatFigure(ax,N):
    ax.set_ylabel('Number')
    ax.set_xlabel('Step')
    ax.set_ylim((0,1))
    ax.set_xlim((0,N))
    ax.set_xticks(range(0,N+1,10))
    ax.set_yticks(range(0,1,5))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

fig,ax=plt.subplots(num=1)
ax.plot(random_decimals, color='black')
formatFigure(ax,N)
plt.show()


##############################################################################
# 
# Lets make histograms
#

rcParams['figure.figsize'] = 12/2.54, 9/2.54

def formatHist(ax,N):
    ax.set_ylim(0,N/5) 
    ax.set_xlim(0.049,1.052) 
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylabel('')
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    ax.set_xticks(np.arange(0.1,1.1,step=0.1)) 
    ax.set_xticklabels(ax.get_xticks(), rotation = 90)
    ax.set_xticklabels(['0.0 to 0.1','0.1 to 0.2','0.2 to 0.3','0.3 to 0.4','0.4 to 0.5','0.5 to 0.6','0.6 to 0.7','0.7 to 0.8','0.8 to 0.9','0.9 to 1.0'])
 
fig,ax=plt.subplots(num=1)
ax.hist(random_decimals, np.arange(0.0,1.01,0.1), color='orange', edgecolor = 'black',linestyle='-',alpha=0.5, density=False, align='right')
formatHist(ax,N)

plt.show()


##############################################################################
# 
# And now lets repeat it 2000 times.
#

random_decimals=[]
N=2000

for i in range(N):
    middle_string = generate_ca(rule, steps, input_string=middle_string,print_output=0)
    random_decimals.append(string_to_decimal(middle_string))

fig,ax=plt.subplots(num=1)
ax.hist(random_decimals, np.arange(0.0,1.01,0.1), color='orange', edgecolor = 'black',linestyle='-',alpha=0.5, density=False, align='right')
formatHist(ax,N)

plt.show()


