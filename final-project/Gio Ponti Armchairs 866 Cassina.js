var GRID = SIMPLEX_GRID
var domain = INTERVALS(1)(10)
var domain2= PROD1x1([INTERVALS(1)(20),INTERVALS(1)(20)]);

function bezier_circle_map(scale,selector,h)
{
	var circle_points = [[-1*scale,0,0+h],[-1*scale,1.6*scale,0+h],[1.6*scale,1.6*scale,0+h],[1.6*scale,0,0+h],[1.6*scale,-1.6*scale,0+h],[-1*scale,-1.6*scale,0+h],[-1*scale,0,0+h]];
	return BEZIER(selector)(circle_points)
}

function toRGBplasm(rgb)
{
	var r = rgb[0]
	var g = rgb[1]
	var b = rgb[2]
	var newrgb = [r/255.0,g/255.0,b/255.0]
	return newrgb
}

function from2to3plusY(list)
{
	var newList = []
	for (i=0; i<list.length;i++)
		{
			var x = list[i][0]
			var y = list[i][1]
			newList.push([x,0,y])
		}
	return newList;
}

function BEZIERCURVE(points)
{
	return BEZIER(S0)(points)
}

function MAPBCURVE(points,domain)
{
	return MAP(BEZIERCURVE(points))(domain)
}

function scalepoints(list,scale,dx,dy,dz)
{
	var newList = []
	for (i=0; i<list.length;i++)
		{
			var x = list[i][0]
			var y = list[i][1]
			var z = list[i][2]
			newList.push([x*scale+dx,y*scale+dy,z*scale+dz])
		}
	return newList;
}

function nodi (points) { 
  var m = points.length;
  var k = 2;
  var n = (m + k + 1);
  var l = n - 3;
  var j = 1;
  var knots = [];
  for (var i = 0; i < 3; i++) {
	knots[i] = 0;
  };
  for (var i = 3; i < l; i++, j++) {
	knots[i] = j;
  };
  for (var i = l; i < n; i++) {
	knots[i] = j;
  };
  return knots;
};

var domainsphere = DOMAIN([[0,PI],[0,PI]])([12,18])

var sphere = function(r){
	return function (v)
		{
			return [r*SIN([v[0]])*COS(v[1]),-r*SIN([v[0]])*SIN(v[1]),r*COS(v[0])]
		}
	}

var platoA = from2to3plusY([[1.63, 0.84], [2.22, 1.59], [1.5, 2.3], [0.81, 5.1]])
var clatoA = BEZIERCURVE(platoA)
var scaledA = scalepoints(platoA,0.99,0.45,0,0)
var clatoAscaled = BEZIERCURVE(scaledA)
var olatoA = MAPBCURVE(platoA,domain)

var platoB = from2to3plusY([[0.81, 5.1], [0.76, 5.24], [0.84, 5.38], [0.97, 5.39]])
var clatoB = BEZIERCURVE(platoB)
var scaledB = scalepoints(platoB,0.99,0.2,0,-0.2)
var clatoBscaled = BEZIERCURVE(scaledB)
var olatoB = MAPBCURVE(platoB,domain)

var platoC = from2to3plusY([[0.97, 5.39], [1.18, 5.46], [1.22, 5.48], [1.44, 5.47]])
var clatoC = BEZIERCURVE(platoC)
var scaledC = scalepoints(platoC,0.99,0,0,-0.4)
var clatoCscaled = BEZIERCURVE(scaledC)
var olatoC = MAPBCURVE(platoC,domain)

var platoD = from2to3plusY([[1.44, 5.47], [1.57, 5.42], [1.59, 5.41], [1.67, 5.22]])
var clatoD = BEZIERCURVE(platoD)
var scaledD = scalepoints(platoD,0.99,-0.4,0,0)
var clatoDscaled = BEZIERCURVE(scaledD)
var olatoD = MAPBCURVE(platoD,domain)

