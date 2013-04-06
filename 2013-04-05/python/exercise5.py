from pyplasm import *

l = 50.0
n = 13.0
g = 4.0
a = 35.0/n 
p = l/n

vertici = [[0,0],[0,g+a/2.0],[p,a/2.0],[p,g+a/2.0]]
celle = [[1,2,3,4]]
step2D = MKPOL([vertici,celle,None])

step3D = PROD([step2D,Q(15)])
step3D = MAP([S1,S3,S2])(step3D)

ramp = STRUCT(NN(n)([step3D,T([1,3])([p,a])]))

# VIEW(ramp)

stair1 = T([1,2])([35,72])(ramp)

stair2 = T([1,2,3])([17.5,72,38])(ramp)

stair3 = T([1,2,3])([75,77,74])(ramp)