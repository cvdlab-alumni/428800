from pyplasm import *

# exercise 1

# create singular objects
circularColumn = CYLINDER([2, 4+33])(24)
rectagularColumn = CUBOID([4,4,33])
miniRectagularColumn = CUBOID([2,2,33])

# --- start sequence of columns for first level ---
rectangularColumns0 = INSR(PROD)(AA(QUOTE)([[-4,-35,4,-35,4,-35,4],[-4,-71,4],[4+33]]))
multplyAndTranslateColumn0 = CONS(AA(T([1,2]))([[0,0],[39,0],[78,0],[117,0],[156,0],[0,75],[156,75]]))
seriesOfCircularColumn = STRUCT(multplyAndTranslateColumn0(circularColumn))

pillars0 = STRUCT([rectangularColumns0,T([1,2])([2,2])(seriesOfCircularColumn)])

# --- start sequence of columns for second level ---

rectangularColumns1 = INSR(PROD)(AA(QUOTE)([[4,-35,4,-35,4,-35,-4,-35,4],[4,-71,4],[-4-33,-7,33]]))
rectagularColumnShifted1 = T([1,3])([117,44])(rectagularColumn)
circularColumnShifted1 = T([1,2,3])([117,75,44])(circularColumn)
pillars1 = STRUCT([rectangularColumns1,rectagularColumnShifted1,T([1,2])([2,2])(circularColumnShifted1)])
pillars1 = T([3])([-2])(pillars1)

# --- start sequence of columns for third level ---

rectangularColumns2 = INSR(PROD)(AA(QUOTE)([[4,-35,4,-35,-4,-35,-4,-35,4],[4,-71,4],[-4-33,-7,-33,-7,33]]))
multplyAndTranslateColumn2 = CONS(AA(T([1,2,3]))([[78,75,84],[117,75,84]]))
seriesOfrectangularColumns2 = STRUCT(multplyAndTranslateColumn2(rectagularColumn))
pillars2 = STRUCT([rectangularColumns2,seriesOfrectangularColumns2])
pillars2 = T([3])([-4])(pillars2)


# --- start sequence of columns for last level ---

rectangularColumns3 = INSR(PROD)(AA(QUOTE)([[-4,-35,-4,-35,4,-35,-4,-35,4],[4,-71,4],[-4-33,-7,-33,-7,-33,-7,33]]))
multiplyAndTranslateMiniRectagularColumn3 = CONS(AA(T([1,2,3]))([[0,75,124],[39,75,124]]))
seriesOfMiniRectagularColumn3 = STRUCT(multiplyAndTranslateMiniRectagularColumn3(miniRectagularColumn))
pillars3 = STRUCT([rectangularColumns3,T([1,2,3])([117,75,124])(rectagularColumn),seriesOfMiniRectagularColumn3])
pillars3 = T([3])([-6])(pillars3)


# exercise 2

# --- start sequence of horizontal partitions for first level ---

horizontalPartition1F0 = INSR(PROD)(AA(QUOTE)([[20],[-71,20],[4]]))
horizontalPartition2F0 = INSR(PROD)(AA(QUOTE)([[-20,112],[-29,62],[4]])) #pezzo grosso
horizontalPartition3F0 = INSR(PROD)(AA(QUOTE)([[-20,17],[-22,7],[4]])) #pezzettino da attaccare semicerchio
horizontalPartition4F0 = INSR(PROD)(AA(QUOTE)([[-132,15],[-54,37],[4]])) #secondo pezzetto da attaccare semicerchio
horizontalPartition5F0 = CYLINDER([18.5,4])(12) #todo
horizontalPartition6F0 = CYLINDER([8.5,4])(12) #semi cerchio piccolo
horizontalPartition7F0 = INSR(PROD)(AA(QUOTE)([[-132,5],[-49,10],[4]]))

circleShifted1F0 = T([1,2])([28.5,22])(horizontalPartition6F0) #piccolo
circleShifted2F0 = T([1,2])([147,72.5])(horizontalPartition5F0)

floor0 = STRUCT([horizontalPartition1F0,horizontalPartition2F0,horizontalPartition3F0,horizontalPartition4F0,circleShifted1F0,circleShifted2F0,horizontalPartition7F0])

# --- start sequence of horizontal partitions for second level ---

horizontalPartition1F1 = INSR(PROD)(AA(QUOTE)([[17],[91],[-4,-33,5]]))
horizontalPartition2F1 = INSR(PROD)(AA(QUOTE)([[-17,144],[-87,4],[-4,-33,5]]))
horizontalPartition3F1 = INSR(PROD)(AA(QUOTE)([[-17,144],[73],[-4,-33,5]]))
horizontalPartition4F1 = INSR(PROD)(AA(QUOTE)([[-17,-70,74],[-73,14],[-4,-33,5]]))
horizontalPartition5F1 = INSR(PROD)(AA(QUOTE)([[16],[-72,15],[-4,-33,5]])) #balcone
hP5f1Shifted = T([1,2])([-16,3])(horizontalPartition5F1)

