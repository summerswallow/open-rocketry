# ==================
#
# retainer.py
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

from solid import difference, cylinder, square, sphere, circle, rotate_extrude, rotate, union, cube
from solid.utils import up, right

from misc import utils
from misc.threaded import Threaded
from misc.utils import to_mm
from math import sqrt

class Coupler(Threaded):
    def __init__(self, height, thickness, threads_per_inch, **kwargs):
        height = to_mm(height)
        threads_per_inch = threads_per_inch
        o_d = kwargs.get('outer_diameter',1)
        i_d = kwargs.get('inner_diameter')

        tooth = to_mm(1. / threads_per_inch * sqrt(3) / 2.)

        if 'bodytube' in kwargs:
            i_d = kwargs['bodytube'].inner_diameter

        if 'inner_bodytube' in kwargs:
            o_d = kwargs['inner_bodytube'].outer_diameter

        i_d -= kwargs.get('fudge_inner',0.0)
        o_d += kwargs.get('fudge_outer',0.0)
        if 'fudge' in kwargs:
            i_d -= kwargs.get('fudge')
            o_d += kwargs.get('fudge')

        i_r = to_mm(i_d/2.)
        o_r = to_mm(o_d/2.)

        self.male=union() (cylinder(h=height/2, r=i_r), 
                           self.threaded_male_column(height, 
                                                     i_r * 2 - thickness - tooth, threads_per_inch))
        if o_r:
            self.male -= cylinder(h=height, r=o_r)

        self.female= difference() (cylinder(h=height/2, r=i_r), 
                           self.threaded_female_column(height, 
                                                       i_r * 2 - thickness -tooth, threads_per_inch))
        self._o_r=o_r
        self._i_r=i_r
        
        
    def fittest(self, height=.125):
        return cylinder(h=to_mm(height), r=self._i_r)-cylinder(h=to_mm(height), r=self._o_r)

