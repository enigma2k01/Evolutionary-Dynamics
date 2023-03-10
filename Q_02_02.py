#Question 2 part 2

import matplotlib.pyplot as plt
import random
#Define population size N
N = 500
pop = []
#define population with equal number of type 0s and type 1s
for i in range(int(N/2)):
    pop.append(0)
    pop.append(1)
A = [0.5] #list for frequency of type 0 over time
T = 0 #Define generation at which population gets fixed T
type0 = N/2 #no. of type 0s in the population
while sum(pop)/N != 1 and sum(pop)/N != 0:
    p = random.randint(0,N-1)
    q = pop[random.randint(0,N-1)]
    if pop[p] == 0:
        type0 -= 1
    del pop[p]
    pop.append(q)
    if q == 0:
        type0 += 1
    A.append(type0/N)
    T+=1
    #print(pop)
B = [1-x for x in A] #frequency of type 1 over time
plt.title("Moran process, N = 500")
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.plot(range(T+1),A, label = 'Type 0')
plt.plot(range(T+1),B, label = 'Type 1')
plt.legend()
plt.show()
