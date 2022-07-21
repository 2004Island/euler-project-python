###EULER 1 Multiples of 3 or 5: Python
###Varun Sreedharan 07/20/22

numbers = []

for i in range (0,1000):
    if i%3 == 0 or i%5 == 0:
        numbers.append(i)
    else:
        continue

print(sum(numbers))
