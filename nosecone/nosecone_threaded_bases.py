# ==================
#
# nosecone_threaded_bases.py
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

from nosecone import NoseConeWithBase
from misc.threaded import Threaded
from misc.utils import to_mm, to_inch
from solid.utils import up, down
from math import sqrt
from  solid import cylinder, difference, union, color,intersection


class ThreadedBase(NoseConeWithBase, Threaded):
    pass


class ThreadedBaseFlat(ThreadedBase):
    def __init__(self, cone, shoulder=None, thickness=None, threads_per_inch=6):
        super(ThreadedBaseFlat, self).__init__(cone, shoulder, thickness)
        shoulder = to_mm(self.shoulder)
        thickness = to_mm(self.thickness)
        radius = to_mm(cone.inner_diameter / 2.)
        tooth = to_mm(1. / threads_per_inch * sqrt(3) / 2.)

        self.cone = cone.cone + self.slice(cone.cone, thickness) + down(shoulder)(
            self.threaded_male_column(length=shoulder,
                                      diameter=radius * 2 - thickness * 2,
                                      threads_per_inch=threads_per_inch)) \
                    - down(shoulder - thickness)(cylinder(h=shoulder + thickness, r=radius - thickness - tooth))
        self.mate = down(shoulder)(cylinder(h=shoulder, r=radius)) \
                    - down(shoulder)(
            self.threaded_female_column(length=shoulder + thickness, diameter=radius * 2 - thickness * 2,
                                        threads_per_inch=threads_per_inch))
        sectioner = down(shoulder+self.epsilon)(cylinder(h=shoulder+self.epsilon, r=radius)) + cylinder(h=thickness/2, r=radius-thickness-thickness/2. - tooth)+ cylinder(h=thickness, r=radius-thickness-thickness - tooth)
        self.cone_section1 = self.cone-sectioner
        self.cone_section2 = self.cone*sectioner

class ThreadedBaseInset(ThreadedBase):
    def __init__(self, cone, shoulder=None, thickness=None, threads_per_inch=6):
        super(ThreadedBaseInset, self).__init__(cone, shoulder, thickness)
        shoulder = to_mm(self.shoulder)
        thickness = to_mm(self.thickness)
        radius = to_mm(cone.inner_diameter / 2.)
        tooth = to_mm(1. / threads_per_inch * sqrt(3) / 2.)

        self.cone = difference()(union()(cone.cone,
                                         down(thickness)(cylinder(h=thickness, r=radius)),
                                         down(shoulder)(self.threaded_male_column(length=shoulder,
                                                                                  diameter=radius * 2 - thickness * 2,
                                                                                  threads_per_inch=threads_per_inch))),
                                 down(shoulder - thickness)(cylinder(h=shoulder, r=radius - thickness - tooth)))
        self.mate = down(shoulder)(cylinder(h=shoulder - thickness, r=radius)) \
                    - down(shoulder)(self.threaded_female_column(length=shoulder, diameter=radius * 2 - thickness * 2,
                                                                 threads_per_inch=threads_per_inch))


class ThreadedBaseOutset(ThreadedBase):
    def __init__(self, cone, shoulder=None, thickness=None, threads_per_inch=6, offset=None):
        super(ThreadedBaseOutset, self).__init__(cone, shoulder, thickness)
        shoulder = to_mm(self.shoulder)
        thickness = to_mm(thickness, self.thickness)
        radius = to_mm(cone.inner_diameter / 2.)
        offset = to_mm(offset, to_inch(thickness))
        tooth = to_mm(1. / threads_per_inch * sqrt(3) / 2.)

        self.cone = union()((cone.cone - cylinder(h=offset, r=3 * radius)),
                            down(shoulder)(
                                self.threaded_male_column(length=shoulder + offset, diameter=radius * 2 - thickness * 2,
                                                          threads_per_inch=threads_per_inch)),
                            self.slice(cone.cone, thickness, offset=offset)) - down(shoulder - thickness)(
            cylinder(h=shoulder + offset, r=radius - thickness - tooth))

        self.mate = down(shoulder)(cylinder(h=shoulder, r=radius)) + self.slice(cone.cone, offset) \
                    - down(shoulder)(
            self.threaded_female_column(length=shoulder + offset, diameter=radius * 2 - thickness * 2,
                                        threads_per_inch=threads_per_inch))

class ScrewInBase(ThreadedBase):
    def __init__(self, cone, shoulder=None, thickness=None, threads_per_inch=6, thread_height=None, thread_diameter=None):
        super(ScrewInBase, self).__init__(cone, shoulder, thickness)
        shoulder = to_mm(self.shoulder)
        thickness = to_mm(thickness, self.thickness)
        radius = to_mm(cone.inner_diameter / 2.)
        thread_height = to_mm(thread_height, self.length/3)
        thread_diameter = to_mm(thread_diameter,cone.inner_diameter/2.)
        tooth = to_mm(1. / threads_per_inch * sqrt(3) / 2.)

        self.cone = (cone.cone + self.slice(cone.cone, thread_height)) - self.threaded_female_column(length = thread_height, diameter=thread_diameter,
                                                                                                    threads_per_inch=threads_per_inch)

        self.mate = union()(down(shoulder)(cylinder(h=shoulder, r=radius)) - down(shoulder-thickness)(cylinder(h=shoulder-thickness*2, r=radius-thickness)),
                            self.threaded_male_column(length = thread_height, diameter=thread_diameter,
                                                      threads_per_inch=threads_per_inch)) - down(thickness)(cylinder(h=thread_height+thickness,r=thread_diameter/2-thickness-tooth))

