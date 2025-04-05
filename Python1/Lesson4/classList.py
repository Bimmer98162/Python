#创建一个列表，其中存储了3个Point对象。每个点（Point)都在与x,y轴夹角为45度的直线上（意思是x和y的值相同）。
#打印输出这些点的坐标。
class Point:
    equality = False
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if x == y:
            self.equality = True

lst = []
point1 = Point(1, 1)
point2 = Point(3, 4)
point3 = Point(5, 6)
lst.append(point1)
lst.append(point2)
lst.append(point3)

for point in lst:
    if point.equality:
        print(point.x, point.y)