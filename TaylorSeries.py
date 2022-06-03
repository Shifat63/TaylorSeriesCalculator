import numpy as np
import random

maxDegree = 10

#### Your Function Here
sincoe = []
expcoe = []
arctancoe = []
#Generating coefficients for Sin and store them in sincoe array
for i in range(maxDegree+1):
    if(i%4)==0:
        sincoe.append(0) # Sin(0) = 0
    elif(i%4)==1:
        sincoe.append(1/np.math.factorial(i)) #Cos(0) = 1
    elif(i%4)==2:
        sincoe.append(0) # -Sin(0) = 0
    else:
        sincoe.append(-1/np.math.factorial(i)) # -Cos(0) = -1

#Generating coefficients for exp and store them in expcoe array
for i in range(maxDegree+1):
    expcoe.append(1/np.math.factorial(i))

#Generating coefficients for arctan and store them in arctancoe array
for i in range(maxDegree+1):
    if (i % 4) == 0:
        arctancoe.append(0)
    elif (i % 4) == 1:
        arctancoe.append(1 / i)
    elif (i % 4) == 2:
        arctancoe.append(0)
    else:
        arctancoe.append(-1 / i)

def taylor(maxDegree, xValue, coefficients):
    result = 0
    for i in range(maxDegree+1):
        result = result + coefficients[i]*pow(xValue,i)
    return result

#### Helper Functions

def getRealValue(funktion, punkt):
    return funktion(punkt)

def getError(approxValue, realValue):
    return np.abs(approxValue-realValue)

#### Debug Data
for degree in range(0, maxDegree):
    print(f"----Degree {degree}----")
    x = 0.4 # You can play with this value to a get feeling for what is going on here
            # Watch the radius of convergence
    print(f"Error Sinus at {x}: {getError(taylor(degree, x, sincoe), getRealValue(np.sin, x)):.4f}")
    print(f"Error Exp at {x}: {getError(taylor(degree, x, expcoe), getRealValue(np.exp, x)):.4f}")
    print(f"Error Atan at {x}: {getError(taylor(degree, x, arctancoe), getRealValue(np.arctan, x)):.4f}")

#### Test Data
for noOfTries in range(0, 1000):
    xValue = random.uniform(0, 1)
    if getError(taylor(10, xValue, sincoe), getRealValue(np.sin, xValue)) > 0.01:
        print(f"Computer says no. Sin error at {xValue}. Approximiation bad.")
    if getError(taylor(10, xValue, expcoe), getRealValue(np.exp, xValue)) > 0.01:
        print(f"Computer says no. Exp error at {xValue}. Approximiation bad.")
    if getError(taylor(10, xValue, arctancoe), getRealValue(np.arctan, xValue)) > 0.062:
        print(f"Computer says no. Tan error at {xValue}. Approximiation bad.")