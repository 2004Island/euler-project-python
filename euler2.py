###EULER 2 Even Fibonacci numbers: Python
###Varun Sreedharan 07/20/22

fibnums = [0, 1, 2]
evenfibnums = [0, 2]
tempfib = 0
while tempfib < 4000000:
    tempfib = fibnums[-1] + fibnums[-2]
    fibnums.append(tempfib)
    
    if tempfib%2 == 0:
        evenfibnums.append(tempfib)
    else:
        continue
    
print(sum(evenfibnums))
