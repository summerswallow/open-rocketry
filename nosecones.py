from flask import Flask
from solid import *
from solid.utils import up, down, left, forward
from bodytubes import semroc_bt5 as bt5
from bodytubes import semroc_bt20 as bt20
from math import sqrt, atan, acos, cos, sin, fabs, pi
import os
def use_lib(x):
    use(os.path.join("/Users/hlu/Documents/OpenSCAD/libraries/",x+".scad"))

use_lib("threads")
use_lib("pipe")
MM2IN=25.4

def disk(diameter, thickness):
    return cylinder(h=thickness*25.4, r=diameter*25.4/2.0)

class NoseCone(object):
    epsilon = 0.001
    resolution=50
    def __init__(self, type_, length, shoulder=None, thickness=None, **kwargs):
        if 'outer_diameter' in kwargs:
            self.outer_diameter = kwargs['outer_diameter']
            
        if 'inner_diameter' in kwargs:
            self.inner_diameter = kwargs['inner_diameter']
            
        if 'bodytube' in kwargs:
            self.outer_diameter = kwargs['bodytube'].outer_diameter
            self.inner_diameter = kwargs['bodytube'].inner_diameter
            
        self.thickness = thickness

        self.length=length
        self.shoulder=shoulder
        if type_== "elliptical":
            self.cone = self.elliptical_nosecone()

        if type_ == "conical":
            self.cone = self.conical_nosecone()

        if type_ == "blunted_conical":
            self.cone = self.blunted_conical_nosecone(kwargs['blunt_radius'])

        if type_ == "biconic":
            self.cone = self.biconic_nosecone(kwargs['base_height'],kwargs['mid_radius'])

        if type_ == "tangent_ogive":
            self.cone = self.tangent_ogive_nosecone()

        if type_ == "blunted_tangent_ogive":
            self.cone = self.blunted_tangent_ogive_nosecone(kwargs['blunt_radius'])

        if type_ == "secant_ogive":
            self.cone = self.secant_ogive_nosecone(kwargs['offset'])

        if type_ == "parabolic":
            self.cone = self.parabolic_nosecone(kwargs.get('k_factor', 0.5))

        if type_ == "haack_series":
            self.cone = self.haack_series_nosecone(kwargs.get('c_factor', 0.3))

        if type_ == "power_series":
            self.cone = self.power_series_nosecone(kwargs.get('exponent', 0.3))

    def elliptical_nosecone(self):
        def _solid_nose(length, radius):
            return scale([1,1,length/radius])(sphere(r=radius)) * cylinder(h=length, r=radius)

        length = self.length*MM2IN
        radius = self.outer_diameter*MM2IN/2
        nose = _solid_nose(length, radius)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _solid_nose(length-thickness, radius-thickness)
        return nose

    def conical_nosecone(self):
        def _solid_nose(length, radius):
            return cylinder(h=length, r1=radius, r2=0)

        length = self.length*MM2IN
        radius = self.outer_diameter*MM2IN/2
        nose = _solid_nose(length, radius)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _solid_nose(length-thickness, radius-thickness)
        return nose

    def biconic_nosecone(self, base_height, mid_diameter):
        def _solid_nose(length, radius, base_height, mid_radius):
            return cylinder(h=base_height, r1=radius, r2=mid_radius) + up(base_height)(cylinder(h=length-base_height, r1=mid_radius, r2=0))
        
        length = self.length*MM2IN
        radius = self.outer_diameter*MM2IN/2
        base_height = base_height*MM2IN
        mid_radius = mid_diameter*MM2IN/2
        nose = _solid_nose(length, radius, base_height, mid_radius)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _solid_nose(length-thickness, radius-thickness, base_height, mid_radius-thickness)
        return nose


    def blunted_conical_nosecone(self, r_nose):
        def _solid_nose(length, radius, r_nose):
            l=length
            while True:
                x_t = l*l/radius*sqrt(r_nose*r_nose/(radius*radius+l*l))
                y_t = x_t*radius/l
                x_o = x_t + sqrt(r_nose*r_nose - y_t * y_t)
                x_a = x_o - r_nose
                if fabs(length-l+x_a)<self.epsilon:
                    break
                l += length-l+x_a
            return translate([0, 0, l-x_o]) (sphere(r=r_nose)) + cylinder(h=l-x_t, r1=radius, r2=y_t)
            
        radius=self.outer_diameter*MM2IN/2
        length=self.length*MM2IN
        r_nose = r_nose * MM2IN
        nose = _solid_nose(length, radius, r_nose)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _solid_nose(length-thickness, radius-thickness, r_nose)
        return nose

    def tangent_ogive_nosecone(self):
        def _2d_nosecone(length, radius):
            rho = (radius**2 + length**2) / (2. * radius)
            return translate([radius-rho, 0])(circle(r=rho))*square(size=[radius, length])

        radius=self.outer_diameter*MM2IN/2
        length=self.length*MM2IN
        nose = _2d_nosecone(length, radius)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _2d_nosecone(length-thickness, radius-thickness)
        
        return rotate_extrude()(nose)

    def blunted_tangent_ogive_nosecone(self,r_nose):
        def _2d_nosecone(length, radius,r_nose):
            l=length
            while True:
                rho = (radius**2 + l**2) / (2. * radius)
                x_o = l - sqrt((rho - r_nose)**2 - (rho - radius)**2)
                x_a = x_o - r_nose
                y_t = (r_nose * (rho - radius)) / (rho - r_nose)
                x_t = x_o - sqrt(r_nose**2- y_t**2)
                if fabs(length-l+x_a)<self.epsilon:
                    break
                l += length-l+x_a
                
            return union()(square(size=[radius, l-x_t]) * translate([radius-rho, 0])(circle(r=rho)),
                           translate([0, l-x_o])(square(size=r_nose)*circle(r=r_nose)))

        radius=self.outer_diameter*MM2IN/2
        length=self.length*MM2IN
        r_nose = r_nose * MM2IN
        nose = _2d_nosecone(length, radius, r_nose)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _2d_nosecone(length-thickness, radius-thickness, r_nose)
        return rotate_extrude()(nose)


    def secant_ogive_nosecone(self, offset=0):
        def _2d_nosecone(length, radius, rho):
            alpha = atan(radius/length) -  acos(sqrt(length*length + radius*radius) / (2*rho))
            return translate([0,length-rho*cos(alpha)])(
                translate([rho*sin(alpha),0])(circle(r=rho))*translate([0,-length+rho*cos(alpha)])(square(size=[rho+rho*(sin(alpha)), length])))
        
        radius=self.outer_diameter*MM2IN/2
        length=self.length*MM2IN
        offset=offset*MM2IN
        rho = (radius**2 + length**2) / (2. * radius) - offset
        if "error_condition_check":
            "add error"
        nose = _2d_nosecone(length, radius, rho)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _2d_nosecone(length-thickness, radius-thickness, rho-thickness)
        return rotate_extrude()(nose)


    def parabolic_nosecone(self, k_factor):
        def _2d_nosecone(length, radius, k_factor=0.5):
            def f(x):
                return radius * ((2. * x/ length) - k_factor * x*x /length/length)/(2-k_factor)
            return polygon([[0,0]]+[[f(length*float(x)/self.resolution),length-length*float(x)/self.resolution] for x in xrange(0, self.resolution+1)])
        if k_factor <0.0 or k_factor>1.0:
            raise ValueError("Illegal k value")

        radius=self.outer_diameter*MM2IN/2
        length=self.length*MM2IN
        nose = _2d_nosecone(length, radius, k_factor)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _2d_nosecone(length-thickness, radius-thickness, k_factor)
        return rotate_extrude()(nose)

    def haack_series_nosecone(self, c_factor):
        def _2d_nosecone(length, radius, c_factor):
            def f(x):
                theta = acos(1 - (2 * x / length))
                return (radius / sqrt(pi)) * sqrt(theta - (sin(2 * theta) / 2) + c_factor * sin(theta)**3)
            return polygon([[0,0]]+[[f(length*float(x)/self.resolution),length-length*float(x)/self.resolution] for x in xrange(0, self.resolution+1)])

        radius=self.outer_diameter*MM2IN/2
        length=self.length*MM2IN
        nose = _2d_nosecone(length, radius, c_factor)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _2d_nosecone(length-thickness, radius-thickness, c_factor)
        return rotate_extrude()(nose)
    def power_series_nosecone(self, exponent):
        def _2d_nosecone(length, radius, exponent):
            def f(x):
                return radius * pow((x / length), exponent)
            return polygon([[0,0]]+[[f(length*float(x)/self.resolution),length-length*float(x)/self.resolution] for x in xrange(0, self.resolution+1)])

        radius=self.outer_diameter*MM2IN/2
        length=self.length*MM2IN
        if exponent <=0.0 or exponent>1.0:
            raise ValueError("Illegal k value")

        nose = _2d_nosecone(length, radius, exponent)
        if self.thickness:
            thickness = self.thickness*MM2IN
            nose -= _2d_nosecone(length-thickness, radius-thickness, exponent)
        return rotate_extrude()(nose)


    def slice(self, thickness, offset=0):
        return  hull()(self.cone * up(offset)(disk(self.outer_diameter*3, self.thickness)))
        return  self.cone * up(offset)(disk(self.outer_diameter, self.thickness)) + up(offset)(disk(self.outer_diameter-self.thickness, self.thickness))

    def render(self):
        self.cone.params['segments']=200
        scad_render(self.cone)

    def render_to_file(self, file_):
        self.cone.params['segments']=200
        scad_render_to_file(self.cone, file_)

    def threaded_male_column(self, length, diameter, threads_per_inch):
        length/=MM2IN
        diameter/=MM2IN
        return english_thread(length=length, diameter=diameter, threads_per_inch=threads_per_inch)

    def threaded_female_column(self, length, diameter, threads_per_inch):
        length/=MM2IN
        diameter/=MM2IN
        return english_thread(length=length, diameter=diameter, threads_per_inch=threads_per_inch, internal=True)

    """

module hollow_base_threaded_mate_V1(diameter, shoulder, thickness, tpi) 
{
   radius = diameter*MM2IN/2
    shoulder = shoulder*MM2IN
    thickness = thickness *MM2IN
    translate([0,0, -shoulder]) 
    difference () {
        cylinder(h=shoulder-thickness, r1=radius, r2=radius)
    english_thread(length=shoulder/MM2IN-thickness/MM2IN, diameter=diameter-thickness/MM2IN, threads_per_inch=tpi, internal=true)
    }
}
"""

    def render_threaded_base(self, file_, shoulder, tpi):
        out = self.cone + hollow_base_threaded(self.inner_diameter, shoulder, self.thickness, tpi=tpi) + self.slice(self.thickness)
        scad_render_to_file(out, file_)

    def render_threaded_base_mate(self, file_, shoulder, tpi):
        out = hollow_base_threaded_mate(self.inner_diameter, shoulder, self.thickness, tpi=tpi)
        scad_render_to_file(out, file_)

    def render_threaded_base_inset(self, file_, shoulder, tpi):
        out = self.cone + hollow_base_threaded_V1(self.inner_diameter, shoulder, self.thickness, tpi=tpi)
        scad_render_to_file(out, file_)

    def render_threaded_base_inset_mate(self, file_, shoulder, tpi):
        out = hollow_base_threaded_mate_V1(self.inner_diameter, shoulder, self.thickness, tpi=tpi)
        scad_render_to_file(out, file_)

    def nose_with_solid_base(self, **kwargs):
        shoulder = kwargs.get("shoulder", self.shoulder) * MM2IN
        thickness = kwargs.get("thickness", self.thickness) *MM2IN
        radius = self.inner_diameter *MM2IN/2
        return down(shoulder)(cylinder(h=thickness, r=radius))

    def hollow_base(self, radius, shoulder, thickness):
        return down(shoulder)(cylinder(h=shoulder, r=radius))-down(shoulder-thickness)(cylinder(h=shoulder-thickness, r=radius-thickness))

    def nose_with_hollow_base(self, **kwargs):
        shoulder = kwargs.get("shoulder", self.shoulder) * MM2IN
        thickness = kwargs.get("thickness", self.thickness) *MM2IN
        radius = self.inner_diameter *MM2IN/2
        return self.hollow_base(radius, shoulder, thickness)

    def nose_with_open_hollow_base(self, **kwargs):
        shoulder = kwargs.get("shoulder", self.shoulder) * MM2IN
        thickness = kwargs.get("thickness", self.thickness) *MM2IN
        radius = self.inner_diameter *MM2IN/2
        return down(shoulder)(cylinder(h=shoulder, r=radius))-down(shoulder)(cylinder(h=shoulder, r=radius-thickness))

    def hollow_base_and_cutout(self, radius, shoulder, thickness, cutout_length, cutout_width):
        chord = sqrt(radius * radius - (radius-cutout_width**2))

        return difference () (union () (self.hollow_base(radius, shoulder, thickness),
                                 down(shoulder-cutout_length)(cylinder(h=thickness, r=radius)),
                                 intersection ()(translate([radius-cutout_width-thickness,-chord,-shoulder])(cube([thickness, 
                                                                                                                   chord*2, 
                                                                                                                   cutout_length])),
                                                 down(shoulder)(cylinder(h=shoulder , r=radius)))),
                       translate([radius-cutout_width, -radius,-shoulder-1])(cube([cutout_width, 2*radius, cutout_length+1])))


    def nose_with_hollow_base_and_cutout(self, **kwargs):
        cutout_length = kwargs.get("cutout_length", self.shoulder/2.0) *MM2IN
        cutout_width = kwargs.get("cutout_width", self.inner_diameter * 0.3) *MM2IN
        shoulder = kwargs.get("shoulder", self.shoulder) * MM2IN
        thickness = kwargs.get("thickness", self.thickness) *MM2IN
        radius = self.inner_diameter *MM2IN/2
    
        return self.hollow_base_and_cutout(radius, shoulder, thickness, cutout_length, cutout_width)

    def nose_with_hollow_base_and_elbow(self, **kwargs):
        cutout_length = kwargs.get("cutout_length", self.shoulder/2.0) *MM2IN
        cutout_width = kwargs.get("cutout_width", self.inner_diameter * 0.3) *MM2IN
        shoulder = kwargs.get("shoulder", self.shoulder) * MM2IN
        thickness = kwargs.get("thickness", self.thickness) *MM2IN
        elbow_radius = kwargs.get("elbow_radius", self.thickness/2.) *MM2IN
        radius = self.inner_diameter *MM2IN/2
        return union() (self.hollow_base_and_cutout(radius, shoulder, thickness, cutout_length, cutout_width),
                        translate([radius-cutout_width,0, -shoulder +cutout_length/2])(elbow(elbow_radius, 0, 1, cutout_width/2, cutout_length/2+thickness)))

    def _donut(self, radius, big_radius):
        return down(big_radius+radius)(rotate([90,0,0, 0])(
                rotate_extrude()(translate([big_radius,0, 0])(circle(radius)))))

    def nose_with_hollow_base_cutout_and_ring(self, **kwargs):
        cutout_length = kwargs.get("cutout_length", self.shoulder/2.0) *MM2IN
        cutout_width = kwargs.get("cutout_width", self.inner_diameter * 0.3) *MM2IN
        shoulder = kwargs.get("shoulder", self.shoulder) * MM2IN
        thickness = kwargs.get("thickness", self.thickness) *MM2IN
        ring_radius = kwargs.get("ring_radius", self.thickness) *MM2IN
        ring_thickness = kwargs.get("ring_thickness", self.thickness/2.) *MM2IN
        radius = self.inner_diameter *MM2IN/2

        return union ()(self.hollow_base_and_cutout(radius, shoulder, thickness, cutout_length, cutout_width),
                        translate([radius-cutout_width+ring_radius-ring_thickness,0, -shoulder+4*ring_thickness+2*ring_radius])(self._donut(ring_thickness, ring_radius)))


    def nose_with_hollow_base_and_screw_hole(self,**kwargs):
        shoulder = kwargs.get("shoulder", self.shoulder) * MM2IN
        thickness = kwargs.get("thickness", self.thickness) *MM2IN
        screw_length = kwargs.get("screw_length", self.shoulder) *MM2IN
        screw_radius = kwargs.get("screw_diameter", 0.125) *MM2IN/2
        screw_size = kwargs.get("screw_size")
        radius = self.inner_diameter *MM2IN/2

        return difference ()(union () (self.hollow_base(radius, shoulder, thickness),
                                down(shoulder)(cylinder(h=screw_length, r=screw_radius+thickness/2.)),
                                up(min(screw_length-shoulder-thickness, -thickness))(cylinder(h=thickness, r=radius))),
                      down(shoulder)(cylinder(h=screw_length, r=screw_radius)))

    def render_hollow_base_cutout_with_ring(self, file_, shoulder,thickness, cutout_length, cutout_width, ring_radius, screw_radius):
        out = hollow_base_cutout_with_ring(self.inner_diameter, shoulder, thickness, cutout_length, cutout_width, ring_radius, screw_radius)
        scad_render_to_file(out, file_)

    def render_hollow_base_with_screw(self, file_, shoulder,thickness, screw_length, screw_diameter): 
        out = hollow_base_with_screw(self.inner_diameter, shoulder, thickness, screw_length, screw_diameter)
        scad_render_to_file(out, file_)

    def nose_with_threaded_base_outset(self, **kwargs):
        shoulder = kwargs.get("shoulder", self.shoulder) * MM2IN
        thickness = kwargs.get("thickness", self.thickness) *MM2IN
        offset = kwargs.get("offset", self.thickness) *MM2IN
        radius = self.inner_diameter * MM2IN/2
        tpi = kwargs.get("threads_per_inch", 8)
        tooth = 1./tpi *sqrt(3)/2.*MM2IN
        out = union()((self.cone - cylinder(h=offset, r=3*radius)),
                      down(shoulder)(self.threaded_male_column(length=shoulder+offset, diameter=radius*2-thickness*2, threads_per_inch=tpi)),
                      self.slice(thickness, offset=offset)) - down(shoulder-thickness)(cylinder(h=shoulder+offset, r=radius-thickness-tooth))
        return out

    def threaded_base_outset_mate(self, **kwargs):
        shoulder = kwargs.get("shoulder", self.shoulder) * MM2IN
        thickness = kwargs.get("thickness", self.thickness) *MM2IN
        radius = self.inner_diameter * MM2IN/2
        tpi = kwargs.get("threads_per_inch", 8)
        out = down(shoulder)(cylinder(h=shoulder, r=radius))+self.slice(self.thickness)
        out -= down(shoulder)(self.threaded_female_column(length=shoulder+thickness, diameter=radius*2-thickness*2, threads_per_inch=tpi))
        tooth = 1./tpi *sqrt(3)/2.*MM2IN
        return out

    def render(self, object):
        scad=scad_render(object)
        lines = scad.split("\n")
        count=0
        for each in lines:
            if each.startswith('use') or each.startswith('import'):
                count += 1
            else:
                break
        return '\n'.join(lines[0:count]+['$fn=100;']+lines[count:])

    def render_to_file(self, object, file_):
        with open(file_, "w") as f:
            f.write(self.render(object))

    def cross_section(self, object):
        size= (self.length+self.outer_diameter)*2*MM2IN
        return object*forward(size/2)(cube(size,center=True));


