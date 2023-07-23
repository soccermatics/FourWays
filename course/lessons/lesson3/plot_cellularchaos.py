"""
.. _cellularchaos:

Cellular chaos
==============

In Santa Fe, Esther shows how to write rule tables for cellular automata.

.. image:: ../../images/lesson3/EstherRules.png

The figure below shows how these rules result in a chequerboard pattern.

.. image:: ../../images/lesson3/EstherRules.png

The top of the figure shows the rules, then the pattern underneath is each time step 
of the cellular automata. 

On this page we will implement a cellular automata that takes in a set of rules and 
outputs a pattern.

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
    
    
    # Create a dictionary for mapping inputs to outputs 
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
# We can write Esther's rule in the form of the outputs it produces for 
# a particular input. So '1' when the input is '111', '0' when the input is '110' and
# so on.
# 
# We then run the rule for 30 steps for a single black cell, with all other cells white.

rule = [1, 0, 1, 1, 0, 0, 1, 0] 
size = 50
steps = 30

generate_ca(rule, steps,size=size,print_output=1)


##############################################################################
# In Santa Fe, David finds the following rules, which make a fractal like pattern.
# 
# .. image:: ../../images/lesson3/DavidFractal.png
#
# Let's simulate this rule and we chould get the same pattern.

rule = [0, 0, 0, 1, 0, 1, 1, 0] 
size = 50
steps = 30

generate_ca(rule, steps,size=size,print_output=1)

##############################################################################
# The random rule which David discovers is illustrated below.
#
# .. image:: ../../images/lesson3/DavidRandom.png
# 
# Let's simulate this now. We use this function to calculate the middle
# column. The middle string printed below is the column starting at 
# the single 1 in the middle and then going down from there.

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
# The method to generate random numbers from the cellular automata is
# to first run a size 20 cellular automata for 20 steps....

rule = [0, 0, 0, 1, 1, 1, 1, 0] 
size = 20
steps = 20

middle_string = generate_ca(rule, steps,size=size,print_output=1)

print('\n')
print('The middle string is: ' + middle_string)


##############################################################################
# We can then convert the output number to a decimal.

def string_to_decimal(string):

    decimal=np.array(0)
    for i,c in enumerate(list(map(int, [*string]))):
        decimal=decimal + c*np.power(np.array(2, dtype=np.float128),-np.array(i+1, dtype=np.float128)) 

    return decimal

decimal=string_to_decimal(middle_string)
print('In decimal form this is: %f\n'%decimal)


##############################################################################
# 
# We then rerun the cellular automata with the middle string as input for 
# the first row of the cellular automata to get a new middle string.
#

middle_string = generate_ca(rule, steps, input_string=middle_string,print_output=1)

print('\n')
print('The middle string is: ' + middle_string)
decimal=string_to_decimal(middle_string)
print('In decimal form this is: %f\n'%decimal)


##############################################################################
# 
# And then we do the same thing again
#

middle_string = generate_ca(rule, steps, input_string=middle_string,print_output=1)

print('\n')
print('The middle string is: ' + middle_string)
decimal=string_to_decimal(middle_string)
print('In decimal form this is: %f\n'%decimal)


##############################################################################
# 
# Now lets repeat this without printing out the whole cellular automata,
# just collecting up the output numbers in a list. 
#
# These numbers are random.
#

random_decimals=[]
N=100

for i in range(N):
    middle_string = generate_ca(rule, steps, input_string=middle_string,print_output=0)
    random_decimals.append(string_to_decimal(middle_string))

print(random_decimals)



##############################################################################
# 
# To see this more clearly, lets make these in to a graph over time
# of the output numbers.
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
# And finally let's make histograms. First for the 100 times we have just run.
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



##############################################################################
# 
# This is a uniform random distribtion of numbers, i.e. all outputs between
# 0 and 1 are equally likely.
#
# Further reading
# ---------------
#
# ADD REFENCES HERE.