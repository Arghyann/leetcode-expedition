def findPath(m,n):
    # Base case: reached destination (1,1)
    if(m==1 and n==1):
        return [[]]  # Empty path - we're already at destination
    
    # Base case: out of bounds
    if(m<=0 or n<=0):
        return []  # No valid paths
    
    paths = []
    
    # Try going down (decrease m)
    if m > 1:
        down_paths = findPath(m-1, n)
        for path in down_paths:
            paths.append(['d'] + path)
    
    # Try going right (decrease n) 
    if n > 1:
        right_paths = findPath(m, n-1)
        for path in right_paths:
            paths.append(['r'] + path)
    
    return paths

print(findPath(2,3))