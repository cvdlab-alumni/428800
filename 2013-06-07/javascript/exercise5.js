function strada(larghezza,altezza){
	return CUBOID([larghezza,altezza,0.1])
}

var strada1 = strada(0.5,3)

var strada2=strada(20,0.3)

var mulAndTrans = CONS(AA(T([0,1]))([[25,4],[29,4],[33,4],[37,4],[41,4],[45,4],[25,8],[29,8],[33,8],[37,8],[41,8],[45,8]]))

var st21 = T([0,1])([25,9])(strada2)

var st22 = T([0,1])([25,6])(strada2)

var strade1 = STRUCT(mulAndTrans(strada1))	

var strade1 = STRUCT([strade1,st21,st22])

var strade1 = T([2])([2])(strade1)

DRAW(strade1)

var strada1 = strada(0.5,4)

var strada2=strada(22,0.5)

var mulAndTrans = CONS(AA(T([0,1]))([[-25,3],[-22,3],[-19,3],[-16,3],[-13,3],[-10,3],[-7,3],[-4,3]]))

var st22 = T([0,1])([-25,6])(strada2)

var strade1 = STRUCT(mulAndTrans(strada1))	

var strade1 = STRUCT([strade1,st21,st22])

var strade1 = T([2])([2])(strade1)

DRAW(strade1)