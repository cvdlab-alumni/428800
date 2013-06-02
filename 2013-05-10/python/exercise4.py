#exercise 4
def traslaPointsZ(points,value):
	return map(lambda item:\
		[item[0],item[1],item[2]+value], points)

#Funzione che trasla i punti sull'asse y
def traslaPointsY(points,value):
	return map(lambda item:\
		[item[0],item[1]+value,item[2]], points)

#Funzione che trasla i punti sull'asse x
def traslaPointsX(points,value):
	return map(lambda item:\
		[item[0]+value,item[1],item[2]], points)

def scalePoints(points,values):
	return map(lambda item:\
		map(lambda elem: elem*values, item), points)

def bezier_circle_map(r,selector):
	base_points = [[-1,0,0],[-1,1.6,0],[1.6,1.6,0],[1.6,0,0],[1.6,-1.6,0],[-1,-1.6,0],[-1,0,0]];
	circle_points = scalePoints(base_points,r);
	return BEZIER(selector)(circle_points)

def bezier_circle_not_centered_map(r,x_value,y_value,z_value,selector):

	base_points = [[-1,0,0],[-1,1.6,0],[1.6,1.6,0],[1.6,0,0],[1.6,-1.6,0],[-1,-1.6,0],[-1,0,0]]
	circle_points = scalePoints(base_points,r)

	if (x_value != 0):
		circle_points = traslaPointsX(circle_points,x_value)
	if (y_value != 0):
		circle_points = traslaPointsY(circle_points,y_value)
	if (z_value != 0):
		circle_points = traslaPointsZ(circle_points,z_value)

	return BEZIER(selector)(circle_points)

def circle(r):
	def ball(p):
 		a,r = p
		return [r*COS(a), r*SIN(a)]
	dom2D = PROD([INTERVALS(2*PI)(50), INTERVALS(1)(1)])
	return S([1,2])([r,r])(MAP(ball)(dom2D))

def extrude(obj,z):
	return PROD([obj, Q(z)])


bordovolante = TORUS([0.1,0.15])([20,20])
bordovolante = COLOR(BLACK)(bordovolante)

primopezzo1 = [[0.31, 4.86,0], [0.65, 4.68,0], [0.79, 4.62,0], [1.26, 4.49,0]]
primopezzo2 = [[1.26, 4.49,0], [1.24, 4.35,0], [1.23, 4.37,0], [1.25, 4.15,0]]
primopezzo3 = [[1.25, 4.15,0], [0.81, 4.29,0], [0.61, 4.53,0], [0.31, 4.42,0]]
primopezzo4 = [[0.31, 4.42,0], [0.27, 4.57,0], [0.32, 4.77,0], [0.31, 4.86,0]]

supp1 = BEZIERCURVE(primopezzo1)
supp2 = BEZIERCURVE(primopezzo2)
supp3 = BEZIERCURVE(primopezzo3)
supp4 = BEZIERCURVE(primopezzo4)

bucoprimopezzo1 = [[0.74, 4.52,0], [0.86, 4.49,0], [0.94, 4.46,0], [1.09, 4.39,0]]
bucoprimopezzo2 = [[1.09, 4.39,0], [1.08, 4.39,0], [1.12, 4.35,0], [1.06, 4.32,0]]
bucoprimopezzo3 = [[1.06, 4.32,0], [0.92, 4.37,0], [0.87, 4.4,0], [0.74, 4.48,0]]
bucoprimopezzo4 = [[0.74, 4.48,0], [0.68, 4.51,0], [0.72, 4.53,0], [0.74, 4.52,0]]

bsupp1 = BEZIER(S1)(bucoprimopezzo1)
bsupp2 = BEZIER(S1)(bucoprimopezzo2)
bsupp3 = BEZIER(S1)(bucoprimopezzo3)
bsupp4 = BEZIER(S1)(bucoprimopezzo4)


