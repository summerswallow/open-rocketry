from solid import cylinder, scad_render, translate, union


def to_mm(v, default=None):
    if v is None:
        if default is None:
            raise ValueError("Value must be integer")
        v = default
    return v * 25.4


def to_inch(v, default=None):
    if v is None:
        if default is None:
            raise ValueError("Value must be integer")
        v = default
    return v / 25.4


def disk(diameter, thickness):
    return cylinder(h=thickness * 25.4, r=diameter * 25.4 / 2.0)


def render(object):
    scad = scad_render(object)
    lines = scad.split("\n")
    count = 0
    for each in lines:
        if each.startswith('use') or each.startswith('import'):
            count += 1
        else:
            break
    return '\n'.join(lines[0:count] + ['$fn=100;'] + lines[count:])


def render_to_file(object, file_):
    with open(file_, "w") as f:
        f.write(render(object))


def array(width, space, cones):
    ix = 0
    iy = 0
    array = []
    for each in cones:
        array.append(translate([ix * space, iy * space, 0])(each.cone))
        ix += 1
        if ix >= width:
            iy += 1
            ix = 0
    return union()(*array)


def array_crosssection(width, space, cones, angle=0):
    ix = 0
    iy = 0
    array = []
    for each in cones:
        if hasattr(each, 'crosssection'):
            array.append(translate([ix * space, iy * space, 0])(each.crosssection(angle)))
        else:
            array.append(translate([ix * space, iy * space, 0])(each))
        ix += 1
        if ix >= width:
            iy += 1
            ix = 0
    return union()(*array)


class AbstractClassError(Exception):
    pass
