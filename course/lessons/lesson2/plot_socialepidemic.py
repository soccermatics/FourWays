"""
.. _socialepidemic:

The social epidemic
===================

In this section we go on to solve some more differential equations which describe rules of
interaction. Here I assume you have already worked through and understood 
the section on :ref:`predator prey models<rabbitsandfoxes>`. 

In the book I first introduce the SIR model of disease spread, by looking at infections.

.. image:: ../../images/lesson2/Epidemic1.png

Then I discuss recoveries.

.. image:: ../../images/lesson2/Epidemic2.png

Let's turn these rules of interaction in to differential equations and analyse how they describe
disease spread.


The SIR model
-------------
  
In terms of differential equations, the rate of change of susceptible individuals is

.. math::
   :label: susc
 
   \\frac{dS}{dt} = \\underbrace{-b S I }_{\mbox{I} + \mbox{S} \\xrightarrow{b} 2 \mbox{I}}

and the rate of change of infectives is 

.. math::
   :label: infect
 
   \\frac{dI}{dt} = \\underbrace{b S I }_{\mbox{I} + \mbox{S} \\xrightarrow{b} 2 \mbox{I}} - \\underbrace{c I }_{\mbox{I} \\xrightarrow{c} \mbox{R}} 

The constant :math:`b` is the rate of contact between people and :math:`c` is the rate of recovery.
We can also write down an equation for recovery as follows,

.. math::
   :label: recover
 
   \\frac{dR}{dt} = \\underbrace{c I }_{\mbox{I} \\xrightarrow{c} \mbox{R}} 

In this model :math:`S`, :math:`I` and :math:`R` are proportions of the population. Summing them up gives :math:`S+I+R=1`, since 
everyone in the popultaion is either susceptible, infective or recovered.

Let's now solve these equations numerically. We start by importing the libraries we need from Python.

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pylab import rcParams
matplotlib.font_manager.FontProperties(family='Helvetica',size=11)
rcParams['figure.figsize'] = 9/2.54, 9/2.54
from scipy import integrate


##############################################################################
# Now we define the model. This code creates a function 
# which we can use to simulate differential equations :eq:`susc` and :eq:`infect`. 
# We also define the parameter values. You can change these to see how
# changes to the paramaters leads to changes in the outcome of the model. 

# Parameter values
b = 3.5
c = 1

# Differential equation
def dXdt(X, t=0):
    # Growth rate of fox and rabbit populations.
    return np.array([  - b*X[0]*X[1] ,      #Susceptible X[0] is S
                      b*X[0]*X[1]   - c*X[1],      #Infectives X[1] is I
                      c*X[1]])                     #Recovered X[2] is R


##############################################################################
# We solve the equations numerically and plot solution over time. 

def plotEpidemicOverTime(ax,S,I,R):

    ax.plot(t, S, '-',color='k', label='Suceptible (S)')
    ax.plot(t, I  , '--',color='k', label='Infectives (I)')
    ax.plot(t, R  , '--',color='k', label='Recovered (R)')
    ax.legend(loc='best')
    ax.set_xlabel('Time: t')
    ax.set_ylabel('Population')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,20,step=2))
    ax.set_yticks(np.arange(0,1.01,step=0.5))
    ax.set_xlim(0,20)
    ax.set_ylim(0,1) 
    

t = np.linspace(0, 20,  1000)               # time
X0 = np.array([0.9999, 0.0001,0.0000])      # initially 99.99% are uninfected
X = integrate.odeint(dXdt, X0, t)           # uses a Python package to simulate the interactions
S, I, R = X.T
fig,ax=plt.subplots(num=1)
plotEpidemicOverTime(ax,S,I,R)
plt.show()

# .. admonition:: Think yourself!
#   
#     When :math:`b=1`, for what values of :math:`c` does the number of infectives  
#     always decrease? Try changing the initial number of infectives to :math:`0.5`.
#     Now find values of :math:`c` where the number of infectives  
#     always decreases? 



##############################################################################
# As with the  :ref:`precator prey model<rabbitsandfoxes>` we can find
# the equilibria where the rate at which people become infected equals the 
# rate at which they recover by solving
# 
# .. math::
# 
#   \\frac{dI}{dt} = b S I - c I =0  
#
# This occurs either when :math:`I=0` (no-one has the disease) or 
# when :math:`S=c/b`. We can now plot these equilibrium on the phase plane
# 

def plotPhasePlane(ax,S,I):
    ax.plot(S, I, '-',color='k')
    ax.set_xlabel('Susceptibles: S')
    ax.set_ylabel('Infectives: I')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks(np.arange(0,1.01,step=0.5))
    ax.set_yticks(np.arange(0,1.01,step=0.5))
    ax.set_ylim(0,1)   
    ax.set_xlim(0,1) 

def drawArrows(ax,dXdt):
    x = np.linspace(0.05, 1 ,6)
    y = np.linspace(0.05, 1, 6)
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


##############################################################################
# The solution to :math:`S=c/b` is known as herd immunity. When :math:`S>c/b` 
# then the number of infectives increase. So when :math:`S=0.9999` then if
# :math:`b>0.9999c` then the infection increases and when 
# :math:`b<0.9999c` then the infection decreases. Simiarly, when :math:`S=0.5`then if
# :math:`b>0.5c` then the infection increases and it decreases when 
# :math:`b<0.5c`.



##############################################################################
# Social recovery
# ---------------
# For many social behaviours, it isn’t just the adoption of a fad or a news cycle that 
# is contagious, but also the way in which we recover. When we get a cold, flu or Covid-19, 
# the best thing to do is to go home, rest and not spread the virus. Spending time with people 
# who have already been ill doesn’t help us recover more quickly (even if their sympathy might 
# help us feel a bit better). Recovery is independent between individuals. In the book, I look at
# social recovery, when it depends on how many are recovered.
#
# .. image:: ../../images/lesson2/SocialEpidemic.png
#
# In terms of differential equations, the rate of change of susceptible individuals 
# remains the same as before
#
# .. math::
#
#    \frac{dS}{dt} = \underbrace{-b S I }_{\mbox{I} + \mbox{S} \xrightarrow{b} 2 \mbox{I}}
#
# but the rate of change of infectives is now
#
# .. math::
# 
#    \frac{dI}{dt} = \underbrace{b S I }_{\mbox{I} + \mbox{S} \xrightarrow{b} 2 \mbox{I}} - \underbrace{c I }_{\mbox{I} \xrightarrow{c} \mbox{R}} - \underbrace{d I R }_{\mbox{I} + \mbox{R}  \xrightarrow{d} 2 \mbox{R}} 
#
# The constant :math:`b` is the rate of contact between people and :math:`c` is the rate of contact between infectives and recovered individuals.
# We can also write down an equation for recovery as follows,
#
# .. math::
# 
#    \frac{dR}{dt} = \underbrace{c I }_{\mbox{I} \xrightarrow{c} \mbox{R}} + \underbrace{d I R }_{\mbox{I} + \mbox{R}  \xrightarrow{d} 2 \mbox{R}} 
#
# In Python these equations are written as follows.

# Parameter values
b = 3.5
c = 1
d = 1

# Differential equation
def dXdt(X, t=0):
    # Growth rate of fox and rabbit populations.
    return np.array([  - b*X[0]*X[1] ,      #Susceptible X[0] is S
                      b*X[0]*X[1]   - c*X[1] - d*X[1]*X[2],      #Infectives X[1] is I
                      c*X[1] + d*X[1]*X[2]])                     #Recovered X[2] is R

t = np.linspace(0, 20,  1000)               # time
X0 = np.array([0.9999, 0.0001,0.0000])      # initially 99.99% are uninfected
X = integrate.odeint(dXdt, X0, t)           # uses a Python package to simulate the interactions
S, I, R = X.T
fig,ax=plt.subplots(num=1)
plotEpidemicOverTime(ax,S,I,R)
plt.show()


##############################################################################
# Again, we can find the equilibria where the rate at which people become infected equals the 
# rate at which they recover by solving
# 
# .. math::
# 
#    \frac{dI}{dt} = b S I - c I - d I (1- S -I) =0  
#
# This occurs either when :math:`I=0` (no-one has the disease) or 
#
# when 
#
# .. math::
# 
#    b S I = c I + d I - d S I - dI^2 
#
#
# or, equivalently,
#
# .. math::
# 
#    (b + d) SI = (c+d) I  - d I^2
#
# or
# .. math::
# 
#    S = \frac{c+d}{b+d} - \frac{d}{b+d} I
#
# We can now plot these equilibrium on the phase plane
# 

I_equilibrium = np.linspace(0, 1,  1000)               
S_equilibrium = (c+d)/(b+d) - (d/(b+d))*I_equilibrium     

fig,ax=plt.subplots(num=1)
ax.plot(S_equilibrium,I_equilibrium,linestyle=':',color='k')
plotPhasePlane(ax,S,I)

X0 = np.array([0.6999, 0.0001,0.3])      # initially 99.99% are uninfected
X = integrate.odeint(dXdt, X0, t)           # uses a Python package to simulate the interactions
S, I, R = X.T
plotPhasePlane(ax,S,I)

drawArrows(ax,dXdt)

plt.show()


##############################################################################
#
# Examples of social epidemics
# ----------------------------
#
# The following references describe social contagion using models similar to the one we 
# have seen in this section to explain donations, laughter, applause, dog breeds, smoking, alchohol usage
# and even divorce.
#
# `Frank Schweitzer and Robert Mach, ‘The epidemics of donations: logistic growth
# and power-laws’, PLoS One 3, no. 1 (2008): e1458 <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0001458>`_
#
# `Sarah Seewoester Cain, ‘When laughter fades: individual participation during open-mic comedy performances’, PhD dissertation, Rice Univer- sity, 2018 <https://scholarship.rice.edu/bitstream/handle/1911/105806/CAIN-DOCUMENT-2018.pdf?sequence=1>`_
#
# `Richard P. Mann et al., ‘The dynamics of audience applause’, Journal of the Royal Society Interface 10, no. 85 (2013): 20130466 <https://royalsocietypublishing.org/doi/full/10.1098/rsif.2013.0466>`_
# 
# `Harold Herzog, ‘Forty-two thousand and one Dalmatians: fads, social contagion, and dog breed popularity’, Society and Animals 14, no. 4 (2006): 383‒97 <https://brill.com/downloadpdf/journals/soan/14/4/article-p383_3.pdf?casa_token=C2H6lT2hut4AAAAA:qyexw8uGG1Iip3pXxKQoBp5CFLP3AGnkh0W95xiRbKB7aOkcJiTITcvDWPWJdbKvAgc2i74>`_
# 
# `Nicholas A. Christakis, and James H. Fowler, ‘Social contagion theory: examining dynamic social networks and human behavior’, Statistics in Medicine 32, no. 4 (2013): 556‒77 <https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=0e249d965290fc3c6dd0cf264a002946d7e10dea>`_
#
# `Yvonne Aberg, ‘The contagiousness of divorce’, The Oxford Handbook of Analytical Sociology (2009): 342‒64 <https://academic.oup.com/edited-volume/38173/chapter-abstract/333033850?redirectedFrom=fulltext>`_
#
# .. admonition:: Think yourself!
#   
#     What aspects of your interactions with others do you think are dominated by social contagion?
#     Write a short list and think back to it next time you find yourself caught up in the crowd.
#     Social contagion can be a force for both good and bad.  
 