class ScrewInBaseWithScrewHole(ScrewInBase):
    def __init__(self, cone, shoulder=None, thickness=None, threads_per_inch=6, thread_height=None, thread_diameter=None, screw_length=None, screw_diameter=None, screw_size=None):
        super(ScrewInBaseWithScrewHole, self).__init__(cone, shoulder, thickness, threads_per_inch, thread_height, thread_diameter)
        radius = to_mm(cone.inner_diameter  / 2)

        shoulder = to_mm(self.shoulder)
        thickness = to_mm(self.thickness)
        screw_length = to_mm(screw_length )
        screw_radius = to_mm(screw_diameter  / 2)
        if not screw_radius:
            "get_screw_size"

        self.mate = difference()(union()(self.mate,
                                         down(shoulder)(cylinder(h=screw_length, r=screw_radius + thickness / 2.)),
                                         up(min(screw_length - shoulder - thickness, -thickness))(
                                             cylinder(h=thickness, r=radius))),
                                 down(shoulder)(cylinder(h=screw_length, r=screw_radius)))

class ThreadedBaseOutsetScrewInBase(ThreadedBase):
    def __init__(self, cone, shoulder=None, thickness=None, upper_tpi=6, lower_tpi=4,  offset=None, thread_height=None, thread_diameter=None):
        super(ThreadedBaseOutsetScrewInBase, self).__init__(cone, shoulder, thickness)
        shoulder = to_mm(self.shoulder)
        thickness = to_mm(thickness, self.thickness)
        radius = to_mm(cone.inner_diameter / 2.)
        offset = to_mm(offset, to_inch(thickness))
        upper_tooth = to_mm(1. / upper_tpi * sqrt(3) / 2.)
        lower_tooth = to_mm(1. / lower_tpi * sqrt(3) / 2.)
        thread_height = to_mm(thread_height, self.length/3)
        thread_diameter = to_mm(thread_diameter,cone.inner_diameter/2.)

        self.cone = difference () (union()((cone.cone - cylinder(h=offset, r=3 * radius)),
                                           color("red")(self.slice(cone.cone, thread_height, offset))),
                                   up(offset-self.epsilon)(self.threaded_female_column(length = thread_height+2*self.epsilon, diameter=thread_diameter,
                                                               threads_per_inch=upper_tpi)),
                                   cylinder(h=to_mm(0.25), r=radius-thickness))

        core_radius = min(thread_diameter/2-thickness-upper_tooth, radius - thickness - lower_tooth)
        lower_thread = down(shoulder)(self.threaded_male_column(length=shoulder + offset, diameter=radius * 2 - thickness * 2.,
                                                                threads_per_inch=lower_tpi))
        upper_thread = up(offset)(self.threaded_male_column(length = thread_height, diameter=thread_diameter,
                                                            threads_per_inch=upper_tpi))
        self.center_mate = upper_thread+lower_thread+cylinder(h=thickness,r=radius-thickness)-down(shoulder-thickness)(cylinder(h=shoulder+offset+thread_height, r=core_radius))

        self.mate = difference ()(down(shoulder)(cylinder(h=shoulder, r=radius)) + self.slice(cone.cone, offset),
                                  down(shoulder)(self.threaded_female_column(length=shoulder + offset, diameter=radius * 2 - thickness * 2,
                                                                             threads_per_inch=lower_tpi)),
                                  cylinder(h=thickness,r=radius-thickness))

if __name__ == '__main__':
    """ Generate Examples"""
    from standard_nosecones import EllipticalNoseCone
    from nosecone_threaded_bases import *
    from bodytubes.semroc import bt55
    from bodytubes.modelrockets_us import _3_00
    from nosecone_library.specific_noses import BNC5V
    from misc import utils

    nc = EllipticalNoseCone(2.75, bodytube=bt55, thickness=1 / 16.0)
    nc = BNC5V(scale_bodytube=_3_00, thickness = 3/32.)
    sib = ScrewInBase(nc, shoulder=0.5, thread_height=0.75, thread_diameter=1.2)
    sib = ScrewInBaseWithScrewHole(nc, shoulder=0.5, thread_height=0.75, thread_diameter=1.2, screw_diameter=1 / 16., screw_length=0.25)
    sib = ThreadedBaseOutsetScrewInBase(nc, shoulder=1.5, thread_height=1.0, thread_diameter=2.8)

    array = utils.array(4, to_mm(5), [
        sib.crosssection(),
        nc.crosssection(sib.center_mate),
        nc.crosssection(sib.mate)])
    #ThreadedBaseFlat(nc, shoulder=0.5).cone_section1,
    #        ThreadedBaseFlat(nc, shoulder=0.5).cone_section2])
    utils.render_to_file(array, "test.scad")

