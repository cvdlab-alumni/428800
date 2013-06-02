from pyplasm import *

import scipy
from scipy import *

def VERTEXTRUDE((V,coords)):
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

def cumsum(iterable):
<<<<<<< HEAD
    # cumulative addition: list(cumsum(range(4))) => [0, 1, 3, 6]
=======
>>>>>>> 8102c8cf27bec7c81a48385f5f68a2e9ee298ed2
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
<<<<<<< HEAD
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
=======
        tube = [v + k*offset for k in range(m+1) for v in cell]
>>>>>>> 8102c8cf27bec7c81a48385f5f68a2e9ee298ed2
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

<<<<<<< HEAD
# puntiparabrezzayz = [[0,0.55, 5.15],[0,0.75, 5.66],[0,2.49, 5.66],[0,2.8, 5.14],[0,0.55, 5.15]]
# parabrezzayz = NURBSPLINE(2)(nodi(puntiparabrezzayz))(puntiparabrezzayz)

sidesxz = STRUCT([csidesxz1,csidesxz2,csidesxz3,csidesxz4,csidesxz5,csidesxz6,csidesxz7,csidesxz8,csidesxz9,csidesxz10,
	csidesxz11,csidesxz12,csidesxz13,csidesxz14,csidesxz15,csidesxz16,csidesxz17,csidesxz18])
=======
sidesxz = STRUCT([csidesxz1,csidesxz2,csidesxz3,csidesxz4,csidesxz5,csidesxz6,csidesxz7,csidesxz8,csidesxz9,csidesxz10,
  csidesxz11,csidesxz12,csidesxz13,csidesxz14,csidesxz15,csidesxz16,csidesxz17,csidesxz18])
>>>>>>> 8102c8cf27bec7c81a48385f5f68a2e9ee298ed2

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

<<<<<<< HEAD
=======
# adding details high
pfaro1 = [[0.72, 4.91],[0.64, 4.95],[0.77, 5.28],[0.85, 5.33],[1.09, 5.38],[1.13, 5.34],[1.08, 5.01],[1.03, 4.95],[0.72, 4.91]]
faro1 = NUBSPLINE(2)(nodi(pfaro1))(pfaro1)
psoprafaro1 = [[1.27, 5],[1.35, 5.39],[1.35, 5.39],[2.17, 5.45],[2.17, 5.45],[2.09, 5.06],[2.09, 5.06],[1.27, 5]]
soprafaro1 = NUBSPLINE(2)(nodi(psoprafaro1))(psoprafaro1)
prigafaro1 = [[0.7, 4.88],[0.7, 4.88],[2.66, 5.07]]
rigafaro1 = NUBSPLINE(2)(nodi(prigafaro1))(prigafaro1)

pfaro2 = [[0.85, 3.15],[0.76, 3.21],[0.65, 3.55],[0.7, 3.58],[1.03, 3.54],[1.08, 3.48],[1.14, 3.14],[1.1, 3.1],[0.85, 3.15]]
faro2 = NUBSPLINE(2)(nodi(pfaro2))(pfaro2)
prigafaro2 = [[0.7, 3.6],[0.7, 3.6],[2.64, 3.42]]
rigafaro2 = NUBSPLINE(2)(nodi(prigafaro2))(prigafaro2)
psoprafaro2 = [[1.35, 3.09],[1.29, 3.48],[1.29, 3.48],[2.05, 3.43],[2.05, 3.43],[2.16, 3.04],[2.16, 3.04],[1.35, 3.09]]
soprafaro2 = NUBSPLINE(2)(nodi(psoprafaro2))(psoprafaro2)
faro2 = T([1])([0.03])(faro2)

pperimetrocofano = [[0.89, 3.12],[0.77, 3.22],[0.49, 4.24],[0.71, 5.28],[0.85, 5.36],[3.13, 5.5],[3.19, 5.46],[2.66, 4.26],[3.19, 3.03],[3.13, 2.97],[0.89, 3.12]]
perimetrocofano = NUBSPLINE(2)(nodi(pperimetrocofano))(pperimetrocofano)

pfanalino1 = [[3.28, 5.45],[3.37, 5.74],[3.5, 5.77],[3.51, 5.57],[3.51, 5.57],[3.42, 5.54], [3.38, 5.45],[3.28, 5.45]]
fanalino1 = NUBSPLINE(2)(nodi(pfanalino1))(pfanalino1)

