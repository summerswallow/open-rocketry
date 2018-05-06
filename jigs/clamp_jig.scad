IN=25.4;
$fn=200;
module inner_clamp_jig(radius, width, height, thickness, wall_height, wall_width) {
    radius =radius *IN;
    height=height *IN;
    thickness=thickness *IN;
    width=width*IN;
    wall_height=wall_height*IN;
    wall_width=wall_width*IN;
    difference () {
        intersection() {
            translate([radius-thickness-wall_height,-width/2-wall_width,0]) color("red") cube([thickness+wall_height,width+wall_width*2, height]);
            cylinder(h=height, r=radius);
        }
        translate([radius-thickness-wall_height,-width/2,0]) color("blue") cube([wall_width,width, height]);
    }
}

module fin_clamp_jig(fin_width=0.25, radius=3.1, thickness=0.9, base=.125, angle=72, offset=10, height=1.5, reinforcement=1, blade_width=0.0625,
    blade_length=1.5) {
    fin_width=fin_width*IN;
    radius=radius*IN;
    thickness=thickness*IN;
    base=base*IN;
    height=height*IN;
    reinforcement=reinforcement*IN;
    blade_width=blade_width*IN;
    blade_length=blade_length*IN;
    outer=thickness+radius;
    epsilon=1;  // Not necessary, but it makes the preview look nicer in open SCAD
    rotate([0,0, -angle/2]) 
    difference () {
        union() {
            difference () {
                cylinder(h=height, r=outer);
                rotate([0, 0, angle])
                    translate([0, -fin_width/2, -epsilon]) 
                    cube([radius+3*IN, fin_width, height+2*epsilon]);
                translate([0, -fin_width/2, -epsilon])
                    cube([radius+3*IN, fin_width, height+2*epsilon]);
                rotate([0, 0, offset])
                    translate([radius+thickness/2+base, 0, reinforcement/2+height/2])
                    cube([thickness, radius*3, height-reinforcement+epsilon], center=true);
                rotate([0, 0, angle-offset])
                    translate([radius+thickness/2+base, 0, reinforcement/2+height/2])
                    cube([thickness, radius*3, height-reinforcement+epsilon], center=true);
            }


            translate([0, fin_width/2, 0])color("red")cube([radius+blade_length, blade_width, height]);
            rotate([0, 0, angle])translate([0, -fin_width/2-blade_width, 0])color("red")cube([radius+blade_length, blade_width, height]);
        }
        translate([0, 0, -epsilon]) 
            union () {
            cylinder(h=height+2*epsilon, r=radius);
            translate([0, -outer/2, height/2+epsilon])cube([2*outer, outer, height+2*epsilon], center=true);
            rotate([0, 0, angle+180]) translate([0, -outer/2, height/2+epsilon])cube([2*outer, outer, height+2*epsilon], center=true);
        }
    }
}
fin_clamp_jig(reinforcement=0.5,offset=36);
translate([0,0,0.5*IN]) inner_clamp_jig(3, .75, 1, 1/16, 1/16, 1/32);
