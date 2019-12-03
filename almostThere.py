import math
import matplotlib.pyplot as plt

Points = [[]] # List of Points

Convexes = [False] * 1000 # List of bool which can tell us whether a point is convex, or concave otherwise

Principales = [False] * 1000 # List of bool which can tell us whether a point is principal, or non-principal otherwise

NoOfPoints = 0
def setNoOfPoints(x):
    global NoOfPoints
    NoOfPoints = int(x)
def Read_Data(): # Function that reads data from the "puncte.txt" file
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

        i+=1
# Part of CONVEX - CONCAVE POINTS --------------------------------------------------------------------------------------
def ArePointsCollinear(a,b,c):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    x3 = c[0]
    y3 = c[1]

    doublearea = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))

    if doublearea == 0:
        return True
    else:
        return False

def IsConvex(One, Two, Three): # indexes
    A = Points[One]
    B = Points[Two]
    C = Points[Three]
    if ArePointsCollinear(A,B,C) ==  True :
        return True
    else:
        return False
    #TBC
# End of CONVEX - CONCAVE POINTS Part--------------------------------------------------------------------------------------
# Part of PRINCIPAL - NOT-PRINCIPAL POINTS --------------------------------------------------------------------------------
def comparatorFunction(a,b):
    if abs(a-b) < 1e-5:
        return True
    else:
        return False

def onSegment(p,q,r):
    if q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]):
        return True
    else:
        return False
def orientation(p,q,r):
    ans = (q[1]-p[1])*(r[0]-q[0]) + (q[0]-p[0])*(r[1]-q[1])
    if ans == 0:
        return ans
    elif ans > 0:
        return 1
    else:
        return 2
def IntersectLines(firstPoint,secondPoint,thirdPoint,fourthPoint):
    p1 = firstPoint
    q1 = secondPoint
    p2 = thirdPoint
    q2 = fourthPoint

    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and onSegment(p1, p2, q1):
        return True
    if o2 == 0 and onSegment(p1, q2, q1) :
        return True
    if o3 == 0 and onSegment(p2, p1, q2):
        return True
    if o4 == 0 and onSegment(p2, q1, q2) :
        return True
    return False

def IntersectThePolygon(equationLine,firstHead,secondHead,firstPoint,secondPoint):
    for i in range(0,NoOfPoints):
        if i <= firstHead - 2 or secondHead + 1 <= i:
            if i != NoOfPoints - 1:
                A = Points[i]
                B = Points[i+1]
            else:
                A = Points[NoOfPoints-1]
                B = Points[0]

            eqAB = []

            eqAB.append(B[1] - A[0])
            eqAB.append(A[0] - B[1])
            eqAB.append(eqAB[0] * A[0] + eqAB[1] * A[1])

            if IntersectLines(firstPoint,secondPoint,A,B) == True :
                return True
    return False

def IsPrincipal(One, Two, Three): #indexes
    #Punctul B este principal daca impreuna cu punctele a si c formeaza triangulare

    A = Points[One]
    B = Points[Two]
    C = Points[Three]

    #eqAB = []
    #eqBC = []
    eqCA = []
    """
    eqAB[0] = B[1] - A[0]
    eqAB[1] = A[0] - B[1]
    eqAB[2] = eqAB[0] * A[0] + eqAB[1] * A[1]

    eqBC[0] = C[1] - B[1]
    eqBC[1] = B[0] - C[1]
    eqBC[2] = eqBC[0] * B[0] + eqBC[1] * B[1]
    """
    eqCA.append(A[1] - C[0])
    eqCA.append(C[0] - A[1])
    eqCA.append(eqCA[0] * C[0] + eqCA[1] * C[1])

    if IntersectThePolygon(eqCA,One,Three,C,A) == False: #and IntersectThePolygon(eqBC) == False and IntersectThePolygon(eqCA) == False:
        return True
    else:
        return False
    #TBC

def DecidePrincipalPoints():
    n = NoOfPoints
    for i in range(0,NoOfPoints):
        x, y = Points[i][0], Points[i][1]
        if i==0 :
            if IsPrincipal(n-1,i,i+1) == True:
                Principales[i] = True
            else:
                Principales[i] = False

        if i>=1 and i<=n-2:
            if IsPrincipal(i-1, i, i + 1) == True:
                Principales[i] = True
            else:
                Principales[i] = False

        if i==n-1:
            if IsPrincipal(i-1, i, 0) == True:
                Principales[i] = True
            else:
                Principales[i] = False
# End of PRINCIPAL - NOT-PRINCIPAL POINTS Part-----------------------------------------------------------------------------
def DecideConvexPoints():
    n = NoOfPoints
    for i in range(0,NoOfPoints):
        x, y = Points[i][0], Points[i][1]
        if i==0 :
            if IsConvex(n-1,i,i+1) == True:
                Convexes[i] = True
            else:
                Convexes[i] = False

        if i>=1 and i<=n-2:

            if IsConvex(i-1, i, i + 1) == True:
                Convexes[i] = True
            else:
                Convexes[i] = False

        if i==n-1:
            if IsConvex(i-1, i, 0) == True:
                Convexes[i] = True
            else:
                Convexes[i] = False

def PrintPoint(P, attribute):
    px , py = P[0], P[1]
    print("Punctul de coordonate ( {} , {} ) este {} ".format( px, py,attribute))

def PrintConvexesConcaves():
    for i in range(0,NoOfPoints):
        if Convexes[i] == True:
            PrintPoint(Points[i],"convex")
        else:
            PrintPoint(Points[i],"concav")
    print("\n")

def PrintPrincipalsNotPrincipals():
    for i in range(0,NoOfPoints):
        if Principales[i] == True:
            PrintPoint(Points[i],"principal")
        else:
            PrintPoint(Points[i],"neprincipal")
    print("\n")

def Main():
    Read_Data()
    """
    PrintPoint(Points[7],"a")
    PrintPoint(Points[0],"b")
    PrintPoint(Points[1],"b")
    PrintPoint(Points[2],"b")
    print(IntersectLines([0,0],[3,3],[0,3],[3,3]))
    """
    DecidePrincipalPoints() # Aproape gata

    DecideConvexPoints() # TBC

    PrintPrincipalsNotPrincipals() # Gata

    PrintConvexesConcaves() #TBC


if __name__=='__main__':
    Main()