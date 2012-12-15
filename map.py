class Map(object):
    def __init__(self, _map):
        self._map = _map
    def __getitem__(key):
        return self._map[key]
    def draw(self, console, fov_map = None):
        for x, row in enumerate(self._map):
            for y, tile in enumerate(row):
                #if tile.explored:
                    if fov_map == None or tile.inSight(fov_map):
                        tile.draw(console, x, y)
                    
                
