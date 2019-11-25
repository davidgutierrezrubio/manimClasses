from manimlib.imports import *
from myProjects.Polyhedra import *
class DodecahedronGraph(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(phi=80 * DEGREES,theta=45*DEGREES,distance=6)

        #papel
        self.add(Square(fill_color=BLUE,fill_opacity=1).scale(3.4))
        self.set_camera_orientation(phi=45*DEGREES)
        dodecaedro=Dodecahedron(vertexNumbers=False,vertexObject=Dot(fill_color=GOLD,fill_opacity=1))
        self.add(dodecaedro)
        upperPoints=VGroup(*map(lambda o:dodecaedro.vertices[o],[1,5,9,13,15]))

        centerOfUpperFace=np.array([0.,0.,0.])
        for p in upperPoints:
            centerOfUpperFace+=p.get_center()
        centerOfUpperFace=.2*centerOfUpperFace#Divide by 5 to get mean of the 5 coordinates

        self.begin_ambient_camera_rotation(rate=0.1)            #Start move camera
        self.wait(2)
        anims=[]
        for p in upperPoints:
            pc=p.get_center()
            #Scale by 3 the distance to the center (add 2 times the vector)
            anims.append(ApplyMethod(p.shift,2*(pc-centerOfUpperFace)))

        self.play(*anims,run_time=2)

        anims=[]
        for p in dodecaedro.vertices:
            p_coord=p.get_center()
            zz=p_coord[2]
            anims.append(ApplyMethod(p.shift,np.array([0,0,-zz])))


        self.play(*anims,run_time=2)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0,gamma=0,theta=-90*DEGREES,run_time=2)
        self.wait(3)
