from nosecone_library.specific_noses import BNC20B
from bodytubes.semroc import bt5, bt2, bt50, bt30, bt55, bt60,bt70, bt80

from misc import utils
from nosecone.nosecone_bases import HollowBase
from nosecone.nosecone_threaded_bases import ScrewInBase, ThreadedBaseOutsetScrewInBase
import os

basedir = os.path.dirname(__file__)

nc = BNC20B(scale_bodytube=bt2, thickness = 1/16., shoulder=0.5)
nc = HollowBase(nc, shoulder=0.25)
utils.render_to_file(nc.cone, os.path.join(basedir, "nosecones", "bt2_nose.scad"))
nc = BNC20B(scale_bodytube=bt5, thickness = 1/16., shoulder=0.5)
nc = HollowBase(nc, shoulder=0.375)
utils.render_to_file(nc.cone, os.path.join(basedir, "nosecones", "bt5_nose.scad"))
nc = BNC20B(thickness = 1/16.)
nc = HollowBase(nc, shoulder=0.5)
utils.render_to_file(nc.cone, os.path.join(basedir, "nosecones", "bt20_nose.scad"))
nc = BNC20B(scale_bodytube=bt30, thickness = 1/16., shoulder=0.5)
nc = HollowBase(nc, shoulder=0.5625)
utils.render_to_file(nc.cone, os.path.join(basedir, "nosecones", "bt30_nose.scad"))
nc = BNC20B(scale_bodytube=bt50, thickness = 1/16., shoulder=0.5)
nc = HollowBase(nc, shoulder=0.625)
utils.render_to_file(nc.cone, os.path.join(basedir, "nosecones", "bt50_nose.scad"))
nc = BNC20B(scale_bodytube=bt55, thickness = 1/16., shoulder=0.5)
nc = HollowBase(nc, shoulder=0.75)
utils.render_to_file(nc.cone, os.path.join(basedir, "nosecones", "bt55_nose.scad"))
nc = BNC20B(scale_bodytube=bt60, thickness = 5/64., shoulder=0.5)
nc = ScrewInBase(nc, shoulder=0.75, thread_height=.375, thread_diameter=1.5, threads_per_inch=10)
utils.render_to_file(nc.cone,os.path.join(basedir, "nosecones", "bt60_nose.scad"))
utils.render_to_file(nc.mate, os.path.join(basedir, "nosecones", "bt60_nose_base.scad"))
nc = BNC20B(scale_bodytube=bt70, thickness = 5/64., shoulder=0.5)
nc = ScrewInBase(nc, shoulder=1.0, thread_height=.5, thread_diameter=bt70.inner_diameter-.1, threads_per_inch=10)
utils.render_to_file(nc.cone,os.path.join(basedir, "nosecones", "bt70_nose.scad"))
utils.render_to_file(nc.mate, os.path.join(basedir, "nosecones", "bt70_nose_base.scad"))
nc = BNC20B(scale_bodytube=bt80, thickness = 3/32, shoulder=0.5)
nc = ThreadedBaseOutsetScrewInBase(nc, shoulder=1.0, thread_height=.5, thread_diameter=bt80.inner_diameter-.15, lower_tpi=6, upper_tpi=8)
utils.render_to_file(nc.cone,os.path.join(basedir, "nosecones", "bt80_nose.scad"))
utils.render_to_file(nc.center_mate, os.path.join(basedir, "nosecones", "bt80_nose_center.scad"))
utils.render_to_file(nc.mate, os.path.join(basedir, "nosecones", "bt80_nose_base.scad"))
nc = BNC20B(scale_bodytube=bt80, thickness = 3/32, shoulder=0.5)
nc = ThreadedBaseOutsetScrewInBase(nc, shoulder=1.0, thread_height=.5, thread_diameter=bt80.inner_diameter-.15, lower_tpi=6, upper_tpi=8)
utils.render_to_file(nc.crosssection(nc.cone),os.path.join(basedir, "nosecones", "bt80_nose.scad"))
utils.render_to_file(nc.crosssection(nc.center_mate), os.path.join(basedir, "nosecones", "bt80_nose_center.scad"))
utils.render_to_file(nc.crosssection(nc.mate), os.path.join(basedir, "nosecones", "bt80_nose_base.scad"))
