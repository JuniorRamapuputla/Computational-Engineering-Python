
# 1. Numpy library
from numpy import pi, sin, deg2rad


#A function that finds the value of a sinousoidal wave at 45 degrees (Numpy library)
def findVal(angle):
    #convert degrees to radians
    theta = deg2rad(angle)
    
    return round(sin(theta), 1) 

# 2. SciPy library
from scipy import integrate

#A function that finds the area under a parabola (x^2) at the given bounds
def findArea(lowerBound = 0, UpperBound = 0):
    #equation: y = x^2
    y = lambda x: x**2
    
    #using the integration function from scipy
    return integrate.quad(y, lowerBound,UpperBound)

def main():
    #1. Numpy
    #angle = float(input('Enter the angle in degrees: '))
    # print(f'The value of sinousoidal wave at {angle} \N{DEGREE SIGN} is {findVal(angle)}')
    
    #2.1 SciPy
    lowerBound = float(input('Enter the lower bound: '))
    upperBound = float(input('Enter the upper bound: '))
   
    area = round(findArea(lowerBound, upperBound)[0],1)
    
    print(f'The area under the parabola from {lowerBound} to {upperBound} is {area}')


if __name__ == '__main__':
    main()
    