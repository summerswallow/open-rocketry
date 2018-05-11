# ==================
#
# nosecone_threaded_bases.py
#
#   License: https://github.com/summerswallow/open-rocketry/blob/master/LICENSE
#  (c) 2018 Summer Swallow Consulting
#
# ==================

from flask import Flask
from math import sqrt, atan, acos, cos, sin, fabs, pi
import os
from solid import *
from solid.utils import up, down, left, forward

from nosecone import NoseCone, FunctionBasedNoseCone
import utils
MM2IN = 25.4


class EllipticalNoseCone(NoseCone):
    def __init__(self, length, thickness=None, **kwargs):
        super(EllipticalNoseCone, self).__init__(length, thickness, **kwargs)

        def _solid_nose(length, radius):
            return scale([1, 1, length / radius])(sphere(r=radius)) * cylinder(h=length, r=radius)

        length = self.length * MM2IN
        radius = self.outer_diameter * MM2IN / 2
        self.cone = _solid_nose(length, radius)
        if self.thickness:
            thickness = self.thickness * MM2IN
            self.cone -= _solid_nose(length - thickness, radius - thickness)


class ConicalNoseCone(NoseCone):
    def __init__(self, length, thickness=None, **kwargs):
        super(ConicalNoseCone, self).__init__(length, thickness, **kwargs)

        def _solid_nose(length, radius):
            return cylinder(h=length, r1=radius, r2=0)

        length = self.length * MM2IN
        radius = self.outer_diameter * MM2IN / 2
        nose = _solid_nose(length, radius)
        if self.thickness:
            thickness = self.thickness * MM2IN
            nose -= _solid_nose(length - thickness, radius - thickness)
        self.cone = nose


class BiconicNoseCone(NoseCone):
    def __init__(self, length, thickness=None, base_height=None, mid_diameter=None, **kwargs):
        super(BiconicNoseCone, self).__init__(length, thickness, **kwargs)

        def _solid_nose(length, radius, base_height, mid_radius):
            return cylinder(h=base_height, r1=radius, r2=mid_radius) + up(base_height)(
                cylinder(h=length - base_height, r1=mid_radius, r2=0))

        length = self.length * MM2IN
        radius = self.outer_diameter * MM2IN / 2
        base_height = base_height * MM2IN
        mid_radius = mid_diameter * MM2IN / 2
        nose = _solid_nose(length, radius, base_height, mid_radius)
        if self.thickness:
            thickness = self.thickness * MM2IN
            nose -= _solid_nose(length - thickness, radius - thickness, base_height, mid_radius - thickness)
        self.cone = nose


class BluntedConicalNoseCone(NoseCone):
    def __init__(self, length, thickness=None, blunt_radius=None, **kwargs):
        super(BluntedConicalNoseCone, self).__init__(length, thickness, **kwargs)

        def _solid_nose(length, radius, blunt_radius):
            l = length
            while True:
                x_t = l * l / radius * sqrt(blunt_radius * blunt_radius / (radius * radius + l * l))
                y_t = x_t * radius / l
                x_o = x_t + sqrt(blunt_radius * blunt_radius - y_t * y_t)
                x_a = x_o - blunt_radius
                if fabs(length - l + x_a) < self.epsilon:
                    break
                l += length - l + x_a
            return translate([0, 0, l - x_o])(sphere(r=blunt_radius)) + cylinder(h=l - x_t, r1=radius, r2=y_t)

        radius = self.outer_diameter * MM2IN / 2
        length = self.length * MM2IN
        blunt_radius = blunt_radius * MM2IN
        nose = _solid_nose(length, radius, blunt_radius)
        if self.thickness:
            thickness = self.thickness * MM2IN
            nose -= _solid_nose(length - thickness, radius - thickness, blunt_radius)
        self.cone = nose


class TangentOgiveNoseCone(NoseCone):
    def __init__(self, length, thickness=None, **kwargs):
        super(TangentOgiveNoseCone, self).__init__(length, thickness, **kwargs)

        def _2d_nosecone(length, radius):
            rho = (radius ** 2 + length ** 2) / (2. * radius)
            return translate([radius - rho, 0])(circle(r=rho)) * square(size=[radius, length])

        radius = self.outer_diameter * MM2IN / 2
        length = self.length * MM2IN
        nose = _2d_nosecone(length, radius)
        if self.thickness:
            thickness = self.thickness * MM2IN
            nose -= _2d_nosecone(length - thickness, radius - thickness)

        self.cone = rotate_extrude()(nose)


