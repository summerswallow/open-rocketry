from solid import *
from solid.utils import up, forward

from utils import AbstractClassError, disk

MM2IN = 25.4


class NoseCone(object):
    """ Requirement for subclasses: nose cones start at z=0 upwards, below z=0 is reserved for nosecone shoulders 
                                    nose cones should be centered at the origin 
          This requirements are necessary for modular features to work"""

    epsilon = 0.001
    resolution = 50

    def __init__(self, length, thickness=None, **kwargs):
        if 'outer_diameter' in kwargs:
            self.outer_diameter = kwargs['outer_diameter']

        if 'inner_diameter' in kwargs:
            self.inner_diameter = kwargs['inner_diameter']

        if 'bodytube' in kwargs:
            self.outer_diameter = kwargs['bodytube'].outer_diameter
            self.inner_diameter = kwargs['bodytube'].inner_diameter

        self.thickness = thickness

        self.length = length

        self.cone = None

    def slice(self, thickness, offset=0):
        return hull()(self.cone * up(offset)(disk(self.outer_diameter * 3, self.thickness)))

    def render(self):
        self.cone.params['segments'] = 200
        scad_render(self.cone)

    def crosssection(self, object=None, angle=0):
        size = (self.length + self.outer_diameter) * 2 * MM2IN
        if object:
            return object * forward(size / 2)(cube(size, center=True));
        return self.cone * forward(size / 2)(cube(size, center=True));

class FunctionBasedNoseCone(NoseCone):
    def __init__(self, length, thickness=None, **kwargs):
        super(FunctionBasedNoseCone, self).__init__(length, thickness, **kwargs)

        def _2d_nosecone(length, radius, **kwargs):
            return polygon([[0, 0]] + [[self.func(length * float(x) / self.resolution, length, radius, **kwargs),
                                        length - length * float(x) / self.resolution] for x in
                                       xrange(0, self.resolution + 1)])

        params = self.process_params(kwargs)

        radius = self.outer_diameter * MM2IN / 2
        length = self.length * MM2IN
        nose = _2d_nosecone(length, radius, **params)
        if self.thickness:
            thickness = self.thickness * MM2IN
            nose -= _2d_nosecone(length - thickness, radius - thickness, **params)
        self.cone = rotate_extrude()(nose)

    def process_params(kwargs):
        raise AbstractClassError("process_params method must be overridden")


class DerivativeNoseCone(NoseCone):
    """ Some nosecone features won't work with these operations """
    pass


class NoseConeWithBase(DerivativeNoseCone):
    def __init__(self, cone, shoulder=None, thickness=None):
        self.length = cone.length
        self.outer_diameter = cone.outer_diameter
        self.inner_diameter = cone.inner_diameter
        if not thickness:
            self.thickness = cone.thickness
        self.shoulder = shoulder
        self.cone = cone

    def slice(self, cone, thickness, offset=0):
        return hull()(cone * up(offset)(disk(self.outer_diameter * 3, thickness / MM2IN)))
