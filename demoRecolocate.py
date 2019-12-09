#!/usr/bin/env python

from manimlib.imports import *
from myProjects.Recolocate import *
class demoRecolocate(Scene):
    def dotWithLabel(self,coords,label,colorPoint):
        vg=VGroup()
        punto=Dot().shift(coords)
        vg.add(punto)
        punto.set_color(colorPoint)
        te=TextMobject(label)
        te.next_to(punto,DOWN)
        te.set_color(colorPoint)
        vg.add(te)
        return vg
    def construct(self):
        A=-2*RIGHT-UP
        B=2*RIGHT-UP
        C=2.2*RIGHT+UP
        D=3*RIGHT-.5*UP
        rec=Rectangle()
        texto=TextMobject("Recolocate(mobject,","A",",","B",",","C",",","D",")").to_edge(UP)
        texto[1].set_color(RED)
        texto[3].set_color(RED)
        texto[5].set_color(BLUE)
        texto[7].set_color(BLUE)

        self.play(FadeIn(texto))

        vgA=self.dotWithLabel(A,"A",RED)
        vgB=self.dotWithLabel(B,"B",RED)
        vgC=self.dotWithLabel(C,"C",BLUE)
        vgD=self.dotWithLabel(D,"D",BLUE)
        anims=map(lambda r:FadeIn(r),[vgA,vgB,vgC,vgD])
        self.play(*anims)
        self.play(ShowCreation(rec))
        anim=Recolocate(rec,vgA[0],B,C,D)
        self.play(anim)
        self.wait(3)

        #Borro
        self.play(FadeOut(rec),FadeOut(texto))
        #Ahora demo con recolocate scaling=False
        texto=TextMobject("Recolocate(mobject,","A",",","B",",","C",",","D",",scaling=False)").to_edge(UP)
        texto[1].set_color(RED)
        texto[3].set_color(RED)
        texto[5].set_color(BLUE)
        texto[7].set_color(BLUE)
        self.play(FadeIn(texto))
        rec=Rectangle()
        self.play(ShowCreation(rec))
        anim=Recolocate(rec,A,B,C,D,scaling=False)
        self.play(anim)
        self.wait(3)

        #Borro
        self.play(FadeOut(rec),FadeOut(texto))
        #Ahora demo con recolocate rotate=False
        texto=TextMobject("Recolocate(mobject,","A",",","B",",","C",",","D",",rotate=False)").to_edge(UP)
        texto[1].set_color(RED)
        texto[3].set_color(RED)
        texto[5].set_color(BLUE)
        texto[7].set_color(BLUE)
        self.play(FadeIn(texto))
        rec=Rectangle()
        self.play(ShowCreation(rec))
        anim=Recolocate(rec,A,B,C,D,rotate=False)
        self.play(anim)
        self.wait(3)

        #Borro
        self.play(FadeOut(rec),FadeOut(texto),FadeOut(vgB),FadeOut(vgD))
        #Ahora demo con recolocatesimple
        texto=TextMobject("RecolocateFromToSimple(mobject,",
        "A",
        ",",
        "C",
        ",PI/3)").to_edge(UP)
        texto[1].set_color(RED)
        texto[3].set_color(BLUE)
        self.play(FadeIn(texto))
        rec=Rectangle()
        self.play(ShowCreation(rec))
        anim=RecolocateFromToSimple(rec,A,C,PI/4)
        self.play(anim)
        self.wait(3)
