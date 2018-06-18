# ==================
#
# morph_nosecones.py
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

from math import pi, cos, sin, sqrt

from solid import square, cylinder, hull, scale, linear_extrude, polygon, union, circle, multmatrix, sphere
from solid.utils import up

from misc import utils
from nosecone import DerivativeNoseCone, NoseCone
from misc.utils import to_mm


class MorphedNoseCone(NoseCone):
    def __init__(self, length, polygon, thickness=None, **kwargs):
        """

        :param length: Nosecone length
        :param polygon: Convex polygon
        :param thickness: Nosecone wall thickness
        :param kwargs:
        """
        super(MorphedNoseCone, self).__init__(length, thickness, **kwargs)

        def _solid_nose(length, radius, ratio=1):
            return hull()(self._flatten(cylinder(h=self.epsilon, r=radius)) + up(length)(
                scale(ratio)(self._flatten(linear_extrude()(polygon)))))

        length = to_mm(self.length)
        radius = to_mm(self.outer_diameter / 2.)
        self.cone = _solid_nose(length, radius)
        if self.thickness:
            thickness = to_mm(self.thickness)
            ratio = (radius - thickness) / radius
            self.cone -= _solid_nose(length - thickness, radius - thickness, ratio)

    def _flatten(self, object):
        return scale([1, 1, 0])(object)


class RectangularNoseCone(MorphedNoseCone):
    def __init__(self, length, thickness=None, width=None, depth=None, **kwargs):
        super(MorphedNoseCone, self).__init__(length, thickness, **kwargs)
        width = to_mm(width, sqrt(0.5) * self.outer_diameter)
        depth = to_mm(depth, sqrt(0.5) * self.outer_diameter)
        super(RectangularNoseCone, self).__init__(length, square([width, depth], center=True), thickness, **kwargs)


class EllipseNoseCone(MorphedNoseCone):
    def __init__(self, length, thickness=None, major=None, minor=None, **kwargs):
        super(MorphedNoseCone, self).__init__(length, thickness, **kwargs)
        major = to_mm(major, self.outer_diameter / 2.)
        minor = to_mm(minor, self.outer_diameter / 4.)
        super(EllipseNoseCone, self).__init__(length, scale([major / minor, 1])(circle(r=minor)), thickness, **kwargs)


class StarNoseCone(MorphedNoseCone):
    def __init__(self, length, thickness=None, inner=None, outer=None, points=5, **kwargs):
        """

        :param length:
        :param thickness:
        :param inner:
        :param outer:
        :param points:
        :param kwargs:
        Hollow doesn't work quite right yet.
        """
        super(MorphedNoseCone, self).__init__(length, thickness, **kwargs)
        outer = to_mm(outer, self.outer_diameter / 4.)
        inner = to_mm(inner, self.outer_diameter / 8.)
        out = []
        for i in xrange(0, points):
            alpha = i * 2. * pi / points
            p = polygon([[0, 0], [inner * cos(alpha - pi / points), inner * sin(alpha - pi / points)],
                         [outer * cos(alpha), outer * sin(alpha)],
                         [inner * cos(alpha + pi / points), inner * sin(alpha + pi / points)]])
            out.append(
                MorphedNoseCone(length, p, inner_diameter=self.inner_diameter, outer_diameter=self.outer_diameter,
                                thickness=thickness).cone)
        self.cone = union()(*out)


if __name__ == '__main__':
    from bodytubes.semroc import bt5

    utils.render_to_file(utils.array(2, to_mm(1), [RectangularNoseCone(0.75, bodytube=bt5, thickness=1 / 16.),
                                                   RectangularNoseCone(0.75, bodytube=bt5, width=.1, depth=.25,
                                                                       thickness=1 / 16.),
                                                   EllipseNoseCone(0.75, bodytube=bt5, thickness=1 / 16.),
                                                   StarNoseCone(0.75, bodytube=bt5, thickness=1 / 16.)]),
                         "examples/morphed_nosecone.scad")
