function casa(x,y){

	var punti = [[0,0],[x,0],[0,y],[x,y],[x/2,y+y*0.5]];

	var cells = [[0,1,2],[1,3,2],[2,3,4]];

	var casa1 = SIMPLICIAL_COMPLEX(punti)(cells);

	casa1 = EXTRUDE([1])(casa1);

	return casa1;
}


function villaggio(offset_x,offset_y,offset_casa_x,offset_casa_y, nx,ny) {

		var seriecase = STRUCT(REPLICA(nx)([casa(Math.random()*0.5+1,Math.random()*0.5+1), T([0])([offset_casa_x]), casa(Math.random()*0.5+1,Math.random()*0.5+1), T([0])([offset_casa_x])]))

		var seriecase  = R([1,2])([PI/2])(seriecase)

		var ncase = []

		for (var i = 0;i < ny; i++) {
			ncase.push(seriecase);
			ncase.push(T([1])([offset_casa_y]))
		};

		var ncase = STRUCT(ncase);
		
		var ncase = T([0,1])([offset_x,offset_y])(ncase);

		return ncase
}

var villaggio1 = villaggio(25,4,4,4,3,3)

var villaggio2 = villaggio(-25,3,3,5,4,2)

var villaggio1 = T([2])([2])(villaggio1)

var villaggio2 = T([2])([2])(villaggio2)

DRAW(villaggio1)

DRAW(villaggio2)