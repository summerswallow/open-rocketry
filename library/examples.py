from nosecone.standard_nosecones import *
from misc import utils
if __name__ == '__main__':
    from bodytubes.semroc import bt20
    from bodytubes.semroc import bt5
    array = utils.array(4, MM2IN, [
        InvertedTangentOgiveNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                                     mid_diameter=.3),
        EllipticalNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                           mid_diameter=.3),
        ConicalNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125, mid_diameter=.3),
        BiconicNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125, mid_diameter=.3),
        ParabolicNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                          mid_diameter=.3),
        HaackSeriesNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                            mid_diameter=.3),
        PowerSeriesNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                            mid_diameter=.3),
        BluntedConicalNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                               mid_diameter=.3),
        TangentOgiveNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                             mid_diameter=.3),
        BluntedTangentOgiveNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                                    mid_diameter=.3),
        SecantOgiveNoseCone(0.75, bodytube=bt5, thickness=1 / 16.0, base_height=0.25, blunt_radius=0.125,
                            mid_diameter=.3)])

    utils.render_to_file(array, "examples/standard_nosecones.scad")

