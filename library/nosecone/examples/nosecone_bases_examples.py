""" Generate Examples"""
from nosecone.standard_nosecones import EllipticalNoseCone
from nosecone.nosecone_threaded_bases import *
from nosecone.nosecone_bases import *
from misc import utils
from bodytubes.semroc import bt5


if __name__ == '__main__':

    nc = EllipticalNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                            mid_diameter=.3)

    array = utils.array_crosssection(4, utils.to_mm(1), [
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
