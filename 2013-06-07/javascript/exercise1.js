var domain = DOMAIN([[0,20],[0,20]])([15,15])



var points = []

var altezza = 2


function montagne(p) {

	var x = p[0]

	var y = p[1]

	if(x<5)
		var z = altezza + ( Math.random()*altezza*0.3 )

	else if (y<5)
		var z = altezza + ( Math.random()*altezza*0.3 )

	else if(x>=5 && x<=12)
		var z = altezza + ( Math.random()*altezza*1.5 )

	else if (y>= 5 && y<=12 )
		var z = altezza + ( Math.random()*altezza*1.5 )


	else if(x>12 && y>12)
		var z = altezza - ( Math.random()*altezza*0.5 )	

	else
		var z = altezza

	points.push([x,y,z])
	
	return [x,y,z]

}

var paesaggio = MAP(montagne)(domain);

DRAW(paesaggio)