# ==================
#
# bodytubes
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

class BodyTube(object):
    def __init__(self, od, id_, name=None):
        self.outer_diameter = float(od)
        self.inner_diameter = float(id_)
        self.name=name
        assert(od>id_)
        
class LaunchLug(BodyTube):
    pass

from . import estes
from . import loc_precision

from .semroc import bt20, bt2, bt50, bt30, bt40, bt55, bt5, bt55, bt60, bt80, bt70
from .balsa_machining import t300
from .modelrockets_us import _3_00, _3_90, _5_38
standard_tube_sizes=[bt2, bt5, bt20, bt50, bt55, bt60, bt70, bt80, t300, _3_00, _3_90, _5_38]
