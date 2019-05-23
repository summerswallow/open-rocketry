from solid import *
from solid.utils import up, forward, down

from misc.utils import AbstractClassError, disk, to_mm, render_to_file
from bodytubes.semroc import bt20, bt50, bt55
class Transition(object):
    def __init__(self, height, **kwargs):
        bt1 = kwargs.get('bodytube1')
        bt2 = kwargs.get('bodytube2')
        bt3 = kwargs.get('bodytube3')
        fudge = to_mm(kwargs.get('fudge'), default=0.0)
        self.open_end = kwargs.get('open_end', False)
        self.r1= to_mm(kwargs.get('r1'),safe=True)
        self.r2= to_mm(kwargs.get('r2'),safe=True)
        self.r3= to_mm(kwargs.get('r3'),safe=True)
        self.r4= to_mm(kwargs.get('r4'),safe=True)
        if bt1:
            self.r1=to_mm(bt1.inner_diameter/2.0)
            self.r2=to_mm(bt1.outer_diameter/2.0)
        if bt2:
            self.r4=to_mm(bt2.inner_diameter/2.0)
            self.r3=to_mm(bt2.outer_diameter/2.0)
        self.shoulder= to_mm(kwargs.get('shoulder'),default=0.5)
        self.shoulder1 = to_mm(kwargs.get('shoulder1'),safe=True)
        self.shoulder2 = to_mm(kwargs.get('shoulder2'),safe=True)
        self.r1-=fudge
        self.r4-=fudge
        if self.shoulder1 is None:
            self.shoulder1 = self.shoulder
        if self.shoulder2 is None:
            self.shoulder2 = self.shoulder
        self.height = to_mm(height)
        self.shoulder=to_mm(0.5)
        self.thickness = to_mm(kwargs.get('thickness'),safe=True)
        self.transition = cylinder(h=self.shoulder1, r=self.r1)+up(self.shoulder1+self.height)(cylinder(h=self.shoulder2, r=self.r4))+    up(self.shoulder1)(cylinder(h=self.height, r1=self.r2, r2=self.r3))

        if bt3 and not self.thickness:
            self.transtion -= cylinder(h=shoulder1+height+shoulder2, r=bt3.outer_diameter/2.0);

        if self.thickness:
            subtract =  cylinder(h=self.shoulder1, r=self.r1-self.thickness)+up(self.shoulder1+self.height)(cylinder(h=self.shoulder2, r=self.r4-self.thickness))+    up(self.shoulder1)(cylinder(h=self.height, r1=self.r2-self.thickness, r2=self.r3-self.thickness))
            self.transition -= subtract
            if bt3 or not self.open_end:
                self.transition+=cylinder(h=self.thickness, r=self.r1)+ up(self.shoulder1+self.height+self.shoulder2-self.thickness)(cylinder(h=self.thickness, r=self.r4))
                if bt3:
                    self.transition+=cylinder(h=self.shoulder1+self.height+self.shoulder2, r=to_mm(bt3.outer_diameter/2.0)+self.thickness)
                    self.transition-=cylinder(h=self.shoulder1+self.height+self.shoulder2, r=to_mm(bt3.outer_diameter/2.0)+fudge)

    def render(self):
        return 

    def crosssection(self, object=None, angle=0):
        size = (self.height + self.shoulder1 +self.shoulder2 + self.r1) * 2
        if object:
            return object * forward(size / 2)(cube(size, center=True));
        return self.transition * forward(size / 2)(cube(size, center=True));


if __name__=="__main__":
    t=Transition(1, bodytube1=bt50, bodytube2=bt55, shoulder2=1.0, thickness = 1/16., bodytube3=bt20, open_end=True)

    render_to_file(t.crosssection(), "test.scad")
