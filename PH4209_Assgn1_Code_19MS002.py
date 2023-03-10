import matplotlib.pyplot as plt
import random
#Define population size N, mutation rates u1, u2, and total generations T
N = 1000
u1 = 0.07
u2 = 0.001
T = 2000
#Define no. of individuals of each type 0 as A, type 1 as B 
A = N/2
B = N/2
#Define a list for frequency of Type 0 in each generations
freqA=[0.5]
#Initialize population with equal number of type 0 and type 1 individuals
pop = []
for i in range(int(N/2)):
    pop.append(0)
    pop.append(1)

#print(pop)

#Start loop over generations
for j in range (T):
    #Start loop over population
    for k in range(len(pop)):
        #Check if individual is type 0 or type 1
        if pop[k] == 0:
            r = random.random()
            #Mutate individual from 0 to 1 with probability u1
            if r<u1:
                pop[k] = 1
                B+=1
                A-=1
        else:
            r = random.random()
            #Mutate individual from 1 to 0 with probability u2
            if r<u2:
                pop[k] = 0
                A+=1
                B-=1
    freqA.append(A/N)
freqB = [1-x for x in freqA]
#print(freqA)
#print (freqB)
print(A/N,B/N)
#Record generation versus frequency data
plt.title("N = 1000, u1 = 0.07, u2 = 0.001, T = 2000")
plt.xlabel("Generations")
plt.ylabel("Frequency")
#T+1 is to compensate the 0th generation with 0.5 frequency
plt.plot(range(T+1),freqA, label = 'Type 0')
plt.plot(range(T+1),freqB, label = 'Type 1')
plt.legend()
plt.show()

