from pyplasm import *
# --- l = stair width
# --- n = number of steps
# --- g = height of ground
# --- a = raiser
# --- p = footprint
l = 50.0
n = 13.0
g = 4.0
a = 35.0/n 
p = l/n

vertex = [[0,0],[0,g+a/2.0],[p,a/2.0],[p,g+a/2.0]]
cells = [[1,2,3,4]]

# --- generate the step with vertex and cells
step2D = MKPOL([vertex,cells,None])

# --- generate the step in 3D from the step in 2D
step3D = PROD([step2D,Q(15)])
step3D = MAP([S1,S3,S2])(step3D)

# --- generate a singular stair
ramp = STRUCT(NN(n)([step3D,T([1,3])([p,a])]))

# --- traslate and multiplicate them to fit with the building
stair1 = T([1,2])([35,72])(ramp)

stair2 = T([1,2,3])([17.5,72,38])(ramp)

stair3 = T([1,2,3])([75,77,74])(ramp)

# --- putting all togheter---
building = STRUCT([stair1,stair2,stair3])
VIEW(building)