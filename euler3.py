###EULER 3 Largest prime factor: Python 
###Varun Sreedharan 07/21/22


def primefact(num):
    divisor = 2
    while divisor < num:
        if num%divisor == 0:
            num /= divisor
            divisor = 1
        divisor += 1
    return num

print(primefact(13195))
print(primefact(600851475143))



            

