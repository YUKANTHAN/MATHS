import math

# Defining Function
def f(x):
    return 3*math.cos(x) - math.exp(x)

# Defining derivative of function
def g(x):
    return -3*math.sin(x) - math.exp(x)

# Implementing Newton Raphson Method

def newtonRaphson(x0,e):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f, f(x1) = %0.6f and g(x1) = %0.6f' % (step, x1, f(x1), g(x1)))
        x0 = x1
        step = step + 1
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

while True:
    # Input Section
    x0 = input('Enter Guess: ')
    e = input('Tolerable Error: ')
    
    
    # Converting x0 and e to float
    x0 = float(x0)
    e = float(e)
    
    # Converting N to integer
    
    
    
    #Note: You can combine above three section like this
    # x0 = float(input('Enter Guess: '))
    # e = float(input('Tolerable Error: '))
    # N = int(input('Maximum Step: '))
    
    # Starting Newton Raphson Method
    newtonRaphson(x0,e)