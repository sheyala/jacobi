# Driver program for the Jacobi solver for Laplace equation.
# Description: This file contains the driver program for the solver of
#              the Laplace equation using Jacobi iterative method on a
#              square grid, given the boundary conditions
#
# Author: G.P. Brandino
# Copyright: 2019 eXact-lab s.r.l.
# License: GPLv2
#

import argparse
import jacobi_functions as jacobi

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dimension', type=int)
    parser.add_argument('iterations', type=int)

    # read input paramters
    args  = parser.parse_args()
    dimension   = args.dimension
    iterations = args.iterations

    print("m size = " + str(dimension))
    print("number of iter = " + str(iterations))

    # fill initial values
    grid  = [[0 for x in range(dimension + 2)] for y in range(dimension + 2)] 
    gridNew = [[0 for x in range(dimension + 2)] for y in range(dimension + 2)] 

    # set up boundary conditions
    # Note that the borders are never modified by the update, so we need to
    # set up b.c. on BOTH the buffers
    jacobi.setBoundaryConditions(grid, gridNew, dimension)

    for it in range(iterations):
        jacobi.update(grid, gridNew, dimension)
        #we use list to force a deep copy, otherwise for lists only the reference is copied        
        grid = list(gridNew)

    jacobi.printOutput(grid, dimension)

if __name__ == "__main__":
    main()