if __name__=='__main__':
    h=NoseCone('biconic', 0.75, bodytube=bt5, thickness=1/16.0, shoulder=0.375, base_height=0.25, blunt_radius=0.125, mid_radius=.3)
#    h=NoseCone('blunted_tangent_ogive', 0.75, bodytube=bt5, thickness=1/16.0, shoulder=0.375, blunt_radius=0.125, offset=-10)
#    h=NoseCone('power_series', 0.75, bodytube=bt5, thickness=1/16.0, shoulder=0.375, base_height=0.25, exponent=0.1)
#    g=NoseCone('parabolic', 0.75, bodytube=bt5, thickness=1/16.0, shoulder=0.375, base_height=0.25)

#    h.render_hollow_base_cutout_with_elbow("test.scad", shoulder=0.5, thickness=1/16.0, cutout_length=0.4 , cutout_width=0.3, elbow_radius=1/32.)
#    h.render_hollow_base_cutout_with_ring("test.scad", shoulder=0.5, thickness=1/16.0, cutout_length=0.4 , cutout_width=0.3, ring_radius=1/8., screw_radius=1/16.)
#    h.render_hollow_base_with_screw("test.scad", shoulder=0.5, thickness=1/16.0, screw_length=0.25, screw_diameter=0.0625)
#    h.render_threaded_base_outset_mate("test2.scad", shoulder=0.5, tpi=8)
#    h.render_to_file("test.scad")
    print h.cone
    h.render_to_file(h.cross_section(h.nose_with_threaded_base_outset(tpi=4,offset=1/8.0)),"test.scad")
#    h.render_to_file(h.cone+left(5)(g.cone),"test.scad")
    app=Flask(__name__)
    app.run(debug=True)

