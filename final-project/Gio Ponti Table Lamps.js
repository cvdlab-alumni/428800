function bezier_circle_map(scale,selector,h)
{
	circle_points = [[-1*scale,0,0+h],[-1*scale,1.6*scale,0+h],[1.6*scale,1.6*scale,0+h],[1.6*scale,0,0+h],[1.6*scale,-1.6*scale,0+h],[-1*scale,-1.6*scale,0+h],[-1*scale,0,0+h]];
	return BEZIER(selector)(circle_points)
}

function toRGBplasm(rgb)
	{
		r = rgb[0]
		g = rgb[1]
		b = rgb[2]
		newrgb = [r/255.0,g/255.0,b/255.0]
		return newrgb
	}
	
var domain = PROD1x1([INTERVALS(1)(20),INTERVALS(1)(6)]);

var apex = [0,0,5];

var funbase = bezier_circle_map(1,S0,0)
var sbase = MAP(CONICAL_SURFACE(apex)(funbase))(domain);

var funbasec12 = bezier_circle_map(1.0,S0,0)
var funbasec13 = bezier_circle_map(1.03,S0,-0.01)
var funbasec14 = bezier_circle_map(1.0,S0,-0.02)
var pc1a = BEZIER(S1)([funbasec12,funbasec13,funbasec14])
var sc1a = MAP(pc1a)(domain)


var pc1b = BEZIER(S1)([funbasec14,[0,0,-0.02]])
var sc1b = MAP(pc1b)(domain)


var chiusura = STRUCT([sc1a,sc1b])

var base = STRUCT([chiusura,sbase])

var domainsphere = DOMAIN([[0,PI],[0,2*PI]])([24,36])
var sphere = function(r){
	return function (v)
		{
			return [r*SIN([v[0]])*COS(v[1]),r*SIN([v[0]])*SIN(v[1]),r*COS(v[0])]
		}
	}

var mapsfera = MAP(sphere(1.3))
var luce = T([2])([4.5])(mapsfera(domainsphere))

var funbasec22 = bezier_circle_map(0.5,S0,0)
var funbasec23 = bezier_circle_map(0.53,S0,-0.01)
var funbasec24 = bezier_circle_map(0.5,S0,-0.02)
var pc22 = BEZIER(S1)([funbasec22,funbasec23,funbasec24])
var sc22 = MAP(pc22)(domain)

var pc23 = BEZIER(S1)([funbasec24,[0,0,-0.02]])
var sc23 = MAP(pc23)(domain)

var chiusura2 = STRUCT([sc22,sc23])
var chiusura2 = T([2])([3.28])(chiusura2)

var luce = COLOR(toRGBplasm([254, 255, 255]))(luce)
var chiusura2 = COLOR(toRGBplasm([253, 226, 178]))(chiusura2)
var base = COLOR(toRGBplasm([59, 53, 39]))(base)

DRAW(luce)
DRAW(chiusura2)
DRAW(base)