var platoE = from2to3plusY([[1.67, 5.22], [2.04, 4.32], [2.03, 4.31], [2.22, 3.76]])
var clatoE = BEZIERCURVE(platoE)
var scaledE = scalepoints(platoE,1.2,-1,0,-1)
var clatoEscaled = BEZIERCURVE(scaledE)
var olatoE = MAPBCURVE(platoE,domain)

var platoF = from2to3plusY([[2.22, 3.76], [2.29, 3.43], [2.1, 3.42], [2.01, 3.24]])
var clatoF = BEZIERCURVE(platoF)
var scaledF = scalepoints(platoF,0.99,-0.6,0,-0.1)
var clatoFscaled = BEZIERCURVE(scaledF)
var olatoF = MAPBCURVE(platoF,domain)

var platoG = from2to3plusY([[2.01, 3.24], [1.82, 2.47], [2.34, 1.6], [2.89, 1.63]])
var clatoG = BEZIERCURVE(platoG)
var scaledG = scalepoints(platoG,1.4,-1.2,0,-1)
var clatoGscaled = BEZIERCURVE(scaledG)
var olatoG = MAPBCURVE(platoG,domain)

var platoH = from2to3plusY([[2.89, 1.63], [3.13, 1.6], [3.74, 1.59], [3.66, 2.84]])
var clatoH = BEZIERCURVE(platoH)
var scaledH = scalepoints(platoH,1.03,0.3,0,-0.3)
var clatoHscaled = BEZIERCURVE(scaledH)
var olatoH = MAPBCURVE(platoH,domain)

var platoI = from2to3plusY([[3.66, 2.84], [3.69, 3.04], [3.68, 3.33], [4.31, 3.38]])
var clatoI = BEZIERCURVE(platoI)
var scaledI = scalepoints(platoI,0.99,0,0,-1)
var clatoIscaled = BEZIERCURVE(scaledI)
var olatoI = MAPBCURVE(platoI,domain)

var platoJ = from2to3plusY([[4.31, 3.38], [5.09, 3.4], [5.72, 3.49], [6.32, 3.48]])
var clatoJ = BEZIERCURVE(platoJ)
var scaledJ = scalepoints(platoJ,0.99,-0.2,0,-2)
var clatoJscaled = BEZIERCURVE(scaledJ)
var olatoJ = MAPBCURVE(platoJ,domain)

var platoK = from2to3plusY([[6.32, 3.48], [6.57, 3.47], [6.81, 3.45], [6.87, 2.95]])
var clatoK = BEZIERCURVE(platoK)
var scaledK = scalepoints(platoK,0.99,-0.7,0,-0.2)
var clatoKscaled = BEZIERCURVE(scaledK)
var olatoK = MAPBCURVE(platoK,domain)

var platoL = from2to3plusY([[6.87, 2.95], [6.93, 2.73], [6.98, 2.66], [7, 1.81]])
var clatoL = BEZIERCURVE(platoL)
var scaledL = scalepoints(platoL,0.99,-3,0,0)
var clatoLscaled = BEZIERCURVE(scaledL)
var olatoL = MAPBCURVE(platoL,domain)

var platoM = from2to3plusY([[7, 1.81], [6.97, 1.64], [6.93, 1.53], [6.51, 1.49]])
var clatoM = BEZIERCURVE(platoM)
var scaledM = scalepoints(platoM,0.99,-0.3,0,0.4)
var clatoMscaled = BEZIERCURVE(scaledM)
var olatoM = MAPBCURVE(platoM,domain)

var platoN = from2to3plusY([[6.51, 1.49], [6.19, 1.42], [5.79, 1.48], [5.81, 0.81]])
var clatoN = BEZIERCURVE(platoN)
var scaledN = scalepoints(platoN,0.99,0,0,0.4)
var clatoNscaled = BEZIERCURVE(scaledN)
var olatoN = MAPBCURVE(platoN,domain)

var platoO = from2to3plusY([[5.81, 0.81], [5.54, 0.73], [5.64, 0.76], [5.39, 0.68]]) // GAMBA
var clatoO = BEZIERCURVE(platoO)
var scaledO = scalepoints(platoO,0.99,0,0,1)
var clatoOscaled = BEZIERCURVE(scaledO)
var olatoO = MAPBCURVE(platoO,domain)

