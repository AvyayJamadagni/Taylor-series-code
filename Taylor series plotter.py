'''
INFORMATION ABOUT THIS PROGRAM:

This program graphically shows a desired number of orders of a Taylor series at a point on a function of your choice. 
It uses a forward-finite difference approach to calculate the derivatives needed to compute the Taylor series. After analyzing
the formulae for higher order forward finite differences, it was noted that the coefficients of the terms are binomial. Using 
FOR loops, each term in the numerator of the forward finite difference is calculated, and then the forward finite difference
is calculated by summing these terms and dividing by the step size, h. This approximation for the derivative is then used to 
calculate each term in the Taylor series, and then increasing orders of the Taylor series are graphed.

INSTRUCTIONS:

First input the step size, function, and desired number of orders in the relevant fields below. Then, run the code
and in the terminal, state if you wish to input the exact value of the point of interest, or would like to choose one from the graph.

If you choose to select a point from the graph, when the graph appears, click on the point on the line where you would like
the Taylor series to be computed, and then wait for it to appear. If you would like to choose another point, please close the
pop-up window and run the code again to select a new point.

'''

import numpy as np
import matplotlib.pyplot as plt

# step size
h = 0.01  #<<<<<<<<<<<<< EDIT STEP SIZE HERE
# compute function
y = lambda x: np.sin(np.exp(np.cos(x))) #<<<<<<<<<<<<<< EDIT FUNCTION HERE
# number of orders
orders = 5 #<<<<<<<<<<<<<<<< EDIT NUMBER OF ORDERS HERE

# setting up the initial plot in case the student wants to choose a point from the graph
a = 0   
xlist = np.arange(a - 4, a + 4,h)
plt.plot(xlist,y(xlist), 'b')
plt.plot(np.zeros(2000),np.arange(-1000, 1000), color = 'black') #x axis
plt.plot(np.arange(-1000, 1000), np.zeros(2000), color = 'black') # y axis
plt.axis([a - 4, a + 4, y(a) - 4, y(a) + 4])

# value for taylor series
taylorpoint = input("Type the desired value here. If you would like to select a point on the graph, type 'g': ")
if taylorpoint == 'g':
    inputvalue = plt.ginput(show_clicks = True)
    a = inputvalue[0][0]
else:
    a = float(taylorpoint)

# setting up a new plot with the 'a' value
xlist = np.arange(a - 4, a + 4,h)
plt.plot(xlist,y(xlist), 'b', label = 'Actual function')
plt.axis([a - 4, a + 4, y(a) - 4, y(a) + 4])

# function to calculate binomial coefficients which are used in formula for forward finite difference
def binomialcoeff(n,r):
    coeff = np.math.factorial(n)/(np.math.factorial(r)*np.math.factorial(n-r))
    return coeff

# code below calculates forward finite difference and then taylor series
for taylororder in range(orders + 1): # 
    yvaluelist = []
    for x in xlist:
        taylorvalue = 0
        for derivativeorder in range(taylororder + 1):
            numerator = 0
            for term in range(derivativeorder + 1): # the formula below calculates one term of the forward finite difference, and the FOR loop iterates to calculate all terms.
                numerator += ((-1)**term) * binomialcoeff(derivativeorder, term) * y(a + (h*(derivativeorder - term))) 
            forwarddiffvalue = numerator/(h ** derivativeorder)
            taylorvalue += (forwarddiffvalue/np.math.factorial(derivativeorder)) * ((x - a) ** derivativeorder) # using the derivative approximation, terms of the Taylor series are iteratively calculated
        yvaluelist.append(taylorvalue)
    plt.plot(xlist,yvaluelist,'--', label = f'{derivativeorder} order')

plt.legend()
plt.show()
