#Question 1 part 1

import matplotlib.pyplot as plt
import random
#Define population size N
N = 500
#type0 and type1 is defined to see how many times each type is fixed
type0 = 0
type1 = 0
T = 100
#start loop of T trials
for j in range(T):
    #Define population consisting of equal number of type 0s and 1s
    pop = []
    for i in range(int(N/2)):
        pop.append(0)
        pop.append(1)
    #while loop runs until one of the type gets fixed. Here if type 0 is fixed,
    #mean of list pop will be 0 and if type 1 is fixed,
    #mean of pop will be 1
    while sum(pop)/N != 1 and sum(pop)/N != 0: 
        p = pop[random.randint(0,N-1)]
        q = random.randint(0,N-1)
        pop.append(p) #random element from pop is reproduced
        del pop[q]  #random element of pop is dead
    print(j)
    #type0 and type1 is updated based on which type is fixed
    if pop[0] == 0:
        type0+=1
    else:
        type1+=1
print(type0/T,type1/T) #fixation frequencies of type 0 and 1 respectively

