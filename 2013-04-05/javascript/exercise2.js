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

// --- putting all togheter---
building = STRUCT([pillars0,pillars1,pillars2,pillars3,floor0,floor1,floor2,floor3,floor4,terrain])
VIEW(building)