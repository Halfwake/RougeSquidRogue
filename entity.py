import random
import libtcodpy as libtcod

import conf
import camera

class Entity(object):
    "A game object that can move and be drawn."
    def __init__(self, owner, x, y, symbol, color, name, blocks):
        self.owner = owner
        self.x = x
        self.y = y
        self.symbol = symbol
        self.color = color
        self.name = name
        self.blocks = blocks

        self.lastConsole = None
    def move(self, dx, dy):
        if -1 < self.x + dx < conf.GAME_WIDTH:
            if not self.owner.isBlocked(self.x + dx, self.y):
                self.x += dx
        if -1 < self.y + dy < conf.GAME_HEIGHT:
            if not self.owner.isBlocked(self.x, self.y + dy):
                self.y += dy
    def draw(self, console):
        "Draws the tile to the screen."
        self.lastConsole = console
        libtcod.console_set_default_foreground(console, self.color)
        #print (x, y) #debugging
        libtcod.console_put_char(console, self.x, self.y, self.symbol, libtcod.BKGND_NONE)
    def erase(self, console = None):
        "Erases the tile on the selected console. If no console is specified it usees the console from the last draw call."
        assert self.lastConsole, "Attempted to erase before drawing."
        console = console or self.lastConsole
        libtcod.console_put_char(console, self.x, self.y, ' ', libtcod.BKGND_NONE)
    def makeName(self, nameParts, joiner = " "):
        "Allows for objects with variable name choices to autogenerate a name."
        name = []
        for section in nameParts:
            name.append(random.choice(section))
        return joiner.join(name)

class Player(Entity):
    "The player class, you can have as many as you want."
    Symbol = '@'
    Color = libtcod.orange
    Name = "Humprhey"
    def __init__(self, owner, x, y):
        super(Player, self).__init__(owner, x, y, Player.Symbol, Player.Color, Player.Name, True)
    def moveAttack(self, dx, dy):
        x = self.x + dx
        y = self.y + dy
        
        target = None
        for entity in self.owner.entities:
            if (x, y) == (entity.x, entity.y):
                target = entity
                break
        if not target:
            self.move(dx, dy)
        elif target:
            self.attack(target)
    def attack(self, target):
        print target.talk("fight")

class Monster(Entity):
    "An enemy."
    def __init__(self, owner, x, y, symbol, color, name):
        super(Monster, self).__init__(owner, x, y, symbol, color, name, True)

#Example Monster subclass
class Imp(Monster):
    Symbol = 'i'
    Color = libtcod.Color(0, 0, 255)
    NameInfo = [["Ackah", "Backah", "Cacka", "Dacka"],
                ["Ackah", "Backah", "Cacka", "Dacka"]]
    def __init__(self, owner, x, y):
        super(Imp, self).__init__(owner, x, y, Imp.Symbol, Imp.Color, self.makeName(Imp.NameInfo, ""))
