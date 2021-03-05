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

#This computes the partial Basel sum with n terms. The full basel sum produces the values pi^2/6, so we multiply by 6 and take a square root.
def basel(n):
    basel_sum = sum([1/i**2 for i in range(1,n+1)])
    return math.sqrt(6*basel_sum)

#This computes the trapezoidal sum of sqrt(1-x^2), the formula for the top half of the unit circle from 0 to 1 using n trapezoids. The integral produces the value pi/4.
def trapezoid(n):
    sum = 0
    for i in range(n):
        left_endpoint = i/n
        right_endpoint = (i+1)/n
        average_height = (math.sqrt(1-(left_endpoint)**2)+math.sqrt(1-(right_endpoint)**2))/2
        sum+=average_height*1/n
    return 4*sum

#This computes the partial sum of (-1)^(n+1)/(2n-1) from 1 to infinity which evaluates to pi/4
def leibniz(n):
    leibniz_sum = sum([(-1)**(n+1)/(2*n-1) for n in range (1,n+1)])
    return 4*leibniz_sum

#This computes the partial sum of 3 + 4(-1)^(n+1)/((2n)(2n+1)(2n+2)) which evaluates to pi.
def nilakantha(n):
    nilakantha_sum = sum([4*(-1)**(n+1)/((2*n)*(2*n+1)*(2*n+2)) for n in range(1,n+1)])
    return 3+nilakantha_sum

#This uses Borwein's algorithm to recursively find pi. The value of borwein_p(n) converges to pi:
bor_a = dict()
bor_a[1] = math.sqrt(2)
def borwein_a(n):
    while n not in bor_a.keys():
        if n-1 in bor_a.keys():
            bor_a[n] = (math.sqrt(bor_a[n-1])+1/math.sqrt(bor_a[n-1]))/2
        else:
            borwein_a(n-1)
    return bor_a[n]

bor_b = dict()
bor_b[1] =0
def borwein_b(n):
    while n not in bor_b.keys():
        if n-1 in bor_b.keys():
            bor_a_temp = borwein_a(n-1)
            bor_b[n] = (1+bor_b[n-1])*math.sqrt(bor_a_temp)/(bor_a_temp+bor_b[n-1])
        else:
            borwein_b(n-1)
    return bor_b[n]

    
bor_p = dict()
bor_p[1] =2+math.sqrt(2)
def borwein_p(n):
    while n not in bor_p.keys():
        if n-1 in bor_p.keys():
            bor_a_temp = borwein_a(n)
            bor_b_temp = borwein_b(n)
            bor_p[n] = (1+bor_a_temp)*bor_p[n-1]*bor_b_temp/(1+bor_b_temp)
        else:
            borwein_p(n-1)
    return bor_p[n]

#This uses the monte carlo method with n points in a 2x2 square that circumscribes a circle with radius 1.
def monte_carlo(n):
    yeses = 0
    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if math.sqrt(x**2+y**2)<1:
            yeses+=1
    return 4*yeses/n

#This computes the Riemann sum of 1/sqrt(1-x^2), the derivative of arcsin(x) from 0 to 1 using n rectangles and left endpoints. The integral produces the value pi/2.
def riemann(n):
    riemann_sum = sum([(1/math.sqrt(1-(i/n)**2))*(1/n) for i in range(n)])
    return 2*riemann_sum


def basel_count(epsilon):
    basel_counter = 1
    while abs(basel(basel_counter)-math.pi)>=epsilon:
        basel_counter+=1
    return basel_counter

def trapezoid_count(epsilon):
    trapezoid_counter = 1
    while abs(trapezoid(trapezoid_counter)-math.pi)>=epsilon:
        trapezoid_counter +=1
    return trapezoid_counter

def leibniz_count(epsilon):
    leibniz_counter = 1
    while abs(leibniz(leibniz_counter)-math.pi)>=epsilon:
        leibniz_counter +=1
    return leibniz_counter

def nilakantha_count(epsilon):
    nilakantha_counter = 1
    while abs(nilakantha(nilakantha_counter)-math.pi)>=epsilon:
        nilakantha_counter +=1
    return nilakantha_counter

def borwein_count(epsilon):
    borwein_counter = 1
    while abs(borwein_p(borwein_counter)-math.pi)>=epsilon:
        borwein_counter+=1
    return borwein_counter

def monte_count(epsilon):
    monte_list = []
    for n in range(100):
        carlo_count = 1
        while abs(monte_carlo(carlo_count)-math.pi)>=epsilon:
            carlo_count+=1
        monte_list.append(carlo_count)
    return numpy.median(monte_list)

def monte_count_k(epsilon,k):
    monte_list = []
    for n in range(k):
        carlo_count = 1
        while abs(monte_carlo(carlo_count)-math.pi)>=epsilon:
            carlo_count+=1
        monte_list.append(carlo_count)
    return numpy.median(monte_list)

