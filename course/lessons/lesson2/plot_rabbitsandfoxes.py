"""
.. _rabbitsandfoxes:

Rabbits and foxes
=================


Differential equations
----------------------

In the book, I write Lotka's equations in the form of chemical reactions, 
e.g. 

.. math::
   
   \mbox{F} +  \mbox{R} \\rightarrow 2 \mbox{F} 

This means that an F and R together becomes two F's. Parker expalins as follows,

IMAGE FROM BOOK HERE

While in Leipzig, A. J. Lotka learnt how chemical reactions can be used to 
specify the rate of change of populations, i.e. in terms of the derivates 
above, using an approach, known as the law of mass action. 
The idea is to think about the rate at which these chemical reactions take place. 
For the first reaction 

.. math::
   
   \mbox{R} \\xrightarrow{a} 2 \mbox{R} 

We can think of :math:`a` as being the rate of reproduction of the rabbits, 
how many baby rabbits an adult rabbit has per day. So, the rabbits grow 
according to 

.. math::
   :label: rabbitgrow

   \\frac{dR}{dt} = a R 
   
This equation denotes the rate of change of :math:`R` over time. 
the top part of the fraction :math:`dR` denotes the change in rabbits, :math:`R`, 
and the bottom part, :math:`dt`, denotes the change in time, :math:`t`. 

This type of equation, known as a differential equation can appear a bit strange 
the first rime we encounter it. When we first meet differntiation in school
we write, for example,

.. math::
   :label: timeint

   R(t) = \\frac{1}{2} a t^2


then take the derivative to get 

.. math::
   :label: timegrow
 
   \\frac{dR}{dt} = a t

  
This is also a differential equation. It says that the rate of change of :math:`R` over time
is proportional to time. The modelling difference between equation :eq:`timegrow` and 
:eq:`rabbitgrow` is that the former says that rabbits grow proportionally to time, while
the latter says that rabbits grow proportionally to the number of rabbits. In the case that
rabbits grow in proportion to time, then we say that :eq:`timeint` is the solution to 
equation :eq:`timegrow` since it tells us how many rabbits there 
will be at any point in time. I think this is where differential equations can be a bit
confusing, because in school we are usually given :eq:`timeint` and asked to find :eq:`timegrow`. 
For most differential equations it is the other way round. We are given equation :eq:`rabbitgrow` 
and asked to find the the number of rabbits :math:`R` as a function of time. 

We aren't going to solve these equations yet. First we need to have the equations for foxes. In chemical 
reaction form these are,

.. math::
      \mbox{F} +  \mbox{R} \\xrightarrow{b}  2 \mbox{F} 

for foxes eating rabbits and

.. math::
      \mbox{F}   \\xrightarrow{d}  \mbox{D} 
   
for foxes dying. Converted to differential equations, the rate of change for rabbits becomes

.. math::
 
   \\frac{dR}{dt} = \\underbrace{a R}_{\mbox{R} \\xrightarrow{a} 2 \mbox{R}} - \\underbrace{b R F}_{\mbox{F} + \mbox{R} \\xrightarrow{b} 2 \mbox{F}}

Similarly, we can write the rate of change of foxes as 

.. math::
 
   \\frac{dF}{dt} =  \\underbrace{c R F}_{\mbox{F} + \mbox{R} \\xrightarrow{c} 2 \mbox{F}} - \\underbrace{d R}_{\mbox{R} \\xrightarrow{d} 2 \mbox{R}}

Notice that we have a different rate parameter for the death of rabbits (:math:`b`) 
than for the birth of foxes (:math:`c`). This is because
it takes more than one rabbit to feed a fox and we set the parameters so that :math:`c<b`.

It may seem strange to treat rabbits and foxes as chemicals.  
As we all know, two rabbits are needed to produce baby rabbits and when a fox eats a rabbit, 
it doesn’t simply transform it directly in to a new fox, as the chemical equation suggests. 
Also, in the description above, the grass is not depleted: there is no chemical equation 
describing how grass is transformed to rabbit poop. But the point of a mathematical model 
like this is not to be entirely realistic. Rather, it tries to capture the essence of the problem. 
We want to imagine a big grassy meadow, where the more rabbits there are, the faster the rabbit 
population grows and the more foxes there are the faster the rabbits are eaten. We will try to 
understand this abstract problem first, before we make any claims about what happens to real 
rabbits and real foxes. 

"""



##############################################################################
# Simulating the model
# --------------------
# Let's do ..

import numpy as np



x=np.zeros(1)
