from nosecone.standard_nosecones import EllipticalNoseCone, TangentOgiveNoseCone
from nosecone.nosecone_bases import HollowBase
from nosecone.nosecone_threaded_bases import ThreadedBaseOutset
from bodytubes import *
from misc import utils


class BNC20B(EllipticalNoseCone):
    def __init__(self, shoulder=0.5, thickness=None, **kwargs):
        super(BNC20B, self).__init__(length=1.7, shoulder=shoulder, bodytube=estes.bt20, thickness=thickness, **kwargs)


class BNC5V(EllipticalNoseCone):
    def __init__(self, shoulder=0.5, thickness=None, **kwargs):
        super(BNC5V, self).__init__(length=0.75, shoulder=shoulder, bodytube=estes.bt5, thickness=thickness, **kwargs)


class BNC50J(EllipticalNoseCone):
    def __init__(self, shoulder=0.5, thickness=None, **kwargs):
        super(BNC50J, self).__init__(length=1.37, shoulder=shoulder, bodytube=estes.bt50, thickness=thickness, **kwargs)

class BNC50K(TangentOgiveNoseCone):
    def __init__(self, shoulder=0.5, thickness=None, **kwargs):
        super(BNC50K, self).__init__(length=2.75, shoulder=shoulder, bodytube=estes.bt50, thickness=thickness, **kwargs)


if __name__ == '__main__':
    # Upscale Mosquito
    utils.render_to_file(ThreadedBaseOutset(BNC5V(thickness=3 / 32., scale_bodytube=loc_precision._3_00), shoulder=1.5).cone,
                         "mos.scad")
    utils.render_to_file(ThreadedBaseOutset(BNC5V(thickness=3 / 32., scale_bodytube=loc_precision._3_00), shoulder=1.5).mate,
                         "mos2.scad")
