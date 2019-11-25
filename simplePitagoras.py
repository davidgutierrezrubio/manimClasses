from manimlib.imports import *

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