ssbs1 = BEZIER(S2)([supp1,bsupp1])
ssbs2 = BEZIER(S2)([supp2,bsupp2])
ssbs3 = BEZIER(S2)([supp3,bsupp3])
ssbs4 = BEZIER(S2)([supp4,bsupp4])

osbs1 = MAP(ssbs1)(domain2)
osbs2 = MAP(ssbs2)(domain2)
osbs3 = MAP(ssbs3)(domain2)
osbs4 = MAP(ssbs4)(domain2)

primopezzo1z = traslaPointsZ(primopezzo1,0.01)
primopezzo2z = traslaPointsZ(primopezzo2,0.01)
primopezzo3z = traslaPointsZ(primopezzo3,0.01)
primopezzo4z = traslaPointsZ(primopezzo4,0.01)

supp1z = BEZIERCURVE(primopezzo1z)
supp2z = BEZIERCURVE(primopezzo2z)
supp3z = BEZIERCURVE(primopezzo3z)
supp4z = BEZIERCURVE(primopezzo4z)

bucoprimopezzo1z = traslaPointsZ(bucoprimopezzo1,0.01)
bucoprimopezzo2z = traslaPointsZ(bucoprimopezzo2,0.01)
bucoprimopezzo3z = traslaPointsZ(bucoprimopezzo3,0.01)
bucoprimopezzo4z = traslaPointsZ(bucoprimopezzo4,0.01)

bsupp1z = BEZIER(S1)(bucoprimopezzo1z)
bsupp2z = BEZIER(S1)(bucoprimopezzo2z)
bsupp3z = BEZIER(S1)(bucoprimopezzo3z)
bsupp4z = BEZIER(S1)(bucoprimopezzo4z)

ssbs1z = BEZIER(S2)([supp1,supp1z])
ssbs2z = BEZIER(S2)([supp2,supp2z])
ssbs3z = BEZIER(S2)([supp3,supp3z])
ssbs4z = BEZIER(S2)([supp4,supp4z])

bssbs1z = BEZIER(S2)([bsupp1,bsupp1z])
bssbs2z = BEZIER(S2)([bsupp2,bsupp2z])
bssbs3z = BEZIER(S2)([bsupp3,bsupp3z])
bssbs4z = BEZIER(S2)([bsupp4,bsupp4z])

osbs1 = MAP(ssbs1)(domain2)
osbs2 = MAP(ssbs2)(domain2)
osbs3 = MAP(ssbs3)(domain2)
osbs4 = MAP(ssbs4)(domain2)

ob1z = MAP(bssbs1z)(domain2)
ob2z = MAP(bssbs2z)(domain2)
ob3z = MAP(bssbs3z)(domain2)
ob4z = MAP(bssbs4z)(domain2)

os1z = MAP(ssbs1z)(domain2)
os2z = MAP(ssbs2z)(domain2)
os3z = MAP(ssbs3z)(domain2)
os4z = MAP(ssbs4z)(domain2)


osbstru = STRUCT([osbs1,osbs2,osbs3,osbs4])
osbstruT = T([3])([0.01])(osbstru)

manico1 = STRUCT([osbstru,osbstruT,ob1z,ob2z,ob3z,ob4z,os1z,os2z,os3z,os4z])
manico1 = S([1,2])([0.12,0.12])(manico1)
manico1 = T([1,2])([-0.16,-0.52])(manico1)

manico2 = R([1,2])(2*PI/3)(manico1)
manico3 = R([1,2])(2*PI/3)(manico2)

manico = STRUCT([manico1,manico2,manico3])
manico = COLOR(GREEN)(manico)

centrovolante = circle(0.02)
centrovolante = extrude(centrovolante,0.01)
centrovolante = COLOR(YELLOW)(centrovolante)

volante = STRUCT([bordovolante,manico,centrovolante])
volante = R([1,3])(-PI/2)(volante)
volante = T([1,2,3])([4,1,1.5])(volante)

volante = T([1,2,3])([-4,-1.5,-0.4])(volante)
