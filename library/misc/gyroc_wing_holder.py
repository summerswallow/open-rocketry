from solid import polygon, linear_extrude, translate, cylinder, rotate, scale, cube, multmatrix
from math import sqrt
def to_mm(x):
    return 25.4*x
def hold_down(od, wing_thickness, alpha, height, width, angle):
    
    half_thickness=to_mm(wing_thickness/2);
    r=to_mm(od/2);
    depth = r * sqrt(1-alpha*alpha);
    h=to_mm(height);
    w=to_mm(width);
    hprime = h*w/(w-(1-alpha)*r);
    basic_wedge = linear_extrude(h, center=True)(polygon([[0,half_thickness], [0,depth], [w, half_thickness]]))

    basic_cylinder = rotate([angle, 0,0])(cylinder(h=h*1.5, r=r,center=True))
    cone_envelope = translate([alpha*r, half_thickness,-h*0.5])(
                    rotate([0,90,0])(
                        scale([hprime/(depth-half_thickness),1,1])(
                            cylinder(r1=depth-half_thickness, r2=0, h=w))))
    clipping_cube = cube([10000,r*1.2, 10000],center=True);

    holder = (translate([alpha*r, 0, 0])(basic_wedge)- basic_cylinder)* cone_envelope *clipping_cube
    return holder
def standard_hold_down(od, wing_thickness, alpha, angle, left=False):
    hd= hold_down(od, wing_thickness, alpha, od*0.75, od, angle)
    x = -1 if left else 1
    rectify = 180 if left else 0
    ret=rotate([90,rectify,0])(
        multmatrix([[1,0,0,0],
                    [0,x,0,0],
                    [-0.4,0,1,0],
                    [0,0,0,1]])(hd))
    return ret