pfanalino2 = [[3.29, 3.02], [3.38, 3.03],[3.38, 2.97],[3.52, 2.9],[3.51, 2.68],[3.51, 2.68],[3.36, 2.73],[3.29, 3.02]]
fanalino2 = NUBSPLINE(2)(nodi(pfanalino2))(pfanalino2)

pparabrezza = [[3.08, 3.09],[2.65, 4.18],[3.06, 5.37],[3.06, 5.37],[3.93, 5.1],[3.98, 5.03],[3.86, 4.29],[3.97, 3.44],[3.95, 3.35],[3.08, 3.09]]
parabrezza = NUBSPLINE(2)(nodi(pparabrezza))(pparabrezza)
parabrezza = T([1])([0.07])(parabrezza)

pfinestrino2 = [[3.2, 3.02],[4.06, 3.29],[5.36, 3.31],[5.56, 3.26],[5.61, 3.18],[5.34, 2.98], [5.17, 2.97],[3.2, 3.02]]
finestrino2 = NUBSPLINE(2)(nodi(pfinestrino2))(pfinestrino2)

pfinestrino1 = [[3.19, 5.45],[5.17, 5.5], [5.38, 5.45],[5.58, 5.31],[5.51, 5.19],[4.2, 5.13],[3.93, 5.19],[3.19, 5.45]]
finestrino1 = NUBSPLINE(2)(nodi(pfinestrino1))(pfinestrino1)

plunotto = [[6.62, 3.35],[5.62, 3.42],[5.53, 3.51],[5.5, 4.94],[5.6, 5.03],[6.62, 5.1],[6.62, 5.1],[6.81, 4.26],[6.62, 3.35]]
lunotto = NUBSPLINE(2)(nodi(plunotto))(plunotto)

prigalunotto2 = [[6.63, 3.35],[6.63, 3.35],[7.23, 3.42]]
rigalunotto2 = NUBSPLINE(2)(nodi(prigalunotto2))(prigalunotto2)

prigalunotto1 = [[6.61, 5.11],[6.61, 5.11],[7.25, 5.02]]
rigalunotto1 = NUBSPLINE(2)(nodi(prigalunotto1))(prigalunotto1)

pseparatorefinestrino1 = [[5.06, 5.16], [5.09, 5.27], [4.97, 5.36], [4.97, 5.5]]
separatorefinestrino1 = BEZIERSTRIPE([pseparatorefinestrino1,0.2,11])

pseparatorefinestrino1 = [[5.06, 5.16], [5.09, 5.27], [4.97, 5.36], [4.97, 5.5]]
separatorefinestrino1 = BEZIERSTRIPE([pseparatorefinestrino1,0.2,11])

pseparatorefinestrino2 = [[4.98, 2.93], [5.02, 3.1], [5.05, 3.2], [5.09, 3.29]]
separatorefinestrino2 = BEZIERSTRIPE([pseparatorefinestrino2,0.2,11])

prigafinestrinodietro2 = [[5.02, 2.94],[5.02, 2.94],[6.31, 3.03],[6.61, 3.34]]
rigafinestrinodietro2 =  NUBSPLINE(2)(nodi(prigafinestrinodietro2))(prigafinestrinodietro2)

prigafinestrinodietro1 = [[4.97, 5.54],[4.97, 5.54],[6.47, 5.44],[6.62, 5.11]]
rigafinestrinodietro1 =  NUBSPLINE(2)(nodi(prigafinestrinodietro1))(prigafinestrinodietro1)

prighinafinestrino2 = [[3.18, 3.01],[3.18, 3.01],[3.06, 2.84]]
righinafinestrino2 =  NUBSPLINE(2)(nodi(prighinafinestrino2))(prighinafinestrino2)

prighinafinestrino1 = [[3.17, 5.43],[3.17, 5.43],[3.05, 5.63]]
righinafinestrino1 =  NUBSPLINE(2)(nodi(prighinafinestrino1))(prighinafinestrino1)

