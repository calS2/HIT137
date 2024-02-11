tile_size = 64
screen_height = 1000
#screen_width = len(level_map) * tile_size
screen_width =  20 * tile_size

level_map1 = {'mapdata':[
'                            ',
'                            ',
'                            ',
'        P                   ',
' XX    XXX              XXX ',
' XXX    B  CE    B       XX ',
' XX      XXXXXXXX           ',
' X    XX                X   ',
'      XX            C XX   X',
'     XXXX           XXXC  X ',
'    XXXX     C        XXX   ',
'C XXXXXX    XX    XX        ',
'XXXXXXXX  XXXXXX  XX        '],
'text':'This is level 1',
'unlock':1,
'pos':((screen_width/5),400)
 }

level_map2 = {'mapdata':[
'                            ',
'                            ',
' P      C B   E CC B        ',
' XX    XX  XXXXXXXX         ',
'          X        X   C    ',
'B   E B       C             ',
' XXXXX       XX       XXXX  ',
' XCCC             XX        ',
' XXXX   XX             C    ',
'     X       C        XCX   ',
'            XX         XX   ',
'                            '],
'text':'This is level 2',
'unlock':2,
'pos':((screen_width/5)*2,400)
 }

level_map3 = {'mapdata':[
'                            ',
'                           ',
'                            ',
'                            ',
'             P              ',
'             X              ',
'                            ',
'                            ',
'                            ',
'        X    X   X          ',
'   XXX     X C X      XXX   ',
' B   K     B K B    K     B ',
'  XXXXXXXXXXXXXXXXXXXXXXXX  ',
'                            ',
'                            '],
'text':'This is level 3',
'unlock':3,
'pos':((screen_width/5*3),400)
 }

winning_map = {'mapdata':[
'                      ',
'  X       X           ',
'   X     X            ',
'    X X X C           ',
'     X X  P           ',
'          X           ',
'          X           ',
'          X           ',
'          X           ',
'            X   X     ',
'            XX  X     ',
'            X X X     ',
'            X  XX     ',
'                      '],
'text':'You Won',
'unlock':4,
'pos':((screen_width/5*4),400)
 }

levels = {
    0:level_map1,
    1:level_map2,
    2:level_map3,
    3:winning_map
}
