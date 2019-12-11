import math
import matplotlib.pyplot as plt

Points = [] # List of Points

BottomLeftPoint = [1e10, 1e10]
indexOfBottomLeftPoint = 0
principalSign = -1

Convexes = [False] * 1000 # List of bool which can tell us whether a point is convex, or concave otherwise
Principals = [True] * 1000 # List of bool which can tell us whether a point is principal, or non-principal otherwise
NoOfPoints = 0

# Handle data --------------------------------------------------------------------------------------
def setNoOfPoints(x):
    global NoOfPoints
    NoOfPoints = int(x)
def Read_Data(): # Function that reads data from the "puncte.txt" file
    global BottomLeftPoint
    global indexOfBottomLeftPoint
    f = open("puncte.txt", "r+")
    i = 0
    for line in f.readlines():
        if i < 1:
            e = line.split()
            setNoOfPoints(e[0])
        else:
            a,b = line.split()
            c = float(a)
            d = float(b)
            read_point = []
            read_point.append(c)
            read_point.append(d)
            Points.insert(i-1,read_point)
            if d < BottomLeftPoint[1]:
                indexOfBottomLeftPoint = i - 1
                BottomLeftPoint = read_point
            elif d == BottomLeftPoint[1]:
                if c < BottomLeftPoint[0]:
                    BottomLeftPoint = read_point
                    indexOfBottomPoint = i - 1	
        i+=1

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
    for i in range (0, n):
        Points[i] = auxList2[i]


def PrintPoint(P, attribute):
    px , py = P[0], P[1]
    print("Punctul de coordonate ( {} , {} ) este {} ".format( px, py,attribute))


# Part of CONVEX - CONCAVE POINTS --------------------------------------------------------------------------------------
def orientation(p,q,r):
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
    for i in range(1,NoOfPoints):
        p1 = i - 1
        p2 = i
        p3 = i + 1
        if (i == n - 1):
            p3 = 0
        o = orientation(Points[p1], Points[p2], Points[p3])
        if o == principalSign:
            Convexes[i] = True

def PrintConvexesConcaves():
    global Convexes
    for i in range(0,NoOfPoints):
        if Convexes[i] == True:
            PrintPoint(Points[i],"convex")
        else:
            PrintPoint(Points[i],"concav")
    print("\n")

# End of CONVEX - CONCAVE POINTS Part--------------------------------------------------------------------------------------
# Part of PRINCIPAL - NOT-PRINCIPAL POINTS --------------------------------------------------------------------------------
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
    if (A == A1 + A2 + A3):
        return True
    else:
        return False

def DecidePrincipalsPoints(): # Asume the points are in clockwise order
    global NoOfPoints
    global Points
    n = NoOfPoints
    for i in range(n):
        p1 = i - 1
        p2 = i
        p3 = i + 1
        if i == 0:
            p1 = n - 1
        if i == n - 1:
            p3 = 0

        for j in range(n):
            if (p1 != j and p2 != j and p3 != j):
                if isInside(Points[p1], Points[p2], Points[p3], Points[j]) == True:
                    Principals[i] = False


def PrintPrincipalsNotPrincipals():
    for i in range(0,NoOfPoints):
        if Principals[i] == True:
            PrintPoint(Points[i],"principal")
        else:
            PrintPoint(Points[i],"neprincipal")
    print("\n")

# End of PRINCIPAL - NOT-PRINCIPAL POINTS Part-----------------------------------------------------------------------------



def Main():
    Read_Data()
    translatePoints()
    setPrincipalSign()
    DecideConvexConcavePoints()
    DecidePrincipalsPoints()
    PrintConvexesConcaves()
    PrintPrincipalsNotPrincipals()

    # A ramas partea grafica
    
if __name__=='__main__':
    Main()