pretro = [[4.39, 5.61],[5.79, 5.64],[7.08, 5.42],[7.08, 5.42],[7.35, 4.26],[7.12, 3.08],[7.12, 3.08],[6.32, 2.86],[4.52, 2.84]]
retro =  NUBSPLINE(2)(nodi(pretro))(pretro)

pfanalino1 = [[7.28, 5.19],[7.22, 5.27],[7.19, 5.37],[7.27, 5.3],[7.28, 5.19]]
fanalino1 =  NUBSPLINE(2)(nodi(pfanalino1))(pfanalino1)

fanalino2 = T([1,2])([0.05,-0.15])(fanalino1)

pfanalino3 = [[7.37, 3.51],[7.39, 3.43],[7.34, 3.34], [7.3, 3.32], [7.31, 3.43],[7.37, 3.51]]
fanalino3 =  NUBSPLINE(2)(nodi(pfanalino3))(pfanalino3)

fanalino4 = T([1,2])([-0.05,-0.15])(fanalino3)

prigafanalini = [[7.31, 3.54], [7.34, 4.35],[7.28, 4.93],[7.28, 4.93],[7.37, 4.88],[7.37, 4.88],[7.46, 4.29],[7.4, 3.61],[7.4, 3.61],[7.31, 3.54]]
rigafanalini =  NUBSPLINE(2)(nodi(prigafanalini))(prigafanalini)

high= STRUCT([high,faro1,faro2,soprafaro1,rigafaro1,rigafaro2,soprafaro2,perimetrocofano,fanalino1,
  fanalino2,parabrezza,finestrino2,finestrino1,lunotto,rigalunotto2,rigalunotto1,separatorefinestrino1,
  separatorefinestrino2,rigafinestrinodietro2,rigafinestrinodietro1,righinafinestrino2,righinafinestrino1,
  retro,fanalino1,fanalino2,fanalino3,fanalino4,rigafanalini])

# adding details side
pforodavanti = [[0.55, 0,4.01],[0.51, 0,4.08],[0.54, 0,4.12],[0.75, 0,4.12],[0.8, 0,4.09],[0.77, 0,4.02],[0.71, 0,4.01],[0.55, 0,4.01]]
forodavanti =  NUBSPLINE(2)(nodi(pforodavanti))(pforodavanti)

prigasopraforo = [[0.38, 0,4.19],[0.38, 0,4.19],[1.42, 0,4.18],[1.5, 0,4.2]]
rigasopraforo =  NUBSPLINE(2)(nodi(prigasopraforo))(prigasopraforo)

def sidefun(points,y):
  points = map(lambda item: [item[0],y,item[1]], points)
  return NUBSPLINE(2)(nodi(points))(points)

rigavicinoruotadavanti = sidefun([[2.48, 4.24],[2.48, 4.24],[2.82, 4.25]],0)
sporgenza = sidefun([[5.32, 3.87],[3.32, 3.87],[3.02, 4],[2.8, 4.32],[2.85, 4.43],[7.13, 4.6],[7.28, 4.7], [7.36, 4.72]],0)
sottosporgenza = sidefun([[5.32, 3.74],[5.32, 3.74],[2.64, 3.76]],0)
sottovicinoruotasx = sidefun([[1.37, 3.86],[1.37, 3.86],[0.69, 3.9]],0)
buchettosottoavanti = sidefun([[0.51, 3.9],[0.63, 3.9],[0.69, 3.87],[0.69, 3.82],[0.63, 3.81],[0.45, 3.81]],0)
finestrinos = sidefun([[3.33, 4.72],[3.9, 5.15],[4.3, 5.24],[5.1, 5.2],[5.54, 5.12],[5.57, 4.96],[5.34, 4.79],[4.98, 4.74],[3.33, 4.72]],0)
parabrezzas = sidefun([[3.09, 4.71],[3.88, 5.22],[3.95, 5.27],[3.88, 5.29],[2.79, 4.75],[2.91, 4.71],[3.09, 4.71]],0)
lunottos = sidefun([[5.47, 5.25],[5.47, 5.25],[6.62, 4.85],[6.62, 4.85],[6.79, 4.88]],0)
cofanos = sidefun([[0.66, 4.24],[0.66, 4.24],[1.32, 4.53],[2.49, 4.63],[3.14, 4.65]],0)
rigasxsportello = sidefun([[3.14, 4.66],[3.14, 4.66],[3.03, 4.48], [3.1, 3.95]],0)
rigadxsportello = sidefun([[4.78, 3.88],[4.78, 3.88],[4.97, 4.55],[4.95, 4.7]],0)
rigadxruota = sidefun([[6.51, 3.91],[6.51, 3.91],[6.98, 3.96],[7.43, 3.94]],0)
rigadxruotasopra = sidefun([[6.4, 4.22],[6.4, 4.22],[7.51, 4.25]],0)
rigadxruotasopra2 = sidefun([[6.32, 4.29],[6.32, 4.29],[7.47, 4.31]],0)
rlucepost1 =sidefun([[7.37, 4.63],[7.23, 4.62],[7.14, 4.55]],0)
lucepost1 = sidefun([[7.3, 4.58],[7.28, 4.49],[7.35, 4.38],[7.37, 4.47],[7.3, 4.58]],0)
lucepost2 = T([1,3])([-0.1,-0.01])(lucepost1)

