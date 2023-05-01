"""
Cellular automata
=================



The domino rule
---------------

"""

def apply_domino(string):

    # Convert the strong to cells 
    cells=list(map(int, [*string]))
    new_cells=cells.copy()
    N=len(cells)
    
    # Loop over every cell and update its state based on the neighboring cells
    for j in range(N):
        # Get the neighbors left, above and right.
        # The %N is to take mod, to deal with the edge cases
        left = cells[(j-1)%N]
        above = cells[j]
        right= cells[(j+1)%N]
        
        
        # If the cell to the left is a 1 then the cell becomes a 1
        # Otherwise it remains the same.
        if left==1:
            new_cells[j] = 1
        else:
            new_cells[j]=cells[j]
        
    # Convert back to a new string    
    string=''.join([str(item) for item in new_cells])
    
    return string



##############################################################################
# Let's now apply the rule


string='11101100001111000011111111101'
print('Before applying rule: ' + string)
string=apply_domino(string)
print('After applying rule : ' + string)


##############################################################################
# We can repeadtedly apply the rule as follows:

steps = 5
string='11101100001111000011111111101'


for i in range(steps):
    print('Time step %d:'%i + string)
    string=apply_domino(string)
    


##############################################################################
# The politics rule
# -----------------


def apply_political(string):

    # Convert the strong to cells 
    cells=list(map(int, [*string]))
    new_cells=cells.copy()
    N=len(cells)
    
    # Loop over every cell and update its state based on the neighboring cells
    for j in range(N):
        # Get the neighbors left, above and right.
        # The %N is to take mod, to deal with the edge cases
        left = cells[(j-1)%N]
        above = cells[j]
        right= cells[(j+1)%N]
        
        
        # If the cell to the left is a 1 then the cell becomes a 1
        # Otherwise it remains the same.
        if ((left==0) & (right==0)):
            new_cells[j] = 0
        elif ((left==1) & (right==1)):
            new_cells[j] = 1
        else:
            new_cells[j]=cells[j]
        
    # Convert back to a new string    
    string=''.join([str(item) for item in new_cells])
    
    return string

##############################################################################
# Let's now apply the rule

string='0100011011110101011010'
print('Before applying rule: ' + string)
string=apply_political(string)
print('After applying rule : ' + string)


##############################################################################
# We can repeadtedly apply the rule as follows:

steps = 5
string='0100011011110101011010'


for i in range(steps):
    print('Time step %d:'%i + string)
    string=apply_political(string)
    


##############################################################################
# The alternate rule
# -----------------

def apply_alternate(string):

    # Convert the strong to cells 
    cells=list(map(int, [*string]))
    new_cells=cells.copy()
    N=len(cells)
    
    # Loop over every cell and update its state based on the neighboring cells
    for j in range(N):
        # Get the previous value

        above = cells[j]
        
        # Switch the value of the cell on every time step
        if (above==1):
            new_cells[j] = 0
        else:
            new_cells[j] = 1
        
    # Convert back to a new string    
    string=''.join([str(item) for item in new_cells])
    
    return string


##############################################################################
# We can repeadtedly apply the rule as follows:

steps = 20
string='01110111001100110110'


for i in range(steps):
    print(string)
    string=apply_alternate(string)
    
    
    

##############################################################################
# The checquerboard rule
# ---------------------

def apply_checquerboard(string):

    # Convert the strong to cells 
    cells=list(map(int, [*string]))
    new_cells=cells.copy()
    N=len(cells)
    
    # Loop over every cell and update its state based on the neighboring cells
    for j in range(N):
        # Get the previous value

        left = cells[(j-1)%N]
        above = cells[j]
        right= cells[(j+1)%N]
         
        # Switch the value of the cell on every time step
        if (above==1):
            if ((left==1) & (right==1)):
                new_cells[j] = 1
            else:
                new_cells[j] = 0
        else:
            if ((left==0) & (right==0)):
                new_cells[j] = 0
            else:
                new_cells[j] = 1
                
                
    # Convert back to a new string    
    string=''.join([str(item) for item in new_cells])
    
    return string


##############################################################################
# We can repeadtedly apply the rule as follows:

steps = 20
string='10000001110000000011'

for i in range(steps):
    print(string)
    string=apply_checquerboard(string)
    
