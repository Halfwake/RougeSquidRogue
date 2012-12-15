import libtcodpy as libtcod

import conf
import entity
import tile
import map
import camera

class Mode(object):
    "Mode is an abstract class used to allow the developer to implement parts of a new Mode subclass without needing placeholder methods and fields."
    def __init__(self, owner):
        self.entities = []
    def update(self, key):
        pass
    def draw(self):
        pass
    def erase(self):
        pass
    def isBlocked(self, x, y):
        return False

class DungeonMode(Mode):
    def __init__(self, owner):
        super(DungeonMode, self).__init__(owner)
        self.con = libtcod.console_new(conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT)
        self.player = entity.Player(self, conf.GAME_WIDTH / 2, conf.GAME_HEIGHT / 2)
        self.entities.append(self.player)
        self.makeMap()
    def makeMap(self):
        self.map = map.Map([[tile.BrickWall(self) for y in xrange(50)] for x in xrange(50)])
    def update(self, key):
        camera.Camera.X = self.player.x
        camera.Camera.Y = self.player.y
        self.handleKeys(key)
    def draw(self):
        self.map.draw(self.con)
        self.player.draw(self.con)
        
        x = camera.Camera.X - (conf.GAME_WIDTH / 2)
        y = camera.Camera.Y - (conf.SCREEN_HEIGHT / 2)
        libtcod.console_blit(self.con, x, y, conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT, 0, 0, 0)
    def erase(self):
        self.player.erase()
    def handleKeys(self, key):
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            self.player.moveAttack(0, -1)
        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            self.player.moveAttack(0, 1)
        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            self.player.moveAttack(-1, 0)
        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            self.player.moveAttack(1, 0)


