import libtcodpy as libtcod

import camera

class Tile(object):
    "Base tiles have a background color, and can block movement and/or sight. They may also have a symbol is desired."
    def __init__(self, owner, backgroundColor, blocked, blockSight = None, symbol = None, symbolColor = None):
        self.owner = owner
        self.backgroundColor = backgroundColor
        self.blocked = blocked
        if blockSight is None: blockSight = blocked
        self.blockSight = blockSight
        self.symbol = symbol
        self.symbolColor = symbolColor

        self.explored = False
    def draw(self, console, x, y):
        x += (camera.Camera.X / 2)
        y += (camera.Camera.Y / 2)
        libtcod.console_set_char_background(console, x, y, self.backgroundColor, libtcod.BKGND_SET)
        if self.symbol and self.symbolColor:
            libtcod.console_set_default_foreground(console, self.symbolColor)
            libtcod.console_put_char(console, x, y, self.symbol, libtcod.BKGND_NONE)
    def inSight(fov_map):
        if self in fov_map:
            return True
#Example floor tile
class GrassFloor(Tile):
    Color = libtcod.green
    def __init__(self, owner):
        super(GrassFloor, self).__init__(owner, GrassFloor.Color, False)

#Example wall tile
class BrickWall(Tile):
    Color = libtcod.red
    def __init__(self, owner):
        super(BrickWall ,self).__init__(owner, BrickWall.Color, True)
