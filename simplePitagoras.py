#!/usr/bin/env python

import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'c:\\manim\\manim-3feb')
sys.path.insert(1, 'c:\\manim\\manim-3feb\\myProjects')
from big_ol_pile_of_manim_imports import *

from  screengrid import *
from Recolocate import *
if __name__ == "__main__":
    os.chdir('c:\\manim\\manim-3feb')
    module_name = 'myProjects\\'+ os.path.basename(__file__)
    print(module_name)
    command_A = "python -m manim "
    command_B = module_name +" " +"pitagoras"+" -pl"
    os.system(command_A + command_B)
class pitagoras(MovingCameraScene):
    def construct(self):
        plane=NumberPlane(x_radius=20,y_radius=20)
        #self.add(plane)

        puntos=[]
        A=np.array([0,0,0])
        B=np.array([3,0,0])
        C=np.array([0,4,0])
        puntos.append(A)
        puntos.append(B)
        puntos.append(C)
        triangulo=Polygon(*puntos,fill_color=GOLD_B,fill_opacity=1)

        self.camera_frame.set_width(21)
        self.camera_frame.move_to(triangulo)
        self.camera_frame.shift(4*RIGHT)
        self.add_sound("myProjects\\Blop.wav")
        self.play(FadeIn(triangulo))
        #Lados al Cuadrado
        cua1=Square(fill_color=RED,fill_opacity=1).shift(3*LEFT)
        cua2=Square(fill_color=GREEN,fill_opacity=1).shift(3*LEFT)
        cua3=Square(fill_color=BLUE,fill_opacity=1).shift(3*LEFT)
        anim1=Recolocate(cua1,cua1.get_center()+RIGHT+UP,cua1.get_center()+LEFT+UP,B,A)
        anim2=Recolocate(cua2,cua2.get_center()+RIGHT+UP,cua3.get_center()+LEFT+UP,C,B)
        anim3=Recolocate(cua3,cua2.get_center()+RIGHT+UP,cua3.get_center()+LEFT+UP,A,C)

        self.add_sound("myProjects\\Blop.wav")
        self.play(anim1,anim2,anim3,run_time=1)
        #self.play(FadeOut(cua1),FadeOut(cua2),FadeOut(cua3))


        #self.play(Restore(self.camera_frame))

        A1=8*RIGHT
        A2=A1+4*UP+3*UP
        A3=A2+4*RIGHT+3*RIGHT
        A4=A3+4*DOWN+3*DOWN
        tr1=triangulo.copy()
        self.add_sound("myProjects\\Blop.wav")
        anim=recolocateFromToSimple(tr1,A,A1,0)
        self.play(anim,run_time=1)
        tr2=tr1.copy()
        self.add_sound("myProjects\\Blop.wav")
        anim=recolocateFromToSimple(tr2,A1,A2,-PI/2)
        self.play(anim,run_time=1)
        tr3=tr2.copy()
        self.add_sound("myProjects\\Blop.wav")
        anim=recolocateFromToSimple(tr3,A2,A3,-PI/2)
        self.play(anim,run_time=1)
        tr4=tr3.copy()
        self.add_sound("myProjects\\Blop.wav")
        anim=recolocateFromToSimple(tr4,A3,A4,-PI/2)
        self.play(anim,run_time=1)



        shift_v=3*UP+2*RIGHT
        self.play(ApplyMethod(cua2.shift,8*RIGHT))

        self.play(ApplyMethod(cua1.shift,shift_v),
        ApplyMethod(cua3.shift,shift_v),
        ApplyMethod(triangulo.shift,shift_v))
        A=A+shift_v
        B=B+shift_v
        C=C+shift_v

        tr5=triangulo.copy()
        tr6=triangulo.copy()
        tr7=triangulo.copy()
        anim1=recolocateFromToSimple(tr5,C,B,-PI)
        anim2=recolocateFromToSimple(tr6,C,A,-PI/2)
        anim3=recolocateFromToSimple(tr7,B,A,PI/2)
        self.add_sound("myProjects\\Blop.wav")
        self.play(anim1,anim2,anim3,run_time=1)



        image = ImageMobject("myProjects\\balanza.png").scale(10).shift(6.5*RIGHT+2.9* UP)
        self.play(FadeIn(image),self.camera_frame.set_width,26,self.camera_frame.shift,2.5*UP)


        self.play(FadeOut(tr1),FadeOut(triangulo))
        self.play(FadeOut(tr2),FadeOut(tr6))
        self.play(FadeOut(tr3),FadeOut(tr5))
        self.play(FadeOut(tr4),FadeOut(tr7))

        self.wait(2)
    def p(self,x,y):
        return np.array([x,y,0])

