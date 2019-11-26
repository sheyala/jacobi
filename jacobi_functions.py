# This file is a part of the Jacobi solver for Laplace equation.
# Description: This file provides several routines for the solver of the
#              Laplace equation using Jacobi iterative method on a square grid,
#              given the boundary conditions
#
# Author: G.P. Brandino
# Copyright: 2019 eXact-lab s.r.l.
# License: GPLv2
#

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

