from Body import Body
import time
import numpy as np




G = -30

dt = 0.3

EPSILON = 25

ITERATION = 500

NUMBER_BODY = 100

SIZE = 3000


np.savetxt("gravity.cvs",[np.array([0.,0.,0.])],delimiter=',',fmt='%f')

Body.create_body(SIZE,NUMBER_BODY)
#Body.generate_ring(NUMBER_BODY,SIZE/10,SIZE,15,10)


start_time = time.time()



for i in range(0,ITERATION+1):
    Body.update(G,EPSILON,dt)
    print(i,time.time() - start_time)



exe_time = time.time() - start_time

print(exe_time)