class SVGTest(Scene):
    def construct(self):
        svg = SVGMobject("myProjects\\Finger.svg")
        #svg = SVGMobject("camera")
        self.play(DrawBorderThenFill(svg,rate_func=linear))
        self.wait()
class ImageTest(Scene):
    def construct(self):
        image = ImageMobject("myProjects\\balanza.png").scale(4)
        self.play(FadeIn(image))
        self.wait()

class HoldUpMathExchange(TeacherStudentsScene):
    def construct(self):
        cua=Square()
        self.add(cua)
        title = TextMobject("Mathematics Stack Exchange")
        title.scale(1.5)
        title.to_edge(UP)

        self.add(title)
        self.play(self.teacher.change, "raise_right_hand", ORIGIN),
        self.teacher_says("HOLA")
        self.change_all_student_modes("thinking", look_at_arg=LEFT)
        self.wait(3)
        self.teacher_holds_up(cua)
        self.change_all_student_modes("confused", look_at_arg=RIGHT)
        self.wait(3)


class ChangePositionAndSizeCameraInAnotherScene(GraphScene,MovingCameraScene):
    CONFIG = {
        "y_max" : 1.2,
        "y_min" : -1.2,
        "x_max" : 6.5,
        "x_min" : 0,
        "y_tick_frequency" : 5,
        "x_tick_frequency" : 0.5,
    }
    # Setup the scenes
    def setup(self):
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.setup_axes(animate=True)

        graph = self.get_graph(lambda x : np.sin(x),
                                    color = GREEN,
                                    x_min = 0,
                                    x_max = 7
                                    )
        dot_at_start_graph=Dot().move_to(graph.points[0])
        dot_at_end_grap=Dot().move_to(graph.points[-1])

        self.add(dot_at_end_grap,dot_at_start_graph)
        self.play(ShowCreation(graph))

        self.play(
            self.camera_frame.scale,.5,
            self.camera_frame.move_to,dot_at_start_graph
        )

        self.play(
            self.camera_frame.move_to,dot_at_end_grap
        )
        self.wait()

class MultipleMethods(Scene):
    def construct(self):
        sq = Square().scale(0.5)
        sq.init_state = sq.copy()

        def get_sg_udpate(a,b,ang,sca):
            return lambda mob,alpha: (
                mob.become(mob.init_state),
                mob.shift((a*RIGHT+b*UP)*alpha),
                mob.rotate(ang*DEGREES*alpha),
                mob.scale(1*(1-alpha)+sca*alpha))

        sq_update=get_sg_udpate(2,2,45,3)
        self.add(Dot(3*(RIGHT+UP)))
        self.play(
            UpdateFromAlphaFunc(sq,sq_update),
            run_time=4
        )
        self.wait()


class pruebaMatriz(Scene):
    def punto(self,x,y,nombre):
        p=np.array([x,y,0])
        res=VGroup(Dot(p),TextMobject(nombre)).arrange_submobjects(direction=DOWN,center=False)
        # res.center(p)
        return res
    def construct(self):


        # aa=VGroup(cua,cir).arrange_submobjects(direction=DOWN,center=False)
        puntoA=self.punto(0,0,"A")
        self.add(puntoA)
        self.add(Dot(RIGHT))
        B=2*RIGHT+UP
        self.add(Dot(B))
        tri=Polygon(0*UP,RIGHT,2*UP)
        self.add(tri)
        animPuntoA=recolocateFromToSimple(puntoA,0*UP,B,0)
        animTri=recolocateFromToSimple(tri,0*UP,B,PI/4)
        self.play(animPuntoA,animTri)
        self.wait(2)
