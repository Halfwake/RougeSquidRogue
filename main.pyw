import libtcodpy as libtcod
from sys import exit

import conf
import mode
import entity

class GameRoot(object):
    "The main object that owns all other modes."
    Title = conf.TITLE
    ScreenWidth, ScreenHeight = conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT
    GameWidth, GameHeight = conf.GAME_WIDTH, conf.GAME_HEIGHT
    LimitFPS = conf.LIMIT_FPS
    Font = conf.FONT
    def __init__(self):
        #Basic libtcod work
        libtcod.console_set_custom_font(GameRoot.Font, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
        libtcod.console_init_root(GameRoot.ScreenWidth, GameRoot.ScreenHeight, GameRoot.Title, False)
        libtcod.sys_set_fps(GameRoot.LimitFPS)

        #Clear Con
        self.clearConsole = libtcod.console_new(conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT)
        
        #Creating a dictionary of modes and setting the intitial one
        self.modes = {"dungeonMode" : mode.DungeonMode(self)}
        self.mode = self.modes["dungeonMode"]
        self.game_state = "playing"
    def handleKeys(self, key):
        "Handles top level key actions that are available in every mode."
        if key.vk == libtcod.KEY_ENTER and key.lalt:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
        elif key.vk == libtcod.KEY_ESCAPE:
            exit()
    def update(self):
        "Updates the game as long as it is not paused."
        if self.game_state != "paused":
            key = libtcod.console_check_for_keypress()
            self.handleKeys(key)
            self.mode.update(key)
    def clear(self):
        "Calls the erase method of the current mode."
        self.mode.erase()
        libtcod.console_blit(self.clearConsole, 0, 0, conf.SCREEN_WIDTH, conf.SCREEN_HEIGHT, 0, 0, 0)
    def draw(self):
        "Draws whatever mode it needs to. Modes do not need to handle console flushing on their own"
        self.mode.draw()
        libtcod.console_flush()
        
        self.clear()
    def run(self):
        "The main game loop."
        while not libtcod.console_is_window_closed():     
            self.draw()
            self.update()

if __name__ == "__main__":
    root = GameRoot()
    root.run()
