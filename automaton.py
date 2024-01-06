# This code is developed and maintained by Goktug Islamoglu using PyCX 0.3 Realtime Visualization Template
# goktugislamoglu@gmail.com
##
# PyCX 0.3 Realtime Visualization Template
# Written by:
# Chun Wong
# email@chunwong.net
##
# Revised by:
# Hiroki Sayama
# sayama@binghamton.edu
##
# Running on the simulator package "pycxsimulator.py"
# Realtime Simulation GUI for PyCX
##
# Developed by:
# Chun Wong
# email@chunwong.net
##
##

import matplotlib
matplotlib.use('TkAgg')

from pylab import *
import numpy as np


L = 100  # size of space: LxL

#p = 0.853553390594 ##above upper bound paramagnetic, first-order phase transition
#p = float(0.5 + (1 / (2 * sqrt(2)))) ##upper bound critical range ferrimagnetic
#p = float(0.5 - (1 / (2 * sqrt(2)))) ##lower bound critical range antiferromagnetic
#p = 0.14644660940 #below lower bound paramagnetic, first-order phase transition
#p = 1/(1+np.exp(-np.log(1+sqrt(2))/2))

#p = -(np.log(np.log(2))-(sqrt(2)-1)) #returns same as Ising critical inverse temperature
#p = np.log(1+sqrt(2))/2 ##Ising critical inverse temperature
#p = 1 - np.log(1+sqrt(2))/2

p = 1/(1 + np.exp(-(1/sqrt(2)))) ##critical point, maximum count1, minimum H
#p = (1/(1+np.exp(-(2*1/(2*sqrt(2))))))/2 + 0.5 ##returns Ising critical inverse temperature as H

#p = 0.592746 #percolation threshold for 2D square lattice, minimum H
print p

# initializing randomly assigned states with probability p


def init():
    global c, nc, slope0, slope1, delta, o
    c = zeros([L, L])
    for x in xrange(L):
        for y in xrange(L):
            c[x, y] = 1 if random() < p else 0
    nc = zeros([L, L])
    o = 0
    slope0 = []
    slope1 = []
    delta = []

# visualizing the content of an array


def draw():
    cla()
    imshow(c)

# count of upper neighbors of a live cell's Moore neighborhood


def number_of_upper_neighbors(x, y):
    upper_count = 0
    for dx in range(-1, 2):
        upper_count += c[(x + dx) % L, (y + 1) % L]
        # print upper_count
    return upper_count

# count of lower neighbors of a live cell's Moore neighborhood


def number_of_lower_neighbors(x, y):
    lower_count = 0
    for dx in range(-1, 2):
        lower_count += c[(x + dx) % L, (y - 1) % L]
        # print lower_count
    return lower_count

# count of right neighbors of a live cell's Moore neighborhood


def number_of_right_neighbors(x, y):
    right_count = 0
    for dy in range(-1, 2):
        right_count += c[(x + 1) % L, (y + dy) % L]
        # print right_count
    return right_count

# count of left neighbors of a live cell's Moore neighborhood


def number_of_left_neighbors(x, y):
    left_count = 0
    for dy in range(-1, 2):
        left_count += c[(x - 1) % L, (y + dy) % L]
        # print left_count
    return left_count

# count of von Neumann neighbors of a live cell


def number_of_Neumann_neighbors(x, y):
    Vertical_count = 0
    Horizontal_count = 0
    for dy in range(-1, 2):
        Vertical_count += c[x, (y + dy) % L]
        # print Vertical_count
    for dx in range(-1, 2):
        Horizontal_count += c[(x + dx) % L, y]
        # print Horizontal_count
    return Vertical_count + Horizontal_count - c[x, y]

# count of Moore neighbors of an alive cell


def number_of_Moore_neighbors(x, y):
    Moore_count = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            Moore_count += c[(x + dx) % L, (y + dy) % L]
            # print Moore_count
    return Moore_count - c[x, y]


def step():
    global c, nc, array, array0, array1, count, count0, count1, num, num1, slope0, slope1, delta, o
    count0 = 0
    count1 = 0
    count = 0
    num1 = 0
    num = 0
    i = 0
    j = 0
    array = []
    array0 = []
    array1 = []
    for x in xrange(L):
        for y in xrange(L):
            if c[x, y] == 1:
                array.append(c[x, y])
            g = number_of_Moore_neighbors(x, y)
            if c[x, y] == 0:
                nc[x, y] = 0 if g <= 6 else 1
                array0.append(c[x, y])
            elif c[x, y] == 1:
                array1.append(c[x, y])
                for z in range(-1, 2):
                    # block generation from randomly distributed points
                    m = number_of_upper_neighbors(x, y)
                    if m == 1:
                        nc[x, (y + 1) % L] = 1

                    n = number_of_lower_neighbors(x, y)
                    if n == 1:
                        nc[x, (y - 1) % L] = 1

                    k = number_of_right_neighbors(x, y)
                    if k == 0 and (m <= 1 or n <= 1):
                        nc[(x + 1) % L, (y + z) % L] = 1

                    l = number_of_left_neighbors(x, y)
                    if l == 1 and (m > 1 or n > 1):
                        nc[(x - 1) % L, (y + z) % L] = 0

                    h = number_of_Neumann_neighbors(x, y)
                    if h >= 1:
                        nc[x, y] = 1 if g <= 6 else 0

                    if g / 8 > (1 - p) * p:  
                        nc[(x + 1) % L, y] = 1
                    elif g / 8 < (1 - p) * p:
                        nc[(x - 1) % L, y] = 1
                    else:
                        nc[x, y] = 1
            i += 1
            j += g
    count = len(array)
    # print count
    count0 = len(array0)
    # print count0
    count1 = len(array1)
    print count1
    o += 1
    #print o
    if o == 1:
        # print count
        slope0.append(float(count0))
        slope1.append(float(count1))
        delta.append(float(j))
    elif o > 1:
        slope0.append(float(count0))
        # print slope0[o-1]
        # print slope0[o-2]
        slope1.append(float(count1))
        # print slope1[o-1]
        # print slope1[o-2]
        delta.append(float(j))
        # print delta[o-1]
        # print delta[o-2]
        num = count0 / float(count1)
        num0 = (j / i)
        num1 = num0 / num
        num2 = (slope0[o - 1] / float(slope1[o - 1])) - (slope0[o - 2] / float(slope1[o - 2]))
        num3 = (delta[o - 2] - delta[o - 1]) / i
        # num4 = num2 * num0
        # num5 = num3 * num
        #print num
        # print num0
        # print num1
        # print num2
        # print num3
        # print num4
        # print num5

        if num1 != 1:
           print (num3 / float(num1 * num1) + (1 / float(num1)) - num2)
    c, nc = nc, c

import pycxsimulator
pycxsimulator.GUI(title='My Simulator', interval=0,
                  parameterSetters=[]).start(func=[init, draw, step])
