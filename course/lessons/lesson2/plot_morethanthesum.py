"""
.. _morethanthesum:

More Than The Sum of Its Parts
==============================

FROM BOOK

The model
---------
 
"""



import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import rcParams
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)
rcParams['figure.figsize'] = 9/2.54, 6/2.54
from scipy import integrate


# Parameter values
b = 3.5
c = 1

def dXdt(X, t=0):
    # Growth rate of fox and rabbit populations.
    return np.array([  - c*X[0]*X[1] ,      #Susceptible X[0] is S
                      c*X[0]*X[1]   - b*X[1],      #Infectives X[1] is I
                      b*X[1]])                     #Recovered X[2] is R


def plotEpidemicOverTime(ax,S,I,R):

    ax.plot(t, S, '-',color='k', label='Suceptible (S)')
    ax.plot(t, I  , '--',color='k', label='Infectives (I)')
    ax.plot(t, R  , '--',color='k', label='Recovered (R)')
    ax.legend(loc='best')
    ax.set_xlabel('Time: t')
    ax.set_ylabel('Population')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,12,step=1))
    ax.set_yticks(np.arange(0,50,step=10))
    ax.set_xlim(0,12)
    ax.set_ylim(0,25) 
    plt.show()

t = np.linspace(0, 20,  1000)               # time
X0 = np.array([0.9999, 0.0001,0.0000])                     # initially 99.99% are uninfected
X = integrate.odeint(dXdt, X0, t)
S, I, R = X.T
fig,ax=plt.subplots(num=1)
plotEpidemicOverTime(ax,S,I,R)

##############################################################################
# We can find
# the equilibria where the rate at which people become infected equals the 
# rate at which they recover by solving
# 
# .. math::
# 
#   \\frac{dI}{dt} = b S I^2 - c I = 0  
#
# This occurs either when :math:`I=0` (no-one has the disease) or 
# when 
# .. math::
# 
#   S = \\frac{c}{bI} 
# 


def plotPhasePlane(ax,S,I):
    ax.plot(S, I, '-',color='k')
    ax.set_xlabel('Suceptible: S')
    ax.set_ylabel('Infectives: I')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,30,step=5))
    ax.set_yticks(np.arange(0,20,step=5))
    ax.set_ylim(0,12)   
    ax.set_xlim(0,30) 

def drawArrows(ax,dXdt):
    x = np.linspace(1, 30 ,6)
    y = np.linspace(1, 12, 5)
    X , Y  = np.meshgrid(x, y)
    dX, dY, dZ = dXdt([X, Y,1-X-Y]) 
    #Make in to unit vectors. 
    M = np.hypot(dX,dY)
    dX = dX/M
    dY = dY/M
    ax.quiver(X, Y, dX, dY, pivot='mid')


fig,ax=plt.subplots(num=1)
ax.plot([c/b,c/b],[-100,100],linestyle=':',color='k')
plotPhasePlane(ax,S,I)
drawArrows(ax,dXdt)
plt.show()