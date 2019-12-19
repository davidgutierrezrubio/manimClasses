#!/usr/bin/env python

import sys
sys.path.insert(1, 'c:\\manim\\manim-3feb')

from manimlib.imports import *
#
# if __name__ == "__main__":
#     os.chdir('c:\\manim\\manim-3feb')
#     module_name = 'myProjects\\'+ os.path.basename(__file__)
#     print(module_name)
#     command_A = "python -m manim "
#     command_B = module_name +" " +"Midy"+" -pl"
#     os.system(command_A + command_B)

class Midy(Scene):
    def construct(self):
        title=TextMobject("Midy's theorem").scale(3)
        self.play(ShowCreation(title))
        self.wait()
        self.play(FadeOut(title))
        self.primeBox = ImageMobject("myProjects\\cajaPrimos.png").to_edge(LEFT+DOWN)
        self.play(FadeIn(self.primeBox))
        self.integersBox=TexMobject("{\mathbb N}").scale(4).to_edge(UP+LEFT)
        self.add(self.integersBox)
        #self.wait(3)
        #Now, extract a prime number from the box
        self.fractionLine=Line(ORIGIN,RIGHT).to_edge(LEFT)
        self.fractionLine.shift(self.primeBox.get_width()*1.2*RIGHT)
        self.scaleOfDigits=1.5
        # self.writeDecimals("1","7","=0.","142","857")
        # self.sumSuccesful()
        self.writeDecimals("25","13","=1.","923","076")
        self.sumSuccesful()
        #3/17=0,17647058 82352941...
        self.writeDecimals("3","17","=0.","17647058","82352941")
        self.sumSuccesful()

        #1/31 doesn't meet the requirements for theorem
        #0,0322580 64516129...
        self.writeDecimals("1","31","=0.","0322580","64516129")
        self.sumUnsucessful()

        self.wait()
    def writeDecimals(self,integer,prime,intPart,decPart1,decPart2):
        self.primeNumber=TexMobject(prime).scale(self.scaleOfDigits).move_to(self.primeBox)
        self.anyInteger=TexMobject(integer).scale(self.scaleOfDigits).move_to(self.integersBox)
        sc=self.primeNumber.get_width()/self.fractionLine.get_width()*1.2
        self.fractionLine.scale(sc)
        self.play(
        GrowFromCenter(self.primeNumber),
        GrowFromCenter(self.anyInteger),
        )
        self.play(
        ApplyMethod(self.primeNumber.next_to,self.fractionLine,DOWN,path_arc=3.1415/2),
        ApplyMethod(self.anyInteger.next_to,self.fractionLine,UP,path_arc=-3.1415/2),
        FadeIn(self.fractionLine),
        run_time=2)
        #Now write the decimal expansion
        self.integerPart=TexMobject(intPart).scale(self.scaleOfDigits).next_to(self.fractionLine,RIGHT)
        self.decimalPart=TexMobject(decPart1,decPart2).scale(self.scaleOfDigits).next_to(self.integerPart,RIGHT)
        self.play(FadeIn(self.integerPart))
        self.play(FadeIn(self.decimalPart))
        #Now replicate the periodic part
        self.decimalPart2=self.decimalPart.copy()
        self.play(ApplyMethod(self.decimalPart2.next_to,self.decimalPart,RIGHT,path_arc=-3.1415))
        #Once more...
        self.decimalPart3=self.decimalPart2.copy()
        self.play(ApplyMethod(self.decimalPart3.next_to,self.decimalPart2,RIGHT,path_arc=-3.1415))
        self.decimalDots=TexMobject("...").next_to(self.decimalPart3,RIGHT)
        self.play(FadeIn(self.decimalDots))
        #Now do the sum...
        self.dec1=int(decPart1)
        self.dec2=int(decPart2)
        print(self.dec1,self.dec2)
    def sumSuccesful(self):
        #Copy the second half an put it under the first half
        #Darken the rest of the decimals
        self.secondPartDecimals=self.decimalPart[1].copy()
        fadeColor="#0b1b52"
        self.play(
        ApplyMethod(self.secondPartDecimals.next_to,self.decimalPart[0],DOWN,path_arc=-3.1415),
        ApplyMethod(self.integerPart.set_color,fadeColor),
        ApplyMethod(self.decimalPart[1].set_color,fadeColor),
        ApplyMethod(self.decimalPart2.set_color,fadeColor),
        ApplyMethod(self.decimalPart3.set_color,fadeColor),
        ApplyMethod(self.decimalDots.set_color,fadeColor)
        )

        self.plusSign=TexMobject("+").next_to(self.secondPartDecimals,LEFT)
        self.plusLine=Line(ORIGIN,self.secondPartDecimals.get_width()*1.2*RIGHT).next_to(self.secondPartDecimals,DOWN)

        self.play(FadeIn(self.plusLine),FadeIn(self.plusSign))

        self.result=str(self.dec1+self.dec2)
        self.resulMObj=TexMobject(self.result).scale(self.scaleOfDigits).next_to(self.plusLine,DOWN)
        self.play(FadeIn(self.resulMObj))
        self.eqGrp=VGroup(self.decimalPart[0],self.plusSign,self.plusLine,self.secondPartDecimals,self.resulMObj)

        resultBox = SurroundingRectangle(self.eqGrp, buff = .1)
        self.play(ShowCreation(resultBox))
        #Now wait and delete objects
        self.wait()
        self.play(
        FadeOut(self.primeNumber),
        FadeOut(self.anyInteger),
        FadeOut(self.integerPart),
        FadeOut(self.decimalPart),
        FadeOut(self.decimalPart2),
        FadeOut(self.decimalPart3),
        FadeOut(self.secondPartDecimals),
        FadeOut(self.plusSign),
        FadeOut(self.plusLine),
        FadeOut(self.fractionLine),
        FadeOut(self.resulMObj),
        FadeOut(self.resulMObj),
        FadeOut(self.decimalDots),
        FadeOut(resultBox)
        )

    def sumUnsucessful(self):
        #Copy the second half an put it under the first half
        #Darken the rest of the decimals
        self.secondPartDecimals=self.decimalPart[1].copy()
        fadeColor="#0b1b52"
        self.play(
        ApplyMethod(self.secondPartDecimals.next_to,self.decimalPart[0],DOWN,path_arc=-3.1415),
        ApplyMethod(self.integerPart.set_color,fadeColor),
        ApplyMethod(self.decimalPart[1].set_color,fadeColor),
        ApplyMethod(self.decimalPart2.set_color,fadeColor),
        ApplyMethod(self.decimalPart3.set_color,fadeColor)
        )

        self.plusSign=TexMobject("+").next_to(self.secondPartDecimals,LEFT).shift(.2*LEFT)
        self.plusLine=Line(ORIGIN,self.secondPartDecimals.get_width()*1.2*RIGHT).next_to(self.secondPartDecimals,DOWN)

        self.play(FadeIn(self.plusLine),FadeIn(self.plusSign))

        self.wait()

        #First try to adjust to the LEFT
        #Try to sum...
        self.result=str(10*self.dec1+self.dec2)
        self.resulMObj=TexMobject(self.result).scale(self.scaleOfDigits).next_to(self.plusLine,DOWN)

        #Result should be aligned to the RIGHT of the bigger number
        if (self.dec1>self.dec2):
            self.resulMObj.align_to(self.decimalPart[0],RIGHT)
        else:
            self.resulMObj.align_to(self.decimalPart[0],LEFT)
            self.play(
            ApplyMethod(self.secondPartDecimals.align_to,self.decimalPart[0],LEFT),
            FadeIn(self.resulMObj))


        self.wait(1)

        #Now let's try to align the number to RIGHT
        #Try to sum...
        self.result=str(self.dec1+self.dec2)
        self.resulMObj2=TexMobject(self.result).scale(self.scaleOfDigits).next_to(self.plusLine,DOWN)

        #Result should be aligned to the RIGHT of the bigger number
        if (self.dec1>self.dec2):
            self.resulMObj2.align_to(self.decimalPart[0],LEFT)
        else:
            self.resulMObj2.align_to(self.decimalPart[0],RIGHT)
        self.play(
        ApplyMethod(self.secondPartDecimals.align_to,self.decimalPart[0],RIGHT),
        Transform(self.resulMObj,self.resulMObj2)
        )
        self.wait(1)


        self.eqGrp=VGroup(self.decimalPart[0],self.plusSign,self.plusLine,self.secondPartDecimals,self.resulMObj)
        self.add_sound("myProjects\\buzzer.wav")
        self.play(WiggleOutThenIn(self.eqGrp,scale_value=1))
        #Now wait and delete objects
        self.wait()
        self.play(
        FadeOut(self.primeNumber),
        FadeOut(self.anyInteger),
        FadeOut(self.integerPart),
        FadeOut(self.decimalPart),
        FadeOut(self.decimalPart2),
        FadeOut(self.decimalPart3),
        FadeOut(self.secondPartDecimals),
        FadeOut(self.plusSign),
        FadeOut(self.plusLine),
        FadeOut(self.fractionLine),
        FadeOut(self.resulMObj),
        FadeOut(self.resulMObj2),
        FadeOut(self.decimalDots)
        )
