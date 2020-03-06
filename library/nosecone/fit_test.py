from .nosecone_bases import HollowBase
from .standard_nosecones import CylindricalNoseCone
class NoseConeFitTest(HollowBase):
    def __init__(self,length, thickness=1/16.0, **kwargs):
        nc = CylindricalNoseCone(length, thickness, open_top=True, **kwargs)
        super(NoseConeFitTest, self).__init__(nc, shoulder=length)