# ==================
#
# nosecone_bases.py
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

import os
from math import sqrt

from flask import Flask
from solid import *
from solid.utils import up, down

from nosecone import NoseConeWithBase
from utils import to_mm, to_inch

MM2IN = 25.4


class NoBase(NoseConeWithBase):
    def __init__(self, cone, shoulder=None, thickness=None):
        super(NoBase, self).__init__(cone, shoulder, thickness)
        if not self.thickness:
            raise ValueError("Thickness must be specified")
        self.cone = cone.cone + self.slice(cone.cone, self.thickness)


class SolidBase(NoseConeWithBase):
    def __init__(self, cone, shoulder=None, thickness=None):
        super(SolidBase, self).__init__(cone, shoulder, thickness)
        if not self.shoulder:
            raise ValueError("Shoulder must be specified")
        radius = cone.inner_diameter * MM2IN / 2
        thickness = MM2IN * self.thickness
        shoulder = self.shoulder * MM2IN
        self.cone = cone.cone + down(shoulder)(cylinder(h=shoulder, r=radius))


class OpenBase(NoseConeWithBase):
    def __init__(self, cone, shoulder=None, thickness=None):
        super(OpenBase, self).__init__(cone, shoulder, thickness)
        if not self.shoulder:
            raise ValueError("Shoulder must be specified")
        if not self.thickness:
            raise ValueError("Thickness must be specified")
        radius = cone.inner_diameter * MM2IN / 2
        thickness = MM2IN * self.thickness
        shoulder = self.shoulder * MM2IN

        self.cone = cone.cone + down(shoulder)(cylinder(h=shoulder, r=radius)) - down(shoulder)(
            cylinder(h=shoulder, r=radius - thickness))


class HollowBase(NoseConeWithBase):
    def __init__(self, cone, shoulder=None, thickness=None):
        super(HollowBase, self).__init__(cone, shoulder, thickness)
        if not self.shoulder:
            raise ValueError("Shoulder must be specified")
        if not self.thickness:
            raise ValueError("Thickness must be specified")
        radius = cone.inner_diameter * MM2IN / 2
        thickness = MM2IN * self.thickness
        shoulder = self.shoulder * MM2IN

        self.cone = cone.cone + down(shoulder)(cylinder(h=shoulder, r=radius)) - down(shoulder - thickness)(
            cylinder(h=shoulder - thickness, r=radius - thickness))


class HollowBaseWithScrewHole(HollowBase):
    def __init__(self, cone, shoulder=None, thickness=None, screw_length=None, screw_diameter=None, screw_size=None):
        super(HollowBaseWithScrewHole, self).__init__(cone, shoulder, thickness)
        radius = cone.inner_diameter * MM2IN / 2

        shoulder = self.shoulder * MM2IN
        thickness = MM2IN * self.thickness
        screw_length = screw_length * MM2IN
        screw_radius = screw_diameter * MM2IN / 2
        if not screw_radius:
            "get_screw_size"

        self.cone = difference()(union()(self.cone,
                                         down(shoulder)(cylinder(h=screw_length, r=screw_radius + thickness / 2.)),
                                         up(min(screw_length - shoulder - thickness, -thickness))(
                                             cylinder(h=thickness, r=radius))),
                                 down(shoulder)(cylinder(h=screw_length, r=screw_radius)))


class SolidBaseWithScrewHole(SolidBase):
    def __init__(self, cone, shoulder=None, thickness=None, screw_length=None, screw_diameter=None, screw_size=None):
        super(SolidBaseWithScrewHole, self).__init__(cone, shoulder, thickness)
        radius = cone.inner_diameter * MM2IN / 2

        shoulder = self.shoulder * MM2IN
        screw_length = screw_length * MM2IN
        screw_radius = screw_diameter * MM2IN / 2
        if not screw_radius:
            "get_screw_size"

        self.cone = difference()(self.cone,
                                 down(shoulder)(cylinder(h=screw_length, r=screw_radius)))


class HollowBaseCutout(HollowBase):
    def __init__(self, cone, shoulder=None, thickness=None, cutout_width=None, cutout_length=None):
        super(HollowBaseCutout, self).__init__(cone, shoulder, thickness)

        cutout_width = to_mm(cutout_width, cone.inner_diameter * 0.3)
        cutout_length = to_mm(cutout_length, self.shoulder / 2.0)
        self.cutout_width = to_inch(cutout_width)
        self.cutout_length = to_inch(cutout_length)
        radius = to_mm(cone.inner_diameter / 2.)
        shoulder = to_mm(self.shoulder)
        thickness = to_mm(self.thickness)

        chord = sqrt(radius * radius - (radius - cutout_width ** 2))

        self.cone = difference()(
            union()(self.cone,
                    difference()(
                        down(shoulder - cutout_length)(cylinder(h=thickness, r=radius)),
                        translate([-radius, -radius, -shoulder + cutout_length])(
                            cube([radius * 2 - cutout_width - thickness,
                                  2 * radius,
                                  cutout_length]))),
                    intersection()(
                        translate([radius - cutout_width - thickness, -chord, -shoulder])(
                            cube([thickness,
                                  chord * 2,
                                  cutout_length])),
                        down(shoulder)(cylinder(h=shoulder, r=radius)))),
            translate([radius - cutout_width, -radius, -shoulder - 1])(
                cube([cutout_width, 2 * radius, cutout_length + 1])))