var platoP = from2to3plusY([[5.39, 0.68], [5.17, 1.23], [5.06, 1.17], [4.76, 1.24]])
var clatoP = BEZIERCURVE(platoP)
var scaledP = scalepoints(platoP,0.99,0.3,0,0.3)
var clatoPscaled = BEZIERCURVE(scaledP)
var olatoP = MAPBCURVE(platoP,domain)

var platoQ = from2to3plusY([[4.76, 1.24], [4.02, 1.27], [3.67, 1.23], [3.06, 1.15]])
var clatoQ = BEZIERCURVE(platoQ)
var scaledQ = scalepoints(platoQ,0.99,0.6,0,0.63)
var clatoQscaled = BEZIERCURVE(scaledQ)
var olatoQ = MAPBCURVE(platoQ,domain)

var platoR = from2to3plusY([[3.06, 1.15], [2.48, 1.04], [2.3, 0.93], [1.96, 0.55]])
var clatoR = BEZIERCURVE(platoR)
var scaledR = scalepoints(platoR,0.99,0.48,0,0.5)
var clatoRscaled = BEZIERCURVE(scaledR)
var olatoR = MAPBCURVE(platoR,domain)

var platoS = from2to3plusY([[1.96, 0.55], [1.71, 0.73], [1.84, 0.59], [1.63, 0.84]]) //GAMBA
var clatoS = BEZIERCURVE(platoS)
var scaledS = scalepoints(platoS,0.99,0.9,0,0.92)
var clatoSscaled = BEZIERCURVE(scaledS)
var olatoS = MAPBCURVE(platoS,domain)

var clatolist = [clatoA,clatoB,clatoC,clatoD,clatoE,clatoF,clatoG,clatoH,clatoI,clatoJ,clatoK,clatoL,clatoM,clatoN,clatoO,
clatoP,clatoQ,clatoR,clatoS]

var clatolistscaled = [clatoAscaled,clatoBscaled,clatoCscaled,clatoDscaled,clatoEscaled,clatoFscaled,clatoGscaled,clatoHscaled,clatoIscaled,clatoJscaled,clatoKscaled,clatoLscaled,clatoMscaled,clatoNscaled,clatoOscaled,
clatoPscaled,clatoQscaled,clatoRscaled,clatoSscaled]

// RIEMPIMENTO LATO

var slato1A = MAP(BEZIER(S1)([clatoA,clatoAscaled]))(domain2)
var slato1B = MAP(BEZIER(S1)([clatoB,clatoBscaled]))(domain2)
var slato1C = MAP(BEZIER(S1)([clatoC,clatoCscaled]))(domain2)
var slato1D = MAP(BEZIER(S1)([clatoD,clatoDscaled]))(domain2)
var slato1E = MAP(BEZIER(S1)([clatoE,clatoEscaled]))(domain2)
var slato1F = MAP(BEZIER(S1)([clatoF,clatoFscaled]))(domain2)
var slato1G = MAP(BEZIER(S1)([clatoG,clatoGscaled]))(domain2)
var slato1H = MAP(BEZIER(S1)([clatoH,clatoHscaled]))(domain2)
var slato1I = MAP(BEZIER(S1)([clatoI,clatoIscaled]))(domain2)
var slato1J = MAP(BEZIER(S1)([clatoJ,clatoJscaled]))(domain2)
var slato1K = MAP(BEZIER(S1)([clatoK,clatoKscaled]))(domain2)
var slato1L = MAP(BEZIER(S1)([clatoL,clatoLscaled]))(domain2)
var slato1M = MAP(BEZIER(S1)([clatoM,clatoMscaled]))(domain2)
var slato1N = MAP(BEZIER(S1)([clatoN,clatoNscaled]))(domain2)
var slato1O = MAP(BEZIER(S1)([clatoO,clatoOscaled]))(domain2)
var slato1P = MAP(BEZIER(S1)([clatoP,clatoPscaled]))(domain2)
var slato1Q = MAP(BEZIER(S1)([clatoQ,clatoQscaled]))(domain2)
var slato1R = MAP(BEZIER(S1)([clatoR,clatoRscaled]))(domain2)
var slato1S = MAP(BEZIER(S1)([clatoS,clatoSscaled]))(domain2)
var slato1HR = MAP(BEZIER(S1)([clatoRscaled,[2.89, 0,1.63]]))(domain2)

