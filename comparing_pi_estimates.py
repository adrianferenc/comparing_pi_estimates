#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:04:00 2021

@author: adrianferenc
"""

import math
import random
import numpy
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

epsilon = 1/20


def basel(n):
    basel_sum = sum([1/i**2 for i in range(1,n+1)])
    return math.sqrt(6*basel_sum)

def monte_carlo(n):
    yeses = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if math.sqrt(x**2+y**2)<1:
            yeses+=1
    return 4*yeses/n

def basel_count(epsilon):
    basel_counter = 1
    while abs(basel(basel_counter)-math.pi)>=epsilon:
        basel_counter+=1
    return basel_counter

def monte_count(epsilon):
    monte_list = []
    for n in range(100):
        carlo_count = 1
        while abs(monte_carlo(carlo_count)-math.pi)>=epsilon:
            carlo_count+=1
        monte_list.append(carlo_count)
    return numpy.median(monte_list)

print('To get your estimate within epsilon = ' + str(epsilon) + ' of π, it takes')
print('The Basel Problem ' + str(basel_count(epsilon)) + ' summands to get within the threshold.')
print('It took the Monte Carlo method approximately ' + str(monte_count(epsilon)) + ' trials to get within the threshold.')
print('NOTE: This number is determined 100 times and the median of those values is what is displayed.')

list_of_basel_values_by_epsilon = [basel_count(1/i) for i in range(1,501)]

list_of_monte_values_by_epsilon = [monte_count(1/i) for i in range(1,501)]

#plt.scatter(list_of_basel_values_by_epsilon,list_of_monte_values_by_epsilon)
#plt.savefig('comparison_graph.png')

X = [[x] for x in list_of_basel_values_by_epsilon]
y = list_of_monte_values_by_epsilon

reg = LinearRegression().fit(X, y)
print(reg.score(X, y))