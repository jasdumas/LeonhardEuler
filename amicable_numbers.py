'''
Project Euler - Problem 21

Evaluate the sum of all the amicable numbers under 10000
'''

def amicable(num1=10000, num2=14211):
    lst = []
    lst2 = []
    for i in range(1, num1):
        if num1 % i == 0:
            #print(i)
            lst.append(i)
        else:
            pass
    for ii in range(1, num2):
        if num2 % ii == 0:
            #print(i)
            lst2.append(ii)
        else:
            pass
       
    num1_sum = sum(lst)
    num2_sum = sum(lst2)
    if num1_sum == num2:
        print("yay")
        yay = num1_sum + num2_sum
    else:
        print("nope")
    print(yay)


amicable()
