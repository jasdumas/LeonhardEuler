'''
Project Euler - Problem 6
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


def sum_sq(num=100):
    total = [] 
    total2 = []
    num_p = num + 1 # need index to go to one past the intended (num)ber
    for i in range(1, num_p):
        a = i**2
        total.append(a)
    print("The sum of the squares: ",sum(total))
    for i in range(1, num_p):
        total2.append(i)
    print("The square of the sum:  ",(sum(total2)**2))
    print("the difference is: ", (sum(total2)**2) - sum(total))
        
    


sum_sq()
