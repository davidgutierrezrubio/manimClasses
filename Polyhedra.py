#!/usr/bin/env python

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'c:\\manim\\manim-3feb')
from manimlib.imports import *
import myProjects.Polyhedra as pol


if __name__ == "__main__":
    os.chdir('c:\\manim\\manim-3feb')
    module_name = 'myProjects\\'+ os.path.basename(__file__)
    print(module_name)
    command_A = "python -m manim "
    command_B = module_name +" " +"testPol"+" -pl"
    os.system(command_A + command_B)
class testPol(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=45*DEGREES,theta=45*DEGREES)
        co=Cube(showVertexNumbers=True,showFaces=True)
        self.add(co)
        self.wait()

class Polyhedra(Group):
    """
    This class represents a general Polyhedra
    pointList: Array of np.array() coordinates of vertices.

    vertexNumbers: if true, add a Decimal object next_to each vertex, denoting its number in the array.
    Mostly for debugging purposes or controlling where is each vertex.
    vertexObject is an instace of a MObject, to use for vertex. You can use Sphere() but is slooooow

    TODO: Add faces
    TODO: Implement scale or rotate funcions, subclass MObject instead of Group
    """
    CONFIG = {
        "showVertex":True,
        "showVertexNumbers": False,
        "showFaces": False
    }
    def __init__(self,pointList,edgeList,facesList,vertexObjectP=Dot(shade_in_3d=True),**kwargs):
        digest_config(self,kwargs)
        self.edgeList=edgeList
        self.vertexObjectP=vertexObjectP
        self.vertices=list(map(lambda a: self.vertexObjectP.copy().shift(np.array(a)),pointList))

        #Update function to ensure edges are always connected to its vertices
        def update_func_aristas(ori,des):
            return lambda r:r.become(Line(ori.get_center(),des.get_center()))
        self.edges=[]
        for edge in edgeList:
            ori=self.vertices[edge[0]]
            des=self.vertices[edge[1]]
            edgeLine=Line(ori,des,shade_in_3d=True)
            edgeLine.add_updater(update_func_aristas(ori,des))
            self.edges.append(edgeLine)
        self.numbers=[]
        if self.showVertexNumbers:#Add number to each vertex
            #Update function to ensure numbers are always next_to its vertices
            def update_func_numberVertices(ori):
                return lambda t: t.next_to(ori)
            counter=0
            for p in self.vertices:
                t=Integer(counter)
                t.next_to(p)
                t.add_updater(update_func_numberVertices(p))
                self.numbers.append(t)
                counter+=1
        todo=self.vertices+self.edges+self.numbers
        self.faces=[]
        if self.showFaces:
            for f in facesList:
                pointsFace=list(map(lambda r: self.vertices[r].get_center(),f))
                pointsFace.append(self.vertices[f[0]].get_center())#Add again first vertex
                pol=Polygon(*pointsFace,fill_color=GREEN,fill_opacity=1,shade_in_3d=True)
                self.faces.append(pol)

        self.GrVertices=Group(*self.vertices)
        self.GrEdges=Group(*self.edges)
        self.GrNumbers=Group(*self.numbers)
        super().__init__(*self.vertices,*self.edges,*self.numbers,*self.faces)

    def getVertexObject(self):
        return self.vertexObject.copy()
    def getAdjacentVertices(self,vertex,onlyNumbers=False):
        """

        Return all adjacent vertices to a given one.
        vertex: may be the MObject or the index of the vertex
        onlyNumbers: if true, return only numbers of vertices, not the objects
        """
        if isinstance(vertex,int):
            numV=vertex
        else:
            numV=self.vertices.index(vertex) #Number of vertex
        adjacentList=[]
        for edge in self.edgeList:
            if edge[0]==numV:
                adjacentList.append(edge[1])
            if edge[1]==numV:
                adjacentList.append(edge[0])
        if onlyNumbers:
            return adjacentList
        else:
            return list(map(lambda r:self.vertices[r],adjacentList))




