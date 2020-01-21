import numpy


def solve(dimension=3):
    matrix = []  # This represents the dimension x dimension board.

    """
    We need to create a diagonal matrix to represent the different variables in the first row
    
    Example:
        For a 3x3 matrix: 
            [[a,b,c],
            [d,e,f],
            [g,h,i]]
        
        The first row will be saved into matrix as:
            [[[1,0,0],[0,1,0],[0,0,1]],
            [d,e,f],
            [g,h,i]]
        Where [1,0,0] = a, [0,1,0] = b, c = [0,0,1].
    """
    for y in range(dimension):
        buf = numpy.zeros(dimension+1)
        buf[y] = 1
        matrix.append(buf)

    """
    For the second row and onwards (to the dimension+1 th row), we define the variables to be dependent on a,b,c
    Their dependents are acquired from the shape that either resembles L, T or +. 
    Our goal is to have each row be equal to 1 eventually (for white).
    
    Example:
        For a 3x3 matrix: 
            [a,b,c],
            [d,e,f],
            [g,h,i],
            [j,k,l]]
        We can give d the following states: 
            1 (it's already white),
            a (if we click on a, we form the L shape and that touches d)
            b (if we click on b, to form an L to a and then d)
        
        Then d = 1 + a + b
        But for d to be white, we need d (mod 2) = 1
        so d = 1 + a + b (mod 2) = 1
        
        We need one more extra row to force the previous row (the row at dimension) to have all values of 1 (white)
    """
    for position in range(dimension, dimension ** 2 + dimension):
        _sum = matrix[position - dimension]

        if position - 2 * dimension >= 0:
            _sum = [sum(x) for x in zip(_sum, matrix[position - 2 * dimension])]

        if position % dimension != 0:
            _sum = [sum(x) for x in zip(_sum, matrix[position - dimension - 1])]

        if position % dimension != dimension - 1:
            _sum = [sum(x) for x in zip(_sum, matrix[position - dimension + 1])]

        _sum[-1] = 1 if _sum[-1] % 2 == 0 else 0

        _sum = [x % 2 for x in _sum]
        matrix.append(numpy.array(_sum))
    """
    We remove the last element of every array and save it into sliced because these arrays are of length dimension + 1
    
    We also solve for the linear system of equations using gaussian elimination
    
    Example:
        in a 3x3 matrix, we said we wanted variables a,b,c and represented as a matrix. But, previously we said that d = 1 + a + b.
        I needed to have d be a matrix of size (4,) rather than (3,) to accommodate for the 1.
        Then I remove that extra 1 and work my way back with a (3,) shape.
    """
    sliced = numpy.array(matrix[-dimension:])
    _s = sliced[:, :-1]
    _ss = numpy.ndarray.flatten(sliced[:, -1:])

    sliced = numpy.linalg.solve(_s, _ss)

    sliced = [int(x % 2) for x in sliced]

    """
    Here we finally solved the values for a,b,c,... which allows the entire dimension x dimension matrix to be 1 (or white).
    
    We then need to substitute these values back to every row.
    
    Luckily, the value of a,b,c... can either be 0 or 1 (black or white resp.).
    
    We can simply use multiplication and sum functions to get our 'probable' matrix. This matrix will tell us the tokens that 
    are legal to play with to solve the equation.
    """

    matrix = matrix[dimension:]
    _sol = [x for x in sliced]
    for array in matrix:
        _var = array[-1]
        z = numpy.multiply(array[:-1], sliced)
        _s = sum(z)
        _sol.append(0 if _s == 0 else ((_s + _var) % 2))

    # We simply get rid of the last row (the row we added to force the previous row to be all white)
    _sol = numpy.array(_sol[:-dimension])
    return _sol.reshape((dimension, dimension))


# WATCH OUT FOR SINGULAR MATRICES. IT MEANS THERE ARE MULTIPLE WAYS TO SOLVE THIS
print(solve(6))
