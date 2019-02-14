from misc import utils
from nosecone.nosecone_bases import HollowBaseWithScrewHole
from nosecone_library.specific_noses import BNC50K

nc = BNC50K(thickness=1. / 16.)
ar = HollowBaseWithScrewHole(nc, shoulder=0.5, screw_diameter=1 / 16., screw_length=0.25),
utils.render_to_file(
    HollowBaseWithScrewHole(BNC50K(thickness=3 / 32.), shoulder=0.5, screw_length=0.3, screw_diameter=7 / 64.0).cone,
    "test.scad")