var slato1 = STRUCT([slato1A,slato1B,slato1C,slato1D,slato1E,slato1F,slato1G,slato1H,slato1I,slato1J,slato1K,slato1L,slato1M,slato1N,slato1O,
slato1P,slato1Q,slato1R,slato1S,slato1HR])

// estrudo lato

var ncpVector = [0,0.3,0]

var el1A = MAP(CYLINDRICAL_SURFACE(clatoA)(ncpVector))(domain2);
var el1B = MAP(CYLINDRICAL_SURFACE(clatoB)(ncpVector))(domain2);
var el1C = MAP(CYLINDRICAL_SURFACE(clatoC)(ncpVector))(domain2);
var el1D = MAP(CYLINDRICAL_SURFACE(clatoD)(ncpVector))(domain2);
var el1E = MAP(CYLINDRICAL_SURFACE(clatoE)(ncpVector))(domain2);
var el1F = MAP(CYLINDRICAL_SURFACE(clatoF)(ncpVector))(domain2);
var el1G = MAP(CYLINDRICAL_SURFACE(clatoG)(ncpVector))(domain2);
var el1H = MAP(CYLINDRICAL_SURFACE(clatoH)(ncpVector))(domain2);
var el1I = MAP(CYLINDRICAL_SURFACE(clatoI)(ncpVector))(domain2);
var el1J = MAP(CYLINDRICAL_SURFACE(clatoJ)(ncpVector))(domain2);
var el1K = MAP(CYLINDRICAL_SURFACE(clatoK)(ncpVector))(domain2);
var el1L = MAP(CYLINDRICAL_SURFACE(clatoL)(ncpVector))(domain2);
var el1M = MAP(CYLINDRICAL_SURFACE(clatoM)(ncpVector))(domain2);
var el1N = MAP(CYLINDRICAL_SURFACE(clatoN)(ncpVector))(domain2);
var el1O = MAP(CYLINDRICAL_SURFACE(clatoO)(ncpVector))(domain2);
var el1P = MAP(CYLINDRICAL_SURFACE(clatoP)(ncpVector))(domain2);
var el1Q = MAP(CYLINDRICAL_SURFACE(clatoQ)(ncpVector))(domain2);
var el1R = MAP(CYLINDRICAL_SURFACE(clatoR)(ncpVector))(domain2);
var el1S = MAP(CYLINDRICAL_SURFACE(clatoS)(ncpVector))(domain2);

var el1 = STRUCT([el1A,el1B,el1C,el1D,el1E,el1F,el1G,el1H,el1I,el1J,el1K,el1L,el1M,el1N,el1O,el1P,el1Q,el1R,el1S])

var pcuscino1A = from2to3plusY([[0.86, 5.06], [1.35, 3.37], [1.54, 3.03], [1.96, 1.5]])
var ccuscino1A = BEZIERCURVE(pcuscino1A)
var ocuscino1A = MAPBCURVE(pcuscino1A,domain)
var scaledc1A = scalepoints(pcuscino1A,0.99,0.45,0,0.25)
var ccuscino1Ascaled = BEZIERCURVE(scaledc1A)

var pcuscino1B = from2to3plusY([[1.96, 1.5], [2.33, 1.63], [2.38, 1.68], [2.75, 2.09]])
var ccuscino1B = BEZIERCURVE(pcuscino1B)
var ocuscino1B = MAPBCURVE(pcuscino1B,domain)

var pcuscino1C = from2to3plusY([[2.75, 2.09], [3.04, 3.01], [2.54, 3.21], [2.11, 3.54]])
var ccuscino1C = BEZIERCURVE(pcuscino1C)
var ocuscino1C = MAPBCURVE(pcuscino1C,domain)

