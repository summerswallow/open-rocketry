import os
from nosecone_library.specific_noses import BNC50J
from bodytubes.semroc import bt20, bt50, bt60
from bodytubes.modelrockets_us import _29mm
from nosecone.nosecone_bases import HollowBaseWithScrewHole

from misc.utils import render_to_file
from transitions import Transition
if __name__=="__main__":
    basedir = os.path.dirname(__file__)
    t=Transition(1.23975, bodytube1=_29mm, bodytube2=bt50, shoulder=.75, thickness = 1/16., bodytube3=bt20, open_end=True, fudge=0.02)
    render_to_file(t.transition, os.path.join(basedir,"bt50t.scad"))
    t=Transition(1.67725, bodytube1=bt60, bodytube2=_29mm, shoulder=.75, thickness = 1/16., bodytube3=bt50, open_end=True)
    render_to_file(t.transition, os.path.join(basedir,"29mmt.scad"))


    nc=BNC50J(thickness=1./16, scale_bodytube=_29mm)
    nc=HollowBaseWithScrewHole(nc, shoulder=0.75, screw_diameter=1 / 16., screw_length=0.25)
    render_to_file(nc.cone, os.path.join(basedir,"bt50n.scad"))
    nc=BNC50J(thickness=1./16, scale_bodytube=bt60)
    nc=HollowBaseWithScrewHole(nc, shoulder=0.75, screw_diameter=1 / 16., screw_length=0.25)
    render_to_file(nc.cone, os.path.join(basedir,"29mmn.scad"))


