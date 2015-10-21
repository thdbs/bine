
class ViewPort:
    def __init__(self, startX, startY, endX, endY):
        self.startx = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY

class Camera:
    def __init__(self, width, height ):
        self.x = width / 2
        self.y = height / 2
        self.Viewport(0, 0, width, height)

    def Update(self, shiftX, shiftY ):
        self.x += shiftX
        self.y += shiftY

    def GetViewPort(self):
        return self.ViewPort