var pcuscino1D = from2to3plusY([[2.11, 3.54], [1.79, 3.84], [1.62, 4.66], [1.51, 5.06]])
var ccuscino1D = BEZIERCURVE(pcuscino1D)
var ocuscino1D = MAPBCURVE(pcuscino1D,domain)

var pcuscino1E = from2to3plusY([[1.51, 5.06], [1.4, 5.17], [1.43, 5.52], [0.94,5.32]])
var ccuscino1E = BEZIERCURVE(pcuscino1E)
var ocuscino1E = MAPBCURVE(pcuscino1E,domain)

var pcuscino1F = from2to3plusY([[0.94, 5.32], [0.83, 5.26], [0.83, 5.18], [0.86, 5.06]])
var ccuscino1F = BEZIERCURVE(pcuscino1F)
var ocuscino1F = MAPBCURVE(pcuscino1F,domain)

var ncpVector = [0,3.77,0]

var ec1A = MAP(CYLINDRICAL_SURFACE(ccuscino1A)(ncpVector))(domain2);
var ec1B = MAP(CYLINDRICAL_SURFACE(ccuscino1B)(ncpVector))(domain2);
var ec1C = MAP(CYLINDRICAL_SURFACE(ccuscino1C)(ncpVector))(domain2);
var ec1D = MAP(CYLINDRICAL_SURFACE(ccuscino1D)(ncpVector))(domain2);
var ec1E = MAP(CYLINDRICAL_SURFACE(ccuscino1E)(ncpVector))(domain2);
var ec1F = MAP(CYLINDRICAL_SURFACE(ccuscino1F)(ncpVector))(domain2);

var sc1A = MAP(BEZIER(S1)([ccuscino1A,ccuscino1Ascaled]))(domain2)
var sc1B = MAP(BEZIER(S1)([ccuscino1B,[1.86, 0,2.34]]))(domain2)
var sc1C = MAP(BEZIER(S1)([ccuscino1C,[1.86, 0,2.34]]))(domain2)
var sc1D = MAP(BEZIER(S1)([ccuscino1D,[1.86, 0,2.34]]))(domain2)
var sc1E = MAP(BEZIER(S1)([ccuscino1E,[1.86, 0,2.34]]))(domain2)
var sc1F = MAP(BEZIER(S1)([ccuscino1F,[1.86, 0,2.34]]))(domain2)

var sc1 = STRUCT([sc1A,sc1B,sc1C,sc1D,sc1E,sc1F])

var ec1 = STRUCT([ec1A,ec1B,ec1C,ec1D,ec1E,ec1F])

var cuscino1 = T([1])([0.3])(STRUCT([sc1,ec1,T([1])([3.77])(sc1)]))

var lato1 = STRUCT([slato1,el1,T([1])([0.3])(slato1)])
var lato2 = T([1])([4.03])(lato1)

var pcuscino2A = from2to3plusY([[1.96, 1.5], [2.33, 1.63], [2.38, 1.68], [2.75, 2.09]])

var ccuscino2A = BEZIERCURVE(pcuscino2A)
var ocuscino2A = MAPBCURVE(pcuscino2A,domain)

var pcuscino2B = from2to3plusY([[2.75, 2.09], [3.88, 2.42], [5.04, 2.64], [6.87, 2.2]])
var ccuscino2B = BEZIERCURVE(pcuscino2B)
var ocuscino2B = MAPBCURVE(pcuscino2B,domain)

var pcuscino2C = from2to3plusY([[6.87, 2.2], [7.01, 2.18], [7, 1.93], [6.97, 1.7]])
var ccuscino2C = BEZIERCURVE(pcuscino2C)
var ocuscino2C = MAPBCURVE(pcuscino2C,domain)

var pcuscino2D = from2to3plusY([[6.97, 1.7], [6.84, 1.55], [6.63, 1.51], [1.96, 1.5]])
var ccuscino2D = BEZIERCURVE(pcuscino2D)
var ocuscino2D = MAPBCURVE(pcuscino2D,domain)

