# ==================
#
# hollowtip_nosecones.py
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

from solid import sphere, hull, cylinder
from solid.utils import up

import utils
from nosecone import DerivativeNoseCone
from utils import to_mm


class HollowTipNoseCone(DerivativeNoseCone):
    def __init__(self, cone, offset, radius):
        super(DerivativeNoseCone, self).__init__(length=cone.length, thickness=cone.thickness,
                                                 outer_diameter=cone.outer_diameter, inner_diameter=cone.inner_diameter)
        offset = to_mm(offset)
        radius = to_mm(radius)
        self.cone = cone.cone - up(offset + radius)(sphere(r=radius))
        if self.thickness:
            thickness = to_mm(self.thickness)
            self.cone = self.cone + hull()(cone.cone) * up(offset + radius)(
                sphere(r=radius + thickness) - sphere(r=radius))


class RamJetNoseCone(HollowTipNoseCone):
    def __init__(self, cone, offset, radius, cone_diameter, cone_length):
        super(RamJetNoseCone, self).__init__(cone, offset, radius)
        offset = to_mm(offset)
        radius = to_mm(radius)
        cone_radius = to_mm(cone_diameter / 2.)
        cone_length = to_mm(cone_length)
        self.cone = self.cone + up(offset)(cylinder(h=cone_length, r1=cone_radius, r2=0))
        """
        if self.thickness:
            thickness=to_mm(self.thickness)
            self.cone=self.cone+hull()(cone.cone)*up(offset+radius)(sphere(r=radius+thickness)-sphere(r=radius))
        """


''
if __name__ == '__main__':
    from standard_nosecones import EllipticalNoseCone, ConicalNoseCone, TangentOgiveNoseCone
    from bodytubes.semroc import bt5

    utils.render_to_file(utils.array(2, to_mm(1), [
        HollowTipNoseCone(EllipticalNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .4, 1.),
        HollowTipNoseCone(EllipticalNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .4, .75),
        HollowTipNoseCone(EllipticalNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .4, .5),
        RamJetNoseCone(EllipticalNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .4, 1., .25, .4),
        RamJetNoseCone(ConicalNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .2, 1., .25, .4),
        RamJetNoseCone(TangentOgiveNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .4, 1., .25, .4)]),
                         "examples/hollowtip_nosecones.scad")
