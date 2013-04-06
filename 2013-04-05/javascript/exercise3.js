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

//ricordarsi il balcone
verticalPartition1E = GRID(([[160],[4],[-144,14]]))
verticalPartition2E = GRID(([[76],[4],[-33,94]]))
verticalPartition3E = GRID(([[-72,4],[4],[-33,125]]))
verticalPartition4E = GRID(([[84],[4],[20]]))
verticalPartition5E = GRID(([[-111,49],[4],[-33,125]]))

multplyAndTranslatevp4e = CONS(AA(T([1,3]))([[76,33],[76,70],[76,107]]))
seriesOfvp4e = STRUCT(multplyAndTranslatevp4e(verticalPartition4E))


east = STRUCT([verticalPartition1E,verticalPartition2E,verticalPartition3E,seriesOfvp4e,verticalPartition5E])

verticalPartition1W = GRID(([[160],[-4,-87,4],[-107,51]]))
verticalPartition2W = GRID(([[160],[-4,-87,4],[20]]))

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

verticalPartition1N = GRID(([[-4,-152,4],[87],[-33,-20,-17,-20,-17,-20,-17,14]]))
verticalPartition2N = GRID(([[-4,-152,4],[87],[20]]))

multplyAndTranslatevp2n = CONS(AA(T([3]))([[33],[33+20+17],[33+20+17+20+17]]))
seriesOfvp2n = STRUCT(multplyAndTranslatevp2n(verticalPartition2N))

verticalPartition3N = GRID(([[-4,-152,4],[4],[-33,158-33]]))
verticalPartition4N = GRID(([[-4,-152,4],[95],[-33,4]]))
verticalPartition5N = GRID(([[-4,-152,4],[95],[5]]))

multplyAndTranslatevp5n = CONS(AA(T([3]))([[33+4+37],[33+4+33+5+36]]))
seriesOfvp5n = STRUCT(multplyAndTranslatevp5n(verticalPartition5N))

verticalPartition6N = GRID(([[-4,-152,4],[95],[-33,-20,-17,-20,-17,-20,-17,-7,7]]))
verticalPartition7N = GRID(([[-4,-152,4],[-95+7+13,13],[-33,158-33]]))

nord = STRUCT([verticalPartition1N,seriesOfvp2n,verticalPartition3N,verticalPartition4N,seriesOfvp5n,verticalPartition6N,verticalPartition7N])
nord = T([1])([1])(nord)

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


building = STRUCT([east,west,nord,sud])
VIEW(building)
