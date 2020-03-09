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

<<<<<<< Updated upstream:library/other_parts/coupler.py

        i_d -= kwargs.get('fudge_inner',0.0)
        o_d += kwargs.get('fudge_outer',0.0)
=======
        if 'fudge' in kwargs:
            i_d -= kwargs.get('fudge')
            o_d += kwargs.get('fudge')
>>>>>>> Stashed changes:other_parts/coupler.py

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
        
        self.fittest = cylinder(h=to_mm(.25), r=i_r)-cylinder(h=to_mm(.25), r=o_r)
from bodytubes.modelrockets_us import _29mm
from bodytubes.semroc import bt50, bt20, bt5

#utils.render_to_file(Coupler(2, bodytube=bt50, threads_per_inch=6, inner_bodytube=bt5, thickness=1 / 16., fudge=0.01).male, "test.scad")
#utils.render_to_file(Coupler(2, bodytube=bt50, threads_per_inch=6, inner_bodytube=bt5, thickness=1 / 16., fudge=0.01).female, "test2.scad")
#utils.render_to_file(Coupler(2, bodytube=_29mm, threads_per_inch=10, inner_bodytube=bt20, thickness=1 / 16.).male, "test.scad")
#utils.render_to_file(Coupler(2, bodytube=_29mm, threads_per_inch=10, inner_bodytube=bt20, thickness=1 / 16.).female, "test2.scad")
<<<<<<< Updated upstream:library/other_parts/coupler.py
utils.render_to_file(Coupler(2, bodytube=_29mm, threads_per_inch=10, inner_bodytube=bt20, thickness=1 / 16.,fudge=0.01).fittest, "29_fit.scad")
utils.render_to_file(Coupler(2, bodytube=bt50, threads_per_inch=6, inner_bodytube=bt5, thickness=1 / 16., fudge=0.01).fittest, "bt50_fit.scad")

utils.render_to_file(Coupler(2, bodytube=bt20, threads_per_inch=20, inner_bodytube=bt5, thickness=1 / 16., fudge=0.01).fittest, "bt20_fit.scad")

=======
utils.render_to_file(Coupler(2, bodytube=_29mm, threads_per_inch=10, inner_bodytube=bt20, thickness=1 / 16.,fudge=0.015).fittest, "29_fit.scad")
utils.render_to_file(Coupler(2, bodytube=bt50, threads_per_inch=6, inner_bodytube=bt5, thickness=1 / 16., fudge=0.015).fittest, "bt50_fit.scad")
>>>>>>> Stashed changes:other_parts/coupler.py

utils.render_to_file(Coupler(2, bodytube=bt20, threads_per_inch=20, inner_bodytube=bt5, thickness=1 / 16., fudge=0.015).fittest, "bt20_fit.scad")
