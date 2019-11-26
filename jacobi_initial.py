# Jacobi solver for Laplace equation.
# Description: This code solves the Laplace equation using Jacobi iterative
#              method on a square grid, given the boundary conditions
#
# Author: G.P. Brandino
# Copyright: 2019 eXact-lab s.r.l.
# License: GPLv2
#

import argparse

def setBoundaryConditions(grid, gridNew, dimension):
    increment = 100.0 / (dimension + 1)
    for i in range(1,dimension + 2):
        grid[i][0] = i * increment
        grid[dimension + 1][ dimension + 1 - i]= i * increment
        gridNew[i][0] = i * increment
        gridNew[dimension + 1][dimension + 1 - i]= i * increment


def update(grid, gridNew, dimension):
    for i in range(1,dimension + 1):
        for j in range(1,dimension + 1):
            gridNew[i][j] = 0.25 * (grid[i-1][j] + grid[i+1][j] + grid[i][j-1] + grid[i][j+1])


def printOutput(grid, dimension):

    outputFile = open("solution.dat","w+")

    for i in range(dimension+2):
        for j in range(dimension+2):
            outputFile.write(str(grid[i][j]) + " ")
        outputFile.write("\n")

    outputFile.close()

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
    setBoundaryConditions(grid, gridNew, dimension)

    for it in range(iterations):
        update(grid, gridNew, dimension)
        #we use list to force a deep copy, otherwise for lists only the reference is copied        
        grid = list(gridNew)

    printOutput(grid, dimension)

if __name__ == "__main__":
    main()
