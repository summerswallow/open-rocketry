# ==================
#
# shear_nosecones.py
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

from solid import multmatrix

import utils
from nosecone import DerivativeNoseCone
from utils import to_mm


class ShearNoseCone(DerivativeNoseCone):
    def __init__(self, cone, x_shear, y_shear):
        super(DerivativeNoseCone, self).__init__(length=cone.length, thickness=cone.thickness,
                                                 outer_diameter=cone.outer_diameter, inner_diameter=cone.inner_diameter)
        shear_matrix = [[1, 0, x_shear / cone.length, 0],

                        [0, 1, y_shear / cone.length, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 1]];
        self.cone = multmatrix(shear_matrix)(cone.cone)


if __name__ == '__main__':
    from standard_nosecones import EllipticalNoseCone, ConicalNoseCone, TangentOgiveNoseCone
    from bodytubes import semroc_bt5 as bt5

    utils.render_to_file(utils.array(2, to_mm(1), [
        ShearNoseCone(EllipticalNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .25, .1),
        ShearNoseCone(ConicalNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .25, .1),
        ShearNoseCone(ConicalNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .25, 0),
        ShearNoseCone(TangentOgiveNoseCone(length=.75, bodytube=bt5, thickness=1 / 16.), .25, 0)]),
                         "examples/shear_nosecones.scad")
