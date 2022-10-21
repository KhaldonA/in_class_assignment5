''' 
Recursion:
1. write out the function in words, what do you want to accomplish using recursion?
2. define the base case FIRST
3. then define what you want to happen within the recursion
4. call the function within the function!
'''

import pandas as pd
import time

#####################################################################################################################
def EvenNums(num):
    print(num)
    if num == 2:
        return num
    else:
        return EvenNums(num-2)


# What could we do to make this function NOT error out with an odd number?


#####################################################################################################################

def Fibonacci(indx):
    if indx <= 1:
        return indx
    else:
        return Fibonacci(indx - 1) + Fibonacci(indx - 2)



##########################################################################################################################

def fibonacci(indx):
    seq = [0,1]
    for i in range(indx):
        seq.append(seq[-1] + seq[-2])
    return seq[-2]



#########################################################################################################################

def main():

    print("Now running the code for EvenNums(10) Function")
    EvenNums(10)

    print("Now we are running the code for the recursion function of Fibonacci(4)")
    rec = time.time()
    Fibonacci(4)
    print("speed of fibonacci recursion: " + str(time.time()- rec))

    print("Now we are running the code for the iteration function of Fibonacci(4)")
    iter = time.time()
    fibonacci(4)
    print("speed of fibonacci iteration: " + str(time.time()- iter))


if __name__ == "__main__":
    main()
