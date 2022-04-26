import pandas as pd 
import sys
wt=[]
val=[]
W=[]

with open('p07_c.txt', 'r') as f:
	for line in f.readlines():
		s = line.split(' ')
		W.append(int(s[0]))

with open('p07_w.txt', 'r') as f:
	for line in f:
		wt.append(line.strip('\n').split(',')[0])

with open('p07_p.txt', 'r') as f:
	for line in f:
		val.append(line.strip('\n').split(',')[0])


print(wt)
print(val)
print(W)


#設定函數
def knapSack(W, wt, val, n):
   # initial conditions
   if n == 0 or W == 0 :
      return 0
   # If weight is higher than capacity then it is not included
   if (wt[n-1] > W):
      return knapSack(W, wt, val, n-1)
   # return either nth item being included or not
   else:
      return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
         knapSack(W, wt, val, n-1))
# input data to above function
wt=[70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
val=[135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
W=750
n = len(val)
print ('optimal profit :',knapSack(W, wt, val, n))

		
