class Camera(object):
    "The static camera."
    X = 0
    Y = 0
    @staticmethod
    def SetPosition(x, y):
        Camera.X = x
        Camera.Y = y
