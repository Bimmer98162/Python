#定义一个桌子类（Desk），包含长（length）、宽（width）、高（height）属性，包含一个打印桌子信息属性的方法（showInfo）。
#实例化2个桌子对象，为其赋予不同的属性值，并调用showInfo方法，输出每个桌子的信息。
class Desk:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def showInfo(self):
        print("length:", self.length)
        print("width:", self.width)
        print("height:", self.height)

desk1 = Desk(100, 100, 100)
desk2 = Desk(200, 200, 200)
desk1.showInfo()
desk2.showInfo()