class SolidBaseCutout(SolidBase):
    def __init__(self, cone, shoulder=None, thickness=None, cutout_width=None, cutout_length=None):
        super(SolidBaseCutout, self).__init__(cone, shoulder, thickness)
        if not cutout_width:
            cutout_width = cone.inner_diameter * 0.3
        if not cutout_length:
            cutout_length = self.shoulder / 2.0
        self.cutout_width = cutout_width
        self.cutout_length = cutout_length
        radius = cone.inner_diameter * MM2IN / 2
        shoulder = self.shoulder * MM2IN
        thickness = MM2IN * self.thickness

        cutout_width = self.cutout_width * MM2IN
        cutout_length = self.cutout_length * MM2IN
        chord = sqrt(radius * radius - (radius - cutout_width ** 2))

        self.cone = difference()(self.cone,
                                 translate([radius - cutout_width, -radius, -shoulder - 1])(
                                     cube([cutout_width, 2 * radius, cutout_length + 1])))


class BaseWithElbow(NoseConeWithBase):
    def __init__(self, cone, shoulder=None, thickness=None, elbow_radius=None, bend_radius=None):
        super(BaseWithElbow, self).__init__(cone, shoulder, thickness)
        if not isinstance(cone, SolidBaseCutout) and not isinstance(cone, HollowBaseCutout):
            raise "Not designed"

        cutout_length = cone.cutout_length * MM2IN
        cutout_width = cone.cutout_width * MM2IN
        shoulder = cone.shoulder * MM2IN
        thickness = self.thickness * MM2IN
        elbow_radius = to_mm(elbow_radius, self.thickness / 2.)
        bend_radius = to_mm(bend_radius, self.thickness)
        radius = to_mm(cone.inner_diameter / 2.)
        self.cone = union()(cone.cone,
                            translate([radius - cutout_width, 0, -shoulder])(
                                self._elbow(elbow_radius, bend_radius, cutout_width,
                                            cutout_length)))

    def _donut(self, radius, big_radius):
        return down(big_radius + radius)(rotate([90, 0, 0, 0])(
            rotate_extrude()(translate([big_radius, 0, 0])(circle(radius)))))

    def _elbow(self, radius, big_radius, width, height):
        return union()(up(radius)(rotate([0, 90, 0])(cylinder(h=width - big_radius - radius, r=radius))),
                       translate([width - radius, 0, big_radius + radius])(
                           cylinder(h=height - big_radius - radius, r=radius)),
                       translate([width - big_radius - radius, 0, big_radius * 2 + radius * 2])(
                           self._donut(radius, big_radius)) * (
                           translate([width - big_radius / 2. - radius / 2., 0, big_radius / 2. + radius / 2.])(
                               cube([big_radius + radius, radius * 2, big_radius + radius], center=True)))
                       )


class BaseWithRing(NoseConeWithBase):
    def __init__(self, cone, shoulder=None, thickness=None, ring_radius=None, ring_thickness=None):
        super(BaseWithRing, self).__init__(cone, shoulder, thickness)
        if not isinstance(cone, SolidBaseCutout) and not isinstance(cone, HollowBaseCutout):
            raise "Not designed"

        cutout_length = cone.cutout_length * MM2IN
        cutout_width = cone.cutout_width * MM2IN
        shoulder = cone.shoulder * MM2IN
        thickness = self.thickness * MM2IN
        ring_radius = to_mm(ring_radius, self.thickness)
        ring_thickness = to_mm(ring_thickness, self.thickness / 2.)
        radius = cone.inner_diameter * MM2IN / 2
        self.cone = cone.cone + translate([radius - cutout_width + ring_radius - ring_thickness, 0,
                                           -shoulder + 4 * ring_thickness + 2 * ring_radius])(
            self._donut(ring_thickness, ring_radius))

    def _donut(self, radius, big_radius):
        return down(big_radius + radius)(rotate([90, 0, 0, 0])(
            rotate_extrude()(translate([big_radius, 0, 0])(circle(radius)))))


if __name__ == '__main__':
    """ Generate Examples"""
    from standard_nosecones import EllipticalNoseCone
    from nosecone_threaded_bases import *
    import utils
    from bodytubes.semroc import bt5

    nc = EllipticalNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                            mid_diameter=.3)

    array = utils.array_crosssection(4, MM2IN, [
        ThreadedBaseOutset(nc, shoulder=0.5),
        ThreadedBaseFlat(nc, shoulder=0.5),
        nc.crosssection(ThreadedBaseOutset(nc, shoulder=0.5).mate),
        BaseWithRing(HollowBaseCutout(nc, shoulder=0.5)),

        BaseWithElbow(HollowBaseCutout(nc, shoulder=0.5)),
        SolidBaseCutout(nc, shoulder=0.5),
        HollowBaseCutout(nc, shoulder=0.5),
        SolidBaseWithScrewHole(nc, shoulder=0.5, screw_diameter=1 / 16., screw_length=0.25),
        HollowBaseWithScrewHole(nc, shoulder=0.5, screw_diameter=1 / 16., screw_length=0.25),
        HollowBase(nc, shoulder=0.5),
        OpenBase(nc, shoulder=0.5), SolidBase(nc, shoulder=0.5), NoBase(nc),
    ])
    utils.render_to_file(array, "examples/nosecone_bases.scad")