floor1 = STRUCT([horizontalPartition1F1,horizontalPartition2F1,horizontalPartition3F1,horizontalPartition4F1,hP5f1Shifted])


# --- start sequence of horizontal partitions for third level ---

horizontalPartition1F2 = INSR(PROD)(AA(QUOTE)([[17],[91],[-4,-33,-5,-33,5]]))
horizontalPartition2F2 = INSR(PROD)(AA(QUOTE)([[-17,144],[-87,4],[-4,-33,-5,-33,5]]))
horizontalPartition3F2 = INSR(PROD)(AA(QUOTE)([[-17,144],[73],[-4,-33,-5,-33,5]]))
horizontalPartition4F2 = INSR(PROD)(AA(QUOTE)([[-17,-70,74],[-73,14],[-4,-33,-5,-33,5]]))

floor2 = STRUCT([horizontalPartition1F2,horizontalPartition2F2,horizontalPartition3F2,horizontalPartition4F2])

# --- start sequence of horizontal partitions for the fourth level ---

horizontalPartition1F3 = INSR(PROD)(AA(QUOTE)([[83],[95],[-4,-33,-5,-33,-5,-33,5]]))
horizontalPartition2F3 = INSR(PROD)(AA(QUOTE)([[-83,77],[-91,4],[-4,-33,-5,-33,-5,-33,5]]))
horizontalPartition3F3 = INSR(PROD)(AA(QUOTE)([[-83,77],[77],[-4,-33,-5,-33,-5,-33,5]]))
horizontalPartition4F3 = INSR(PROD)(AA(QUOTE)([[-83,-44,33],[-77,14],[-4,-33,-5,-33,-5,-33,5]]))

floor3 = STRUCT([horizontalPartition1F3,horizontalPartition2F3,horizontalPartition3F3,horizontalPartition4F3])

# --- start sequence of horizontal partitions for last level ---

horizontalPartition1F4 = INSR(PROD)(AA(QUOTE)([[160],[-72,23],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))
horizontalPartition2F4 = INSR(PROD)(AA(QUOTE)([[-72,88],[72],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))
horizontalPartition3F4 = INSR(PROD)(AA(QUOTE)([[160],[4],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))
horizontalPartition4F4 = INSR(PROD)(AA(QUOTE)([[4],[72],[-4,-33,-5,-33,-5,-33,-5,-33,7]]))

floor4 = STRUCT([horizontalPartition1F4,horizontalPartition2F4,horizontalPartition3F4,horizontalPartition4F4])

# --- the terrain for the building 
terrain = COLOR(BLACK)(T([1,2,3])([-20,-20,-5])(INSR(PROD)(AA(QUOTE)([[205],[135],[5]]))))



# --- exercise 3

# --- start sequence of horizontal partitions for east level ---

verticalPartition1E = INSR(PROD)(AA(QUOTE)([[160],[4],[-144,14]]))
verticalPartition2E = INSR(PROD)(AA(QUOTE)([[76],[4],[-33,94]]))
verticalPartition3E = INSR(PROD)(AA(QUOTE)([[-72,4],[4],[-33,125]]))
verticalPartition4E = INSR(PROD)(AA(QUOTE)([[84],[4],[20]]))
verticalPartition5E = INSR(PROD)(AA(QUOTE)([[-111,49],[4],[-33,125]]))

# --- use this function to multiplicate and translate the object so we can instanziate only one object of that kind---

multplyAndTranslatevp4e = CONS(AA(T([1,3]))([[76,33],[76,70],[76,107]]))
seriesOfvp4e = STRUCT(multplyAndTranslatevp4e(verticalPartition4E))


east = STRUCT([verticalPartition1E,verticalPartition2E,verticalPartition3E,seriesOfvp4e,verticalPartition5E])

# --- start sequence of horizontal partitions for west level ---

verticalPartition1W = INSR(PROD)(AA(QUOTE)([[160],[-4,-87,4],[-107,51]]))
verticalPartition2W = INSR(PROD)(AA(QUOTE)([[160],[-4,-87,4],[20]]))

# --- use this function to multiplicate and translate the object so we can instanziate only one object of that kind---

multplyAndTranslatevp2w = CONS(AA(T([3]))([[33],[70]]))
seriesOfvp2w = STRUCT(multplyAndTranslatevp2w(verticalPartition2W))

verticalPartition3W = INSR(PROD)(AA(QUOTE)([[135],[-4,-87,4],[22]]))
verticalPartition4W = INSR(PROD)(AA(QUOTE)([[103],[-4,-87,4],[-22,7]]))
verticalPartition5W = INSR(PROD)(AA(QUOTE)([[-103,-7,25],[-4,-87,4],[-22,7]]))
verticalPartition6W = INSR(PROD)(AA(QUOTE)([[135],[-4,-87,4],[-22,-7,4]]))
verticalPartition7W = INSR(PROD)(AA(QUOTE)([[90],[-4,-87,4],[-22,-7,-4,-20,17]]))
verticalPartition8W = INSR(PROD)(AA(QUOTE)([[-90,-35,35],[-4,-87,4],[-22,-7,-4,-20,17]]))
verticalPartition9W = INSR(PROD)(AA(QUOTE)([[129],[-4,-87,4],[-22,-7,-4,-20,-17,-20,17]]))
verticalPartition10W = INSR(PROD)(AA(QUOTE)([[-129,-2,7],[-4,-87,4],[-22,-7,-4,-20,-17,-20,17]]))
verticalPartition11W = INSR(PROD)(AA(QUOTE)([[-129,-2,-7,-2,20],[-4,-87,4],[-22,-7,-4,-20,-17,-20,17]]))

west = STRUCT([verticalPartition1W,seriesOfvp2w,verticalPartition3W,verticalPartition4W,verticalPartition5W,verticalPartition6W,verticalPartition7W,verticalPartition8W,verticalPartition9W,verticalPartition10W,verticalPartition11W])



# --- start sequence of horizontal partitions for north level ---

verticalPartition1N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[87],[-33,-20,-17,-20,-17,-20,-17,14]]))
verticalPartition2N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[87],[20]]))

