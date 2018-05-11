# ==================
#
# bodytubes
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

class BodyTube(object):
    def __init__(self, od, id_):
        self.outer_diameter = float(od)
        self.inner_diameter = float(id_)
        assert(od>id_)

import apogee
import balsa_machining
import estes
import loc_precision
import modelrockets_us
import semroc
