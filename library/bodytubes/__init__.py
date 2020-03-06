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
        
from . import estes
from . import loc_precision

