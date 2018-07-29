# Sample code for starting the mesh processing project

from random import randint

rotate_flag = True    # automatic rotation of model?
random_fill_flag = False
gouraud_shading_flag = False
time = 0   # keep track of passing time, for automatic rotation

vertices = []
faces = []
currentFill = [255, 255, 255]
fills = []

geometryTable = []
vTable = []
oTable = []

centroidTable = []
faceNormalTable = []
vertexNormalTable = []

# initalize stuff
def setup():
    size (600, 600, OPENGL)
    noStroke()

# draw the current mesh
def draw():
    global time
    
    background(0)    # clear screen to black

    perspective (PI*0.333, 1.0, 0.01, 1000.0)
    camera (0, 0, 5, 0, 0, 0, 0, 1, 0)    # place the camera in the scene
    scale (1, -1, 1)    # change to right-handed coordinate system
    
    # create an ambient light source
    ambientLight (102, 102, 102)
  
    # create two directional light sources
    lightSpecular (204, 204, 204)
    directionalLight (102, 102, 102, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    fill (currentFill[0], currentFill[1], currentFill[2])            # set polygon color
    ambient (200, 200, 200)
    specular (0, 0, 0)            # no specular highlights
    shininess (1.0)
  
    rotate (time, 1.0, 0.0, 0.0)

    # THIS IS WHERE YOU SHOULD DRAW THE MESH
    # for index in range(len(faces)):
    #     currentFace = faces[index]
    #     if random_fill_flag:
    #         fill(fills[index][0], fills[index][1], fills[index][2])
    #     beginShape()
    #     # normal (0.0, 0.0, 1.0)
    #     # vertex (-1.0, -1.0, 0.0)
    #     # vertex ( 1.0, -1.0, 0.0)
    #     # vertex ( 1.0,  1.0, 0.0)
    #     # vertex (-1.0,  1.0, 0.0)
    #     vertex(vertices[currentFace[0]][0], vertices[currentFace[0]][1], vertices[currentFace[0]][2])
    #     vertex(vertices[currentFace[1]][0], vertices[currentFace[1]][1], vertices[currentFace[1]][2])
    #     vertex(vertices[currentFace[2]][0], vertices[currentFace[2]][1], vertices[currentFace[2]][2])
    #     endShape(CLOSE)
    
    # g shading = build n table, holds vertex normals, call "normal()" fn before each vertex call with corresponding vertex normal
    # range(0, len(vTable), 3)
    for index in range(0, len(vTable), 3):
        beginShape()
        if random_fill_flag:
            fill(fills[index // 3][0], fills[index // 3][1], fills[index // 3][2])
        else:
            fill(255, 255, 255)
        if gouraud_shading_flag:
            normal(vertexNormalTable[vTable[index]][0], vertexNormalTable[vTable[index]][1], vertexNormalTable[vTable[index]][2])
            vertex(geometryTable[vTable[index]][0], geometryTable[vTable[index]][1], geometryTable[vTable[index]][2])
            normal(vertexNormalTable[vTable[index + 1]][0], vertexNormalTable[vTable[index + 1]][1], vertexNormalTable[vTable[index + 1]][2])
            vertex(geometryTable[vTable[index + 1]][0], geometryTable[vTable[index + 1]][1], geometryTable[vTable[index + 1]][2])
            normal(vertexNormalTable[vTable[index + 2]][0], vertexNormalTable[vTable[index + 2]][1], vertexNormalTable[vTable[index + 2]][2])
            vertex(geometryTable[vTable[index + 2]][0], geometryTable[vTable[index + 2]][1], geometryTable[vTable[index + 2]][2])
        else:
            vertex(geometryTable[vTable[index]][0], geometryTable[vTable[index]][1], geometryTable[vTable[index]][2])
            vertex(geometryTable[vTable[index + 1]][0], geometryTable[vTable[index + 1]][1], geometryTable[vTable[index + 1]][2])
            vertex(geometryTable[vTable[index + 2]][0], geometryTable[vTable[index + 2]][1], geometryTable[vTable[index + 2]][2])
        endShape(CLOSE)
    
    popMatrix()
    
    # maybe step forward in time (for object rotation)
    if rotate_flag:
        time += 0.02

# process key presses
def keyPressed():
    global rotate_flag, random_fill_flag, gouraud_shading_flag
    if key == ' ':
        rotate_flag = not rotate_flag
    elif key == '1':
        del geometryTable[:]
        del vTable[:]
        del oTable[:]
        del centroidTable[:]
        del faceNormalTable[:]
        del vertexNormalTable[:]
        del vertices[:]
        del faces[:]
        read_mesh ('tetra.ply')
        # if random_fill_flag:
        makeRandomFills()
    elif key == '2':
        del geometryTable[:]
        del vTable[:]
        del oTable[:]
        del centroidTable[:]
        del faceNormalTable[:]
        del vertexNormalTable[:]
        del vertices[:]
        del faces[:]
        read_mesh ('octa.ply')
        if random_fill_flag:
            makeRandomFills()
    elif key == '3':
        del geometryTable[:]
        del vTable[:]
        del oTable[:]
        del centroidTable[:]
        del faceNormalTable[:]
        del vertexNormalTable[:]
        del vertices[:]
        del faces[:]
        read_mesh ('icos.ply')
        if random_fill_flag:
            makeRandomFills()
    elif key == '4':
        del geometryTable[:]
        del vTable[:]
        del oTable[:]
        del centroidTable[:]
        del faceNormalTable[:]
        del vertexNormalTable[:]
        del vertices[:]
        del faces[:]
        read_mesh ('star.ply')
        if random_fill_flag:
            makeRandomFills()
    elif key == '5':
        del geometryTable[:]
        del vTable[:]
        del oTable[:]
        del centroidTable[:]
        del faceNormalTable[:]
        del vertexNormalTable[:]
        del vertices[:]
        del faces[:]
        read_mesh ('torus.ply')
        if random_fill_flag:
            makeRandomFills()
    elif key == 'n':
        gouraud_shading_flag = not gouraud_shading_flag
        # pass  # toggle per-vertex shading
    elif key == 'r':
        random_fill_flag = True
        makeRandomFills()
    elif key == 'w':
        random_fill_flag = False
        del currentFill[:]
        currentFill.append(255)
        currentFill.append(255)
        currentFill.append(255)
    elif key == 'd':
        findDualMesh()
    elif key == 'q':
        exit()

# read in a mesh file (THIS NEEDS TO BE MODIFIED !!!)
def read_mesh(filename):

    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
        
    # determine number of vertices (on first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (on first second)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read in the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        print "vertex = ", x, y, z
        newVertex = [x, y, z]
        vertices.append(newVertex)
        geometryTable.append(newVertex)
    
    # read in the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if nverts != 3:
            print "error: this face is not a triangle"
            exit()
        
        index1 = int(words[1])
        vTable.append(index1)
        index2 = int(words[2])
        vTable.append(index2)
        index3 = int(words[3])
        vTable.append(index3)
        newFace = [index1, index2, index3]
        faces.append(newFace)
        
        vecAx = geometryTable[index2][0] - geometryTable[index1][0]
        vecAy = geometryTable[index2][1] - geometryTable[index1][1]
        vecAz = geometryTable[index2][2] - geometryTable[index1][2]
        
        vecBx = geometryTable[index3][0] - geometryTable[index1][0]
        vecBy = geometryTable[index3][1] - geometryTable[index1][1]
        vecBz = geometryTable[index3][2] - geometryTable[index1][2]
        
        vecA = PVector(vecAx, vecAy, vecAz)
        vecB = PVector(vecBx, vecBy, vecBz)
        
        crossAb = vecB.cross(vecA)
        
        faceNormalTable.append([crossAb.x, crossAb.y, crossAb.z])
        
        centroidX = (geometryTable[index1][0] + geometryTable[index2][0] + geometryTable[index3][0]) / 3
        centroidY = (geometryTable[index1][1] + geometryTable[index2][1] + geometryTable[index3][1]) / 3
        centroidZ = (geometryTable[index1][2] + geometryTable[index2][2] + geometryTable[index3][2]) / 3
        
        centroidTable.append([centroidX, centroidY, centroidZ])
        
        # print "face =", index1, index2, index3
        
    for i in range(len(vTable)):
        oTable.append(0)
    
    for a in range(len(vTable)):
        for b in range(len(vTable)):
            if ((vTable[getNextCorner(a)] == vTable[getPrevCorner(b)]) and (vTable[getPrevCorner(a)] == vTable[getNextCorner(b)])):
                oTable[a] = b
                oTable[b] = a
                
    for currentIndex in range(len(geometryTable)):
        currentCorner = vTable.index(currentIndex)
        numTriangles = vTable.count(currentIndex)
        
        faceNormals = []
        
        for index in range(numTriangles):
            faceNormals.append(faceNormalTable[getCornerTriangle(currentCorner)])
            currentCorner = getSwingCorner(currentCorner)
        
        sumXComponents = 0.0
        sumYComponents = 0.0
        sumZComponents = 0.0
        
        for faceNormal in faceNormals:
            sumXComponents += faceNormal[0]
            sumYComponents += faceNormal[1]
            sumZComponents += faceNormal[2]
            
        averageNormalX = sumXComponents / (len(faceNormals))
        averageNormalY = sumYComponents / (len(faceNormals))
        averageNormalZ = sumZComponents / (len(faceNormals))
        
        vertexNormalTable.append([averageNormalX, averageNormalY, averageNormalZ])
        
    # println(vTable)
    # println(oTable)r
    
def getCornerTriangle(corner):
    return int(corner/3)

def getNextCorner(corner):
    return 3 * (getCornerTriangle(corner)) + ((corner + 1) % 3)

def getPrevCorner(corner):
    return getNextCorner(getNextCorner(corner))

def getCornerVertex(corner):
    return gTable(vTable(c))

def getRightCorner(corner):
    return oTable[getNextCorner(corner)]

def getLeftCorner(corner):
    return oTable[getPrevCorner(corner)]

def getSwingCorner(corner):
    return getPrevCorner(getLeftCorner(corner))

def makeRandomFills():
    del fills[:]
    for i in range(len(vTable) / 3):
        newFill = [randint(0, 255), randint(0, 255), randint(0, 255)]
        fills.append(newFill)
        
def findDualMesh():
    
    newVTable = []
    newGeometryTable = []
    newOTable = []
    newCentroidTable = []
    newFaceNormalTable = []
    newVertexNormalTable= []
    
    global geometryTable
    global centroidTable
    global faceNormalTable
    global vertexNormalTable
    global vTable
    global oTable
    
    for currentIndex in range(len(geometryTable)):
        
        normals = []
        centroids = []
        
        currentCorner = vTable.index(currentIndex)
        # centroids.append(centroidTable[getCornerTriangle(currentCorner)])
        numTriangles = vTable.count(currentIndex)
        
        # println("still running")
        
        # stopCorner = currentCorner
        for index in range(numTriangles):
            centroids.append(centroidTable[getCornerTriangle(currentCorner)])
            currentCorner = getSwingCorner(currentCorner)

        
        # currentCorner = getSwingCorner(currentCorner)
        # println("still running")
        # while currentCorner != stopCorner:
        #     # println("i am an infinite loop")
        #     centroids.append(centroidTable[getCornerTriangle(currentCorner)])
        #     currentCorner = getSwingCorner(currentCorner)
        
        # println("still running")

        # centroids.append(geometryTable[currentIndex])
        
        sumXCoords = 0.0
        sumYCoords = 0.0
        sumZCoords = 0.0
        
        for centroid in centroids:
            sumXCoords += centroid[0]
            sumYCoords += centroid[1]
            sumZCoords += centroid[2]
            
        # println("still running")
        # sumXCoords += geometryTable[currentIndex][0]
        # sumYCoords += geometryTable[currentIndex][1]
        # sumZCoords += geometryTable[currentIndex][2]
        
        superCentroidX = sumXCoords / (len(centroids))
        superCentroidY = sumYCoords / (len(centroids))
        superCentroidZ = sumZCoords / (len(centroids))
        
        centroidIndices = []
        for centroid in centroids:
            if centroid in newGeometryTable:
                centroidIndices.append(newGeometryTable.index(centroid))
            else:
                newGeometryTable.append(centroid)
                centroidIndices.append(len(newGeometryTable) - 1)
            
        
        newGeometryTable.append([superCentroidX, superCentroidY, superCentroidZ])
        centroidIndices.append(len(newGeometryTable) - 1)
        
        
        newVTable.append(centroidIndices[len(centroidIndices) - 2])
        newVTable.append(centroidIndices[0])
        newVTable.append(centroidIndices[len(centroidIndices) - 1])
        
        for i in range(len(centroidIndices) - 2):
            newVTable.append(centroidIndices[i])
            newVTable.append(centroidIndices[i + 1])
            newVTable.append(centroidIndices[len(centroidIndices) - 1])
        # newVTable.append(len(newGeometryTable) - 1)
        # newVTable.append(len(newGeometryTable) - 3)
        # newVTable.append(len(newGeometryTable) - 2)
        
    
    # return [newVTable, newGeometryTable]
    
    for i in range(len(newVTable) / 3):
        currentVertex = i * 3
        centroidX = (newGeometryTable[newVTable[currentVertex]][0] + newGeometryTable[newVTable[currentVertex + 1]][0] + newGeometryTable[newVTable[currentVertex + 2]][0]) / 3
        centroidY = (newGeometryTable[newVTable[currentVertex]][1] + newGeometryTable[newVTable[currentVertex + 1]][1] + newGeometryTable[newVTable[currentVertex + 2]][1]) / 3
        centroidZ = (newGeometryTable[newVTable[currentVertex]][2] + newGeometryTable[newVTable[currentVertex + 1]][2] + newGeometryTable[newVTable[currentVertex + 2]][2]) / 3
        newCentroidTable.append([centroidX, centroidY, centroidZ])
    
    for i in range(len(newVTable)):
        newOTable.append(-1)
    
    for a in range(len(newVTable)):
        for b in range(len(newVTable)):
            if ((newVTable[getNextCorner(a)] == newVTable[getPrevCorner(b)]) and (newVTable[getPrevCorner(a)] == newVTable[getNextCorner(b)])):
                newOTable[a] = b
                newOTable[b] = a
    
    oTable = newOTable
    
    for index in range(0, len(newVTable), 3):
        vecAx = newGeometryTable[newVTable[index + 1]][0] - newGeometryTable[newVTable[index]][0]
        vecAy = newGeometryTable[newVTable[index + 1]][1] - newGeometryTable[newVTable[index]][1]
        vecAz = newGeometryTable[newVTable[index + 1]][2] - newGeometryTable[newVTable[index]][2]
        
        vecBx = newGeometryTable[newVTable[index + 2]][0] - newGeometryTable[newVTable[index]][0]
        vecBy = newGeometryTable[newVTable[index + 2]][1] - newGeometryTable[newVTable[index]][1]
        vecBz = newGeometryTable[newVTable[index + 2]][2] - newGeometryTable[newVTable[index]][2]
        
        vecA = PVector(vecAx, vecAy, vecAz)
        vecB = PVector(vecBx, vecBy, vecBz)
        
        crossAb = vecB.cross(vecA)
        
        newFaceNormalTable.append([crossAb.x, crossAb.y, crossAb.z])
        
    
    for currentIndex in range(len(newGeometryTable)):
        currentCorner = newVTable.index(currentIndex)
        numTriangles = newVTable.count(currentIndex)
        
        faceNormals = []
        
        for index in range(numTriangles):
            faceNormals.append(newFaceNormalTable[getCornerTriangle(currentCorner)])
            currentCorner = getSwingCorner(currentCorner)
        
        sumXComponents = 0.0
        sumYComponents = 0.0
        sumZComponents = 0.0
        
        for faceNormal in faceNormals:
            sumXComponents += faceNormal[0]
            sumYComponents += faceNormal[1]
            sumZComponents += faceNormal[2]
            
        averageNormalX = sumXComponents / (len(faceNormals))
        averageNormalY = sumYComponents / (len(faceNormals))
        averageNormalZ = sumZComponents / (len(faceNormals))
        
        newVertexNormalTable.append([averageNormalX, averageNormalY, averageNormalZ])
    
    # println(newGeometryTable)
    # println(newVTable)
    # println(newOTable)
    # println(len(newVTable))
    vTable = newVTable
    geometryTable = newGeometryTable
    
    centroidTable = newCentroidTable
    faceNormalTable = newFaceNormalTable
    vertexNormalTable = newVertexNormalTable
    makeRandomFills()
        
        
        
        
        
            
    
            