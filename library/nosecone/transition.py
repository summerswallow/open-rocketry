from solid import *
from solid.utils import up, forward, down

from misc.utils import AbstractClassError, disk, to_mm, render_to_file
from bodytubes.semroc import bt50, bt55
class Transition(NoseCone):
    def __init__(self, length, thickness=None, **kwargs):
        super(Transition, self).__init__(length, thickness, **kwargs)

        def _solid_nose(length, radius):
            return cylinder(h=length, r1=radius, r2=0)

        length = self.length * MM2IN
        radius = self.outer_diameter * MM2IN / 2
        nose = _solid_nose(length, radius)
        if self.thickness:
            thickness = self.thickness * MM2IN
            nose -= _solid_nose(length - thickness, radius - thickness)
            self.mid_cone = _solid_nose(length - thickness/2., radius-thickness/2.)
        self.cone = nose

class Transition(object):
    def __init__(self, height, **kwargs):
        bt1 = kwargs.get('bodytube1')
        bt2 = kwargs.get('bodytube2')
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
        if self.shoulder1 is None:
            self.shoulder1 = self.shoulder
        if self.shoulder2 is None:
            self.shoulder2 = self.shoulder
        self.height = to_mm(height)
        self.shoulder=to_mm(0.5)
        self.thickness = to_mm(kwargs.get('thickness'),safe=True)
        self.transition = cylinder(h=self.shoulder1, r=self.r1)+up(self.shoulder1+self.height)(cylinder(h=self.shoulder2, r=self.r4))+    up(self.shoulder1)(cylinder(h=self.height, r1=self.r2, r2=self.r3))

        if self.thickness:
            subtract =  cylinder(h=self.shoulder1, r=self.r1-self.thickness)+up(self.shoulder1+self.height)(cylinder(h=self.shoulder2, r=self.r4-self.thickness))+    up(self.shoulder1)(cylinder(h=self.height, r1=self.r2-self.thickness, r2=self.r3-self.thickness))
            self.transition -= subtract

    def render(self):
        return 
    
t=Transition(1, bodytube1=bt50, bodytube2=bt55, shoulder2=1.0, thickness = 1/16.)

render_to_file(t.transition, "test.scad")
