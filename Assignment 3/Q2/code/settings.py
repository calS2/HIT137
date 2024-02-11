tile_size = 64
screen_height = 1200
#screen_width = len(level_map) * tile_size
screen_width =  28 * tile_size

level_map1 = {'mapdata':[
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
'                            ',
' CC     P                   ',
' XX    XXX              XXX ',
' XXX     CCCC            XX ',
' XX      XXXX               ',
' X    XX                XX  ',
'      XX            C XXX   ',
'     XXXX           XXXC    ',
'    XXXX     C        XXX   ',
'C XXXXXX    XX    XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXXX '],
'text':'This is level 0',
'unlock':3,
'pos':((screen_width/5*3),400)
 }

levels = {
    0:level_map1,
    1:level_map2,
    2:level_map3,
}
