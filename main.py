from collections import defaultdict
from drawing import Drawing

MAX_NO_POINTS = 1000

# List of Points
Points = []

# Drawing Points
drawing_points = defaultdict(list)

BottomLeftPoint = [1e10, 1e10]
indexOfBottomLeftPoint = 0
principalSign = -1

# List of bool which can tell us whether a point is convex, or concave otherwise
Convexes = [False] * MAX_NO_POINTS
# List of bool which can tell us whether a point is principal, or non-principal otherwise
Principals = [True] * MAX_NO_POINTS
NoOfPoints = 0


# Handle data --------------------------------------------------------------------------------------
def setNoOfPoints(x):
    global NoOfPoints
    NoOfPoints = int(x)


# Function that reads data from the "puncte.txt" file
def Read_Data():
    global BottomLeftPoint
    global indexOfBottomLeftPoint
    f = open("puncte.txt", "r+")
    i = 0
    for line in f.readlines():
        if i < 1:
            e = line.split()
            setNoOfPoints(e[0])
        else:
            a, b = line.split()
            c = float(a)
            d = float(b)
            read_point = []
            read_point.append(c)
            read_point.append(d)
            Points.insert(i-1, read_point)
            if d < BottomLeftPoint[1]:
                indexOfBottomLeftPoint = i - 1
                BottomLeftPoint = read_point
            elif d == BottomLeftPoint[1]:
                if c < BottomLeftPoint[0]:
                    BottomLeftPoint = read_point
                    indexOfBottomPoint = i - 1	
        i += 1


def Print_Data():
    global BottomLeftPoint
    global Points 
    global NoOfPoints
    for point in Points:
        print(point)


def translatePoints():
    # translates points such that bottom poin will be the first one
    global NoOfPoints
    global indexOfBottomLeftPoint
    global Points
    n = NoOfPoints
    ind = indexOfBottomLeftPoint
    auxList1 = []
    auxList2 = []
    for i in range(0, n):
        auxList1.append(Points[i])
    for i in range(0, n):
        auxList1.append(Points[i])
    for i in range(ind, ind + n):
        auxList2.append(auxList1[i])
    for i in range(0, n):
        Points[i] = auxList2[i]


def PrintPoint(P, attribute):
    px, py = P[0], P[1]
    print("Punctul de coordonate ( {} , {} ) este {} ".format(px, py, attribute))


# Part of CONVEX - CONCAVE POINTS --------------------------------------------------------------------------------------
def orientation(p, q, r):
    ans = (q[1]-p[1])*(r[0]-q[0]) - (q[0]-p[0])*(r[1]-q[1])
    if ans == 0:
        return ans
    elif ans > 0:
        return 1
    else:
        return -1


def setPrincipalSign():
    global Points
    global principalSign
    global NoOfPoints
    global Convexes
    Convexes[0] = True
    principalSign = orientation(Points[NoOfPoints - 1], Points[0], Points[1])


def DecideConvexConcavePoints():
    global NoOfPoints
    global Convexes
    n = NoOfPoints
    for i in range(1, NoOfPoints):
        p1 = i - 1
        p2 = i
        p3 = i + 1
        if i == n - 1:
            p3 = 0
        o = orientation(Points[p1], Points[p2], Points[p3])
        if o == principalSign:
            Convexes[i] = True


def PrintConvexesConcaves():
    global Convexes
    for i in range(0, NoOfPoints):
        if Convexes[i]:
            PrintPoint(Points[i], "convex")
        else:
            PrintPoint(Points[i], "concav")
    print("\n")


# End of CONVEX - CONCAVE POINTS Part-----------------------------------------------------------------------------------
# Part of PRINCIPAL - NOT-PRINCIPAL POINTS -----------------------------------------------------------------------------
def area(p1, p2, p3):
    return abs((
        p1[0] * (p2[1] - p3[1]) +
        p2[0] * (p3[1] - p1[1]) +
        p3[0] * (p1[1] - p2[1])
        ) / 2.0)


def isInside(p1, p2, p3, q):
    A = area(p1, p2, p3)
    A1 = area(q, p2, p3)
    A2 = area(p1, q, p3)
    A3 = area(p1, p2, q) 
    if A == A1 + A2 + A3:
        return True
    else:
        return False


# Asume the points are in clockwise order
def DecidePrincipalsPoints():
    global NoOfPoints
    global Points
    n = NoOfPoints
    for i in range(n):
        if Convexes[i]:
            p1 = i - 1
            p2 = i
            p3 = i + 1
            if i == 0:
                p1 = n - 1
            if i == n - 1:
                p3 = 0
            for j in range(n):
                if p1 != j and p2 != j and p3 != j:
                    if isInside(Points[p1], Points[p2], Points[p3], Points[j]):
                        Principals[i] = False
        elif Convexes[i] == False:
            Principals[i] = False



def PrintPrincipalsNotPrincipals():
    for i in range(0, NoOfPoints):
        if Principals[i]:
            PrintPoint(Points[i], "principal")
        else:
            PrintPoint(Points[i], "neprincipal")
    print("\n")


def map_points():
    for index in range(NoOfPoints):
        drawing_points['coordinates'].append(Points[index])
        drawing_points['convexity'].append(Convexes[index])
        drawing_points['principality'].append(Principals[index])


# End of PRINCIPAL - NOT-PRINCIPAL POINTS Part--------------------------------------------------------------------------
def Main():
    Read_Data()
    translatePoints()
    setPrincipalSign()
    DecideConvexConcavePoints()
    DecidePrincipalsPoints()
    PrintConvexesConcaves()
    PrintPrincipalsNotPrincipals()

    # Partea grafica
    map_points()
    drawing = Drawing(drawing_points)
    drawing.draw()


if __name__ == '__main__':
    Main()
