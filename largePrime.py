# a prime number is divisibale by itself and one
'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
lst = []
n = 600851475143

for i in range(1, n, 1):
    if i % 2 == 1:
        lst.append(i)
    if i % i == 0:
        lst.append(i)
    
print(max(lst))
