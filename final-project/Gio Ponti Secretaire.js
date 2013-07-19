var GRID = SIMPLEX_GRID

function toRGBplasm(rgb)
{
	var r = rgb[0]
	var g = rgb[1]
	var b = rgb[2]
	var newrgb = [r/255.0,g/255.0,b/255.0]
	return newrgb
}

var lati = COLOR(toRGBplasm([221, 124, 12]))(GRID(([[0.2,-6.6,0.2],[3],[14]])))
var alto = COLOR(toRGBplasm([221, 124, 12]))(GRID(([[7],[3],[-13.8,0.2]])))
var basso = COLOR(toRGBplasm([200, 127, 56]))(GRID(([[7],[3],[0.4]])))
var dietro = COLOR(toRGBplasm([221, 124, 12]))(GRID(([[7],[0.2],[14]])))
var vetro1 = COLOR([1, 1, 1,0.3])(GRID(([[-0.2,6.6,-0.2],[-0.1,2.9],[-10,0.1]])))
var vetro2 = COLOR([1, 1, 1,0.3])(GRID(([[-0.2,6.6,-0.2],[-0.1,2.9],[-12,0.1]])))
var sottodisegno = COLOR(toRGBplasm([55, 29, 20]))(GRID(([[-0.2,6.6,-0.2],[-0.1,2.9],[-5,0.1]])))
var sopradisegno = COLOR(toRGBplasm([55, 29, 20]))(GRID(([[-0.2,6.6,-0.2],[-0.1,2.9],[-8.1,0.1]])))
var sopracassetto = COLOR(toRGBplasm([55, 29, 20]))(GRID(([[-0.2,6.6,-0.2],[-0.1,2.9],[-3.7,0.1]])))

var internocassetto = COLOR(toRGBplasm([ 246, 204, 158]))(GRID(([[-0.2,6.6],[-0.1,2.60],[-0.4,0.1]])))
var mattinternocassetto = CONS(AA(T([2]))([[0],[1.2],[2.4],[3.2],[4.7],[7.6]]))
var sinternocassetto = STRUCT(mattinternocassetto(internocassetto))
var internocassetto2 = COLOR(toRGBplasm([ 246, 204, 158]))(GRID(([[-0.2,6.6],[-0.2,0.1],[-0.4,3.4]])))
var internocassetto3 = COLOR(toRGBplasm([ 246, 204, 158]))(GRID(([[-0.2,0.1],[-0.2,2.5],[-0.4,3.4]])))
var internocassetto4 = COLOR(toRGBplasm([ 246, 204, 158]))(GRID(([[-0.2,-6.5,0.1],[-0.2,2.5],[-0.4,3.4]])))

var internodisegno1 = COLOR(toRGBplasm([246, 204, 158]))(GRID(([[-0.2,6.6,-0.2],[-0.2,0.3],[-5.1,3]])))
var internodisegno2 = COLOR(toRGBplasm([246, 204, 158]))(GRID(([[-0.2,0.1],[-0.2,2.5],[-5.1,3]])))
var internodisegno3 = COLOR(toRGBplasm([246, 204, 158]))(GRID(([[-0.2,-6.5,0.1],[-0.2,2.5],[-5.1,3]])))


var cassetto1a = GRID([[-0.2,0.02,-0.08,0.02],[-2.7,0.3],[-0.4,3.3]])
var armadioConCassetto1a1 = COLOR(toRGBplasm([ 133, 42, 29]))(STRUCT(REPLICA(20)([cassetto1a,T([0])([0.12])])))
var armadioConCassetto1a2 = T([0])([2.4])(COLOR(toRGBplasm([ 133, 42, 29]))(STRUCT(REPLICA(15)([cassetto1a,T([0])([0.12])]))))
var armadioConCassetto1a3 = T([0])([4.2])(COLOR(toRGBplasm([ 133, 42, 29]))(STRUCT(REPLICA(20)([cassetto1a,T([0])([0.12])]))))


var cassetto1b = GRID([[-0.2,-0.02,0.08,-0.02],[-2.7,0.15],[-0.4,3.3]])
var armadioConCassetto1b1 = COLOR(toRGBplasm([ 87, 36, 27]))(STRUCT(REPLICA(20)([cassetto1b,T([0])([0.12])])))
var armadioConCassetto1b2 = T([0])([2.4])(COLOR(toRGBplasm([ 87, 36, 27]))(STRUCT(REPLICA(15)([cassetto1b,T([0])([0.12])]))))
var armadioConCassetto1b3 = T([0])([4.2])(COLOR(toRGBplasm([ 87, 36, 27]))(STRUCT(REPLICA(20)([cassetto1b,T([0])([0.12])]))))

var cassetto2a = COLOR(toRGBplasm([231, 219, 200]))(GRID([[-0.2,6.6],[-2.7,0.3],[-5.1,3]]))

var cassetti = STRUCT([armadioConCassetto1a1,armadioConCassetto1a3,armadioConCassetto1b1,armadioConCassetto1b3,cassetto2a])

var armadio1 = STRUCT([lati,alto,basso,dietro,vetro1,vetro2,sottodisegno,sopradisegno,sopracassetto,sinternocassetto,internocassetto2,internocassetto3,internocassetto4,
internodisegno1,internodisegno2,internodisegno3,armadioConCassetto1a2,armadioConCassetto1b2])

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

var domain2 = DOMAIN([[0,1],[0,1]])([30,10]);

