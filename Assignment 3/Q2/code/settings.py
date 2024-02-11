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
' X    XX                XX  ',
'      XX            C XXX   ',
'     XXXX           XXXC    ',
'    XXXX     C        XXX   ',
'C XXXXXX    XX    XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXXX '],
'text':'This is level 0',
'unlock':1,
'pos':((screen_width/5),400)
 }

level_map2 = {'mapdata':[
'                            ',
'                            ',
' C      PC                  ',
' XX    XXX              XXX ',
' XXX       C             XX ',
' XX      XXXX               ',
' X    XX                XX  ',
'      XX            C XXX   ',
'     XXXX           XXXC    ',
'    XXXX     C        XXX   ',
'C XXXXXX    XX    XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXXX '],
'text':'This is level 0',
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
'        X        X          ',
'   XXX                XXX   ',
' B           K            B ',
'  XXXXXXXXXXXXXXXXXXXXXXXX  ',
'                            ',
'                            '],
'text':'This is level 0',
'unlock':3,
'pos':((screen_width/5*3),400)
 }

winning_map = {'mapdata':[
'                            ',
'                            ',
'                            ',
'       X     X              ',
'        X X X               ',
'         X X  P             ',
'              X             ',
'              X             ',
'              X             ',
'                XX  X       ',
'                X X X       ',
'                X  XX       ',
'                            ',
'              C             '],
'text':'This is level 0',
'unlock':4,
'pos':((screen_width/5*4),400)
 }

levels = {
    0:level_map1,
    1:level_map2,
    2:level_map3,
    3:winning_map
}
