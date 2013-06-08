function circle (R) {
  var domain = DOMAIN([[0,2*PI],[0,R]])([36,1]);
  var mapping = function (v) {
    var a = v[0];
    var r = v[1];
    
    return [r*COS(a), r*SIN(a)];
  }
  var model = MAP(mapping)(domain);
  return model;
}

basepoints = [[-1,0,0],[-1,1.6,0],[1.6,1.6,0],[1.6,0,0],[1.6,-1.6,0],[-1,-1.6,0],[-1,0,0]]

var domaintree = PROD1x1([INTERVALS(1)(5),INTERVALS(1)(5)]);

var apex = [0,0,0.5];

var funProfile = BEZIER(S0)(basepoints);

var chiomaPunta = MAP(CONICAL_SURFACE(apex)(funProfile))(domaintree);

var chiomaBase = MAP(CONICAL_SURFACE([0,0,0])(funProfile))(domaintree);

var chioma = COLOR([0,1,0])(STRUCT([chiomaBase,chiomaPunta]))

var tronco = COLOR([139/255.0,69/255.0,19/255.0])(EXTRUDE([1])(circle([0.1])))

tree = STRUCT([tronco,T([2])([1])(chioma)])

function generateTranslations(points)
{
	punti = []
	for(i = points.length / 2 - 50 ; i< points.length / 2; i++)
	{
		x = points[i][0]
		y = points[i][1]
		z = points[i][2]
		if(x<5 && y>5)
			punti.push([x,y,z])
		else if (y<5 && x>5)
			punti.push([x,y,z-0.5])

	}

	return punti

}

var treetransl = generateTranslations(points);
var mulAndTrans = CONS(AA(T([0,1,2]))(treetransl))
var trees = STRUCT(mulAndTrans(tree))

DRAW(trees)
