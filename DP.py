#import module
import numpy as np
import random
import matplotlib.pyplot as plt
import configparser as config

#read and create dataset
file_empty = 0
#capacity
with open('p07_c.txt', mode="r") as file:
    capacity = np.loadtxt(file)
    if capacity.size == 0:
        file_empty = 1

#weights
with open('p07_w.txt', mode="r") as file:
    weights = np.loadtxt(file)
    weights = weights.astype(np.int32)
    if weights.size == 0:
        file_empty = 1

#profits
with open('p07_p.txt', mode="r") as file:
    profits = np.loadtxt(file)
    profits = profits.astype(np.int32)
    if profits.size == 0:
        file_empty = 1

#selections
with open('p07_s.txt', mode="r") as file:
    selects = np.loadtxt(file)
    selects = selects.astype(np.int32)
    if selects.size == 0:
        file_empty = 1

if file_empty == 1:
    print('file is empty')
    exit()


#dynamic programming
items = np.size(weights)
C = np.array([[0 for x in range(int(capacity) + 1)] for x in range(int(items) + 1)])

for i in range(int(items)+1): #0~15
    for k in range(int(capacity)+1): #0~750
            C[i][k] = 0

for i in range(int(items)+1): #0~15
    for k in range(int(capacity)+1): #0~750
        if k==0 or i==0:# initial conditions
            C[i][k] = 0
        elif int(weights[i-1]) <= k: #return either ith item being included or not
            C[i][k] = max(profits[i-1] + C[i-1][k-int(weights[i-1])], C[i-1][k])
        else:
            C[i][k] = C[i-1][k] #If weight is higher than capacity then item is not included


#check items is select or not
is_selects = np.array([0 for x in range(int(items))])
n = items
res = C[int(items)][int(capacity)]
w = int(capacity)
print("maximum value:" + str(res))

for i in range(n,0,-1):
    if res <=0:
        break
    if res == C[i-1][w]: #item i沒取
        continue
    else:
        is_selects[i-1] = 1
        res = res - profits[i-1]
        w = w - weights[i-1]

if np.array_equal(is_selects, selects):
    print('correct answer:', end='')
    print(selects)
else:
    print('wrong answer')