var punti = [[0,0,0],[0.18,0,0],[0.18,0,0],[0.18,0,0],[0.16,0.03,0],[0.13,0.08,0],[0.10,0.1,0],[0.07,0.14,0],[0.04,0.18,0],[0.03,0.2,0],[0,0.23,0],[0,0.23,0],[0,0.23,0],[0,0,0]]

var knots = nodi(punti)

var p1 = NUBS(S0)(2)(knots)(punti)

var riempimento = [p1,p1,p1,[0,0,0]]

var knots2 = nodi(riempimento)
var criemp = NUBS(S1)(2)(knots2)(riempimento)
var oriemp = MAP(criemp)(domain2)
var oriemp2 = T([2])([14])(oriemp)

var ncpVector = [0,0,14];

var bordino1 = MAP(CYLINDRICAL_SURFACE(p1)(ncpVector))(domain2);
var bordino1 = STRUCT([bordino1,oriemp,oriemp2])
var bordino2 = R([0,1])([PI/2])(bordino1)
var bordino1 = R([1,2])([PI])(bordino1)
var bordino1 = T([2])([14])(bordino1)
var bordino1 = R([0,1])([PI/2])(bordino1)
var bordino1 = T([1])([3])(bordino1)
var bordino2 = T([0,1])([7,3])(bordino2)

var punti = [[0,0,0],[0,0.18,0],[0,0.18,0],[0,0.18,0],[0,0.16,0.03],[0,0.13,0.08],[0,0.10,0.1],[0,0.07,0.14],[0,0.04,0.18],[0,0.03,0.2],[0,0,0.23],[0,0,0.23],[0,0,0.23],[0,0,0]]

var ncpVector = [7,0,0];

var knots = nodi(punti)

var p1 = NUBS(S0)(2)(knots)(punti)

var bordino3 = MAP(CYLINDRICAL_SURFACE(p1)(ncpVector))(domain2);
var bordino3 = R([0,2])([PI])(bordino3)
var bordino3 = T([0,1,2])([7,3,14])(bordino3)
var bordino = COLOR(toRGBplasm([131, 70, 57]))(STRUCT([bordino1,bordino2,bordino3]))

var armadio1 = STRUCT([armadio1,bordino])

var pv1 = [[0,0,0],[0,0,0],[0,0,0],[2,0,0]]
var pv2 = [[0,0,0],[0,0,0],[0,0,0],[0,2.60,0]]
var pv3 = [[0,2.60,0],[1.6,2.60,0],[2,2.08,0],[2,0,0]]

var bpv1 = BEZIER(S0)(pv1)
var bpv2 = BEZIER(S0)(pv2)
var bpv3 = BEZIER(S0)(pv3)

var ccentropv1 = BEZIER(S1)([bpv1,[1,1,0]])
var ccentropv2 = BEZIER(S1)([bpv2,[1,1,0]])
var ccentropv3 = BEZIER(S1)([bpv3,[1,1,0]])

var cpv1 = MAP(ccentropv1)(domain2);
var cpv2 = MAP(ccentropv2)(domain2);
var cpv3 = MAP(ccentropv3)(domain2);

var sottov = STRUCT([cpv1,cpv2,cpv3])
var soprav = T([2])([0.1])(sottov)

var ncpVector = [0,0,0.1];

var spv1 = MAP(CYLINDRICAL_SURFACE(bpv1)(ncpVector))(domain2)
var spv2 = MAP(CYLINDRICAL_SURFACE(bpv2)(ncpVector))(domain2)
var spv3 = MAP(CYLINDRICAL_SURFACE(bpv3)(ncpVector))(domain2)

var vetrinosx = COLOR([1, 1, 1,0.3])(STRUCT([spv1,spv2,spv3,sottov,soprav]))
var vetrinodx = R([1,2])([-PI])(vetrinosx)
var vetrinodx = T([1,2])([7,0.1])(vetrinodx)
var vetrini = STRUCT([vetrinosx,vetrinodx])
var vetrini = R([0,1])([PI/2])(vetrini)
var vetrini = T([0,1,2])([7,0.1,7])(vetrini)
var amradio1 = STRUCT([armadio1,vetrini])


// ornamenti

function generatepoints(points,n)
{
	var newpoints = [];
	for(i=0;i<n;i++)
	{	
		for(j=0;j<points.length;j++)
		{
			var x = points[j][0]
			var y = points[j][1]
			var z = points[j][2]
			
			newpoints.push([x,y,z-1.4*i])
		}
	}
	return newpoints
}

var puntiA = generatepoints([[1.2,0.201,13],[1.2+1.5,0.201,13],[1.2+3,0.201,13],[1.2+4.5,0.201,13]],9)
var puntiB = generatepoints([[0.6,0.201,12.3],[0.6+1.35,0.201,12.3],[0.6+2.8,0.201,12.3],[0.6+4.3,0.201,12.3],[0.6+5.8,0.201,12.3]],9)

var ornamento1 = R([1,2])([PI/2])(DISK(0.05)())
var matornamento = CONS(AA(T([0,1,2]))(puntiA))
var matornamento2 = CONS(AA(T([0,1,2]))(puntiB))
var orn = STRUCT(matornamento(ornamento1))
var orn2 = STRUCT(matornamento2(ornamento1))

var ornamenti = COLOR([0,0,0,0.4])(STRUCT([orn,orn2]))

DRAW(ornamenti)
DRAW(armadio1)
DRAW(cassetti)


