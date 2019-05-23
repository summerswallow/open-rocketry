# ==================
#
# retainer.py
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

from solid import difference, cylinder, square, sphere, circle, rotate_extrude, rotate, union
from solid.utils import up, right

from misc import utils
from misc.threaded import Threaded
from misc.utils import to_mm


class Retainer(Threaded):
    def __init__(self, retainer_diameter, height, depth, threads_per_inch, cap_diameter, hole_diameter, cap_thickness,**kwargs):
        r_r = to_mm(retainer_diameter/2.)
        height = to_mm(height)
        h_r = to_mm(hole_diameter/2.)
        c_r = to_mm(cap_diameter/2.)
        c_t = to_mm(cap_thickness)
        threads_per_inch = threads_per_inch
        o_d = kwargs.get('outer_diameter')
        i_d = kwargs.get('inner_diameter')

        if 'bodytube' in kwargs:
            o_d = kwargs['bodytube'].outer_diameter
            i_d = kwargs['bodytube'].inner_diameter

        print i_d
        i_r = to_mm(i_d/2.)
        o_r = to_mm(o_d/2.)

        print retainer_diameter
        flange_d = to_mm(kwargs.get('flange_diameter'), safe=True)
        flange_t = to_mm(kwargs.get('flange_thickness'), safe=True)
        
        spine_diameter = to_mm(kwargs.get('spine_diameter'), safe=True)

        round_radius = to_mm(kwargs.get('round_radius',0))

        if flange_d and flange_t:
            flange = cylinder(h=flange_t, r=flange_d/2.)
        else:
            flange = cylinder(h=height, r=o_r/2.)  # HACK because this will be removed

        self.retainer = difference() (self.threaded_male_column(height, to_mm(retainer_diameter), threads_per_inch) + flange,
                                      cylinder(h=height, r=o_r),
                                      up(height-depth), cylinder(h=depth, r=i_r))
        
        self.cap = difference()(cylinder(h=height,r=c_r),
                                self.threaded_female_column(height-c_t, to_mm(retainer_diameter), threads_per_inch),
                                cylinder(h=height, r=h_r))

        if spine_diameter:
            no_spines = kwargs.get('spines',0)
            spines = []
            for idx in xrange(0, no_spines):
                spines.append(rotate([0,0,360/no_spines*idx])(right(c_r)(cylinder(h=height-c_t-spine_diameter/2, r=spine_diameter/2)+
                                  up(height-c_t-spine_diameter/2)(sphere(r=spine_diameter/2.)))))
            self.cap+=union()(*spines)

        self.round = rotate_extrude()(right(c_r-round_radius)(square([round_radius,round_radius])*circle(round_radius)))
        self.cap -= up(height-round_radius)(rotate_extrude()(right(c_r-round_radius)(square([round_radius,round_radius]))))
        self.cap += up(height-round_radius)(self.round)

from bodytubes.modelrockets_us import _29mm

utils.render_to_file(Retainer(2, 1, depth=.875, bodytube=_29mm, threads_per_inch=6, cap_diameter=2.25, flange_diameter=4, flange_thickness=1 / 16., hole_diameter=.5, cap_thickness=1 / 16., spine_diameter=1 / 8., round_radius=1 / 16., spines=12).retainer, "test.scad")