var ec2A = MAP(CYLINDRICAL_SURFACE(ccuscino2A)(ncpVector))(domain2);
var ec2B = MAP(CYLINDRICAL_SURFACE(ccuscino2B)(ncpVector))(domain2);
var ec2C = MAP(CYLINDRICAL_SURFACE(ccuscino2C)(ncpVector))(domain2);
var ec2D = MAP(CYLINDRICAL_SURFACE(ccuscino2D)(ncpVector))(domain2);

var sc2A = MAP(BEZIER(S1)([ccuscino2A,[4.25, 0,1.6]]))(domain2)
var sc2B = MAP(BEZIER(S1)([ccuscino2B,[4.25, 0,1.6]]))(domain2)
var sc2C = MAP(BEZIER(S1)([ccuscino2C,[4.25, 0,1.6]]))(domain2)
var sc2D = MAP(BEZIER(S1)([ccuscino2D,[4.25, 0,1.6]]))(domain2)

var sc2 = STRUCT([sc2A,sc2B,sc2C,sc2D])

var sc22 = T([1])([3.77])(sc2)

var cuscino2 = T([1])([0.3])(STRUCT([sc2,sc22,ec2A,ec2B,ec2C,ec2D]))

// gambaletto1

var pgambaletto1 = from2to3plusY([[1.63, 0.84],[1.96, 0.55],[1.96, 0.55],[0.85, -0.55],[0.85, -0.55],[0.74, -0.54],[0.69, -0.51],[0.73, -0.46],[1.63, 0.84],[1.63, 0.84]])
var knodi = nodi(pgambaletto1)
var cg1 = NUBS(S0)(2)(knodi)(pgambaletto1)

var prg1 = [cg1,[1.6, 0,0.45],[1.6, 0,0.45],[1.6, 0,0.45]]
var knodi = nodi(prg1)
var rg1 = NUBS(S1)(2)(knodi)(prg1)

var org1 = MAP(rg1)(domain2)

var ncpVector = [0,0.3,0]

var org1 = STRUCT([MAP(CYLINDRICAL_SURFACE(cg1)(ncpVector))(domain2),org1,T([1])([0.3])(org1)])

var org12 = T([1])([4.03])(org1)

var sottog11 = bezier_circle_map(0.095,S0,0)
var sottog12 = bezier_circle_map(0.145,S0,-0.03)
var sottog13 = bezier_circle_map(0.095,S0,-0.06)
var psg1 = BEZIER(S1)([sottog11,sottog12,sottog13])
var ssg1 = MAP(psg1)(domain2)

var psg13 = BEZIER(S1)([sottog13,[0,0,-0.06]])
var ssg13 = MAP(psg13)(domain2)

var fermasedia1 = T([0,1,2])([0.77,0.15,-0.54])(STRUCT([ssg1,ssg13]))

// gambaletto2

var pgambaletto2 = from2to3plusY([[5.39, 0.68],[5.81, 0.81],[5.81, 0.81],[5.81, 0.81],[6.02, -0.54],[6.02, -0.54],[6.02, -0.54],[5.82, -0.56],[5.82, -0.56],[5.82, -0.56],[5.39, 0.68],[5.39, 0.68]])
var knodi = nodi(pgambaletto2)
var cg2 = NUBS(S0)(2)(knodi)(pgambaletto2)

var prg2 = [cg2,[5.78, 0,0.04],[5.78, 0,0.04],[5.78, 0,0.04]]
var knodi = nodi(prg2)
var rg2 = NUBS(S1)(2)(knodi)(prg2)

var org2 = MAP(rg2)(domain2)

var ncpVector = [0,0.3,0]

var org2 = STRUCT([MAP(CYLINDRICAL_SURFACE(cg2)(ncpVector))(domain2),org2,T([1])([0.3])(org2)])

var org22 = T([1])([4.03])(org2)

// ornamenti

