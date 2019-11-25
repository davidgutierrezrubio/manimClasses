#!/usr/bin/env python

import sys

# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'c:\\manim\\manim-3feb')
from big_ol_pile_of_manim_imports import *


# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'c:\\manim\\manim-3feb')
from big_ol_pile_of_manim_imports import *

from  screengrid import *

if __name__ == "__main__":
    os.chdir('c:\\manim\\manim-3feb')
    module_name = 'myProjects\\'+ os.path.basename(__file__)
    print(module_name)
    command_A = "python -m manim "
    command_B = module_name +" " +"pruebaRecolocate"+" -pl"
    os.system(command_A + command_B)
class Recolocate(Homotopy):
    #Clase de animación para recolocar una figura
    def __init__(self,mobject,fromA,fromB,toA,toB,scaling=True,rotate=True,**kwargs):
        mobject.init_state = mobject.copy()

        self.update_function=__class__.get_recolocate_udpate_function(fromA,fromB,toA,toB,scaling,rotate)
        super().__init__(self.update_function,mobject,**kwargs)
    @staticmethod
    def get_recolocate_udpate_function(fromA,fromB,toA,toB,scaling,rotate):
        v1=fromB-fromA
        v2=toB-toA
        transVector=toA-fromA
        if rotate:
            angle=np.arctan2(v2[1],v2[0])-np.arctan2(v1[1],v1[0])
        else:
            angle=0
        if scaling:
            scala=np.linalg.norm(v2)/np.linalg.norm(v1)
        else:
            scala=1
        return lambda x,y,z,t: (np.array([x,y,z])-fromA).dot(np.array([
            [((1-t)+scala*t)*np.cos(t*angle),((1-t)+scala*t)*np.sin(t*angle),0],
            [-((1-t)+scala*t)*np.sin(t*angle),((1-t)+scala*t)*np.cos(t*angle),0],
            [0,0,0]
            ]))+fromA+t*(toA-fromA)
    def applyRtoObj(self,mob,alpha=1):
        mob.apply_function(lambda p:self.update_function(*p,alpha))
        return mob

    @staticmethod
    def recolocateObject(mobject,fromA,fromB,toA,toB,scaling=True):
        fu=Recolocate.get_recolocate_udpate_function(fromA,fromB,toA,toB,scaling)
        mobject.apply_function(lambda p:fu(*p,1))

class recolocateFromToSimple(Recolocate):
    def __init__(self,mobject,fromA,toA,angle,**kwargs):
        fromB=fromA+RIGHT
        toB=toA+np.array([np.cos(angle),np.sin(angle),0])
        super().__init__(mobject,fromA,fromB,toA,toB,False,**kwargs)


class recolocateShiftSimple(Recolocate):
    def __init__(self,mobject,vec,angle,**kwargs):
        fromA=np.array([0,0,0])
        fromB=fromA+RIGHT
        toA=fromA+vec
        toB=toA+np.array([np.cos(angle),np.sin(angle),0])
        super().__init__(mobject,fromA,fromB,toA,toB,False,**kwargs)
        #return Homotopy(Recolocate.get_recolocate_udpate_function(fromA,fromB,toA,toB,False),mobject)
class pruebaRecolocate(Scene):
    def construct(self):
        A=0*UP
        B=2*RIGHT
        C=3*UP
        D=3*RIGHT
        E=D+RIGHT
        cua=Square().scale(.5).move_to(A) #Center at A
        cir=Circle().scale(.5).move_to(B) #Center at B
        self.add(cua)
        self.add(cir)
        # self.add(Dot(A))
        vg=VGroup()
        vg.add(Dot(A),TextMobject("A"))
        self.add(vg)
        # self.add(Dot(B))
        # self.add(Dot(C))
        # self.add(Dot(D))
        self.add(Dot(E))
        tri=Polygon(A,B,C,fill_color=RED,fill_opacity=1)
        anim=Recolocate(tri,A,C,D,E)
        self.play(anim)
        anim.applyRtoObj(cua)
        anim.applyRtoObj(cir)


        anim=recolocateFromToSimple(tri,E,A,-PI/3)
        self.play(anim)



        anim.applyRtoObj(cua)
        anim.applyRtoObj(cir)
        anim=recolocateShiftSimple(tri,UP,PI/3)
        self.play(anim)
        anim.applyRtoObj(cua)
        anim.applyRtoObj(cir)




        # anim=Recolocate(tri,A,B,puntos[3].get_center(),puntos[3].get_center())
        # self.play(anim)
        self.wait(3)
