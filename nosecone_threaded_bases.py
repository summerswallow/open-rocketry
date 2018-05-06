import os
from math import sqrt

import solid
from solid import *
from solid.utils import down

from nosecone import NoseConeWithBase
from utils import to_mm, to_inch


class EnglishThread(solid.IncludedOpenSCADObject):
    """ Hacky Connector for threads.scad library.
        "use" doesn't survive imports welll"""

    """ This requires the thread library found at http://dkprojects.net/openscad-threads/ """

    def __init__(self, diameter=None, threads_per_inch=None, length=None, internal=None, n_starts=None,
                 thread_size=None, groove=None, square=None, rectangle=None, angle=None, taper=None, leadin=None,
                 **kwargs):
        super(EnglishThread, self).__init__('english_thread',
                                            {'diameter': diameter, 'threads_per_inch': threads_per_inch,
                                              'length': length, 'internal': internal, 'n_starts': n_starts,
                                              'thread_size': thread_size, 'groove': groove, 'square': square,
                                              'rectangle': rectangle, 'angle': angle, 'taper': taper,
                                              'leadin': leadin, },
                                            include_file_path=os.path.join(os.environ.get("OPENSCAD_LIBRARY", "."),
                                                                            "threads.scad"),
                                            use_not_include=True, **kwargs)


class ThreadedBase(NoseConeWithBase):
    """ You can refactor this to use a different thread library"""

    def threaded_male_column(self, length, diameter, threads_per_inch):
        return EnglishThread(length=to_inch(length), diameter=to_inch(diameter), threads_per_inch=threads_per_inch)

    def threaded_female_column(self, length, diameter, threads_per_inch):
        return EnglishThread(length=to_inch(length), diameter=to_inch(diameter),
                             threads_per_inch=threads_per_inch, internal=True)


class ThreadedBaseFlat(ThreadedBase):
    def __init__(self, cone, shoulder=None, thickness=None, threads_per_inch=6):
        super(ThreadedBaseFlat, self).__init__(cone, shoulder, thickness)
        shoulder = to_mm(self.shoulder)
        thickness = to_mm(self.thickness)
        radius = to_mm(cone.inner_diameter / 2.)
        tooth = to_mm(1. / threads_per_inch * sqrt(3) / 2.)

        self.cone = cone.cone + self.slice(cone.cone, self.thickness) + down(shoulder)(
            self.threaded_male_column(length=shoulder,
                                      diameter=radius * 2 - thickness * 2,
                                      threads_per_inch=threads_per_inch)) \
                    - down(shoulder - thickness)(cylinder(h=shoulder + thickness, r=radius - thickness - tooth))
        self.mate = down(shoulder)(cylinder(h=shoulder, r=radius)) \
                    - down(shoulder)(
            self.threaded_female_column(length=shoulder + thickness, diameter=radius * 2 - thickness * 2,
                                        threads_per_inch=threads_per_inch))


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
