from misc import utils
from nosecone.nosecone import DerivativeNoseCone
from misc.utils import to_mm
from solid import cylinder
from solid.utils import up

class TaperedBaseNoseCone(DerivativeNoseCone):
    def __init__(self, cone_class, taper_diameter, taper_length, flat_length, **kwargs):
        super(DerivativeNoseCone, self).__init__(**kwargs)
        length=kwargs.pop('length')
        cone = cone_class(outer_diameter=taper_diameter, length=length-taper_length-flat_length, **kwargs)
        flat_length = to_mm(flat_length)
        taper_length = to_mm(taper_length)
        outer_radius = to_mm(self.outer_diameter/2.0)
        taper_radius = to_mm(taper_diameter/2.0)
        flat = (cylinder(r=taper_radius, h=flat_length))
        print(cone.outer_diameter)
        taper = cylinder(r1=outer_radius, r2=taper_radius, h=taper_length)
        if self.thickness:
            thickness = to_mm(self.thickness)
            flat -=(cylinder(r=taper_radius-thickness, h=flat_length))
            taper -=cylinder(r1=outer_radius-thickness, r2=taper_radius-thickness, h=taper_length)
        print (taper_radius, outer_radius)
        self.cone = up(taper_length)(flat)+taper+up(taper_length+flat_length)(cone.cone)
