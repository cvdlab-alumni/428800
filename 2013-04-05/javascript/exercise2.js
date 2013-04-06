 // ricordarsi di sistemarli circolari
 // circolari con 	trunk = CYLINDER([r, (10.0/12)*h])(12)
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

// from pyplasm import *

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

horizontalPartition1F1 = GRID(([[17],[91],[-4,-33,5]]))
horizontalPartition2F1 = GRID(([[-17,144],[-87,4],[-4,-33,5]]))
horizontalPartition3F1 = GRID(([[-17,144],[73],[-4,-33,5]]))
horizontalPartition4F1 = GRID(([[-17,-70,74],[-73,14],[-4,-33,5]]))
horizontalPartition5F1 = GRID(([[16],[-72,15],[-4,-33,5]])) //balcone
hP5f1Shifted = T([1,2])([-16,3])(horizontalPartition5F1)

floor1 = STRUCT([horizontalPartition1F1,horizontalPartition2F1,horizontalPartition3F1,horizontalPartition4F1,hP5f1Shifted])

horizontalPartition1F2 = GRID(([[17],[91],[-4,-33,-5,-33,5]]))
horizontalPartition2F2 = GRID(([[-17,144],[-87,4],[-4,-33,-5,-33,5]]))
horizontalPartition3F2 = GRID(([[-17,144],[73],[-4,-33,-5,-33,5]]))
horizontalPartition4F2 = GRID(([[-17,-70,74],[-73,14],[-4,-33,-5,-33,5]]))

floor2 = STRUCT([horizontalPartition1F2,horizontalPartition2F2,horizontalPartition3F2,horizontalPartition4F2])

horizontalPartition1F3 = GRID(([[83],[95],[-4,-33,-5,-33,-5,-33,5]]))
horizontalPartition2F3 = GRID(([[-83,77],[-91,4],[-4,-33,-5,-33,-5,-33,5]]))
horizontalPartition3F3 = GRID(([[-83,77],[77],[-4,-33,-5,-33,-5,-33,5]]))
horizontalPartition4F3 = GRID(([[-83,-44,33],[-77,14],[-4,-33,-5,-33,-5,-33,5]]))

floor3 = STRUCT([horizontalPartition1F3,horizontalPartition2F3,horizontalPartition3F3,horizontalPartition4F3])

horizontalPartition1F4 = GRID(([[160],[-72,23],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))
horizontalPartition2F4 = GRID(([[-72,88],[72],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))
horizontalPartition3F4 = GRID(([[160],[4],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))
horizontalPartition4F4 = GRID(([[4],[72],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))

floor4 = STRUCT([horizontalPartition1F4,horizontalPartition2F4,horizontalPartition3F4,horizontalPartition4F4])

building = STRUCT([floor0,floor1,floor2,floor3,floor4])
VIEW(building)