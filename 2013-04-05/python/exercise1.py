from pyplasm import *
# ricordarsi di sistemarli circolari
# circolari con 	trunk = CYLINDER([r, (10.0/12)*h])(12)
#ricordarsi di sistemare le altezze vedi il 2
circularColumn = CYLINDER([2, 4+33])(24)
rectagularColumn = CUBOID([4,4,33])
miniRectagularColumn = CUBOID([2,2,33])


rectangularColumns0 = INSR(PROD)(AA(QUOTE)([[-4,-35,4,-35,4,-35,4],[-4,-71,4],[4+33]]))
multplyAndTranslateColumn0 = CONS(AA(T([1,2]))([[0,0],[39,0],[78,0],[117,0],[156,0],[0,75]]))
seriesOfCircularColumn = STRUCT(multplyAndTranslateColumn0(circularColumn))

pillars0 = STRUCT([rectangularColumns0,T([1,2])([2,2])(seriesOfCircularColumn)])
# VIEW(pillars0)
rectangularColumns1 = INSR(PROD)(AA(QUOTE)([[4,-35,4,-35,4,-35,-4,-35,4],[4,-71,4],[-4-33,-7,33]]))
rectagularColumnShifted1 = T([1,3])([117,47])(rectagularColumn)
circularColumnShifted1 = T([1,2,3])([117,75,47])(circularColumn)
pillars1 = STRUCT([rectangularColumns1,rectagularColumnShifted1,T([1,2])([2,2])(circularColumnShifted1)])
# VIEW(STRUCT(pillars1))

rectangularColumns2 = INSR(PROD)(AA(QUOTE)([[4,-35,4,-35,-4,-35,-4,-35,4],[4,-71,4],[-4-33,-7,-33,-7,33]]))
multplyAndTranslateColumn2 = CONS(AA(T([1,2,3]))([[78,75,84],[117,75,84]]))
seriesOfrectangularColumns2 = STRUCT(multplyAndTranslateColumn2(rectagularColumn))
pillars2 = STRUCT([rectangularColumns2,seriesOfrectangularColumns2])
# VIEW(pillars2)

rectangularColumns3 = INSR(PROD)(AA(QUOTE)([[-4,-35,-4,-35,4,-35,-4,-35,4],[4,-71,4],[-4-33,-7,-33,-7,-33,-7,33]]))
multiplyAndTranslateMiniRectagularColumn3 = CONS(AA(T([1,2,3]))([[0,75,124],[39,75,124]]))
seriesOfMiniRectagularColumn3 = STRUCT(multiplyAndTranslateMiniRectagularColumn3(miniRectagularColumn))
pillars3 = STRUCT([rectangularColumns3,T([1,2,3])([117,75,124])(rectagularColumn),seriesOfMiniRectagularColumn3])

building = STRUCT([pillars0,pillars1,pillars2,pillars3])
VIEW(building)

