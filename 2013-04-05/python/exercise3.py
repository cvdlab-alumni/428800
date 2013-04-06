from pyplasm import *

#ricordarsi il balcone
verticalPartition1E = INSR(PROD)(AA(QUOTE)([[160],[4],[-144,14]]))
verticalPartition2E = INSR(PROD)(AA(QUOTE)([[76],[4],[-33,94]]))
verticalPartition3E = INSR(PROD)(AA(QUOTE)([[-72,4],[4],[-33,125]]))
verticalPartition4E = INSR(PROD)(AA(QUOTE)([[84],[4],[20]]))
verticalPartition5E = INSR(PROD)(AA(QUOTE)([[-111,49],[4],[-33,125]]))

multplyAndTranslatevp4e = CONS(AA(T([1,3]))([[76,33],[76,70],[76,107]]))
seriesOfvp4e = STRUCT(multplyAndTranslatevp4e(verticalPartition4E))


east = STRUCT([verticalPartition1E,verticalPartition2E,verticalPartition3E,seriesOfvp4e,verticalPartition5E])

verticalPartition1W = INSR(PROD)(AA(QUOTE)([[160],[-4,-87,4],[-107,51]]))
verticalPartition2W = INSR(PROD)(AA(QUOTE)([[160],[-4,-87,4],[20]]))

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

verticalPartition1N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[87],[-33,-20,-17,-20,-17,-20,-17,14]]))
verticalPartition2N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[87],[20]]))

multplyAndTranslatevp2n = CONS(AA(T([3]))([[33],[33+20+17],[33+20+17+20+17]]))
seriesOfvp2n = STRUCT(multplyAndTranslatevp2n(verticalPartition2N))

verticalPartition3N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[4],[-33,158-33]]))
verticalPartition4N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[95],[-33,4]]))
verticalPartition5N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[95],[5]]))

multplyAndTranslatevp5n = CONS(AA(T([3]))([[33+4+37],[33+4+33+5+36]]))
seriesOfvp5n = STRUCT(multplyAndTranslatevp5n(verticalPartition5N))

verticalPartition6N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[95],[-33,-20,-17,-20,-17,-20,-17,-7,7]]))
verticalPartition7N = INSR(PROD)(AA(QUOTE)([[-4,-152,4],[-95+7+13,13],[-33,158-33]]))

nord = STRUCT([verticalPartition1N,seriesOfvp2n,verticalPartition3N,verticalPartition4N,seriesOfvp5n,verticalPartition6N,verticalPartition7N])
nord = T([1])([1])(nord)

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


building = STRUCT([east,west,nord,sud])
VIEW(building)
