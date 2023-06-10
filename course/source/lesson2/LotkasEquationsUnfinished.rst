
##############################################################################
# A look at Lotka's orginal article
# ----------------------------------
# To find the exact shape of this rotation, we can use a trick that Lotka 
# described in an article he wrote in 1920. By dividing the rabbit equation by the fox equation he got 
#
# .. math::
# 
#    \frac{dR}{dF} = \frac{aR -bRF}{cRF - d F}  
#
# We can then rearrange this equation to get 
# 
# .. math::
# 
#    \left(c -d/R \right) dR = \left(a/F -b \right) dF 
# 
# Integrating both sides ofthis equation we get 
#
# .. math::
# 
#    cR -d\log(R) = a \log(F) - b F + C
# 
# where :math:`C`  is the constant of integration. This last equation tells us a relationship that 
# must always hold between rabbits and foxes. To understand what the relationship implies, 
# imagine  the equation above was simply :math:`Y+X=C`  instead. This would imply the total number of 
# rabbits and foxes is equal to C=10. So, if :math:`C=10` then we could have :math:`Y=3` foxes and :math:`X=7` 
# rabbits (because 3+7=10), 
# or 6 foxes and 4 rabbits (because 6+4=10), but we couldn’t have :math:`Y=6` foxes and :math:`X=7` rabbits (because 6+7≠10). 
# In our case, the relationship in the equation is more complicated, involving logarithms, 
# but the idea is the same: for any particular value of C 
# all values of  X and Y must obey the equation
#
# .. math::
# 
#    C = cR + b F -d\log(R) - a \log(F) 
# 
# Imagine for example, we started with R=4 rabbits and F=6 foxes. 
# This gives 
# 
# .. math::
# 
#    C = c4 + b6 - d\log(4) - a \log(6) 