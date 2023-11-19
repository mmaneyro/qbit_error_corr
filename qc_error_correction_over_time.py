import numpy as np
import random as rm
import matplotlib.pyplot as pl

# simulation of three qubit bit flip error correction
# this code looks at how much we can extend the lifetime of the correct qubit by using this code (before we find an error we can't recover from)


# original state (to preserve) a|0>+b|1>
# then our logical qubit is a|000>+b|111>

#a and b are unknown
#however, we don't need to know this state to do the error correction procedure

# Possible errors considered: one of the three qubits flips

initial_state = np.array([1,1,1])  # logical qubits, eingenstates +1 of the stabilizers

# probability that qubit 1,2,3 flips at a given time step 
#independent for each qubit, here I asigned them arbitrarily to the same values
p1 = p2 = p3 = 0.1 #probability of each bit flipping in some time step

time = np.linspace(0,1000,1001) #time steps considered, if we wanted to we could see a flip probability for some time step and see how long the qubit survives in its state

error1_time = 0
error2_time = 0

for t in time:

    initial_state = np.array([1,1,1]) #Unless we reach an unrecoverable error I'm assuming we always start from a correct state (because for single bit flips we know how the operation needed to error correct)

    #generate tree random numbers between 0 and 1 which will determine if a qbit flipped
    flip1 = rm.random()
    flip2 = rm.random()
    flip3 = rm.random()

    # the state flips (or not) depending on where the random number falls relative to the probability
    if flip1 <= p1: 
        initial_state[0] *= -1
    if flip2 <= p2:
        initial_state[1] *= -1
    if flip3 <= p3:
        initial_state[2] *= -1

    #measurement

    S1 = initial_state[0]*initial_state[1] # will be 1 or -1 depending on if we had a flip in qubits 1 or 2 or not
    S2 = initial_state[1]*initial_state[2] # will be 1 or -1 depending on if we had a flip in qubits 2 or 3 or not

    # check for the occurence of two or more errors (unrecoverable)

    #three flips
    if error2_time==0:
        if initial_state[0] == -1 and initial_state[1] ==-1 and initial_state[2]==-1:
            print("Unrecoverable error at time ", t)
            error2_time = t
            print("The state was preserved for time", error2_time-error1_time, "after a bit flip happened")
            exit()
        #two flips
        elif initial_state[0]*initial_state[1]*initial_state[2]==1:
            if initial_state[0] == 1 and initial_state[1] == 1 and initial_state[2]== 1:
                pass
            else: 
                print("Unrecoverable error at time ", t)

                error2_time = t
                print("The state was preserved for time", error2_time-error1_time, "after a bit flip happened")
                exit()

    # check for the occurence of one error

    if error1_time == 0:
        if initial_state[0] == -1 or initial_state[1] ==-1 or initial_state[2]==-1:
            print("Correction of one error needed for the first time at time",t)
            error1_time = t

    #this is assumed to be corrected and the process allowed to continue

    # optionally we could see the error correction operations we would need to fix the errors  
    if S1 == -1 and S2 == -1: #qubit 2 flipped
        print("Error correct using X2")
    elif S1 == -1 and S2 == 1: #qubit 1 flipped
        print("Error correct using X1")
    elif S1 == 1 and S2 ==-1: #qubit 3 flipped
        print("Error correct using X3")
    else:
        print("No error correction needed")

