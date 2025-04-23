import numpy as np

def newton_forward_backward_derivatives(x, y, target_x, h, order=1):
    """
    Calculate derivatives using Newton's forward and backward interpolation formulas
    
    Parameters:
    x (array): Array of x values (equally spaced)
    y (array): Array of y values corresponding to x
    target_x (float): Point at which to calculate derivative
    h (float): Step size (difference between x values)
    order (int): Order of derivative (1 or 2)
    
    Returns:
    tuple: (forward_derivative, backward_derivative)
    """
    
    n = len(x)
    
    # Create forward difference table
    forward_diff = np.zeros((n, n))
    forward_diff[:,0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            forward_diff[i,j] = forward_diff[i+1,j-1] - forward_diff[i,j-1]
    
    # Create backward difference table
    backward_diff = np.zeros((n, n))
    backward_diff[:,0] = y
    
    for j in range(1, n):
        for i in range(j, n):
            backward_diff[i,j] = backward_diff[i,j-1] - backward_diff[i-1,j-1]
    
    # Find the index where target_x is located
    idx = np.searchsorted(x, target_x) - 1
    idx = max(0, min(idx, n-2))  # Ensure we stay within bounds
    
    # Calculate forward derivative
    p = (target_x - x[idx]) / h
    
    if order == 1:
        # First derivative using forward formula
        fd_deriv = (forward_diff[idx,1] + (2*p - 1)/2 * forward_diff[idx,2] + 
                   (3*p**2 - 6*p + 2)/6 * forward_diff[idx,3]) / h
        
        # First derivative using backward formula
        bd_deriv = (backward_diff[idx+1,1] + (2*p + 1)/2 * backward_diff[idx+1,2] + 
                   (3*p**2 + 6*p + 2)/6 * backward_diff[idx+1,3]) / h
    elif order == 2:
        # Second derivative using forward formula
        fd_deriv = (forward_diff[idx,2] + (p - 1) * forward_diff[idx,3]) / (h**2)
        
        # Second derivative using backward formula
        bd_deriv = (backward_diff[idx+1,2] + (p + 1) * backward_diff[idx+1,3]) / (h**2)
    else:
        raise ValueError("Order must be 1 or 2")
    
    return fd_deriv, bd_deriv


# Example usage
if __name__ == "__main__":
    # Sample data (equally spaced)
    x = np.array([1931,1941,1951,1961,1971])
    y = np.array([40.62,60.8,79.95,103.56,132.65])
    h = x[1] - x[0]  # step size
    target_x = 1971
    
    print(f"Calculating derivatives at x = {target_x}")
    
    # First derivatives
    fd_first, bd_first = newton_forward_backward_derivatives(x, y, target_x, h, order=1)
    print(f"\nFirst derivative:")
    print(f"Forward formula result:  {fd_first:.6f}")
    print(f"Backward formula result: {bd_first:.6f}")
    
    # Second derivatives
    fd_second, bd_second = newton_forward_backward_derivatives(x, y, target_x, h, order=2)
    print(f"\nSecond derivative:")
    print(f"Forward formula result:  {fd_second:.6f}")
    print(f"Backward formula result: {bd_second:.6f}")