# --- use this function to multiplicate and translate the object so we can instanziate only one object of that kind---
multplyAndTranslatevp2n = CONS(AA(T([3]))([[33],[33+20+17],[33+20+17+20+17]]))
seriesOfvp2n = STRUCT(multplyAndTranslatevp2n(verticalPartition2N))

verticalPartition3N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[4],[-33,158-33]]))
verticalPartition4N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[95],[-33,4]]))
verticalPartition5N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[95],[5]]))

# --- use this function to multiplicate and translate the object so we can instanziate only one object of that kind---
multplyAndTranslatevp5n = CONS(AA(T([3]))([[33+4+37],[33+4+33+5+36]]))
seriesOfvp5n = STRUCT(multplyAndTranslatevp5n(verticalPartition5N))

verticalPartition6N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[95],[-33,-20,-17,-20,-17,-20,-17,-7,7]]))
verticalPartition7N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[-95+7+13,13],[-33,158-33]]))

nord = STRUCT([verticalPartition1N,seriesOfvp2n,verticalPartition3N,verticalPartition4N,seriesOfvp5n,verticalPartition6N,verticalPartition7N])
nord = T([1])([1])(nord)


# --- start sequence of horizontal partitions for south level ---


verticalPartition1S = INSR(PROD)(AA(QUOTE)([[4],[95],[-33,-4,-30,-5,-30,-25,-17,14]]))
verticalPartition2S = INSR(PROD)(AA(QUOTE)([[4],[95],[-33,-4,-30,-5,-30,25]]))
verticalPartition3S = INSR(PROD)(AA(QUOTE)([[4],[95],[-33,-4,-30,5]]))
verticalPartition4S = INSR(PROD)(AA(QUOTE)([[4],[95],[-33,4]]))
verticalPartition5S = INSR(PROD)(AA(QUOTE)([[4],[2],[-33,158-33]]))
verticalPartition6S = INSR(PROD)(AA(QUOTE)([[4],[-95+4+4,4],[-33-4,158-33-14-17-4]]))
verticalPartition7S = INSR(PROD)(AA(QUOTE)([[4],[-95+4+2+2+20,10],[-33-4,158-33-4-30-2]]))
verticalPartition8S = INSR(PROD)(AA(QUOTE)([[4],[-95+4+2+2+20,20],[-33-4-5-30,158-33-4-30-2-25-17-14]]))
verticalPartition9S = INSR(PROD)(AA(QUOTE)([[4],[95],[-33-4-30,10]]))


sud = STRUCT([verticalPartition1S,verticalPartition2S,verticalPartition3S,verticalPartition4S,verticalPartition5S,verticalPartition6S,verticalPartition7S,verticalPartition8S,verticalPartition9S])


# --- putting all togheter---
building = STRUCT([pillars0,pillars1,pillars2,pillars3,floor0,floor1,floor2,floor3,floor4,nord,sud,west,east,terrain])
VIEW(building)