class InvertedTangentOgiveNoseCone(NoseCone):
    def __init__(self, length, thickness=None, **kwargs):
        super(InvertedTangentOgiveNoseCone, self).__init__(length, thickness, **kwargs)

        def _2d_nosecone(length, radius):
            rho = (radius ** 2 + length ** 2) / (2. * radius)
            return translate([radius, length])(rotate([0, 0, 180])(
                square(size=[radius, length]) - translate([radius - rho, 0])(circle(r=rho)) * square(
                    size=[radius, length])))

        radius = self.outer_diameter * MM2IN / 2
        length = self.length * MM2IN
        nose = _2d_nosecone(length, radius)
        if self.thickness:
            thickness = self.thickness * MM2IN
            nose -= _2d_nosecone(length - thickness, radius - thickness)

        self.cone = rotate_extrude()(nose)


class BluntedTangentOgiveNoseCone(NoseCone):
    def __init__(self, length, thickness=None, blunt_radius=None, **kwargs):
        super(BluntedTangentOgiveNoseCone, self).__init__(length, thickness, **kwargs)

        def _2d_nosecone(length, radius, blunt_radius):
            l = length
            while True:
                rho = (radius ** 2 + l ** 2) / (2. * radius)
                x_o = l - sqrt((rho - blunt_radius) ** 2 - (rho - radius) ** 2)
                x_a = x_o - blunt_radius
                y_t = (blunt_radius * (rho - radius)) / (rho - blunt_radius)
                x_t = x_o - sqrt(blunt_radius ** 2 - y_t ** 2)
                if fabs(length - l + x_a) < self.epsilon:
                    break
                l += length - l + x_a

            return union()(square(size=[radius, l - x_t]) * translate([radius - rho, 0])(circle(r=rho)),
                           translate([0, l - x_o])(square(size=blunt_radius) * circle(r=blunt_radius)))

        radius = self.outer_diameter * MM2IN / 2
        length = self.length * MM2IN
        blunt_radius = blunt_radius * MM2IN
        nose = _2d_nosecone(length, radius, blunt_radius)
        if self.thickness:
            thickness = self.thickness * MM2IN
            nose -= _2d_nosecone(length - thickness, radius - thickness, blunt_radius)
        self.cone = rotate_extrude()(nose)


class SecantOgiveNoseCone(NoseCone):
    def __init__(self, length, thickness=None, offset=.5, **kwargs):
        super(SecantOgiveNoseCone, self).__init__(length, thickness, **kwargs)

        def _2d_nosecone(length, radius, rho):
            alpha = atan(radius / length) - acos(sqrt(length * length + radius * radius) / (2 * rho))
            return translate([0, length - rho * cos(alpha)])(
                translate([rho * sin(alpha), 0])(circle(r=rho)) * translate([0, -length + rho * cos(alpha)])(
                    square(size=[rho + rho * (sin(alpha)), length])))

        radius = self.outer_diameter * MM2IN / 2
        length = self.length * MM2IN
        offset = offset * MM2IN
        rho = (radius ** 2 + length ** 2) / (2. * radius) - offset
        if sqrt(length * length + radius * radius) > 2 * rho:
            raise ValueError("Illegal Offset")

        nose = _2d_nosecone(length, radius, rho)
        if self.thickness:
            thickness = self.thickness * MM2IN
            nose -= _2d_nosecone(length - thickness, radius - thickness, rho - thickness)
        self.cone = rotate_extrude()(nose)


class ParabolicNoseCone(FunctionBasedNoseCone):
    def func(self, x, length, radius, k_factor):
        return radius * ((2. * x / length) - k_factor * x * x / length / length) / (2 - k_factor)

    def process_params(self, args):
        k_factor = args.get('k_factor', 0.5)
        if k_factor < 0.0 or k_factor > 1.0:
            raise ValueError("Illegal k_factor")
        return dict(k_factor=k_factor)


class HaackSeriesNoseCone(FunctionBasedNoseCone):
    def func(self, x, length, radius, c_factor):
        theta = acos(1 - (2 * x / length))
        return (radius / sqrt(pi)) * sqrt(theta - (sin(2 * theta) / 2) + c_factor * sin(theta) ** 3)

    def process_params(self, args):
        return dict(c_factor=args.get('c_factor', 0.3))


class PowerSeriesNoseCone(FunctionBasedNoseCone):
    def func(self, x, length, radius, exponent):
        return radius * pow((x / length), exponent)
        radius = self.outer_diameter * MM2IN / 2
        length = self.length * MM2IN

    def process_params(self, args):
        exponent = args.get('exponent', 0.3)
        if exponent <= 0.0 or exponent > 1.0:
            raise ValueError("Illegal exponent value")
        return dict(exponent=exponent)

    def cross_section(self, object):
        size = (self.length + self.outer_diameter) * 2 * MM2IN
        return object * forward(size / 2)(cube(size, center=True));


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
