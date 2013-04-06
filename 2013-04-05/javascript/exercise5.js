//convenient method used for translation from pyplasm
T = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });

  return function (values) {
    return function (object) {
     return object.clone().translate(dims, values);
    };
  };
};
  
R = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });
   
  return function (angle) {
    return function (object) {
      return object.clone().rotate(dims, angle);
    };
  };
};
  
S = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });

  return function (values) {
    return function (object) {
      return object.clone().scale(dims, values);
    };
  };
};

S3 = S2;
S2 = S1;
S1 = S0;

GRID = SIMPLEX_GRID;

NN = REPLICA;

VIEW = DRAW;

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
 
// create singular objects
circularColumn = EXTRUDE([4+33])(circle([2]))
rectagularColumn = CUBOID([4,4,33])
miniRectagularColumn = CUBOID([2,2,33])


// --- start sequence of columns for first level ---
rectangularColumns0 = GRID(([[-4,-35,4,-35,4,-35,4],[-4,-71,4],[4+33]]))
multplyAndTranslateColumn0 = CONS(AA(T([1,2]))([[0,0],[39,0],[78,0],[117,0],[156,0],[0,75],[156,75]]))
seriesOfCircularColumn = STRUCT(multplyAndTranslateColumn0(circularColumn))

pillars0 = STRUCT([rectangularColumns0,T([1,2])([2,2])(seriesOfCircularColumn)])

// --- start sequence of columns for second level ---
rectangularColumns1 = GRID(([[4,-35,4,-35,4,-35,-4,-35,4],[4,-71,4],[-4-33,-7,33]]))
rectagularColumnShifted1 = T([1,3])([117,44])(rectagularColumn)
circularColumnShifted1 = T([1,2,3])([117,75,44])(circularColumn)
pillars1 = STRUCT([rectangularColumns1,rectagularColumnShifted1,T([1,2])([2,2])(circularColumnShifted1)])
pillars1 = T([3])([-2])(pillars1)


// --- start sequence of columns for third level ---
rectangularColumns2 = GRID(([[4,-35,4,-35,-4,-35,-4,-35,4],[4,-71,4],[-4-33,-7,-33,-7,33]]))
multplyAndTranslateColumn2 = CONS(AA(T([1,2,3]))([[78,75,84],[117,75,84]]))
seriesOfrectangularColumns2 = STRUCT(multplyAndTranslateColumn2(rectagularColumn))
pillars2 = STRUCT([rectangularColumns2,seriesOfrectangularColumns2])
pillars2 = T([3])([-4])(pillars2)

// --- start sequence of columns for last level ---
rectangularColumns3 = GRID(([[-4,-35,-4,-35,4,-35,-4,-35,4],[4,-71,4],[-4-33,-7,-33,-7,-33,-7,33]]))
multiplyAndTranslateMiniRectagularColumn3 = CONS(AA(T([1,2,3]))([[0,75,124],[39,75,124]]))
seriesOfMiniRectagularColumn3 = STRUCT(multiplyAndTranslateMiniRectagularColumn3(miniRectagularColumn))
pillars3 = STRUCT([rectangularColumns3,T([1,2,3])([117,75,124])(rectagularColumn),seriesOfMiniRectagularColumn3])
pillars3 = T([3])([-6])(pillars3)


// --- exercise 2
// --- start sequence of horizontal partitions for first level ---
horizontalPartition1F0 = GRID(([[20],[-71,20],[4]]))
horizontalPartition2F0 = GRID(([[-20,112],[-29,62],[4]])) ////pezzo grosso
horizontalPartition3F0 = GRID(([[-20,17],[-22,7],[4]])) ////pezzettino da attaccare semicerchio
horizontalPartition4F0 = GRID(([[-132,15],[-54,37],[4]])) ////secondo pezzetto da attaccare semicerchio
horizontalPartition5F0 = EXTRUDE([4])(circle([18.5])) ////todo
horizontalPartition6F0 = EXTRUDE([4])(circle([8.5])) ////semi cerchio piccolo
horizontalPartition7F0 = GRID(([[-132,5],[-49,10],[4]]))

circleShifted1F0 = T([1,2])([28.5,22])(horizontalPartition6F0) ////piccolo
circleShifted2F0 = T([1,2])([147,72.5])(horizontalPartition5F0)

floor0 = STRUCT([horizontalPartition1F0,horizontalPartition2F0,horizontalPartition3F0,horizontalPartition4F0,circleShifted1F0,circleShifted2F0,horizontalPartition7F0])
// // VIEW(floor0)

