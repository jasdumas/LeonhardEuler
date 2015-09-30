## euler Problem 5
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def smallr(n):
    lst = []

    for i in range(1, 21, 1):
        if n % i == 0: # if the integer remainder is 0, than its good!
            lst.append(n)
            #print(lst, "This is ", i)
    if len(lst) != 20: # if there are not the correct remainder zero's in the list
        print("this is not a smallest number")
    else:
        print("hey now, this is a smallest number")
            

#for n in range(1, 10000, 1):
    
    #for x in range(1, n, 