class Dodecahedron(Polyhedra):
    """
    Dodecahedron. Coordinates of points taken from https://en.wikipedia.org/wiki/Regular_dodecahedron
    These points are centered on ORIGIN and not in intuitive equilibrium. Parameters
    rotate and put_on_ground control where to transform in order to lay on one of its faces.

    """
    CONFIG = {
        "lay_in_one_face": True,
        "put_on_ground": True,
    }
    def __init__(self,**kwargs):
        digest_config(self,kwargs)
        goldrat=(1+np.sqrt(5))/2
        pointList=[\
        [1,1,1],#0
        [1,1,-1],#1
        [1,-1,1],#2
        [1,-1,-1],#3
        [-1,1,1],#4
        [-1,1,-1],#5
        [-1,-1,1],#6
        [-1,-1,-1],#7
        [0,goldrat,1/goldrat], #8
        [0,goldrat,-1/goldrat],#9
        [0,-goldrat,1/goldrat],#10
        [0,-goldrat,-1/goldrat],#11
        [1/goldrat,0,goldrat],#12
        [1/goldrat,0,-goldrat],#13
        [-1/goldrat,0,goldrat],#14
        [-1/goldrat,0,-goldrat],#15
        [goldrat,1/goldrat,0],#16
        [goldrat,-1/goldrat,0],#17
        [-goldrat,1/goldrat,0],#18
        [-goldrat,-1/goldrat,0]#19
        ]
        edgeList=[\
        [0,8],#0
        [8,4],#1
        [4,14],#2
        [14,12],#3
        [12,0],#4
        [0,16],#5
        [16,17],#6
        [17,2],#7
        [2,12],#8
        [14,6],#9
        [6,10],#10
        [10,2],#11
        [10,11],#12
        [11,3],#13
        [3,17],#14
        [8,9],#15
        [9,1],#16
        [1,16],#17
        [1,13],#18
        [13,3],#19
        [18,19],#20
        [19,7],#21
        [7,15],#22
        [15,5],#23
        [5,18],#24
        [4,18],#25
        [7,11],#26
        [9,5],#27
        [6,19],#28
        [13,15]#29
        ]
        pointList=list(map(lambda p: np.array(p),pointList))#Convert to np.array
        #Rotate the vertices to lay in one face
        if self.lay_in_one_face:
            co=np.cos(np.arctan(goldrat))
            se=np.sin(np.arctan(goldrat))
            pointList=list(map(lambda p:[p[0],p[1]*se+p[2]*co,p[1]*co-p[2]*se],pointList))
        #Shift on the z-axis to touch the ground
        if self.put_on_ground:
            pointList=list(map(lambda p:[p[0],p[1],p[2]+goldrat],pointList))
        super().__init__(pointList,edgeList,[],**kwargs)



class Cube(Polyhedra):
    """
    A cube of edge length 2 and centered at ORIGIN

    """

    def __init__(self,**kwargs):
        pointList=[\
        [1,1,1],#0
        [1,1,-1],#1
        [1,-1,1],#2
        [1,-1,-1],#3
        [-1,1,1],#4
        [-1,1,-1],#5
        [-1,-1,1],#6
        [-1,-1,-1]#7
        ]
        edgeList=[\
        [0,1],#0
        [0,2],#1
        [0,4],#2
        [1,3],#3
        [1,5],#4
        [2,6],#5
        [2,3],#6
        [3,7],#7
        [4,6],#8
        [4,5],#9
        [7,5],#10
        [7,6]#11
        ]
        facesList=[\
        [1,3,7,5],
        [0,1,3,2],
        [4,5,7,6],
        [1,5,4,0],
        [3,7,6,2],
        [2,0,4,6]
        ]
        pointList=list(map(lambda p: np.array(p),pointList))#Convert to np.array
        super().__init__(pointList,edgeList,facesList,**kwargs)