side = STRUCT([side,forodavanti,rigasopraforo,rigavicinoruotadavanti,sporgenza,sottosporgenza,sottovicinoruotasx
  ,buchettosottoavanti,finestrinos,parabrezzas,lunottos,cofanos,rigasxsportello,rigadxsportello
  ,rigadxruota,rigadxruotasopra,rigadxruotasopra2,rlucepost1,lucepost1,lucepost2])


#adding details front

def frontfun(points,x):
  points = map(lambda item: [x,-item[0],item[1]], points)
  return NUBSPLINE(2)(nodi(points))(points) 

fanalino1f = frontfun([[0.66, 4.73], [0.6, 4.76],[0.54, 4.85],[0.57, 4.88],[0.92, 4.88], [0.98, 4.85], [1.01, 4.77],[0.96, 4.72],[0.66, 4.73]],0)
bucodavanti = frontfun([[1.05, 4.54],[2.27, 4.52],[2.33, 4.49],[2.19, 4.37],[1.66, 4.33],[1.06, 4.39],[0.92, 4.42],[1.05, 4.54]],0)
fanalino2f = frontfun([[2.37, 4.73],[2.3, 4.77],[2.34, 4.86],[2.39, 4.89],[2.73, 4.88],[2.77, 4.85],[2.71, 4.75],[2.66, 4.74],[2.37, 4.73]],0)
rettsopraf2 = frontfun([[2.4, 4.95],[2.46, 5.08],[2.46, 5.08],[2.83, 5.04],[2.83, 5.04],[2.78, 4.93],[2.78, 4.93],[2.4, 4.95]],0)
rettsopraf1 = frontfun([[0.52, 4.93],[0.48, 5.05],[0.48, 5.05],[0.83, 5.08],[0.83, 5.08],[0.9, 4.95], [0.9, 4.95], [0.52, 4.93]],0)
riga1 = frontfun([[0.84, 5.12],[0.84, 5.12],[1.03, 4.76]],0)
riga2 = frontfun([[2.47, 5.12],[2.47, 5.12],[2.27, 4.77]],0)
rparaurti1 = frontfun([[0.37, 4.66], [0.37, 4.66], [1.64, 4.63], [2.93, 4.65]],0)
buco2f = frontfun([[2.93, 4.65],[2.93, 4.65], [2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65]],0)
parabrezzaf = frontfun([[2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65],[2.93, 4.65]],0)


front = STRUCT([front,fanalino1f,bucodavanti,fanalino2f,rettsopraf2,rettsopraf1,riga1,riga2,rparaurti1,
  buco2f,parabrezzaf])

>>>>>>> 8102c8cf27bec7c81a48385f5f68a2e9ee298ed2
front = T([2,3])([3,-4])(front)
high = T([1,2])([0.,-2.85])(high)
side = T(3)(-3.3)(side)

high = T([1,2,3])([-4,-1.5,0.5])(high)
side = T([1,3])([-4,-0.5])(side)
<<<<<<< HEAD
front = T([2,3])([-1.5,-0.25])(front)
=======
front = T([2,3])([-1.5,-0.25])(front)


# VIEW(STRUCT([front,side,high]))
#non mi aggiungeva piu' linee
# VIEW(side)
>>>>>>> 8102c8cf27bec7c81a48385f5f68a2e9ee298ed2
