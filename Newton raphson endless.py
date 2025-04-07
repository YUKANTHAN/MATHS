# Defining Function
def f(x):
    return x**3 - 5*x - N

# Defining derivative of function
def g(x):
    return 3*x**2 - 5

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
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')
i=0
for i in range(0,56):
    # Input Section
    x0 = 0.5
    e = 0.0001
    
    
    N = i
    
        
    print("For the roll number ",N)
    
    # Converting x0 and e to float
    x0 = float(x0)
    e = float(e)
    
    # Converting N to integer
    N = int(N)
    
    newtonRaphson(x0,e)