// --- start sequence of horizontal partitions for second level ---
horizontalPartition1F1 = GRID(([[17],[91],[-4,-33,5]]))
horizontalPartition2F1 = GRID(([[-17,144],[-87,4],[-4,-33,5]]))
horizontalPartition3F1 = GRID(([[-17,144],[73],[-4,-33,5]]))
horizontalPartition4F1 = GRID(([[-17,-70,74],[-73,14],[-4,-33,5]]))
horizontalPartition5F1 = GRID(([[16],[-72,15],[-4,-33,5]])) //balcone
hP5f1Shifted = T([1,2])([-16,3])(horizontalPartition5F1)

floor1 = STRUCT([horizontalPartition1F1,horizontalPartition2F1,horizontalPartition3F1,horizontalPartition4F1,hP5f1Shifted])

// --- start sequence of horizontal partitions for third level ---
horizontalPartition1F2 = GRID(([[17],[91],[-4,-33,-5,-33,5]]))
horizontalPartition2F2 = GRID(([[-17,144],[-87,4],[-4,-33,-5,-33,5]]))
horizontalPartition3F2 = GRID(([[-17,144],[73],[-4,-33,-5,-33,5]]))
horizontalPartition4F2 = GRID(([[-17,-70,74],[-73,14],[-4,-33,-5,-33,5]]))

floor2 = STRUCT([horizontalPartition1F2,horizontalPartition2F2,horizontalPartition3F2,horizontalPartition4F2])

// --- start sequence of horizontal partitions for the fourth level ---
horizontalPartition1F3 = GRID(([[83],[95],[-4,-33,-5,-33,-5,-33,5]]))
horizontalPartition2F3 = GRID(([[-83,77],[-91,4],[-4,-33,-5,-33,-5,-33,5]]))
horizontalPartition3F3 = GRID(([[-83,77],[77],[-4,-33,-5,-33,-5,-33,5]]))
horizontalPartition4F3 = GRID(([[-83,-44,33],[-77,14],[-4,-33,-5,-33,-5,-33,5]]))

floor3 = STRUCT([horizontalPartition1F3,horizontalPartition2F3,horizontalPartition3F3,horizontalPartition4F3])