def riemann_count(epsilon):
    riemann_counter = 1
    while abs(riemann(riemann_counter)-math.pi)>=epsilon:
        riemann_counter +=1
    return riemann_counter

def steps_to_epsilon(epsilon):
    print('To get your estimate within epsilon = ' + str(epsilon) + ' of π, it takes')
    print('The Basel Problem ' + str(basel_count(epsilon)) + ' summands to get within the threshold.')
    print('The Leibniz sum ' + str(leibniz_count(epsilon)) + ' summands to get within the threshold.')
    print('The Nilakantha sum ' + str(nilakantha_count(epsilon)) + ' summands to get within the threshold.')
    print('The Borwein algorithm ' + str(borwein_count(epsilon)) + ' iterations to get within the threshold.')
    #print('The Riemann Sum ' + str(riemann_count(epsilon)) + ' intervals to get within the threshold.')
    print('The Trapezoidal sum ' + str(trapezoid_count(epsilon)) + ' intervals to get within the threshold.')
    print('It took the Monte Carlo method approximately ' + str(monte_count(epsilon)) + ' trials to get within the threshold.')
    print('NOTE: This number is determined 100 times and the median of those values is what is displayed.')


x = range(10,1010,10)

basel_count_list = [basel_count(1/point) for point in x]
trapezoid_count_list = [trapezoid_count(1/point) for point in x]
leibniz_count_list = [leibniz_count(1/point) for point in x]
nilakantha_count_list = [nilakantha_count(1/point) for point in x]
borwein_count_list = [borwein_count(1/point) for point in x]
monte_count_list = [monte_count(1/point) for point in x]



plt.plot(x,x, c='black')    
plt.scatter(x, basel_count_list, s=5)
plt.scatter(x, trapezoid_count_list, s=5)
plt.scatter(x, leibniz_count_list, s=5)
plt.scatter(x, nilakantha_count_list, s=5)
plt.scatter(x, borwein_count_list, s=5)
plt.scatter(x, monte_count_list, s=5)
plt.xlabel('1/ε')
plt.ylabel('Steps')
plt.title('The number of steps it takes for\n each approximation to be within ε of π ')
plt.legend(['y=x', 'Basel', 'Trapezoidal', 'Leibniz', 'Nilakantha', 'Borwein', 'Monte Carlo'])
plt.savefig('Steps to be within epsilon.png', dpi=500)

plt.close()


x2 = range(1,101)

basel_list = [basel(point) for point in x2]
trapezoid_list = [trapezoid(point) for point in x2]
leibniz_list = [leibniz(point) for point in x2]
nilakantha_list = [nilakantha(point) for point in x2]
borwein_list = [borwein_p(point) for point in x2]
monte_list = [monte_carlo(point) for point in x2]
riemann_list = [riemann(point) for point in x2]

plt.plot(x2,[math.pi]*len(x2), c='black')    
plt.scatter(x2, basel_list, s=5)
plt.scatter(x2, trapezoid_list, s=5)
plt.scatter(x2, leibniz_list, s=5)
plt.scatter(x2, nilakantha_list, s=5)
plt.scatter(x2, borwein_list, s=5)
plt.scatter(x2, monte_list, s=5)
plt.scatter(x2, riemann_list, s=5)
plt.xlabel('n')
plt.ylabel('Value')
plt.title('The value of each function for each value of n')
plt.legend(['y=π', 'Basel', 'Trapezoidal', 'Leibniz', 'Nilakantha', 'Borwein', 'Monte Carlo', 'Riemann'])
plt.savefig('Convergence to pi.png', dpi=500)


plt.close()


monte_count_list_1 = [monte_count_k(1/point,1) for point in x]
monte_count_list_10 = [monte_count_k(1/point,10) for point in x]
monte_count_list_50 = [monte_count_k(1/point,50) for point in x]
monte_count_list_100 = [monte_count_k(1/point,100) for point in x]
monte_count_list_200 = [monte_count_k(1/point,200) for point in x]
monte_count_list_500 = [monte_count_k(1/point,500) for point in x]
monte_count_list_1000 = [monte_count_k(1/point,1000) for point in x]

plt.scatter(x, monte_count_list_1, s=11)
plt.scatter(x, monte_count_list_10, s=10)
plt.scatter(x, monte_count_list_50, s=9)
plt.scatter(x, monte_count_list_100, s=8)
plt.scatter(x, monte_count_list_200, s=7)
plt.scatter(x, monte_count_list_500, s=6)
plt.scatter(x, monte_count_list_1000, s=5)

plt.xlabel('1/ε')
plt.ylabel('Steps')
plt.title('Estimating pi within epsilon  by the Monte Carlo Method \nby finding the \nmedian after running it k times')
plt.legend(['k=1','k=10','k=50', 'k=100','k=200','k=500','k=1000'])
plt.savefig('Monte Carlo with variable k trials.png', dpi=500)