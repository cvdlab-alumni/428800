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


#exercise 5
#sup1
psx = [[3.1, 0,3.95], [3.08, 0,4.34], [3, 0,4.61], [3.19, 0,4.7]]
pdx = [[4.77, 0,3.87], [5.05, 0,4.64], [4.88, 0,4.64], [4.95, 0,4.78]]

psxc1 = [[3.0, 0,3.95], [3.00, -0.4,4.34], [3, -0.2,4.61], [3.19, 0,4.7]]


cpsx = BEZIER(S1)(psx)
cpdx = BEZIER(S1)(pdx)

cpsxc1 = BEZIER(S1)(psxc1)


sup1 = BEZIER(S2)([cpsx,cpsxc1,cpdx])

osup1 = MAP(sup1)(domain2)
osup1 = COLOR(RED)(osup1)

lato1dx = [[4.94, 4.76], [4.98, 4.96], [5.02, 5.01], [5.05, 5.19]]
lato2sx = [[3.24, 4.68], [4.03, 5.36], [4.51, 5.31], [5.05, 5.19]]
lato3sx = [[3.25, 4.71], [4.11, 4.68], [4.66, 4.7], [4.94, 4.76]]


l1 = BEZIERSTRIPE([lato1dx,0.05,10])
l2 = BEZIERSTRIPE([lato2sx,0.05,10])
l3 = BEZIERSTRIPE([lato3sx,0.05,10])

finestrino = STRUCT([l1,l2,l3])

finestrino = R([2,3])(PI/2)(finestrino)
finestrino = T([1,3])([-0.01,-0.025])(finestrino)

finestrino = COLOR(RED)(finestrino)

finestrino = S(2)(-1)(finestrino)


superficie1 = STRUCT([osup1,finestrino])
superficie1 = T([3])([-3.3])(superficie1)
superficie1 = T([1,2,3])([-4,-1.5,-0.5])(superficie1)

#sup2
# cofano1 = [[3.13, 2.99,0], [2.12, 3.04,0], [1.83, 2.87,0], [0.73, 3.18,0]]
# cofano2 = [[0.73, 3.18,0], [0.33, 3.78,0], [0.46, 5.18,0], [0.77, 5.26,0]]
# # cofano3 = [[0.77, 5.26], [1.29, 5.44], [1.88, 5.51], [3.07, 5.5]]
# cofano3 = [[3.07, 5.5,0], [1.29, 5.44,0], [1.88, 5.51,0],[0.77, 5.26,0]]
# # cofano4 = [[3.07, 5.5], [2.67, 5.33], [2.35, 3.52], [3.13, 2.99]]
# cofano4 = [[3.13, 2.99,0], [2.67, 5.33,0], [2.35, 3.52,0],[3.07, 5.5,0]]

cofano1 = [[0.84, 5.36,0], [0.45, 5.14,0], [0.36, 3.72,0], [0.76, 3.15,0]]
cofano2 = [[1.31, 5.41,0.1], [0.86, 4.88,0.1], [0.92, 3.46,0.1], [1.27, 3.02,0.1]]
cofano3 = [[1.76, 5.44,0.2], [1.39, 4.76,0.2], [1.49, 3.45,0.2], [1.73, 3,0.2]]
cofano4 = [[2.3, 5.47,0.4], [1.97, 4.99,0.4], [1.97, 3.47,0.4], [2.25, 2.99,0.4]]
cofano5 = [[3.13, 5.44,0.3], [2.39, 4.95,0.3], [2.63, 3.39,0.3], [3.11, 2.99,0.3]]


ccofano1 = BEZIER(S1)(cofano1)
ccofano2 = BEZIER(S1)(cofano2)
ccofano3 = BEZIER(S1)(cofano3)
ccofano4 = BEZIER(S1)(cofano4)
ccofano5 = BEZIER(S1)(cofano5)

# cofano2up1 = [[1.73, 3.18,0.3], [1.33, 3.78,0.3], [1.46, 5.18,0.3], [1.77, 5.26,0.3]]
# ccofano2up1 = BEZIER(S1)(cofano2up1)


scofano = BEZIER(S2)([ccofano1,ccofano2,ccofano3,ccofano4,ccofano5])
# scofano2 = BEZIER(S2)([ccofano2,ccofano4])

superficie2a = MAP(scofano)(domain2)
# superficie2b = MAP(scofano2)(domain2)

superficie2 = STRUCT([superficie2a])

superficie2 = T([2,3])([-2.82,1])(superficie2)
superficie2 = COLOR(RED)(superficie2)
superficie2 = T([1,2,3])([-4,-1.5,-0.5])(superficie2)
# car = STRUCT([side,high,front,wheels4,volante,superficie1,superficie2])

# car = STRUCT([side,high,front,wheels4,superficie1,superficie2])
# car = STRUCT([side,high,front,superficie2])
# car = STRUCT([side,high,front,superficie2])
# VIEW(sidesxz)
# VIEW(car)

