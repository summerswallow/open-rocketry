mm2in=25.4;

module round_clamp_jig(wood_size=0.25*mm2in, inner=3.1*mm2in, thickness=0.9*mm2in, base=.125*mm2in, angle=72, offset=10, height=1.5*mm2in,
reinforcement=mm2in) {
 
    outer=thickness+inner;
    
    difference () {
        union() {
            difference () {
                cylinder(h=1.5*mm2in, r=outer);
                rotate([0, 0, angle])
                    translate([0, -wood_size/2, 0]) 
                    cube([inner+3*mm2in, wood_size, height]);
                translate([0, -wood_size/2, 0])
                    cube([inner+3*mm2in, wood_size, height]);
                rotate([0, 0, offset])
                    color("blue") 
                    translate([inner+thickness/2+base, 0, mm2in])
                    cube([thickness, inner+3*mm2in, mm2in], center=true);
                rotate([0, 0, angle-offset])
                    color("blue") 
                    translate([inner+thickness/2+base, 0, mm2in])
                    cube([thickness, inner+3*mm2in, mm2in], center=true);

            }

            translate([0, wood_size/2, 0])color("red")cube([inner+height, .0625*mm2in, height]);
            rotate([0, 0, angle])translate([0, -wood_size/2-0.0625*mm2in, 0])color("red")cube([inner+height, .0625*mm2in, height]);
        }

        cylinder(h=height, r=inner);

        translate([0, -outer/2, 0.75*mm2in])cube([2*outer, outer, height], center=true);

        rotate([0, 0, angle+180]) translate([0, -outer/2, 0.75*mm2in])cube([2*outer, outer, height], center=true);

    }
}
round_clamp_jig();
