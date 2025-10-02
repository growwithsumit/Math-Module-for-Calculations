#Using the Math Module for Calculations

import math
n=int(input('Enter a number: '))

#calculate the square root
if n>=0:
    sqrt_result=math.sqrt(n)
    print('Square root: ',sqrt_result)
else:
    print('Square root is not defined for negative numbers.')

#Calculate the natural logarithm(log base e)
if n>0:
    log_result=math.log(n)
    print('Logarithm: ',log_result)
else:
    print('Natural log is not defined for zero or negative numbers.')

#Calculate the sine(in radians)
sine_result=math.sin(n)
print('Sine: ',sine_result)



