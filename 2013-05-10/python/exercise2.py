from pyplasm import *

import scipy
from scipy import *

def VERTEXTRUDE((V,coords)):
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

def cumsum(iterable):
    # cumulative addition: list(cumsum(range(4))) => [0, 1, 3, 6]
    iterable = iter(iterable)
    s = iterable.next()
    yield s
    for c in iterable:
        s = s + c
        yield s

def larExtrude(model,pattern):
    V,FV = model
    d = len(FV[0])
    offset = len(V)
    m = len(pattern)
    outcells = []
    for cell in FV:
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
        rangelimit = len(tube)-d
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube,newshape=(m,d,d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    outcells = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    outVerts = VERTEXTRUDE((V,coords))
    newModel = outVerts, CAT(outcells)
    return newModel

def GRID(args):
    model = ([[]],[[0]])
    for k,steps in enumerate(args):
        model = larExtrude(model,steps*[1])
    V,cells = model
    verts = AA(list)(scipy.array(V) / AA(float)(args))
    return MKPOL([verts, AA(AA(lambda h:h+1))(cells), None])

def nodi(points):
  m = len(points)
  k = 2
  n = m+k+1
  l = n-3
  j = 1
  knots = []
  for i in range(n):
    if(i<=2):
      knots += [0]
    if(2<i<l):
      knots += [j]
      j= j+1
    if(i>=l):
      knots += [j]
  return knots

domain = INTERVALS(1)(10)
domain = GRID([15])
domain2 = GRID([10,10])
Domain3 = GRID([5,5,5])

# exercise 2
sidesxz1 = [[0.37,0,4.24], [1.41, 0,4.78], [2.37, 0,4.6], [2.71, 0,4.78]]
fsidesxz1 = BEZIERCURVE(sidesxz1)
csidesxz1 = MAP(fsidesxz1)(domain)

sidesxz2 = [[2.71,0, 4.78], [3.3, 0,5.05], [3.56, 0,5.2], [3.88, 0,5.3]]
fsidesxz2 = BEZIERCURVE(sidesxz2)
csidesxz2 = MAP(fsidesxz2)(domain)

sidesxz3 = [[3.88, 0,5.3], [4.32, 0,5.41], [4.47, 0,5.41], [5.49, 0,5.28]]
fsidesxz3 = BEZIERCURVE(sidesxz3)
csidesxz3 = MAP(fsidesxz3)(domain)

sidesxz4 = [[5.49, 0,5.28], [6.28, 0,5.06], [6.68, 0,4.94], [7.35, 0,4.72]]
fsidesxz4 = BEZIERCURVE(sidesxz4)
csidesxz4 = MAP(fsidesxz4)(domain)

sidesxz5 = [[7.35, 0,4.72], [7.34, 0,4.64], [7.37, 0,4.64], [7.38, 0,4.59]]
fsidesxz5 = BEZIERCURVE(sidesxz5)
csidesxz5 = MAP(fsidesxz5)(domain)

sidesxz6 = [[7.38, 0,4.59], [7.43, 0,4.49], [7.43, 0,4.49], [7.48, 0,4.32]]
fsidesxz6 = BEZIERCURVE(sidesxz6)
csidesxz6 = MAP(fsidesxz6)(domain)

sidesxz7 = [[7.48, 0,4.32], [7.56, 0,4.26], [7.51, 0,4.3], [7.54, 0,4.14]]
fsidesxz7 = BEZIERCURVE(sidesxz7)
csidesxz7 = MAP(fsidesxz7)(domain)

sidesxz8 = [[7.54, 0,4.14], [7.47, 0,4.08], [7.48, 0,4.12], [7.45, 0,3.94]]
fsidesxz8 = BEZIERCURVE(sidesxz8)
csidesxz8 = MAP(fsidesxz8)(domain)

sidesxz9 = [[7.45, 0,3.94], [7.42, 0,3.9], [7.4, 0,3.79], [7.37, 0,3.75]]
fsidesxz9 = BEZIERCURVE(sidesxz9)
csidesxz9 = MAP(fsidesxz9)(domain)

sidesxz10 = [[7.37, 0,3.75], [7.12, 0,3.7], [6.73, 0,3.69], [6.56, 0,3.69]]
fsidesxz10 = BEZIERCURVE(sidesxz10)
csidesxz10 = MAP(fsidesxz10)(domain)

sidesxz11= [[6.56, 0,3.69], [6.56, 0,4.65], [5.31, 0,4.73], [5.33, 0,3.68]]
fsidesxz11 = BEZIERCURVE(sidesxz11)
csidesxz11 = MAP(fsidesxz11)(domain)

sidesxz12 = [[5.31, 0,3.67], [4.09, 0,3.71], [3.31, 0,3.7], [2.62, 0,3.68]]
fsidesxz12 = BEZIERCURVE(sidesxz12)
csidesxz12 = MAP(fsidesxz12)(domain)

sidesxz13 = [[2.62, 0,3.7], [2.68, 0,4.64], [1.38, 0,4.76], [1.38,0, 3.73]]
fsidesxz13 = BEZIERCURVE(sidesxz13)
csidesxz13 = MAP(fsidesxz13)(domain)

sidesxz14 = [[1.38, 0,3.73], [1.07, 0,3.75], [0.79, 0,3.77], [0.43, 0,3.79]]
fsidesxz14 = BEZIERCURVE(sidesxz14)
csidesxz14 = MAP(fsidesxz14)(domain)

sidesxz15 = [[0.43, 0,3.79], [0.45, 0,3.79], [0.42, 0,3.86], [0.43, 0,3.92]]
fsidesxz15 = BEZIERCURVE(sidesxz15)
csidesxz15 = MAP(fsidesxz15)(domain)

sidesxz16 = [[0.43, 0,3.92], [0.51, 0,3.92], [0.57, 0,4.16], [0.37, 0,4.14]]
fsidesxz16 = BEZIERCURVE(sidesxz16)
csidesxz16 = MAP(fsidesxz16)(domain)

sidesxz17 = [[0.37, 0,4.14], [0.35, 0,4.17], [0.36, 0,4.18], [0.37, 0,4.24]]
fsidesxz17 = BEZIERCURVE(sidesxz17)
csidesxz17 = MAP(fsidesxz17)(domain)

sidesxz18 = [[0.46, 0,3.93], [0.42, 0,3.99], [0.39, 0,4.05], [0.39,0, 4.14]]
fsidesxz18 = BEZIERCURVE(sidesxz18)
csidesxz18 = MAP(fsidesxz18)(domain)

# puntiparabrezzayz = [[0,0.55, 5.15],[0,0.75, 5.66],[0,2.49, 5.66],[0,2.8, 5.14],[0,0.55, 5.15]]
# parabrezzayz = NURBSPLINE(2)(nodi(puntiparabrezzayz))(puntiparabrezzayz)

sidesxz = STRUCT([csidesxz1,csidesxz2,csidesxz3,csidesxz4,csidesxz5,csidesxz6,csidesxz7,csidesxz8,csidesxz9,csidesxz10,
	csidesxz11,csidesxz12,csidesxz13,csidesxz14,csidesxz15,csidesxz16,csidesxz17,csidesxz18])

sidesxzT = T([2])([2.77])(sidesxz)

side = STRUCT([sidesxz])

highxy1 = [[1.43, 2.83,0], [0.32, 3.15,0], [0.55, 3.43,0], [0.37, 4.33,0]]
fhighxy1 = BEZIERCURVE(highxy1)
chighxy1 =  MAP(fhighxy1)(domain)

highxy2 = [[0.37, 4.33,0], [0.46, 4.63,0], [0.22, 5.44,0], [1.44, 5.63,0]]
fhighxy2 = BEZIERCURVE(highxy2)
chighxy2 =  MAP(fhighxy2)(domain)

highxy3 = [[1.44, 5.63,0], [3.53, 5.66,0], [3.11, 5.58,0], [6.39, 5.68,0]]
fhighxy3 = BEZIERCURVE(highxy3)
chighxy3 =  MAP(fhighxy3)(domain)

highxy4 = [[6.39, 5.68,0], [6.75, 5.63,0], [7.07, 5.52,0], [7.2, 5.43,0]]
fhighxy4 = BEZIERCURVE(highxy4)
chighxy4 =  MAP(fhighxy4)(domain)

highxy5 = [[7.2, 5.43,0], [7.48, 5.15,0], [7.72, 4.01,0], [7.25, 3.05,0]]
fhighxy5 = BEZIERCURVE(highxy5)
chighxy5 =  MAP(fhighxy5)(domain)

highxy6 = [[7.22, 3.06,0], [6.19, 2.56,0], [3.95, 2.94,0], [1.47, 2.83,0]]
fhighxy6 = BEZIERCURVE(highxy6)
chighxy6 =  MAP(fhighxy6)(domain)

high = STRUCT([chighxy1,chighxy2,chighxy3,chighxy4,chighxy5,chighxy6])

frontyz1 = [[0,-0.29, 5.01], [0,-0.41, 5.2], [0,-0.52, 5.4], [0,-0.8, 5.72]]
ffrontyz1 = BEZIERCURVE(frontyz1)
cfrontyz1 = MAP(ffrontyz1)(domain)

frontyz2 = [[0,-0.8, 5.72], [0,-1.1, 5.8], [0,-1.94, 5.8], [0,-2.48, 5.74]]
ffrontyz2 = BEZIERCURVE(frontyz2)
cfrontyz2 = MAP(ffrontyz2)(domain)

frontyz3 = [[0,-2.48, 5.74], [0,-2.7, 5.52], [0,-2.72, 5.47], [0,-2.93, 5.14]]
ffrontyz3 = BEZIERCURVE(frontyz3)
cfrontyz3 = MAP(ffrontyz3)(domain)

frontyz4 = [[0,-2.93, 5.14], [0,-2.95, 5.13], [0,-2.99, 5.06], [0,-3, 5]]
ffrontyz4 = BEZIERCURVE(frontyz4)
cfrontyz4 = MAP(ffrontyz4)(domain)

frontyz5 = [[0,-3, 5], [0,-2.94, 4.41], [0,-2.98, 4.72], [0,-2.88, 4.12]]
ffrontyz5 = BEZIERCURVE(frontyz5)
cfrontyz5 = MAP(ffrontyz5)(domain)

frontyz6 = [[0,-2.88, 4.12], [0,-2.77, 4.22], [0,-0.62, 4.24], [0,-0.43, 4.11]]
ffrontyz6 = BEZIERCURVE(frontyz6)
cfrontyz6 = MAP(ffrontyz6)(domain)

frontyz7 = [[0,-0.43, 4.11], [0,-0.25, 4.45], [0,-0.46, 4.74], [0,-0.29, 4.86]]
ffrontyz7 = BEZIERCURVE(frontyz7)
cfrontyz7 = MAP(ffrontyz7)(domain)

frontyz8 = [[0,-0.29, 4.86], [0,-0.27, 4.87], [0,-0.29, 4.88], [0,-0.29, 5.01]]
ffrontyz8 = BEZIERCURVE(frontyz8)
cfrontyz8 = MAP(ffrontyz8)(domain)

front = STRUCT([cfrontyz1,cfrontyz2,cfrontyz3,cfrontyz4,cfrontyz5,cfrontyz6,cfrontyz7,cfrontyz8])

front = T([2,3])([3,-4])(front)
high = T([1,2])([0.,-2.85])(high)
side = T(3)(-3.3)(side)

high = T([1,2,3])([-4,-1.5,0.5])(high)
side = T([1,3])([-4,-0.5])(side)
front = T([2,3])([-1.5,-0.25])(front)