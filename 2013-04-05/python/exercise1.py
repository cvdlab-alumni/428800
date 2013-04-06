from pyplasm import *

# create singular objects
circularColumn = CYLINDER([2, 4+33])(24)
rectagularColumn = CUBOID([4,4,33])
miniRectagularColumn = CUBOID([2,2,33])

# --- start sequence of columns for first level ---
rectangularColumns0 = INSR(PROD)(AA(QUOTE)([[-4,-35,4,-35,4,-35,4],[-4,-71,4],[4+33]]))
multplyAndTranslateColumn0 = CONS(AA(T([1,2]))([[0,0],[39,0],[78,0],[117,0],[156,0],[0,75]]))
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

# --- putting all togheter---

building = STRUCT([pillars0,pillars1,pillars2,pillars3])
VIEW(building)