// --- start sequence of horizontal partitions for last level ---
horizontalPartition1F4 = GRID(([[160],[-72,23],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))
horizontalPartition2F4 = GRID(([[-72,88],[72],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))
horizontalPartition3F4 = GRID(([[160],[4],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))
horizontalPartition4F4 = GRID(([[4],[72],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))

floor4 = STRUCT([horizontalPartition1F4,horizontalPartition2F4,horizontalPartition3F4,horizontalPartition4F4])

// --- the terrain for the building 
terrain = COLOR([0,0,0])(T([1,2,3])([-20,-20,-5])(GRID([[205],[135],[5]])))


// --- exercise 3
// --- start sequence of horizontal partitions for east level ---
verticalPartition1E = GRID(([[160],[4],[-144,14]]))
verticalPartition2E = GRID(([[76],[4],[-33,94]]))
verticalPartition3E = GRID(([[-72,4],[4],[-33,125]]))
verticalPartition4E = GRID(([[84],[4],[20]]))
verticalPartition5E = GRID(([[-111,49],[4],[-33,125]]))

// --- use this function to multiplicate and translate the object so we can instanziate only one object of that kind---
multplyAndTranslatevp4e = CONS(AA(T([1,3]))([[76,33],[76,70],[76,107]]))
seriesOfvp4e = STRUCT(multplyAndTranslatevp4e(verticalPartition4E))


east = STRUCT([verticalPartition1E,verticalPartition2E,verticalPartition3E,seriesOfvp4e,verticalPartition5E])

// --- start sequence of horizontal partitions for west level ---
verticalPartition1W = GRID(([[160],[-4,-87,4],[-107,51]]))
verticalPartition2W = GRID(([[160],[-4,-87,4],[20]]))

// --- use this function to multiplicate and translate the object so we can instanziate only one object of that kind---
multplyAndTranslatevp2w = CONS(AA(T([3]))([[33],[70]]))
seriesOfvp2w = STRUCT(multplyAndTranslatevp2w(verticalPartition2W))

verticalPartition3W = GRID(([[135],[-4,-87,4],[22]]))
verticalPartition4W = GRID(([[103],[-4,-87,4],[-22,7]]))
verticalPartition5W = GRID(([[-103,-7,25],[-4,-87,4],[-22,7]]))
verticalPartition6W = GRID(([[135],[-4,-87,4],[-22,-7,4]]))
verticalPartition7W = GRID(([[90],[-4,-87,4],[-22,-7,-4,-20,17]]))
verticalPartition8W = GRID(([[-90,-35,35],[-4,-87,4],[-22,-7,-4,-20,17]]))
verticalPartition9W = GRID(([[129],[-4,-87,4],[-22,-7,-4,-20,-17,-20,17]]))
verticalPartition10W = GRID(([[-129,-2,7],[-4,-87,4],[-22,-7,-4,-20,-17,-20,17]]))
verticalPartition11W = GRID(([[-129,-2,-7,-2,20],[-4,-87,4],[-22,-7,-4,-20,-17,-20,17]]))

west = STRUCT([verticalPartition1W,seriesOfvp2w,verticalPartition3W,verticalPartition4W,verticalPartition5W,verticalPartition6W,verticalPartition7W,verticalPartition8W,verticalPartition9W,verticalPartition10W,verticalPartition11W])

// --- start sequence of horizontal partitions for north level ---
verticalPartition1N = GRID(([[-4,-152,4],[87],[-33,-20,-17,-20,-17,-20,-17,14]]))
verticalPartition2N = GRID(([[-4,-152,4],[87],[20]]))

// --- use this function to multiplicate and translate the object so we can instanziate only one object of that kind---
multplyAndTranslatevp2n = CONS(AA(T([3]))([[33],[33+20+17],[33+20+17+20+17]]))
seriesOfvp2n = STRUCT(multplyAndTranslatevp2n(verticalPartition2N))

verticalPartition3N = GRID(([[-4,-152,4],[4],[-33,158-33]]))
verticalPartition4N = GRID(([[-4,-152,4],[95],[-33,4]]))
verticalPartition5N = GRID(([[-4,-152,4],[95],[5]]))

// --- use this function to multiplicate and translate the object so we can instanziate only one object of that kind---
multplyAndTranslatevp5n = CONS(AA(T([3]))([[33+4+37],[33+4+33+5+36]]))
seriesOfvp5n = STRUCT(multplyAndTranslatevp5n(verticalPartition5N))

verticalPartition6N = GRID(([[-4,-152,4],[95],[-33,-20,-17,-20,-17,-20,-17,-7,7]]))
verticalPartition7N = GRID(([[-4,-152,4],[-95+7+13,13],[-33,158-33]]))

nord = STRUCT([verticalPartition1N,seriesOfvp2n,verticalPartition3N,verticalPartition4N,seriesOfvp5n,verticalPartition6N,verticalPartition7N])
nord = T([1])([1])(nord)

// --- start sequence of horizontal partitions for south level ---
verticalPartition1S = GRID(([[4],[95],[-33,-4,-30,-5,-30,-25,-17,14]]))
verticalPartition2S = GRID(([[4],[95],[-33,-4,-30,-5,-30,25]]))
verticalPartition3S = GRID(([[4],[95],[-33,-4,-30,5]]))
verticalPartition4S = GRID(([[4],[95],[-33,4]]))
verticalPartition5S = GRID(([[4],[2],[-33,158-33]]))
verticalPartition6S = GRID(([[4],[-95+4+4,4],[-33-4,158-33-14-17-4]]))
verticalPartition7S = GRID(([[4],[-95+4+2+2+20,10],[-33-4,158-33-4-30-2]]))
verticalPartition8S = GRID(([[4],[-95+4+2+2+20,20],[-33-4-5-30,158-33-4-30-2-25-17-14]]))
verticalPartition9S = GRID(([[4],[95],[-33-4-30,10]]))


sud = STRUCT([verticalPartition1S,verticalPartition2S,verticalPartition3S,verticalPartition4S,verticalPartition5S,verticalPartition6S,verticalPartition7S,verticalPartition8S,verticalPartition9S])


// --- exercise 4
// --- generate two windows with black color ---
windowssud = COLOR([0,0,0,0.5])(GRID(([[1],[-4,63],[-33-4-5,25]])))
windowssud2 = COLOR([0,0,0,0.5])(GRID(([[1],[-4,63],[-33-4-5-25-5-5-3,22]])))

// --- exercise 5
// --- l = stair width
// --- n = number of steps
// --- g = height of ground
// --- a = raiser
// --- p = footprint
l = 50.0
n = 13.0
g = 4.0
a = 35.0/n 
p = l/n

// --- generate the step with vertex and cells
vertici = [[0,0],[0,g+a/2.0],[p,a/2.0],[p,g+a/2.0]]
celle = [[1,2,3,4]]
var step2D = SIMPLICIAL_COMPLEX(vertici)([[0,2,1],[1,2,3]]);

// --- generate the step in 3D from the step in 2D
step3D = MAP([S1,S3,S2])(EXTRUDE([15])(step2D))

// --- generate a singular stair
ramp = STRUCT(REPLICA(n)([step3D,T([1,3])([p,a])]))

// --- traslate and multiplicate them to fit with the building
stair1 = T([1,2])([35,72])(ramp)

stair2 = T([1,2,3])([17.5,72,38])(ramp)

stair3 = T([1,2,3])([75,77,74])(ramp)

// --- putting all togheter---
building = STRUCT([pillars0,pillars1,pillars2,pillars3,floor0,floor1,floor2,floor3,floor4,stair1,stair2,stair3,windowssud,windowssud2,nord,sud,west,east,terrain])
VIEW(building)