function duplicate(points,n,dx,dy,dz)
{
	var x = points[0]
	var y = points[1]
	var z = points[2]
	var newpoints = []
	for(j=0;j<n;j++)
	{
		newpoints.push([x+j*dx,y+j*dy,z+j*dz])
	}
	return newpoints
}

var mapsfera = MAP(sphere(0.03))
var ornamentoA = mapsfera(domainsphere)
var matornamentoA = CONS(AA(T([0,1,2]))(duplicate([1.65, 0,0.82],8,0.04,0,-0.037)))

var ornamentoB = R([1,2])([PI])(ornamentoA)
var matornamentoB = CONS(AA(T([0,1,2]))(duplicate([1.65, 0+0.3,0.82],8,0.04,0,-0.037)))

var ornamentoC = R([1,2])([PI/2])(ornamentoA)
var ornamentoC = R([0,2])([PI/1.4])(ornamentoC)
var ornamentoD = R([0,2])([PI])(ornamentoC)
var ornamentoC = T([2])([0.82])(ornamentoC)
var matornamentoC = CONS(AA(T([0,1,2]))(duplicate([1.65-0.02, 0.025,0.01],6,0,0.3/6,0)))

var matornamentoD = CONS(AA(T([0,1,2]))(duplicate([1.65+0.305, 0.025,0+0.55],6,0,0.3/6,0)))

var a = [matornamentoA(ornamentoA),matornamentoB(ornamentoB),matornamentoC(ornamentoC),matornamentoD(ornamentoD)]
var a = Array.prototype.concat.apply([], a) 
var ornamentiA = STRUCT(a)
var ornamentiB = T([1])([4.03])(ornamentiA)

var matornamentoE = CONS(AA(T([0,1,2]))(duplicate([5.4, 0,0.67],10,0.045,0,0.015)))

var ornamentoF = R([1,2])([PI])(ornamentoA)
var matornamentoF = CONS(AA(T([0,1,2]))(duplicate([5.4, 0+0.3,0.67],10,0.045,0,0.015)))

var ornamentoG = R([1,2])([PI/2])(ornamentoA)
var ornamentoG = R([0,2])([PI/2])(ornamentoG)
var ornamentoH = R([0,2])([PI])(ornamentoG)
var ornamentoG = T([2])([0.67])(ornamentoG)
var matornamentoG = CONS(AA(T([0,1]))(duplicate([5.4, 0,0],7,0,0.3/6,0)))

var matornamentoH = CONS(AA(T([0,1,2]))(duplicate([5.4+0.41, 0,0+0.805],7,0,0.3/6,0)))

var b = [matornamentoE(ornamentoA),matornamentoF(ornamentoF),matornamentoG(ornamentoG),matornamentoH(ornamentoH)]
var b = Array.prototype.concat.apply([], b) 
var ornamentiC = STRUCT(b)
var ornamentiD = T([1])([4.03])(ornamentiC)

var COLOR = function (rgba) {
    return function (object) {
      return object.color(rgba);
    }	;
  }

var sedia = STRUCT([COLOR(toRGBplasm([ 87, 75, 75]))(ornamentiA),COLOR(toRGBplasm([ 87, 75, 75]))(ornamentiB)
,COLOR(toRGBplasm([ 87, 75, 75]))(ornamentiC),COLOR(toRGBplasm([ 87, 75, 75]))(ornamentiD),
COLOR(toRGBplasm([75, 63, 63]))(org1),COLOR(toRGBplasm([75, 63, 63]))(org12),COLOR(toRGBplasm([75, 63, 63]))(org2),
COLOR(toRGBplasm([75, 63, 63]))(org22),COLOR(toRGBplasm([66, 92, 95]))(cuscino1),
COLOR(toRGBplasm([66, 92, 95]))(cuscino2),COLOR(toRGBplasm([233, 219, 177]))(lato1),COLOR(toRGBplasm([233, 219, 177]))(lato2),
fermasedia1,T([1])([4.03])(fermasedia1),T([0])([5.15])(fermasedia1),T([0,1])([5.15,4.03])(fermasedia1)])
// 
DRAW(sedia)