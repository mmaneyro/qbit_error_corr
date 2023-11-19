import numpy as np
import random as rm
import matplotlib.pyplot as pl

# simulation of three qubit bit flip error correction
# this code looks at the rates of failure of the error correction for different bit flip probabilities

# original state (to preserve) a|0>+b|1>
# then our logical qubit is a|000>+b|111>

#a and b are unknown
#however, we don't need to know this state to do the error correction procedure

# Possible errors considered: one of the three qubits flips

initial_state = np.array([1,1,1])  # logical qubits, eingenstates +1 of the stabilizers

# probability that qubit 1,2,3 flips at a given time step 
#independent for each qubit, here I asigned them arbitrarily to the same values
p1 = p2 = p3 = np.linspace(0,1,21)

ntests=10000 # for each case I'll test what percentage of time the bit flip code manages to preserve the qubit state
failure = np.zeros(len(p1)) #this vector will store the amount of correction failures for each probability value

for i in range(len(p1)):
    for j in range(ntests):

        initial_state = np.array([1,1,1]) #Unless we reach an unrecoverable error I'm assuming we always start from a correct state (because for single bit flips we know how the operation needed to error correct)

        #generate tree random numbers between 0 and 1 which will determine if a qbit flipped
        flip1 = rm.random()
        flip2 = rm.random()
        flip3 = rm.random()

        # the state flips (or not) depending on where the random number falls relative to the probability
        if flip1 <= p1[i]: 
            initial_state[0] *= -1
        if flip2 <= p2[i]:
            initial_state[1] *= -1
        if flip3 <= p3[i]:
            initial_state[2] *= -1

        #measurement

        S1 = initial_state[0]*initial_state[1] # will be 1 or -1 depending on if we had a flip in qubits 1 or 2 or not
        S2 = initial_state[1]*initial_state[2] # will be 1 or -1 depending on if we had a flip in qubits 2 or 3 or not

        # check for the occurence of two or more errors (unrecoverable)

        #three flips
        if initial_state[0] == -1 and initial_state[1] ==-1 and initial_state[2]==-1:
            failure[i] += 1
        #two flips
        elif initial_state[0]*initial_state[1]*initial_state[2]==1:
            if initial_state[0] == 1 and initial_state[1] == 1 and initial_state[2]== 1:
                pass
            else: 
                failure[i] += 1




success_rate = (np.ones(len(p1))*ntests - failure)/ntests

pl.xlabel("Qubit flip probability")
pl.ylabel("Success rate over 10000 tests")
pl.plot(p1,success_rate)
pl.show()
