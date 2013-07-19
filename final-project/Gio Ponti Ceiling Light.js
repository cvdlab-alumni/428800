var GRID = SIMPLEX_GRID
var domain2= PROD1x1([INTERVALS(1)(20),INTERVALS(1)(20)]);

function bezier_circle_map(scale,selector,h)
{
	var circle_points = [[-1*scale,0,0+h],[-1*scale,1.6*scale,0+h],[1.6*scale,1.6*scale,0+h],[1.6*scale,0,0+h],[1.6*scale,-1.6*scale,0+h],[-1*scale,-1.6*scale,0+h],[-1*scale,0,0+h]];
	return BEZIER(selector)(circle_points)
}

function cerchio(r)
{
	function ball(p){
 		var a = p[0]
		var r = p[1]
		return [r*COS(a), r*SIN(a)]
		}
	var dom2D = PROD1x1([INTERVALS(2*PI)(50), INTERVALS(1)(1)])
	return S([0,1])([r,r])(MAP(ball)(dom2D))
}

var cbase11 = bezier_circle_map(1.99,S0,0)
var cbase21 = bezier_circle_map(1.99,S0,1)
var sbase11 = BEZIER(S1)([[0,0,0],cbase11,cbase11,cbase11,cbase21])
var obase1 = MAP(sbase11)(domain2)

var cbase12 = bezier_circle_map(2,S0,0)
var cbase22 = bezier_circle_map(2,S0,1)
var sbase22 = BEZIER(S1)([cbase12,cbase22])
var obase2 = MAP(sbase22)(domain2)
var obase2 = T([2])([1])(obase2)

var cbase13 = bezier_circle_map(2,S0,0)
var sbase33 = BEZIER(S1)([[0,0,0],cbase13])
var obase3 = MAP(sbase33)(domain2)
var obase3 = T([2])([2])(obase3)

var cbullone = cerchio(0.05)
var bullone1 = EXTRUDE([0.05])(cbullone)
var cbullone2 = cerchio(0.025)
var bullone2 = EXTRUDE([0.15])(cbullone2)
var cbullone31 = bezier_circle_map(0.05,S0,0)
var cbullone32 = bezier_circle_map(0.05,S0,0.05)
var sbullone3 = BEZIER(S1)([cbullone31,cbullone32,cbullone32,cbullone32,[0,0,0.05]])
var bullone3 = MAP(sbullone3)(domain2)
var bullone3 = T([2])([0.1])(bullone3)
var cbullone32 = bezier_circle_map(0.05,S0,0)
var sbullone32 = BEZIER(S1)([[0,0,0],cbullone32])
var bullone4 = MAP(sbullone32)(domain2)
var bullone4 = T([2])([0.1])(bullone4)

var bullone = STRUCT([bullone1,bullone2,bullone3,bullone4])


// centro --------------------------

var centro1 = cerchio(0.7)
var ocentro1 = EXTRUDE([1.2])(centro1)
var centro2 = cerchio(0.2)
var ocentro2 = EXTRUDE([1.7])(centro2)
var ocentro2 = T([2])([-0.7])(ocentro2)

var centro = STRUCT([ocentro1,ocentro2])

// coloring ------------

var obase1 = COLOR([1,1,1])(obase1)
var obase2 = COLOR([150.0/255.0,120.0/255.0,64.0/255.0])(obase2)
var obase3 = COLOR([150.0/255.0,120.0/255.0,64.0/255.0])(obase3)
var bullone = COLOR([150.0/255.0,120.0/255.0,64.0/255.0])(bullone)
var centro = COLOR([150.0/255.0,120.0/255.0,64.0/255.0])(T([2])([1.3])(centro))


// sistemo i bulloni --------------------

var bulloneA = R([1,2])([PI/2])(bullone)
var bulloneA = T([1,2])([-1.95,1.2])(bulloneA)

var bulloneB = R([0,1])([2*PI/3])(bulloneA)
var bulloneB = T([1])([0.1])(bulloneB)

var bulloneC = R([0,1])([-2*PI/3])(bulloneA)

var bulloni = STRUCT([bulloneA,bulloneB,bulloneC])

// lampada -------------------------

var lampada1 = STRUCT([obase1,obase2,obase3,T([2])([-1])(obase3),bulloni])

// lampade ---------------------
var stecca1 = GRID(([[8.5],[0.25],[0.5]]))
var stecca1 = T([1,2])([-0.125,1.8])(stecca1)
var stecca1 = R([0,1])([PI/4])(stecca1)

var stecca2 = GRID(([[4.5],[0.25],[0.5]]))
var stecca2 = T([1,2])([-0.125,1.8])(stecca2)
var stecca2 = R([0,1])([PI/4])(stecca2)

// primo livello
var lampada2 = STRUCT([stecca2,T([0,1])([3,3])(lampada1)])
var lampada2 = R([0,1])([-0.1])(lampada2)
var lampada3 = R([0,1])([2*PI/5])(lampada2)
var lampada4 = R([0,1])([-2*PI/5])(lampada2)
var lampada5 = R([0,1])([(-2*PI/5)*2])(lampada2)
var lampada6 = R([0,1])([(2*PI/5)*2])(lampada2)

// secondo livello
var lampada7 = STRUCT([stecca1,T([0,1])([6,6])(lampada1)])

var lampada7 = R([0,1])([PI/6])(lampada7)
var lampada8 = R([0,1])([2*PI/5])(lampada7)
var lampada9 = R([0,1])([-2*PI/5])(lampada7)
var lampada10 = R([0,1])([(-2*PI/5)*2])(lampada7)
var lampada11 = R([0,1])([(2*PI/5)*2])(lampada7)

// var lampade = STRUCT([lampada2,lampada3,lampada4,lampada5,lampada6,lampada7,lampada8,lampada9,lampada10,lampada11])

// lampadario ---------------------
var lampadario = STRUCT([lampada2,lampada3,lampada4,lampada5,lampada6,lampada7,lampada8,lampada9,lampada10,lampada11,centro])

DRAW(lampadario)
