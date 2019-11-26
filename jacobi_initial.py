# Jacobi solver for Laplace equation.
# Description: This code solves the Laplace equation using Jacobi iterative
#              method on a square grid, given the boundary conditions
#
# Author: G.P. Brandino
# Copyright: 2019 eXact-lab s.r.l.
# License: GPLv2
#

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('dim', type=int)
parser.add_argument('iters', type=int)

# read input paramters
args  = parser.parse_args()
dim   = args.dim
iters = args.iters

print("m size = " + str(dim))
print("number of iter = " + str(iters))

# fill initial values
m  = [[0 for x in range(dim + 2)] for y in range(dim + 2)] 
m1 = [[0 for x in range(dim + 2)] for y in range(dim + 2)] 

# set up boundary conditions
# Note that the borders are never modified by the update, so we need to
# set up b.c. on BOTH the buffers
incr = 100.0 / (dim + 1)
for i in range(1,dim + 2):
    m[i][0] = i * incr 
    m[dim + 1][ dim + 1 - i]= i * incr
    m1[i][0] = i * incr
    m1[dim + 1][dim + 1 - i]= i * incr

for it in range(iters):
    for i in range(1,dim + 1):
        for j in range(1,dim + 1):
            m1[i][j] = 0.25 * (m[i-1][j] + m[i+1][j] + m[i][j-1] + m[i][j+1])
    #we use list to force a deep copy, otherwise for lists only the reference is copied        
    m = list(m1)

f = open("solution.dat","w+")

for i in range(dim + 2):
    for j in range(dim + 2):
        f.write(str(m[i][j]) + " ")
    f.write("\n")

f.close()
