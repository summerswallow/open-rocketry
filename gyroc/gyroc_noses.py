from nosecone_library.specific_noses import BNC20B
from bodytubes.semroc import bt5, bt2, bt50, bt30, bt55
from misc import utils
from nosecone.nosecone_bases import HollowBase
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

