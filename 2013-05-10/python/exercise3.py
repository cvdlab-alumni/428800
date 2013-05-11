#esercizio 3
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


gomma1=bezier_circle_map(0.5,S1)
gomma2=bezier_circle_map(0.3,S1)
gomma3 = bezier_circle_not_centered_map(0.5,0,0,-0.25,S1)
gomma4 = bezier_circle_not_centered_map(0.3,0,0,-0.25,S1)


cgomma1 = MAP(gomma1)(INTERVALS(1)(32))
cgomma2 = MAP(gomma2)(INTERVALS(1)(32))

sgomma = BEZIER(S2)([gomma1,gomma2])
sgomma2 = BEZIER(S2)([gomma3,gomma4])
sgomma3 = BEZIER(S2)([gomma1,gomma3])
sgomma4 = BEZIER(S2)([gomma2,gomma4])

ogomma = MAP(sgomma)(domain2)
ogomma2 = MAP(sgomma2)(domain2)
ogomma3 = MAP(sgomma3)(domain2)
ogomma4 = MAP(sgomma4)(domain2)

ruota = STRUCT([ogomma,ogomma2,ogomma3,ogomma4])
ruota = R([2,3])((PI/2))(ruota)
ruota = T([1,3])([2,0.49])(ruota)


# [[1.71, 4.08,0], [1.88, 3.97,0], [1.95, 3.98,0], [1.92, 4.2,0]]

cerchione1points = [[1.71-1.71, 4.08-4.08,0], [1.88-1.71, 3.97-4.08,0], [1.95-1.71, 3.9-4.08,0], [1.92-1.71, 4.2-4.08,0]]
fcerchione1 = BEZIER(S1)(cerchione1points)
# ccerchione1 = MAP(fcerchione1)(domain)

# [[1.71, 4.08,0], [1.75, 4.17,0], [1.83, 4.21,0], [1.92, 4.2,0]]

cerchione2points = [[1.71-1.71, 4.08-4.08,0], [1.75-1.71, 4.17-4.08,0], [1.83-1.71, 4.21-4.08,0], [1.92-1.71, 4.2-4.08,0]]
fcerchione2 = BEZIER(S1)(cerchione2points)
# ccerchione2 = MAP(fcerchione2)(domain)

ffcerchione = BEZIER(S2)([fcerchione1,fcerchione2])

cerchione1pointsz = traslaPointsZ(cerchione1points,0.25)
fcerchione1z = BEZIER(S1)(cerchione1pointsz)
ffcerchione1z = BEZIER(S2)([fcerchione1,fcerchione1z])
scerchione1z = MAP(ffcerchione1z)(domain2)

cerchione2pointsz = traslaPointsZ(cerchione2points,0.25)
fcerchione2z = BEZIER(S1)(cerchione2pointsz)
ffcerchione2z = BEZIER(S2)([fcerchione2,fcerchione2z])
scerchione2z = MAP(ffcerchione2z)(domain2)

scerchione = MAP(ffcerchione)(domain2)
scerchione2 = T([3])([0.25])(scerchione)

cerchione = STRUCT([scerchione,scerchione2z,scerchione1z,scerchione2])


cerchione = T([1,2])([-0.23,0.15])(cerchione)
# cerchione = R([1,2])(-0.2)(cerchione)
# mat = CONS(AA(R([1,2]))([(12*PI)/30,(12*PI)/30,(12*PI)/30,(12*PI)/30]))
c1 = R([1,2])((12*PI)/30)(cerchione)
c2 = R([1,2])((12*PI)/30)(c1)
c3 = R([1,2])((12*PI)/30)(c2)
c4 = R([1,2])((12*PI)/30)(c3)
c5 = R([1,2])((12*PI)/30)(c4)



# cerchions = STRUCT(mat(cerchione))
cerchions2d = STRUCT([c1,c2,c3,c4,c5])
# cerchions3d = PROD([(cerchions2d),QUOTE([1])])
cerchions2d = R([2,3])((-PI/2))(cerchions2d)
cerchions2d = T([1,3])([2,0.49])(cerchions2d)

cerchio = circle(0.38)
cerchio = extrude(cerchio,0.05)
cerchio = R([2,3])((-PI/2))(cerchio)
cerchio = T([1,2,3])([2,0.075,0.49])(cerchio)


wheel = STRUCT([COLOR(BLACK)(ruota),COLOR(RED)(cerchions2d),COLOR(YELLOW)(cerchio)])
wheel = T([1,2,3])([-4,-1.5,-0.4])(wheel)
w1 = T([1])([3.95])(wheel)
w2 = T([2])([2.70])(wheel)
w3 = T([1,2])([3.95,2.70])(wheel)

wheels4 = STRUCT([wheel,w1,w2,w3])
