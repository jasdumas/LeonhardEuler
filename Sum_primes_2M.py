'''
Project Euler - Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

def sum_prime(prime=2000000):
    total = []
    for num in range(0, prime+1):
        # prime numbers are greater than one
        if num > 1:
            # numbers in range starting at 2 to all numbers greater than 1
            for i in range(2, num):
                if (num % i) == 0:  # if the number is divisible by itself with no remainder
                    break
            else:
                # add it to the total list for sum
                total.append(num)
                #print(num)
    print(sum(total))

    
sum_prime()
